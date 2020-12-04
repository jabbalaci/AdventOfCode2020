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

    private Dictionary<string, string> passport = new Dictionary<string, string>();

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

    public bool IsValid()
    {
        return requiredFields.All(id => this.passport.ContainsKey(id));
    }
}
