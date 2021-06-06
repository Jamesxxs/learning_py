#10.1 A list is a sequence
print('[10.1][A list is a sequence]' + '-'*70)
aot = ['eren','mikasa','armin']
print(aot)
animation = ['myHeroAcademic',aot]
print(animation)

#10.2 List are mutable
print('')
print('[10.2][List are mutable]' + '-'*70)
nums = [1,2,4]
nums[2] = 3
print(nums)

#10.3 Traversing a list
print('')
print('[10.3][Traversing a list]' + '-'*70)
for i in range(len(nums)):
    nums[i] = nums[i] * 2
    print(nums)

#10.4 List operatios
print('')
print('[10.4][List operatios]' + '-'*70)
a = [0]
b = [1,2,3]
print((a+b)*4)

#10.5 List slices
print('')
print('[10.5][List slices]' + '-'*70)
letter = ['a','b','c','d','e','f']
print(letter[0:3])
print(letter[3:])
print(letter[:3])
print(letter[:])
print(letter[::-1])
print(letter[0:6:2])

#10.6 List methods
print('')
print('[10.6][List methods]' + '-'*70)
nums = [1]
print(nums)
nums.append(2)
print(nums)
x = [3,4]
nums.extend(x)
print(nums)
t = ['d','f','a','c']
t.sort()
print(t)

#10.7 Map,filter and reduce
print('')
print('[10.7][Map,filter and reduce]' + '-'*70)
#Reduce
t1 = [1,2,3]
print(sum(t1))

#Map
def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res
t2 = ['a','b','c']
print(capitalize_all(t))

#Filter
def only_upper(t):
    res = []
    for s in t:
        if s.isupper():
            res.append(s)
    return res
t3 = ['A','b','C']
print(only_upper(t3))

#10.8 Deleting elements
print('')
print('[10.8][Deleting elements]' + '-'*70)
del t3[1]
print(t3)
t3.remove('A')
print(t3)
t3.pop(0)
print(t3)

#10.9 List and strings
print('')
print('[10.9][List and strings]' + '-'*70)
s = 'List'
t = list(s)
print(t)

s = 'Hello-word'
t = s.split('-')
print(t)
s1 = '+'.join(t)
print(s1)



#10.10 Objects and values
print('')
print('[10.10][Objects and values]' + '-'*70)
a = 'banana'
b = 'banana'
print(a is b)
l1 = [1,2,3]
l2 = [1,2,3]

print(l1 is l2)


#10.11 Aliasing
print('')
print('[10.11][Aliasing]' + '-'*70)
l1 = [1,2,3]
l2 = l1
print(l1 is l2)
l2[1] = 10
print(l1)


#10.12 List arguments
print('')
print('[10.12][List arguments]' + '-'*70)
t1 = [1,2]
t2 = t1.append(3)
print(t1)
print(t2)

t3 = t1 + [4]
print(t1)
print(t3)

#10.15 Exercise
#Ex10.1
print('')
print('[Ex10.1]' + '-'*70)
def nested_sum(list):
    total = 0
    for lt in list:
        x = sum(lt)
        total += x
    return total

l = [[1,2],[3],[4,5,6]]

print(nested_sum(l))

#Ex10.2
print('')
print('[Ex10.2]' + '-'*70)
def consum(list):
    total = 0
    consum_list = []
    for ele in list:
        total += ele
        consum_list.append(total)
    return consum_list

print(consum([1,2,3]))
print(consum([2,3,5,7]))

#Ex10.3
print('')
print('[Ex10.3]' + '-'*70)
def middle(list):
    if len(list)==1:
        return list
    list.pop(0)
    list.pop(len(list) - 1)
    return list

print(middle(['f','u','c','k']))
print(middle([1]))
print(middle([1,2,3]))

#Ex10.4
print('')
print('[Ex10.4]' + '-'*70)
def chop(list):
    list.pop(0)
    list.pop(len(list) - 1)

l = [1,2,3]
print(chop(l))
print(l)

#Ex10.5
print('')
print('[Ex10.5]' + '-'*70)
def is_sorted(list):
    return list == sorted(list)

l1 = [1,2,3]
l2 = [1,3,2]
print(is_sorted(l1))
print(is_sorted(l2))

#Ex10.6
print('')
print('[Ex10.6]' + '-'*70)
def is_anagram(s1,s2):
    lt1 = list(s1)
    lt2 =list(s2)
    if len(lt1) != len(lt2):
        return False
    for ele1 in lt1:
        if ele1 in lt2:
            lt2.remove(ele1)
        else:
            return False
    return True

print(is_anagram('unclear','nuclear'))
print(is_anagram('unclear','nuclearu'))
print(is_anagram('unclear','nucleau'))

#Ex10.7
print('')
print('[Ex10.7]' + '-'*70)
def has_duplicates(l):
    nl = list(l)
    nl.sort()
    for i in range(len(nl)-1):
        if nl[i] == nl[i+1]:
            return True
    return False

print(has_duplicates('good'))
print(has_duplicates('god'))

#Ex10.8
print('')
print('[Ex10.8]' + '-'*70)
import random
def generate_bd(num):
    bd  = []
    for i in range(num):
        bd.append(random.randint(1,365))
    #print(bd)
    return bd

def pb_sameBd(num_bd,num_simulation):
    count = 0
    for i in range(num_simulation):
        bd = generate_bd(num_bd)
        if has_duplicates(bd):
            count += 1
    pb = count/num_simulation
    print('The probability is: ',pb,'%')

pb_sameBd(23,1000)


#Ex10.9
print('')
print('[Ex10.9]' + '-'*70)
fin = open('/Users/gaomingjun/Desktop/thinkInPy2/Char9/word.txt')

def wordList_append(fin):
    l = []
    for line in fin:
        l.append(line.strip())
    fin.close()
    return l


#wordList_append(fin)

def wordList_plus(fin):
    l = []
    for line in fin:
        l = l + [line.strip()]
    fin.close()
    return l

#wordList_plus(fin)

#Ex10.10
print('')
print('[Ex10.10]' + '-'*70)

def in_bisect(word_list,target_val):
    word_list.sort()
    if len(word_list) == 0:
        return False

    i = len(word_list)//2
    if word_list[i] == target_val:
        return True
    elif word_list[i] < target_val:
        return in_bisect(word_list[i+1:],target_val)
    else:
        return in_bisect(word_list[:i],target_val)

word_list = wordList_append(fin)
print(in_bisect(word_list,'zygotc'))

#Ex10.11
print('')
print('[Ex10.11]' + '-'*70)
def reverse_pair(word_list):
    for word in word_list:
        if in_bisect(word_list,word[::-1]):
            print(word)
            print(word[::-1])

#reverse_pair(word_list)


#Ex10.12
print('')
print('[Ex10.12]' + '-'*70)

def interlock(word_list):
    for word in word_list:
        even = word[::2]
        odd = word[::1]
        if in_bisect(word_list,even) and in_bisect(word_list,odd):
            print(word,even,odd)

#interlock(word_list)