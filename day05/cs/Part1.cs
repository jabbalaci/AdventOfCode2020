using System;
using static System.Console;
using System.Linq;
using System.Collections.Generic;

namespace AdventOfCode2020
{
    public class Part1
    {
        public static void Main(string[] args)
        {
            WriteLine("# Part 1");
            WriteLine("--------");
            WriteLine();
            // const string example = "FBFBBFFRLR";    // row 44, column 5, seat ID 357
            // const string example = "BFFFBBFRRR";    // row 70, column 7, seat ID 567
            // const string example = "FFFBBBFRRR";    // row 14, column 7, seat ID 119
            // const string example = "BBFFBBFRLL";    // row 102, column 4, seat ID 820
            const string fname = "input.txt";
            List<string> lines = FileUtils.ReadLines(fname);
            var result = lines.Select(Decode).Max();
            WriteLine(result);

            // WriteLine(example);
            // WriteLine(Decode(example));
        }

        private static int Decode(string seat)
        {
            var rowStr = seat[..7];
            var columnStr = seat[^3..];
            var row = FindPosition(rowStr);
            var column = FindPosition(columnStr);
            var id = row * 8 + column;

            // WriteLine($"# row: {row}");
            // WriteLine($"# column: {column}");
            // WriteLine($"# id: {id}");

            return id;
        }

        private static int FindPosition(string line)
        {
            int lo = 0;
            int hi = (int)Math.Pow(2, line.Length) - 1;    // 127 or 7
            if (line.Length == 3) {
                line = line.Replace("R", "B").Replace("L", "F");    // unify the two encodings
            }
            //
            int result = 0;
            foreach (var c in line)
            {
                if (c == 'F')
                {
                    hi = (lo + hi) / 2;
                    result = hi;
                }
                else    // 'R'
                {
                    lo = (lo + hi) / 2 + 1;
                    result = lo;
                }
            }

            return result;
        }
    }
}
