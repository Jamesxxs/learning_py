print('')
#12.2 Tuples assignment
print('[13.1 Word frequency analysis]' + '-'*70)
print('[Exercise 13.1]' + '-'*70)
import string

book = open('/Users/gaomingjun/Desktop/thinkInPy2/Char13/65336-0.txt')
puncs = string.punctuation

def read_file(fin):
    for line in fin:
       for pc in puncs:
           line = line.replace(pc,)

import re
pattern = string.punctuation
test_text = 'b,b.b/b;'
result_list = re.split(pattern, test_text)
print(result_list)
