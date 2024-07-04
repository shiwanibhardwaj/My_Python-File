# indexing....(indexing start from 0)
str = "Hello shivani"
print(str[2])

# slicing....(accessing parts of a string)
# str[starting_index:ending_index](ending index is not included)
print(str[1:4])
print(str[0:len(str)])

# step argument...
print(str[1:8:2])
print(str[1::2])

# negetive step argument...
print(str[8::-1])
print(str[8:1:-2])
# negetive index(negetive indexing start from -1)
print(str[-7:-2])

# string functions......
print(len("shivani"))
# string methods .....
name = "shivani"
# this methode will insert * on left or right side of word(lenght of name is 7 or star is 4,so th total length is 11).
print(name.center(11, "*"))
name = input("enter your name:")
print(name.center(len(name)+8, "*"))
print(name.title())  # it will convert 1st letter into capital letter.
print(str.lower())  # it will convert all letter into small letter
print(str.upper())  # it will convert all letter into capital letter
print(str.endswith("ni"))  # returns true if string is end with substr
print(str.capitalize())  # capitalize 1st char
print(str.replace("s", "d"))  # replace all occurrences of old with new
print(str.find("shivani"))  # returns 1st index of 1st occurrence
print(str.count("h"))  # counts the occurrence of substr in string

# string formatting in python 3 ....
name = "shivani"
age = 24
print("hello {} your age is {}".format(name, age))
print("hello {} your age is {}".format(name, age+2))

# string formatting in python 3.6 ....
print(f"hello {name} your age is {age}")
print(f"hello {name} your age is {age+3}")

# reversing name ....
n = input("enter your name : ")
print(n[-1::-1])

# question....
name1, char = input("enter your name and character:-(seperated by comma)").split(",")
print(f"your name is {name1} and The given number of charecter is { name.count(char)}")

space = "      shivani    "
dots = "............"
# strip method is used to remove spaces from both sides of text.
print(space.strip()+dots)
# lstrip method is used to remove spaces form left side of text.
print(space.lstrip()+dots)
# rstrip method is used to remove spaces form right side of text.
print(space.rstrip()+dots)
space = "      shivani     kumari     dubey     "
# if we have so many spaces in our sentences or we want to
# remove so we can use "replace(" ","")"method.
print(space.replace(" ", ""))
