"""
Exercise 1 starter code.

This function reads a text file, counts the words in it, and writes the
counts to an output file. It works (sort of) but it's not pretty.

Your job:
  1. List at least 3 code smells you can find in count_words_in_file.
  2. Split it into a pure count_words(text) function and a thin
     count_words_in_file(in_file, out_file) wrapper.
"""


def count_words_in_file(in_file, out_file):
    counts = {}
    with open(in_file, 'r') as f:
        for l in f:
            # Split words on spaces.
            W = l.lower().split(' ')
            for w in W:
                if w != '':
                    if w in counts:
                        counts[w] += 1
                    else:
                        counts[w] = 0
    with open(out_file, 'w') as f:
        for k in counts.keys():
            f.write(k + "," + str(counts[k]) + "\n")
