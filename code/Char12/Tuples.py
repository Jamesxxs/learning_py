#12.1 Tuples are immutable
print('[12.1][Tuples are immutable]' + '-'*70)
t1 = 'a','b','c','d','e'
t2 = ('a','b','c','d','e')
print(t1)
print(t2)
t3 = tuple('good')

print(t3)
t4 = ('m',) + t3[1:]
print(t4)

print((0,1,200000)<(0,3,4))

print('')
#12.2 Tuples assignment
print('[12.2][Tuples assignment]' + '-'*70)
a = 1
b = 2
a,b = b,a
print(a,b)

email = '1059796276@qq.com'
qq,domain = email.split('@')
print('qq: ',qq)
print('domain: ',domain)

print('')
#12.3 Tuples as return value
print('[12.3][Tuples as return value]' + '-'*70)
t = divmod(7,3)
print(t)
#OR
quo,rem = divmod(7,3)
print(quo)
print(rem)

print('')
#12.4 Variable-length argument tuples
print('[12.4][Variable-length argument tuples]' + '-'*70)

def sumall(*args):
    print(args)
    print(sum(args))
sumall(1,2,3,4)

print('')
#12.5 Lists and tuples
print('[12.5][Lists and tuples]' + '-'*70)
s = 'abc'
t = [1,2,3]
print(*zip(s,t))
#OR
for pair in zip(s,t):
    print(pair)

t = list(zip(s,t))
print(t)
for index,ele in enumerate('abc'):
    print(index)


print('')
#12.6 Dictionaries and tuples
print('[12.6][Dictionaries and tuples]' + '-'*70)

#dict => list of tuple (iterator:dict_items)
d = {'a':0,'b':1,'c':2}
t = d.items()
print(t)

for key,val in d.items():
    print(key,val)

#list of tuple => dict
t = [('a',0),('c',2),('b',1)]
d = dict(t)
print(d)

#combine dict() and zip()
d = dict(zip('abc',range(3)))
print(d)

#the key of dicts can be tuple
phone = dict()
last = 'Gao'
first = 'MingJun'
number = 15057503783
phone[first,last] = number
for first,last in phone:
    print(last,first,phone[first,last])


print('')
#12.7 Sequences of sequences
print('[12.7][Sequences of sequences]' + '-'*70)


print('')
#12.8 Debugging
print('[12.8][Debugging]' + '-'*70)



print('')
#12.10 Exercises
print('[12.10][Exercises]' + '-'*70)
#Ex12.1
print('[Ex12.1]' + '-'*70)
print(set('good'))
def most_frequent(s):
    count = 0
    letters = set(s)
    freq = []
    for letter in letters:
        for l in s:
            if l == letter:
                count += 1
        freq.append(count)
        count = 0
    zipObj = sorted(zip(freq,letters),reverse=True)
    lst = []
    for ele in zipObj:
        lst.append(ele)
    return lst

print(most_frequent('scatter'))

print('')
#Ex12.2
print('[Ex12.2]' + '-'*70)

fin = open('/Users/gaomingjun/Desktop/thinkInPy2/Char9/word.txt')


def signature(s):
    """Returns the signature of this string.
    Signature is a string that contains all of the letters in order.
    s: string
    """
    # TODO: rewrite using sorted()
    t = list(s)
    t.sort()
    t = ''.join(t)
    return t


def anagram_sets(fin):
    d = dict()
    for line in fin:
        word = line.strip().lower()
        sig = signature(word)
        if sig not in d:
            d[sig] = [word]
        else:
            d[sig].append(word)
    return d

def print_anagramSet_in_order(d):
    l = []
    for val in d.values():
        if len(val) > 5:
            l.append((len(val), val))
    l.sort(reverse=True)
    for ele in l:
        print(ele)

print_anagramSet_in_order(anagram_sets(fin))


fin.close()

print('')
#Ex12.3
print('[Ex12.3]' + '-'*70)

fin = open('/Users/gaomingjun/Desktop/thinkInPy2/Char9/word.txt')

def count_diff(s1,s2):
    assert len(s1) == len(s2)

    count = 0
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            count += 1

    return count

def matethesis_pair(d):
    for anagrams in d.values():
        for s1 in anagrams:
            for s2 in anagrams:
                if s1 < s2 and count_diff(s1, s2) == 2:
                    print(s1, s2)

matethesis_pair(anagram_sets(fin))
fin.close()


print('')
#Ex12.4
print('[Ex12.4]' + '-'*70)
def make_word_dict():
    """Reads a word list and returns a dictionary."""
    d = dict()
    fin = open('/Users/gaomingjun/Desktop/thinkInPy2/Char9/word.txt')
    for line in fin:
        word = line.strip().lower()
        d[word] = None

    # have to add single letter words to the word list;
    # also, the empty string is considered a word.
    for letter in ['a', 'i', '']:
        d[letter] = letter
    return d



def children(word, word_dict):
    """Returns a list of all words that can be formed by removing one letter.
    word: string
    Returns: list of strings
    """
    res = []
    for i in range(len(word)):
        child = word[:i] + word[i+1:]
        if child in word_dict:
            res.append(child)
    return res


"""memo is a dictionary that maps from each word that is known
to be reducible to a list of its reducible children.  It starts
with the empty string."""

memo = {}
memo[''] = ['']

def is_reducible(word, word_dict):
    """If word is reducible, returns a list of its reducible children.
    Also adds an entry to the memo dictionary.
    A string is reducible if it has at least one child that is
    reducible.  The empty string is also reducible.
    word: string
    word_dict: dictionary with words as keys
    """
     # if have already checked this word, return the answer
    if word in memo:
        return memo[word]

    # check each of the children and make a list of the reducible ones
    res = []
    for child in children(word, word_dict):
        if is_reducible(child, word_dict):
            res.append(child)

    # memoize and return the result
    memo[word] = res
    return res


def all_reducible(word_dict):
    """Checks all words in the word_dict; returns a list reducible ones.
    word_dict: dictionary with words as keys
    """
    res = []
    for word in word_dict:
        t = is_reducible(word, word_dict)
        if t != []:
            res.append(word)
    return res

def print_trail(word):
    """Prints the sequence of words that reduces this word to the empty string.
    If there is more than one choice, it chooses the first.
    word: string
    """
    if len(word) == 0:
        return
    print(word, end=' ')
    t = is_reducible(word,word_dict)
    print_trail(t[0])

def print_longest_words(word_dict):
    """Finds the longest reducible words and prints them.
    word_dict: dictionary of valid words
    """
    words = all_reducible(word_dict)

    # use DSU to sort by word length
    t = []
    for word in words:
        t.append((len(word), word))
    t.sort(reverse=True)

    # print the longest 5 words
    for _, word in t[0:5]:
        print_trail(word)
        print('\n')


word_dict = make_word_dict()
print_longest_words(word_dict)


