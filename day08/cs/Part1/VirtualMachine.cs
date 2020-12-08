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
            int ip = 0;    // instruction pointer
            var visited = new HashSet<int>();

            while (true)
            {
                if (visited.Contains(ip))
                {
                    break;
                }

                var curr = instructions[ip];
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
            }
        }
    }
}
