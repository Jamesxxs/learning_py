
#8.1 A string is a sequence
print('?8.1?'+'-'*70)
word = 'fuck'
f = word[0]
k = word[-1]
print(f)
print(k)

#8.2 len
print('?8.2?'+'-'*70)
print(len(word))

#8.3 Tracersal with a for loop
print('?8.3?'+'-'*70)
def print_letter_bw(word):
    """print letter backwards"""
    index = len(word)-1
    while index >= 0:
        print(word[index])
        index -= 1

def print_letter_fd(word):
    """print letter forwards"""
    for letter in word:
        print(letter)

def duck():
    prefixes = 'JKLMNOPQ'
    suffix = 'ack'
    for letter in prefixes:
        if letter == 'O' or letter == 'Q':
            letter +='u'
        print(letter + suffix)

#duck()

#8.4 String slices
print('?8.4?'+'-'*70)
s = 'what a wonderful day!'
wonderful = s[7:16]
print(wonderful)
print(s[7:])
print(s[3:3],len(s[3:3])) #'' its empty
print(s[:])


#8.5 Strings are immutable
print('?8.5?'+'-'*70)
#Strings are immutable
greeting = 'hello world!'
print(greeting)
new_greeting = 'J' + greeting[1:]
print(new_greeting)

#8.6 Searching
print('?8.6?'+'-'*70)
def find(word,letter,index):
    while index < len(word):
        if word[index] == letter:
            return index
        index += 1
    return -1

#8.7 Looping and counting
print('?8.7?'+'-'*70)
def count(word,letter):
    count = 0
    i = 0
    while i < len(word):
        index = find(word,letter,i)
        if index != -1:
            count += 1
            i = index +1
        i += 1
    print(count)

#count('banana','a')

#8.8 String methods
print('?8.8?'+'-'*70)
banana = 'banana'
#.upper()
print(banana.upper())
#.find()
print(banana.find('a'))
print(banana.find('na'))
print(banana.find('na',3))
#the 2nd and 3rd argument defines the range of searching
print(banana.find('a',3,4))

#8.9 The 'in' operator
print('?8.9?'+'-'*70)
def in_both(word1,word2):
    for letter in word1:
        if letter in word2:
            print(letter)

in_both('apple','orange')

#8.10 String comparison
print('?8.10?'+'-'*70)

#8.11 debug
print('?8.11?'+'-'*70)
def is_reverse(word1,word2):
    if len(word1) != len(word2):
        return False

    i = 0
    j = len(word2) - 1
    while j >= 0:
        if word1[i] != word2[j]:
            return False
        i += 1
        j -= 1
    return True

print(is_reverse('pots','stop'))


#Exercise
print('?Exercise?'+'-'*70)
#Ex8.1
print('?Ex8.1?'+'-'*70)
s = 'some text'
print(s.capitalize())
print(s.join('1234'))
print(s.partition('m'))
print(s.replace('some','new'))
print('www.baidu.com'.strip('w.com'))
print('     hahahah        '.strip())
print(s.title())

#Ex8.2
print('?Ex8.2?'+'-'*70)
print('banana'[0:6:2]) #[x:y:z]?x???y-1???????z???item
print('fuck'[::-1]) #generate a reversed string

#Ex8.3
print('?Ex8.3?'+'-'*70)
def is_palindrome(word):
    if word == word[::-1]:
        return True
    return False

print(is_palindrome('bob'))

#Ex8.4
print('?Ex8.4?'+'-'*70)
def any_lowercase1(s):
    """check whether the first letter in the string is lowercase or not"""
    for c in s:
        if c.islower():
            return True
        else:
            return False

def any_lowercase2(s):
    """check whether the letter 'c' is lowercase or not"""
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

def any_lowercase3(s):
    """return the result of wheather the last letter in the string is lowercase or not """
    for c in s :
        flag = c.islower()
    return flag

def any_lowercase4(s):
    """returns True if one of the last two letter is lowercase in the string"""
    flag  = False
    for c in s:
        flag = flag or c.islower()
    return flag

def any_lowercase5(s):
    """if all letters in string s is lowercase return True"""
    for c in s:
        if not c.islower():
            return False
    return True

#Ex8.5
print('?Ex8.5?'+'-'*70)
print(ord('a'))
print(ord('z'))
print(ord('A'))
print(ord('Z'))
print(chr(97))

def rotate_letter(l,i):
    if l.islower():
        start = ord('a')
    elif l.isupper():
        start = ord('A')
    else:
        return l
    d = ord(l) - start
    index = (d+i)%26 +start
    return chr(index)

def rotate_word(s,i):
    newS = '' #since String is immutable, so i have to create a new empty string
    for letter in s:
        newS += rotate_letter(letter,i)
    return newS

print('name: ',__name__)

if __name__ == '__main__':
    print(rotate_word('cheer', 7))
    print(rotate_word('melon', -10))
    print(rotate_word('sleep', 9))
