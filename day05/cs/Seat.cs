using System;
using static System.Console;
using System.Linq;
using System.Collections;
using System.Collections.Generic;

namespace AdventOfCode2020
{
    public class Seat
    {
        public int Row { get; }
        public int Column { get; }
        public int Id { get; }

        public Seat(int row, int column)
        {
            Row = row;
            Column = column;
            Id = row * 8 + column;
        }

        public override string ToString()
        {
            return $"Seat(row={Row}, column={Column})";
        }
    }
}
