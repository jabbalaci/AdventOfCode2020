using System.IO;
using System.Collections.Generic;
using System.Linq;

namespace AdventOfCode2020
{
    public static class FileUtils
    {
        public static List<string> ReadLines(string fname)
        {
            var lines = new List<string>();
            using (var f = new StreamReader(fname))
            {
                string line;
                while((line = f.ReadLine()) != null)
                {
                    lines.Add(line);
                }
            }
            return lines;
        }

        public static List<int> ReadLinesAsInts(string fname)
        {
            return ReadLines(fname).Select(s => int.Parse(s)).ToList();
        }
    }
}
