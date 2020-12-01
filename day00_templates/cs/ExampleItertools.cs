using System;
using static System.Console;
using System.Linq;
using System.Collections;
using System.Collections.Generic;
using static AdventOfCode2020.Itertools;

namespace AdventOfCode2020
{
    public class ExampleItertools
    {
        public static void Main(string[] args)
        {
            WriteLine("Itertools Examples");
            WriteLine("==================");
            WriteLine();

            WriteLine("Combinations");
            WriteLine("------------");
            var numbers = new List<int> { 3, 4, 5, 6 };
            foreach (IEnumerable<int> iter in Combinations(numbers, 2))
            {
                var lst = iter.ToList();
                WriteLine(string.Join(", ", lst));
            }
        }
    }
}
