# # Vowel Count: --------------------------------------------------------------- #
# # Return the number (count) of vowels in the given string.
# # We will consider a, e, i, o, u as vowels for this Kata (but not y).
# # The input string will only consist of lower case letters and/or spaces.


# # My attempt
# def get_count(sentence):
#     vowels = ["a", "e", "i", "o", "u"]
#     return sum(1 for letter in sentence if letter in vowels)


# # Best Practice
# def getCount(inputStr):
#     return sum(1 for let in inputStr if let in "aeiouAEIOU")


# print(get_count("aeiou"))
# print(get_count("y"))

# # Disemvowel Trolls: --------------------------------------------------------- #
# # Trolls are attacking your comment section!
# # A common way to deal with this situation is to remove all of the vowels
# # from the trolls' comments, neutralizing the threat.
# # Your task is to write a function that takes a string and return a new
# # string with all vowels removed.
# # For example, the string "This website is for losers LOL!"
# # would become "Ths wbst s fr lsrs LL!".
# # Note: for this kata y isn't considered a vowel.


# # My attempt
# def disemvowel(string_):
#     vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
#     string = ""
#     for letter in string_:
#         if letter in vowels:
#             continue
#         string += letter
#     return string


# # Best Practice
# def disemvowel(string):
#     return "".join(c for c in string if c.lower() not in "aeiou")


# print(disemvowel("This website is for losers LOL!"))

# # Square Every Digit: -------------------------------------------------------- #
# # Welcome. In this kata, you are asked to square every digit of a number
# # and concatenate them.
# # For example, if we run 9119 through the function, 811181 will come out,
# # because 92 is 81 and 12 is 1. (81-1-1-81)
# # Example #2: An input of 765 will/should return 493625 because 72 is 49, 62
# # is 36, and 52 is 25. (49-36-25)
# # Note: The function accepts an integer and returns an integer.
# # Happy Coding!


# # My attempt
# def square_digits(num):
#     return int("".join(str(int(n) ** 2) for n in str(num)))


# # Best Practice
# def square_digits(num):
#     ret = ""
#     for x in str(num):
#         ret += str(int(x) ** 2)
#     return int(ret)


# print(square_digits(9119))

# # Highest and Lowest: -------------------------------------------------------- #
# # In this little assignment you are given a string of space separated numbers,
# # and have to return the highest and lowest number.
# # Notes
# # All numbers are valid Int32, no need to validate them.
# # There will always be at least one number in the input string.
# # Output string must be two numbers separated by a single space,
# # and highest number is first.


# # My attempt
# def high_and_low(numbers):
#     numbers = numbers.split(" ")
#     max = int(numbers[0])
#     min = int(numbers[0])
#     for number in numbers:
#         num_int = int(number)
#         if num_int > max:
#             max = num_int
#         if num_int < min:
#             min = num_int
#     return f"{max} {min}"


# # Best Practice
# def high_and_low(numbers):
#     numbers = [int(c) for c in numbers.split(" ")]
#     return f"{max(numbers)} {min(numbers)}"


# # print(high_and_low("1 2 3 4 5"))  # return "5 1"
# # print(high_and_low("1 2 -3 4 5"))  # return "5 -3"
# # print(high_and_low("1 9 3 4 -5"))  # return "9 -5"

# # Descending Order: ---------------------------------------------------------- #
# # Your task is to make a function that can take any non-negative integer as an
# # argument and return it with its digits in descending order. Essentially,
# # rearrange the digits to create the highest possible number.


# # My attempt
# def descending_order(num):
#     list_num = [n for n in str(num)]
#     list_num.sort(reverse=True)
#     return int("".join(list_num))


# # Best Practice
# def Descending_Order(num):
#     return int("".join(sorted(str(num), reverse=True)))


# print(descending_order(42145))

# # Get the Middle Character: -------------------------------------------------- #
# # You are going to be given a word. Your job is to return the middle character
# # of the word. If the word's length is odd, return the middle character. If the
# # word's length is even, return the middle 2 characters.


# # My attempt
# def get_middle(s):
#     print(s)
#     if len(s) % 2:
#         return s[len(s) // 2]
#     else:
#         return "".join((s[(len(s) // 2) - 1], s[len(s) // 2]))


# # Best Practice
# def get_middle(s):
#     print(s)
#     print((len(s) - 1) // 2)
#     i = (len(s) - 1) // 2
#     print(s[i])
#     print(s[-i])
#     return s[i:-i] or s


# print(get_middle("test"))  # 4
# print(get_middle("testing"))  # 7
# print(get_middle("A"))  # 1

# # List Filtering: ------------------------------------------------------------ #
# # In this kata you will create a function that takes a list of non-negative
# # integers and strings and returns a new list with the strings filtered out.


# # My attempt, Best Practice
# def filter_list(l):
#     return [item for item in l if isinstance(item, int)]


# print(filter_list([1, "a", "b", 0, 15]))  # [1,0,15]

# Mumbling: ------------------------------------------------------------------ #
# This time no story, no theory. The examples below show you how to write
# function accum:


def accum(st):
    i = 0
    ret_st = ""
    for item in st:
        i += 1


print(accum("RqaEzty"))
