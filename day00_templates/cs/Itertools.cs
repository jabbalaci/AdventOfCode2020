using System.Linq;
using System.Collections;
using System.Collections.Generic;

/*
    Combinations is from here:
        https://www.technical-recipes.com/2017/obtaining-combinations-of-k-elements-from-n-in-c/
*/

namespace AdventOfCode2020
{
    public static class Itertools
    {
        private static bool NextCombination(IList<int> numbers, int n, int k)
        {
            bool finished;

            var changed = finished = false;

            if (k <= 0) return false;

            for (var i = k - 1; !finished && !changed; --i)
            {
                if (numbers[i] < (n - 1 - (k - 1) + i))
                {
                    ++numbers[i];

                    if (i < k - 1)
                    {
                        for (var j = i + 1; j < k; ++j)
                        {
                            numbers[j] = numbers[j - 1] + 1;
                        }
                    }
                    changed = true;
                }
                finished = (i == 0);
            }

            return changed;
        }

        public static IEnumerable Combinations<T>(IEnumerable<T> elems, int k)
        {
            var elemsArray = elems.ToArray();
            var size = elemsArray.Length;

            if (k > size) yield break;

            var numbers = new int[k];

            for (var i = 0; i < k; ++i)
            {
                numbers[i] = i;
            }

            do
            {
                yield return numbers.Select(n => elemsArray[n]);
            } while (NextCombination(numbers, size, k));
        }
    }
}
