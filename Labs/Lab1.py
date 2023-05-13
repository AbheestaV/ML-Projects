"""

Write a program using variables that will add any two numbers. Assign values to the variables. Print the result.

Write a program using variables that will divide any two numbers. Assign values to the variables. Print the result.

Create 3 variables and assign names of something like people or places to each variable. Write a program to create a meaningful sentence using the 3 variables.

Write a program that will take a long string of text and print it out, inserting a newline after the first 5 characters.

"""


def main():
    a = 5
    b = 10
    name1 = "Che"
    name2 = "Fidel"
    place = "Cuba"
    print("Answer 1: ", (a + b))
    print("Answer 2: ", (b / a))
    s = f"{name1} and {name2} are revolutionaries from {place}."
    print(s)
    print(f"{s[:5]}\n{s[5:]}")


if __name__ == "__main__":
    main()
