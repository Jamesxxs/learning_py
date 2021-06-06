#9.1 Reading word lists
print('[9.1][Reading word list]'+'-'*70)
fin = open('/Users/gaomingjun/Desktop/thinkInPy2/Char9/word.txt')
print(fin,'\n','types: ',type(fin))
print(fin.readline())
print(fin.readline())
#let's get rid of the '\n' for next line
line = fin.readline()
word = line.strip()
print(word)
print(fin.readline())
fin.close()
#OR
'''for line in fin:
    word = line.strip()
    print(word)'''


#9.2 Exercises
print('[9.2][Exercises]'+'-'*70)
#Ex.9.1
print('[Ex.9.1]'+'-'*70)

finEx91 = open('/Users/gaomingjun/Desktop/thinkInPy2/Char9/word.txt')

def char20(fin):
    for line in fin:
        word = line.strip()
        if len(word) > 20:
            print(word)
char20(finEx91)
finEx91.close()

#Ex.9.2
print('[Ex.9.2]'+'-'*70)

#finEx92 = open('/Users/gaomingjun/Desktop/thinkInPy2/Char9/word.txt')

'''
ver.1.0
def has_no_e(word):
    for letter in word:
        if letter == 'e':
            return False
    return True
'''

def has_no_e(word):
    if 'e' in word:
        return False
    return True


def no_e_words(fin):
    n_no_e_word = 0
    total_lines = 0
    for line in fin:
        total_lines += 1
        if has_no_e(line):
            n_no_e_word += 1
            print(line.strip())
    print('The percentage of words that have no \'e\' is:\n ',(n_no_e_word/total_lines)*100,'%')

#no_e_words(finEx92)  too long...
#finEx92.close()

#Ex9.3
print('[Ex.9.3]'+'-'*70)
def avoids(word,forbidden_letter):
    for letter in word:
        if letter in forbidden_letter:
            return False
    return True

print(avoids('hello','good'))
print(avoids('ok','fine'))

#Ex9.4
print('[Ex.9.4]'+'-'*70)
def uses_only(word,required_letter):
    for letter in word:
        if not letter in required_letter:
            return False
    return True

print(uses_only('hello','acefhlo'))

#Ex9.5
print('[Ex.9.5]'+'-'*70)
'''
ver.1.0
def uses_all(word,required_letter):
    for rl in required_letter:
        if rl not in word:
            return  False
    return True'''

def uses_all(word,required):
    return uses_only(required,word)

print(uses_all('hello','hl'))

#Ex9.6
print('[Ex.9.6]'+'-'*70)

#ver.1.0 (for loop)
def is_abecedarian(word):
    index = 0
    for letter in word:
        if ord(letter) < index:
            return False
        index = ord(letter)
    return True

print(is_abecedarian('cab'))
print('b > a is: ','b'>'a')

'''
ver.2.0 (recursion)
# 'b' > 'a' ---> True
def is_abecdarian(word):
    if len(word) <= 1:
        return True
    if word[0] > word[1]:
        return False
    return is_abecdarian(word[1:])'''

'''
ver.3.0 (while loop)
def is_abecdarian(word):
    index = 0
    while index < len(word)-1:
        if word[index] > word[index+1]:
            return False
        index += 1
    return True'''


#9.7 Exercise
print('[9.7][Exercises]'+'-'*70)
#Ex9.7
print('[Ex9.7]'+'-'*70)

'''
这个我写的第一个版本是错的，因为即使不是连续的3个double letter的结果也是True
def is_triple_double(word):
    i = 0
    count = 0
    while i < len(word)-1:
        if word[i] == word[i+1]:
            i += 1
            count += 1
        i += 1
    return count == 3
'''
def is_triple_double(word):
    i = 0
    count = 0
    while i < len(word)-1:
        if word[i] == word[i+1]:
            count += 1
            if count == 3:
                return True
            i += 2
        else:
            i = i+1 - 2*count
            count =0
    return False

def find_triple_double():
    fin = open('/Users/gaomingjun/Desktop/thinkInPy2/Char9/word.txt')
    for line in fin:
        word = line.strip()
        if is_triple_double(word):
            print(word)
    fin.close()
print('Here is all the triple double words in the file:')
find_triple_double()

#Ex9.8
print('[Ex9.8]'+'-'*70)

def int_palindrome(num,start,end):
    s = str(num)[start:end]
    return s == s[::-1]

def check(num):
    return int_palindrome(num,2,6) and\
           int_palindrome(num+1,1,6) and\
           int_palindrome(num+2,1,5) and\
           int_palindrome(num+3,0,6)


def odometer():
    i = 100000
    while int(i) <= 999999:
        if check(i):
            print(i)
        i += 1
    print('that is all.')

odometer()

#Ex9.9
print('[Ex9.9]'+'-'*70)

def str_fill(i,n):
    return str(i).zfill(n)

def are_reversed(son,mother):
    return str_fill(son,2) == str_fill(mother,2)[::-1]

def n_reversed_age(diff):
    son = 0
    count = 0
    while True:
        mother = son + diff
        if are_reversed(son,mother):
            count += 1
            print('----[',count,']----')
            print('mother: ',mother)
            print('son: ',son)
        son += 1
        mother +=1
        if mother > 200:
            break
    return count

def check_diff():
    diff = 10
    while diff < 70:
        n = n_reversed_age(diff)
        if n > 0:
            print('Diff is: ',diff,'\nCount is:',n)
        diff += 1

check_diff()
print('so the answer should be: son is 57 now')