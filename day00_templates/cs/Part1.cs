using System;
using static System.Console;
using System.Linq;
using System.Collections;
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
            const string fname = "example.txt";
            // const string fname = "input.txt";
            List<int> numbers = FileUtils.ReadLinesAsInts(fname);
            WriteLine(string.Join(", ", numbers));
        }
    }
}
