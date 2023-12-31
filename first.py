#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 12:14:48 2023

@author: prestige
"""

# %%

import time
for iteration in range(5):
    count = 0
    while True:
        for letter in "hello, world":
            count += 1
        print("Iteration " + str(iteration) + "; count is: " + str(count))
        break


# %%

s = 'azcbobobegghaklbobob'
substring = 'bob'
count = 0

for i in range(len(s) - len(substring) + 1):
    print(s[i:i + 3])

# %%


s = 'azcbobobegghakl'

currentString = s[0]
answer = s[0]

for l in range(1, len(s)):
    if s[l] >= s[l-1]:
        currentString += s[l]
    else:
        currentString = s[l]

    if len(answer) < len(currentString):
        answer = currentString

print(s[0: 3])


# %%


## DO NOT MODIFY THE IMPLEMENTATION OF THE Person CLASS ##
class Person(object):
    def __init__(self, name):
        # create a person with name name
        self.name = name
        try:
            firstBlank = name.rindex(' ')
            self.lastName = name[firstBlank+1:]
        except:
            self.lastName = name
        self.age = None

    def getLastName(self):
        # return self's last name
        return self.lastName

    def setAge(self, age):
        # assumes age is an int greater than 0
        # sets self's age to age (in years)
        self.age = age

    def getAge(self):
        # assumes that self's age has been set
        # returns self's current age in years
        if self.age == None:
            raise ValueError
        return self.age

    def __lt__(self, other):
        # return True if self's name is lexicographically less
        # than other's name, and False otherwise
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName

    def __str__(self):
        # return self's name
        return self.name


class USResident(Person):
    """ 
    A Person who resides in the US.
    """

    def __init__(self, name, status):
        """ 
        Initializes a Person object. A USResident object inherits 
        from Person and has one additional attribute:
        status: a string, one of "citizen", "legal_resident", "illegal_resident"
        Raises a ValueError if status is not one of those 3 strings
        """
        # Write your code here
        super().__init__(name)
        if status == "citizen" or status == "legal_resident" or status == "illegal_resident":
            self.status = status
        else:
            raise ValueError

    def getStatus(self):
        """
        Returns the status
        """
        # Write your code here
        return self.status


a = USResident('Tim Beaver', 'citizen')
print(a.getStatus())
b = USResident('Tim Horton', 'non-resident')


# %%

maxNumber = 10
maxFactor = 10

for number in range(1, maxNumber + 1):
    for factor in range(1, maxFactor + 1):
        #print(str(number) + " * " + str(factor) + " = " + str(factor*number))
        print(f"{number} * {factor} = {number*factor}", end="\t")
    print()

# %%

for iteration in range(1, 5):
    count = 0
    for letter in "hello, world":
        count += 1

    if iteration % 2 == 0:
        break
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1

# %%

x = 5
epsilon = 1
guess = 0

while abs(guess**2-x) >= epsilon:
    if guess <= x:
        guess += 1
    else:
        break

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))
# %%

print("Please think of a number between 0 and 100!")

# At the start the highest the number could be is 100 and the lowest is 0.
hi = 100
lo = 0
guessed = False

# Loop until we guess it correctly
while not guessed:
    # Bisection search: guess the midpoint between our current high and low guesses
    guess = (hi + lo)//2
    print("Is your secret number " + str(guess) + "?")
    user_inp = input(
        "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

    if user_inp == 'c':
        # We got it right!
        guessed = True
    elif user_inp == 'h':
        # Guess was too high. So make the current guess the highest possible guess.
        hi = guess
    elif user_inp == 'l':
        # Guess was too low. So make the current guess the lowest possible guess.
        lo = guess
    else:
        print("Sorry, I did not understand your input.")

print('Game over. Your secret number was: ' + str(guess))

# %%

l = 0
h = 100
ans = (h + l)//2

while True:
    print
    print(f"Is your secret number {ans}?")
    res = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if res == "h":
        h = ans
        ans = (ans+l)//2
    elif res == "l":
        l = ans
        ans = (l + h)//2
    elif res == "c":
        print(f"Game over. Your secret number was: {ans}")
        break
    else:
        print("Sorry, I did not understand your input.")

# %%


def iterPower(base, exp):
    if exp == 0:
        return 1

    answer = 1

    for i in range(1, exp+1):
        answer = base * answer

    return answer


print(iterPower(9, 0))

# %%


def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    # Your code here

    if exp == 0:
        return 1

    return base * recurPower(base, exp - 1)


print(recurPower(2, 3))

# %%


def gcdIter(a, b):
    start = min(a, b)
    answer = 0

    for i in range(0, start + 1):
        if a % i == 0 and b % i == 0:
            answer = i

    return answer


print(gcdIter(6, 6))

# %%


def gcdRecur(a, b):
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)


print(gcdRecur(2, 4))

# %%
aStr = 'abcdefghijklmnopqrstuvwxyz'
aStr[13: -1]

# %%


def isIn(char, aStr):

    lenOfAStr = len(aStr)

    if lenOfAStr == 0:
        return False

    middleChar = lenOfAStr//2

    if aStr[middleChar] == char:
        return True

    elif aStr[middleChar] > char:
        return isIn(char, aStr[:middleChar])

    elif aStr[middleChar] < char:
        return isIn(char, aStr[middleChar + 1:])

    else:
        return False


isIn('i', 'abcdefghijklmnopqrstuvwxyz')
# %%

balance = 4773
annualInterestRate = 0.2
lowestPayment = 440


for i in range(12):
    unpaidBalance = balance - lowestPayment
    balance = unpaidBalance + annualInterestRate/12.0*unpaidBalance

print('Remaining balance: ' + str(round(balance, 2)))


# %%
balance = 3329
annualInterestRate = 0.2

# Result Your Code Should Generate:
# -------------------
# Lowest Payment: 310

LowestPayment = 0
print('Lowest Payment:', round(LowestPayment))

# %%
balance = 4773
annualInterestRate = 0.2


def findLowestPayment(balance, annualInterestRate):

    lowestPayment = 0.01

    while True:
        abstractBalance = balance

        for i in range(12):
            unpaidBalance = abstractBalance - lowestPayment
            abstractBalance = unpaidBalance + annualInterestRate/12.0*unpaidBalance

        if abstractBalance <= 0:
            return lowestPayment

        else:
            lowestPayment += 0.01


answer = round(findLowestPayment(balance, annualInterestRate), 2)
print(answer)

# %%

balance = 999999
annualInterestRate = 0.18


def findLowestPayment(balance, annualInterestRate):

    lowerBound = balance/12
    upperBound = balance*((1 + annualInterestRate/12)*12)/12

    while True:

        abstractBalance = balance
        lowestPayment = (lowerBound + upperBound)/2

        for i in range(12):
            unpaidBalance = abstractBalance - lowestPayment
            abstractBalance = unpaidBalance + annualInterestRate/12.0*unpaidBalance

        if round(abstractBalance) == 0:
            return lowestPayment

        elif abstractBalance > 0:
            lowerBound = lowestPayment

        else:
            upperBound = lowestPayment


answer = round(findLowestPayment(balance, annualInterestRate), 2)
print(answer)

# %%

l = 0
h = 100
ans = (h + l)//2

while True:
    print
    print(f"Is your secret number {ans}?")
    res = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if res == "h":
        h = ans
        ans = (ans+l)//2
    elif res == "l":
        l = ans
        ans = (l + h)//2
    elif res == "c":
        print(f"Game over. Your secret number was: {ans}")
        break
    else:
        print("Sorry, I did not understand your input.")

# %%


def oddTuples(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    ans = ()
    for i in range(len(aTup)):
        if i % 2 == 0:
            ans += (aTup[i],)

    return ans


oddTuples(('I', 'am', 'a', 'test', 'tuple'))


# %%

def oddTuples(aTuple):
    # Use slicing to create a new tuple with every other element starting from index 0
    print(len(aTuple))
    return aTuple[::2]


# Test the procedure
oddTuples(('I', 'am', 'a', 'test', 'tuple'))


# %%

aList = [0, 1, 2, 3, 4, 5]
bList = [0, 1, 2, 3, 4, 5]

print(aList is bList)

[1, 1, 2, 3, 5, 8, 13]

# %%


def applyEachTo(L, x):
    result = []
    for i in range(len(L)):
        result.append(L[i](x))
    return result


def square(a):
    return a*a


def halve(a):
    return a/2


def inc(a):
    return a+1


applyEachTo([inc, max], -3)

# %%

# -*- coding: utf-8 -*-


def lyrics_to_frequencies(lyrics):
    myDict = {}
    for word in lyrics:
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1
    return myDict


she_loves_you = ['she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
                 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
                 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',

                 'you', 'think', "you've", 'lost', 'your', 'love',
                 'well', 'i', 'saw', 'her', 'yesterday-yi-yay',
                 "it's", 'you', "she's", 'thinking', 'of',
                 'and', 'she', 'told', 'me', 'what', 'to', 'say-yi-yay',

                 'she', 'says', 'she', 'loves', 'you',
                 'and', 'you', 'know', 'that', "can't", 'be', 'bad',
                 'yes', 'she', 'loves', 'you',
                 'and', 'you', 'know', 'you', 'should', 'be', 'glad',

                 'she', 'said', 'you', 'hurt', 'her', 'so',
                 'she', 'almost', 'lost', 'her', 'mind',
                 'and', 'now', 'she', 'says', 'she', 'knows',
                 "you're", 'not', 'the', 'hurting', 'kind',

                 'she', 'says', 'she', 'loves', 'you',
                 'and', 'you', 'know', 'that', "can't", 'be', 'bad',
                 'yes', 'she', 'loves', 'you',
                 'and', 'you', 'know', 'you', 'should', 'be', 'glad',

                 'oo', 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
                 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
                 'with', 'a', 'love', 'like', 'that',
                 'you', 'know', 'you', 'should', 'be', 'glad',

                 'you', 'know', "it's", 'up', 'to', 'you',
                 'i', 'think', "it's", 'only', 'fair',
                 'pride', 'can', 'hurt', 'you', 'too',
                 'pologize', 'to', 'her',

                 'Because', 'she', 'loves', 'you',
                 'and', 'you', 'know', 'that', "can't", 'be', 'bad',
                 'Yes', 'she', 'loves', 'you',
                 'and', 'you', 'know', 'you', 'should', 'be', 'glad',

                 'oo', 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
                 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
                 'with', 'a', 'love', 'like', 'that',
                 'you', 'know', 'you', 'should', 'be', 'glad',
                 'with', 'a', 'love', 'like', 'that',
                 'you', 'know', 'you', 'should', 'be', 'glad',
                 'with', 'a', 'love', 'like', 'that',
                 'you', 'know', 'you', 'should', 'be', 'glad',
                 'yeah', 'yeah', 'yeah',
                 'yeah', 'yeah', 'yeah', 'yeah'
                 ]

beatles = lyrics_to_frequencies(she_loves_you)


def most_common_words(freqs):
    values = freqs.values()
    best = max(freqs.values())
    words = []
    for k in freqs:
        if freqs[k] == best:
            words.append(k)
    return (words, best)


(a, b) = most_common_words(beatles)
print(a)


def words_often(freqs, minTimes):
    result = []
    done = False
    while not done:
        temp = most_common_words(freqs)
        if temp[1] >= minTimes:
            result.append(temp)
            for w in temp[0]:
                del(freqs[w])  # remove word from dictionary
        else:
            done = True
    return result

#print(words_often(beatles, 5))

# %%


aDict = {'a': [15, 2], 'c': [18, 13, 10, 11, 10], 'b': [
    7, 3, 14, 1, 18, 5, 13, 10, 2, 11], 'd': [18]}


def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    bigest = 0
    ans = None

    if len(aDict) == 0:
        return ans

    for a in aDict:
        if len(aDict[a]) >= bigest:
            bigest = len(aDict[a])
            ans = a

    return a


biggest(aDict)

# %%

a = {}

print(len(a))

# %%


def a(aList):
    ans = []
    for item in aList:
        if len(item) <= 4:
            ans.append(item)
    return ans


aList = ['apple', 'cat', 'dog', 'banana']
a(aList)


def Slic_Rev_Conc(Tupl):
    part1 = Tupl[0:int(len(Tupl)/3)]
    part2 = Tupl[int(len(Tupl)/3):2*int(len(Tupl)/3)]
    part3 = Tupl[2*int(len(Tupl)/3):]
    return (part1[::-1]+part2[::-1]+part3[::-1])


Tupl = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
print(Slic_Rev_Conc(Tupl))


#d = {1: 10, 2:20, 3:30}
# dict_invert(d)

def dict_invert(d):
    return dict((v, [k])for k, v in d.items())


d = {1: 10, 2: 20, 3: 30}
dict_invert(d)

# %%


def closest_power(base, num):
    exponent = 0

    if num == 1:
        return exponent

    while True:

        if abs(base**exponent-num) <= abs(base**(exponent + 1) - num):
            return exponent

        exponent += 1


closest_power(4, 11)


# def closest_power(base, num):
#     result = 0
#     if base > num:
#         result = 0
#     elif base == num:
#         result = 1
#     else:
#         for i in range(2, num):
#             if abs(base**i-num) <= abs(base**(i+1)-num):
#                 result = i
#                 break
#     return result
# %%
x = "pi"
y = "pie"
x, y = y, x


def f(x):
    a = []
    while x > 0:
        a.append(x)
        f(x-1)


d = {'a': 'b'}
# print(d['b'])

# %%


def Square(x):
    return SquareHelper(abs(x), abs(x))


def SquareHelper(n, x):
    if n == 0:
        return 0
    return SquareHelper(n-1, x) + x


Square(100)

# %%

# For example, if L = [[1, 2], [3, 4], [5, 6, 7]] then
# deep_reverse(L) mutates L to be [[7, 6, 5], [4, 3], [2, 1]]


def deep_reverse(L):
    ans = []

    for i in reversed(L):
        subAns = []
        for num in reversed(i):
            subAns.append(num)
        ans.append(subAns)

    L[:] = ans


L = [[1, 2], [3, 4], [5, 6, 7]]
deep_reverse(L)

print(L)

# %%


def uniqueValues(aDict):
    ans = []
    listOfvalues = []

    if len(aDict) == 0:
        return ans

    for v in aDict.values():
        listOfvalues.append(v)

    for k in aDict.keys():
        if listOfvalues.count(aDict[k]) > 1:
            continue
        else:
            ans.append(k)

    ans.sort()
    return ans


uniqueValues({1: 1, 2: 1, 3: 3})

# %%


def sum_of_digits(N):
    # Base case: If N is a single-digit number, return N
    if N < 10:
        return N

    # Recursive case: Calculate the sum of digits of N by
    # adding the last digit to the sum of digits of the rest
    last_digit = N % 10
    rest_of_digits = N // 10
    return last_digit + sum_of_digits(rest_of_digits)


# Example usage:
N = 12345
result = sum_of_digits(N)
print(result)  # Output: 15
# %%


def f(i):
    return i + 2


def g(i):
    return i > 5


def applyF_filterG(L, f, g):
    """
    Assumes L is a list of integers
    Assume functions f and g are defined for you. 
    f takes in an integer, applies a function, returns another integer 
    g takes in an integer, applies a Boolean function, 
        returns either True or False
    Mutates L such that, for each element i originally in L, L contains  
        i if g(f(i)) returns True, and no other elements
    Returns the largest element in the mutated L or -1 if the list is empty
    """
    # Your code here

    newL = []

    if len(L) == 0:
        return -1

    for i in L:
        if g(f(i)):
            newL.append(i)

    L[:] = newL

    return max(L)


L = [0, -10, 5, 6, -4]
print(applyF_filterG(L, f, g))
print(L)


# %%
def SquareHelper(n, x):
    if n == 0:
        return 0
    return SquareHelper(n-1, x) + x


def Square(x):
    return SquareHelper(abs(x), abs(x))


Square(1)


# %%

def fancy_divide(numbers, index):
    try:
        denom = numbers[index]
        for i in range(len(numbers)):
            numbers[i] /= denom
    except IndexError:
        fancy_divide(numbers, len(numbers) - 1)
    except ZeroDivisionError:
        print("-2")
    else:
        print("1")
    finally:
        print("0")


fancy_divide([0, 2, 4], 0)


# %%


def fancy_divide(list_of_numbers, index):
    denom = list_of_numbers[index]
    return [simple_divide(item, denom) for item in list_of_numbers]


def simple_divide(item, denom):
    try:
        return item / denom
    except ZeroDivisionError:
        return []


fancy_divide([0, 2, 4], 0)

# %%


def normalize(numbers):
    max_number = max(numbers)
    for i in range(len(numbers)):
        numbers[i] /= float(max_number)
    return numbers


try:
    normalize([0, 0, 0])
except ZeroDivisionError:
    print('Invalid maximum element')

# %%


class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'

    def __eq__(self, other):
        if isinstance(other, Coordinate):
            return self.getX() == other.getX() and self.getY() == other.getY()
        return False

    def __repr__(self):
        return 'Coordinate({},{})'.format(self.getX(), self.getY())


c1 = Coordinate(7, 8)
c2 = Coordinate(7, 8)

print(repr(c1))

# %%


class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self"""
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'

    def intersect(self, other):

        intersect = []
        if isinstance(other, intSet):
            if len(self.vals + other.vals) == 0:
                return {}
            else:
                for el in self.vals:
                    if el in other.vals:
                        intersect.append(el)
                return '{' + ','.join([str(e) for e in intersect]) + '}'

    def __len__(self):
        return len(self.vals)


a = intSet()
a.insert(1)
a.insert(2)
a.insert(2)

b = intSet()
b.insert(1)
b.insert(2)
b.insert(3)

a.intersect(b)

print(len(a))

# %%


class Spell(object):
    def __init__(self, incantation, name):
        self.name = name
        self.incantation = incantation

    def __str__(self):
        return self.name + ' ' + self.incantation + '\n' + self.getDescription()

    def getDescription(self):
        return 'No description'

    def execute(self):
        print(self.incantation)


class Accio(Spell):
    def __init__(self):
        Spell.__init__(self, 'Accio', 'Summoning Charm')


class Confundo(Spell):
    def __init__(self):
        Spell.__init__(self, 'Confundo', 'Confundus Charm')

    def getDescription(self):
        return 'Causes the victim to become confused and befuddled.'


def studySpell(spell):
    print(spell)


# spell = Accio()
# spell.execute()
# studySpell(spell)
studySpell(Confundo())

# %%


class A(object):
    def __init__(self):
        self.a = 1

    def x(self):
        print("A.x")

    def y(self):
        print("A.y")

    def z(self):
        print("A.z")


class B(A):
    def __init__(self):
        A.__init__(self)
        self.a = 2
        self.b = 3

    def y(self):
        print("B.y")

    def z(self):
        print("B.z")


class C(object):
    def __init__(self):
        self.a = 4
        self.c = 5

    def y(self):
        print("C.y")

    def z(self):
        print("C.z")


class D(C, B):
    def __init__(self):
        C.__init__(self)
        B.__init__(self)
        self.d = 6

    def z(self):
        print("D.z")


obj = D()

print(obj.a)

# %%


def genPrimes():
    primes = []
    yield 2
    primes.append(2)

    candidate = 3

    while True:
        is_prime = True

        for prime in primes:
            if candidate % prime == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(candidate)
            yield candidate

        candidate += 2

# %%


a = [1, 2]
b = a[:]

b.append(3)

print(b)


# %%

def linearSearch(L, x):
    for e in L:
        if e == x:
            return True
    return False


time_start = time.time()
linearSearch([1, 2, 3], 2)
time_stop = time.time() - time_start
print("time = ", time_start, " : ", time_stop, "s")


# %%

def program1(x):
    total = 0
    for i in range(1000):
        total += i

    while x > 0:
        x -= 1
        total += x

    return total


print(program1(1))


# %%

def program3(L):
    totalSum = 0
    highestFound = None
    for x in L:
        print('hello')
        totalSum += x


program3([])


# %%

def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False


def newsearch(L, e):
    size = len(L)
    for i in range(size):
        if L[size-i-1] == e:
            return True
        if L[i] < e:
            return False
    return False


print(newsearch([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 2))

# %%


def swapSort(L):
    """ L is a list on integers """
    print("Original L: ", L)
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            if L[j] < L[i]:
                # the next line is a short
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j]
                print(L)
    print("Final L: ", L)


def modSwapSort(L):
    """ L is a list on integers """
    print("Original L: ", L)
    for i in range(len(L)):
        for j in range(len(L)):
            if L[j] < L[i]:
                # the next line is a short
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j]
                print(L)
    print("Final L: ", L)


swapSort([6, 2, 8, 3, 9, 4, 6, 3, 5])


# %%


'''
Q2: The provided McNuggets(n) function checks if you can purchase exactly
'n' McNuggets using combinations of 6, 9, and 20 McNugget packages.
It returns True if possible, or False if not.
'''
# 0.0/10.0 points (graded)
# McDonald’s sells Chicken McNuggets in packages of 6, 9 or 20 McNuggets.
# Thus, it is possible, for example, to buy exactly 15 McNuggets
# (with one package of 6 and a second package of 9),
# but it is not possible to buy exactly 16 McNuggets,
# since no non- negative integer combination of 6's, 9's and 20's
# add up to 16.
# To determine if it is possible to buy exactly n McNuggets,
# one has to find non-negative integer (can be 0) values of a, b, and c
# such that
# 6a + 9b + 20c = n
# Write a function, called McNuggets that takes one argument, n,
# and returns True if it is possible to buy a combination of 6, 9 and 20 pack
# units such that
# the total number of McNuggets equals n, and otherwise returns False.
# Hint: use a guess and check approach.


def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    # Your Code Here

    high = n//6+1

    if n != 0:
        for i in range(high):
            for j in range(high):
                for k in range(high):
                    if 6*k + 9*j + 20*i == n:
                        return True

            return False

    else:
        return False


print(McNuggets(15))
print(McNuggets(16))
print(McNuggets(0))
print(McNuggets(18))
print(McNuggets(66))

# %%


def sum_digits(s):
    """ assumes s a string
        Returns an int that is the sum of all of the digits in s.
          If there are no digits in s it raises a ValueError exception. """
    # Your code here
    answer = 0
    isDigits = False

    for i in s:
        if i.isdigit():
            answer += int(i)
            isDigits = True

    if not isDigits:
        raise ValueError

    return answer


sum_digits("a;d")


# %%

def primes_list(N):
    primeList = [2]

    if N < 2:
        return []

    for i in range(3, N + 1, 2):
        for p in primeList:
            if i % p == 0:
                break
        else:
            primeList.append(i)

    return primeList


print(primes_list(204))


# %%

def uniqueValues(aDict):
    valueCount = {}
    uniqueKeys = []

    for value in aDict.values():
        valueCount[value] = valueCount.get(value, 0) + 1

    for key, value in aDict.items():
        if valueCount[value] == 1:
            uniqueKeys.append(key)

    return sorted(uniqueKeys)


aDict1 = {1: 1, 3: 2, 6: 0, 7: 0, 8: 4, 10: 0}
aDict2 = {1: 1, 2: 1, 3: 1}


uniqueValues(aDict1)
# uniqueValues(aDict2)


# %%

class Container(object):
    """ Holds hashable objects. Objects may occur 0 or more times """

    def __init__(self):
        """ Creates a new container with no objects in it. I.e., any object 
            occurs 0 times in self. """
        self.vals = {}

    def insert(self, e):
        """ assumes e is hashable
            Increases the number times e occurs in self by 1. """
        try:
            self.vals[e] += 1
        except:
            self.vals[e] = 1

    def __str__(self):
        s = ""
        for i in sorted(self.vals.keys()):
            if self.vals[i] != 0:
                s += str(i)+":"+str(self.vals[i])+"\n"
        return s


class ASet(Container):
    def remove(self, e):
        """assumes e is hashable
           removes e from self"""
        # write code here
        if e in self.vals.keys():
            del self.vals[e]

    def is_in(self, e):
        """assumes e is hashable
           returns True if e has been inserted in self and
           not subsequently removed, and False otherwise."""
        # write code here
        if e in self.vals.keys():
            return True
        else:

            return False


d1 = ASet()
d1.insert(4)
print(d1.is_in(4))
d1.insert(5)
print(d1.is_in(5))
d1.remove(5)
print(d1.is_in(5))

'''

True
True
False

'''
