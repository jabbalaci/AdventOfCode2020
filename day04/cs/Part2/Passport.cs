using System;
using System.Text;
using static System.Console;
using System.Linq;
using System.Collections;
using System.Collections.Generic;

public class Passport
{
    // cid is optional, thus it's missing
    private static string[] requiredFields = { "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid" };

    private static string[] eyeColors = { "amb", "blu", "brn", "gry", "grn", "hzl", "oth" };

    private Dictionary<string, string> passport = new Dictionary<string, string>();
    private int byr;
    private int iyr;
    private int eyr;

    public Passport(string data)
    {
        var parts = data.Split();
        foreach (var p in parts)
        {
            var pieces = p.Split(':');
            var key = pieces[0];
            var value = pieces[1];
            passport[key] = value;
        }
        // byr
        if (passport.ContainsKey("byr"))
        {
            this.byr = int.Parse(passport["byr"]);
        }
        // iyr
        if (passport.ContainsKey("iyr"))
        {
            this.iyr = int.Parse(passport["iyr"]);
        }
        // eyr
        if (passport.ContainsKey("eyr"))
        {
            this.eyr = int.Parse(passport["eyr"]);
        }
    }

    public override string ToString()
    {
        var sb = new StringBuilder("{");
        foreach (var key in passport.Keys)
        {
            sb.Append($"{key}: {passport[key]}, ");
        }
        sb.Append("}");
        return sb.ToString();
    }

    public bool HasAllRequiredFields()
    {
        return requiredFields.All(id => this.passport.ContainsKey(id));
    }

    private bool IsByrValid()
    {
        // byr (Birth Year) - four digits; at least 1920 and at most 2002.
        bool result = this.byr >= 1920 && this.byr <= 2002;
        // WriteLine("# byr; value: {0}; valid: {1}", this.passport["byr"], result);
        return result;
    }

    private bool IsIyrValid()
    {
        // iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        bool result = this.iyr >= 2010 && this.iyr <= 2020;
        // WriteLine("# iyr; value: {0}; valid: {1}", this.passport["iyr"], result);
        return result;
    }

    private bool IsEyrValid()
    {
        // eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        bool result = this.eyr >= 2020 && this.eyr <= 2030;
        // WriteLine("# eyr; value: {0}; valid: {1}", this.passport["eyr"], result);
        return result;
    }

    private bool IsHgtValid()
    {
        /*
            hgt (Height) - a number followed by either cm or in:
                - If cm, the number must be at least 150 and at most 193.
                - If in, the number must be at least 59 and at most 76.
        */
        string value = this.passport["hgt"];
        if (!(value.EndsWith("cm") || value.EndsWith("in")))
        {
            // WriteLine("# hgt; value: {0}; valid: {1}", value, false);
            return false;
        }
        // else, if ends with "cm" or "in"
        var number = int.Parse(value[..^2]);
        if (value.EndsWith("cm"))
        {
            bool result = number >= 150 && number <= 193;
            // WriteLine("# hgt; value: {0}; valid: {1}", value, result);
            return result;
        }
        else    // inch
        {
            bool result = number >= 59 && number <= 76;
            // WriteLine("# hgt; value: {0}; valid: {1}", value, result);
            return result;
        }
    }

    private bool IsHexaDigit(char c)
    {
        return (c >= '0' && c <= '9') || (c >= 'a' && c <= 'f');
    }

    private bool IsHclValid()
    {
        // hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        string value = this.passport["hcl"];
        if (!(value.StartsWith('#') && value.Length == 7)) {
            return false;
        }
        // else, i.e. starts with '#' and after the '#' there are 6 characters
        return value[1..].All(IsHexaDigit);
    }

    private bool IsEclValid()
    {
        // ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        string value = this.passport["ecl"];
        return eyeColors.Contains(value);
    }

    private bool IsPidValid()
    {
        // pid (Passport ID) - a nine-digit number, including leading zeroes.
        string value = this.passport["pid"];
        return value.Length == 9 && value.All(char.IsDigit);
    }

    public bool IsStrictlyValid()
    {
        return HasAllRequiredFields() &&
               IsByrValid() &&
               IsIyrValid() &&
               IsEyrValid() &&
               IsHgtValid() &&
               IsHclValid() &&
               IsEclValid() &&
               IsPidValid();
    }
}
