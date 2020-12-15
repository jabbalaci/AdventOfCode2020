using static System.Console;

namespace AdventOfCode2020
{
    public class Part2
    {
        public static void Main(string[] args)
        {
            WriteLine("# Part 2");
            WriteLine("--------");
            WriteLine();

            var original = 2_429_011;    // 379 * 13 * 17 * 29
            long i = 100_000_000_000_000L / 2_429_011;

            while (true)
            {
                long x = i * original - 41;
                if (((x + 0) % 41 == 0)   &&
                    ((x + 35) % 37 == 0)  &&
                    ((x + 41) % 379 == 0) &&
                    ((x + 49) % 23 == 0)  &&
                    ((x + 54) % 13 == 0)  &&
                    ((x + 58) % 17 == 0)  &&
                    ((x + 70) % 29 == 0)  &&
                    ((x + 72) % 557 == 0) &&
                    ((x + 91) % 19 == 0))
                {
                    WriteLine(x);
                    break;
                }
                //
                ++i;
            }
        }
    }
}
