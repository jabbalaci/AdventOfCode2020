using System;
using System.Linq;
using System.Collections.Generic;

namespace AdventOfCode2020
{
    public class VirtualMachine
    {
        private List<string> lines;
        private List<(string, int)> instructions;
        public int Accumulator { get; private set; } = 0;

        public VirtualMachine(List<string> lines)
        {
            this.lines = lines;
            this.instructions = lines.Select(Parse).ToList();
        }

        private (string, int) Parse(string line)
        {
            var parts = line.Split();
            return (parts[0], int.Parse(parts[1]));
        }

        public void Start()
        {
            for (var i = 0; i < instructions.Count; ++i)
            {
                var copy = new List<(string, int)>(this.instructions);
                var curr = copy[i];
                var (inst, value) = curr;

                if (inst == "nop" || inst == "jmp")
                {
                    if (inst == "nop") {
                        curr.Item1 = "jmp";
                    }
                    else {    // if "jmp"
                        curr.Item1 = "nop";
                    }
                    copy[i] = curr;
                }

                bool ok = Run(copy);
                if (ok)
                {
                    break;
                }
            }
        }

        public bool Run(List<(string, int)> program)
        {
            this.Accumulator = 0;                   // reset
            int ip = 0;                             // instruction pointer
            var visited = new HashSet<int>();

            while (true)
            {
                if (visited.Contains(ip))
                {
                    // we are in an infinite loop
                    return false;
                }

                var curr = program[ip];
                visited.Add(ip);
                var (inst, value) = curr;

                switch (inst)
                {
                    case "nop":
                        ++ip;
                        break;
                    case "acc":
                        this.Accumulator += value;
                        ++ip;
                        break;
                    case "jmp":
                        ip += value;
                        break;
                    default:
                        throw new NotImplementedException();    // we should never get here
                }

                if (ip >= program.Count)
                {
                    return true;
                }
            }
        }
    }
}
