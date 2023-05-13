"""

Write a program to read in text from a file and replace every occurrence of the term ‘wolf’ with the term ‘elephant’. The following are the steps to take:
    Download aesop-wolf-dog.txt from Brightspace
    Open file and assign variable name 'f'
    Read the contents of the file
    Close the connection to the file
    Print the contents of the file
Modify your script so that the word ‘wolf’ occurring in any case will be replaced with the world ‘elephant’.
Print the length of the contents of the file
Print out a list of all the occurrences of vowels in the content of your file
Write updated text to a new file

"""

# %%
with open(r'/home/zod/Documents/Git-Projects/ML-Projects/Labs/aesop-wolf-dog.txt', "r") as f:
    data = f.read()
    data2 = data
print(data)

# %%

data = data.replace('wolf', 'elephant')
print(data)

# %%

print(len(data2))

# %%

vowels = []
for i in data2.lower():
    if i in ['a', 'e', 'i', 'o', 'u']:
        vowels.append(i)

print(vowels)

# %%

with open(r'aesop-elephant-dog.txt', "w") as file:
    file.write(data)
