"""
1. Write a function that adds up all elements in a list of integers
2. Write a function that adds up all elements in a list of lists of integers. Eg-
[[2,4],[0,5,9]]
3. Write a function that takes a list of numbers and returns a new list having
increased each number by 2.
4. Here is a list of years of birth for 4 siblings – [2011, 2008, 2005, 2004].
Define a function that will return a list of corresponding ages, rather than
years of birth.
5. Write a function that will take a short paragraph in the form of a string, and
will print out the words that have an even number of letters.
6. Define a function that will take a paragraph replace any spaces with a
comma.
7. Write a program that prompts a user to enter a word. The program then
checks if the word is a palindrome. That is – if the word is the same when
read forwards and backwards.

"""


# %%

def counter():
    s = 0
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in a:
        s += i
    print(s)


counter()


# %%

def counter2():
    s2 = 0
    b = [[2, 4], [0, 5, 9]]
    for i in b:
        for j in i:
            s2 += j
    print(s2)


counter2()


# %%

def age_c(ages):
    new_ages = []
    for yob in ages:
        new_ages.append(2023 - yob)
    return new_ages


print(age_c([2011, 2008, 2005, 2004]))


# %%

def even_letters(s):
    words = []
    new_words = []
    words = s.split(" ")
    for word in words:
        if len(word) % 2 == 0:
            new_words.append(word)
    return new_words


print(even_letters("The quick brown fox jumps over the lazy dog"))


# %%

def space_comma(s):
    return s.replace(" ", ",")


print(space_comma("The quick brown fox jumps over the lazy dog. This happens very often indeed"))


# %%

def palindromer(s):
    if s == s[::-1]:
        return "True"
    else:
        return "False"


print(palindromer("malayalam"))
print(palindromer("NotPalindrome"))
