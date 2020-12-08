using static System.Console;
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
            // const string fname = "example.txt";
            const string fname = "input.txt";
            List<string> lines = FileUtils.ReadLines(fname);

            var vm = new VirtualMachine(lines);
            vm.Start();
            WriteLine(vm.Accumulator);
        }
    }
}
