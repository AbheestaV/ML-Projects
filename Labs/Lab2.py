"""
1. Write a program that will print the 4th letter in the word ‘fantastic’
2. Write a program to calculate and print the length of a long piece of string
3. Write a program to print the last letter in the word ‘springtime’
4. This python scrip will display an error. Fix and run the code –
print (‘Sometimes I don’t get the bus to college’)
5. Define a function that will take any sentence and if the sentence length is
less than 10, it will print the sentence, otherwise it will print ‘this sentence is
too long’.
6. Define a function that could be part of a system to alert people to important
emails. The function should take a long string of text. It should check
whether the word ‘urgent’ is in the string. If it is, it should print a message
you better look at this email pretty quickly. If the word ‘urgent’ isn’t in the
message, do nothing

"""

# %%
print("fantastic"[4])

# %%
s = "The quick brown fox jumps over the lazy dog"
print(len(s))

# %%
s2 = "springtime"
print(s2[-1])

# %%
print("Sometimes I don’t get the bus to college")


# %%
def printer(a):
    if len(a) > 10:
        print("This sentence is too long to print.")
    else:
        print(a)


def urgent(b):
    if 'urgent' in b:
        print("you better look at this email pretty quickly")


def main():
    string1 = input("Enter string: ")
    printer(string1)
    urgent(string1)


if __name__ == "__main__":
    main()
