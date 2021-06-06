#11.1 A dictionaries is a mapping
print('[11.1][A dictionaries is a mapping]' + '-'*70)
eng2chi = dict()
eng2chi['hello'] = '你好'
print(eng2chi)
#or
eng2chi = {'hello':'你好','look':'看','me':'我'}
print(eng2chi)
# In general, the order of items in a dictionary is unpredictable.
print('length of eng2chi is: ',len(eng2chi))
#'in' operator (can only check keys)
print('what' in eng2chi)
print('hello' in eng2chi)
#want to check values
print(eng2chi.values())
print('你好' in eng2chi.values())
print(eng2chi.keys())
#Python dictionaries use a data structure called a hashtable that has a remarkable property:
#the operator takes about the same amount of time no matter how many items are in the dictionary.


#11.2 Dictionary as collection of counters
print('')
print('[11.2][Dictionary as collection of counters]' + '-'*70)
def histogram(s):
    d = dict()
    for l in s:
        if l not in d:
            d[l] = 1
        else:
            d[l] += 1
    return d
# an advantage of the dictionary implementation is that we don’t have to
# know ahead of time which letters appear in the string

print(histogram('hello'))
h = histogram('book')
print(h.get('p',0))

#11.3 Looping and dictionaries
print('')
print('[11.3][Looping and dictionaries]' + '-'*70)
#If you use a dictionary in a statement, it traverses the keys of the dictionary.
def print_hist(h):
    for key in h:
        print(key,h[key])

h = histogram('ace is good')
print_hist(h)

def print_sortHist(h):
    for key in sorted(h):
        print(key,h[key])
print('sorted version: ')
print_sortHist(h)

#11.4 Reverse lookup
print('')
print('[11.4][Reverse lookup]' + '-'*70)
def reverse_lookup(d,v):
    for k in d:
        if d[k] == v:
            return k
    raise LookupError('v not in the dict')

print(reverse_lookup(eng2chi,'你好'))
#print(reverse_lookup(eng2chi,'我艹'))

#A reverse lookup is much slower than a forward lookup; if you have to do it often,
#or if the dictionary gets big, the performance of your program will suffer.


#11.5 Dictionaries and lists
print('')
print('[11.5][Dictionaries and lists]' + '-'*70)
#List can be value of dictionary but can not be the key
#sicne a dictionary is implemented using a hashtable and that means that the keys have to be hashable.

#keys has to be immutable!

def invert_dict(d):
    inverse = dict()
    for k in d:
        val = d[k]
        if val not in inverse:
            inverse[val] = [k]
        else:
            inverse[val].append(k)
    return inverse

h = histogram('parrot')
print(h)
inverse = invert_dict(h)
print(inverse)


#11.6 Memos
print('')
print('[11.6][Memos]' + '-'*70)

known = {0:0,1:1}

def fibonacci(n):
    if n in known:
        return known[n]
    num = fibonacci(n-1) + fibonacci(n-2)
    known[n] = num
    return num

print(fibonacci(10))
print(known)


#11.7 Global variables
print('')
print('[11.7][Global variables]' + '-'*70)
known = {0:0,1:1}
def example1():
    known[2] = 1

example1()
print(known)

def example2():
    known = dict()

example2()
print(known)

def example3():
    global known
    known = dict({'新的':'dict'})

example3()
print(known)

#11.7 Global variables
print('')
print('[11.10][Exercises]' + '-'*70)

#Ex11.1
print('')
print('[Ex11.1]' + '-'*70)

fin = open('/Users/gaomingjun/Desktop/thinkInPy2/Char9/word.txt')
def dict_for_txt(fin):
    word_dict = dict()
    for line in fin:
        word = line.strip()
        word_dict[word] = ''
    return word_dict

dic = dict_for_txt(fin)
print('zymurgy' in dic)
print('zymurg' in dic)
print('aal' in dic)


#Ex11.2
print('')
print('[Ex11.2]' + '-'*70)
def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        inverse.setdefault(val,[]).append(key)
    return inverse

d = dict(a=1, b=2, c=3, z=1)
inverse = invert_dict(d)
for val in inverse:
    keys = inverse[val]
    print(val, keys)

#Ex11.3
print('')
print('[Ex11.3]' + '-'*70)

known = dict()
def ack(m, n):
    if m == 0:
        return n + 1
    if n == 0:
        return ack(m - 1, 1)
    if (m,n) in known:
        return known[m,n]
    else :
        known[m,n] = ack(m - 1, ack(m, n - 1))
        return known[m,n]

print(ack(3,4))
print(ack(3,6))

#Ex11.4
print('')
print('[Ex11.4]' + '-'*70)
def has_duplicate1(s):
    let2fre = dict()
    for l in s:
        if l not in let2fre:
            let2fre[l] = 1
        else:
            let2fre[l] += 1
    return max(let2fre.values()) >= 2

def has_duplicate2(s):
    d = dict()
    for l in s:
        if l in d:
            return True
        else:
            d[l] = True
    return False

def has_duplicate3(s):
    return len(set(s)) < len(s)

print(has_duplicate1('good'))
print(has_duplicate2('good'))
print(has_duplicate3('good'))




#Ex11.5
print('')
print('[Ex11.5]' + '-'*70)

from Char8.String import rotate_word

def make_word_dict():
    """Read the words in words.txt and return a dictionary
    that contains the words as keys"""
    d = dict()
    fin = open('/Users/gaomingjun/Desktop/thinkInPy2/Char9/word.txt')
    for line in fin:
        word = line.strip().lower()
        d[word] = None

    return d


def rotate_pairs(word, word_dict):
    """Prints all words that can be generated by rotating word.
    word: string
    word_dict: dictionary with words as keys
    """
    for i in range(1, 14):
        rotated = rotate_word(word, i)
        if rotated in word_dict:
            print(word, i, rotated)


word_dict = make_word_dict()

for word in word_dict:
    rotate_pairs(word, word_dict)


#Ex11.6
print('')
print('[Ex11.6]' + '-'*70)