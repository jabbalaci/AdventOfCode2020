using System;
using static System.Console;
using System.Linq;
using System.Collections.Generic;

namespace AdventOfCode2020
{
    public class Part2
    {
        public static void Main(string[] args)
        {
            WriteLine("# Part 2");
            WriteLine("--------");
            WriteLine();
            const string fname = "input.txt";
            List<string> lines = FileUtils.ReadLines(fname);
            var seats = lines.Select(Decode).ToList();

            for (var i = 0; i < 128; ++i)
            {
                var seatsInRow = seats.Where(seat => seat.Row == i).ToList();
                if (seatsInRow.Count == 7)
                {
                    WriteLine("Row with only 7 occupied seats:");
                    WriteLine();
                    foreach (var seat in seatsInRow.OrderBy(seat => seat.Column))
                    {
                        WriteLine(seat);
                    }

                    var row = seatsInRow.First().Row;
                    var bag = new HashSet<int> { 0, 1, 2, 3, 4, 5, 6, 7 };
                    var missing = bag.Except(seatsInRow.Select(seat => seat.Column)).First();
                    var result = row * 8 + missing;

                    WriteLine();
                    WriteLine("Missing column: " + missing);
                    WriteLine();
                    WriteLine($"result: {row} * 8 + {missing} = {result}");
                }
            }
        }

        private static Seat Decode(string seat)
        {
            var rowStr = seat[..7];
            var columnStr = seat[^3..];
            var row = FindPosition(rowStr);
            var column = FindPosition(columnStr);

            return new Seat(row, column);
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
