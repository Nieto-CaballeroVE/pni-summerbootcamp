"""
Exercise 1 starter code.

This function reads a text file, counts the words in it, and writes the
counts to an output file. It works (sort of) but it's not pretty.

Your job:
  1. List at least 3 code smells you can find in count_words_in_file.
  2. Split it into a pure count_words(text) function and a thin
     count_words_in_file(in_file, out_file) wrapper.
"""

'''
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

Smells:
function doing more than one thing,
not well documented
uninformative variable names
'''

def count_words(text):
    """Given a text file return a dictionary of counts of word occurences"""
    counts = {}
    with open(text, 'r') as file:
        for line in file:
            # Split words on spaces.
            words = line.lower().split()
            for word in words:
                if word in counts:
                    counts[word] += 1
                else:
                    counts[word] = 0
    return counts

def count_words_in_file(in_file, out_file):
    """Given a text file, count words in file """
    count_words_dict = count_words(in_file)
    with open(out_file, 'w') as f:
        for k in count_words_dict.keys():
            f.write(k + "," + str(count_words_dict[k]) + "\n")


count_words_in_file("/Users/vn0027/Projects/pni-summerbootcamp/data/moby_dick.txt", "/Users/vn0027/Projects/pni-summerbootcamp/results/countwords_mobydick.txt")