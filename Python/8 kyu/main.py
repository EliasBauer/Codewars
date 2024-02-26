# Even or Odd: --------------------------------------------------------------- #
# Create a function that takes an integer as an argument and returns "Even"
# for even numbers or "Odd" for odd numbers.

# My attempt, Best Practice
def even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"

print(even_or_odd(2)) # Even
print(even_or_odd(3)) # Odd
print(even_or_odd(6)) # Even

# Return Negative: ----------------------------------------------------------- #
# In this simple assignment you are given a number and have to make it negative.
# But maybe the number is already negative?

# My attempt
def make_negative(number):
    return -number if number >0 else number

# Best Practice
def make_negative( number ):
    return -abs(number)

print(make_negative(1))  # return -1
print(make_negative(-5)) # return -5
print(make_negative(0))  # return 0

# Multiply: ------------------------------------------------------------------ #
# This code does not execute properly. Try to figure out why.

# My attempt, Best Practice
def multiply(a, b):
    return a * b  # add return statement

# Sum of positive: ----------------------------------------------------------- #
# You get an array of numbers, return the sum of all of the positives ones.
# Example [1,-4,7,12] => 1 + 7 + 12 = 20
# Note: if there is nothing to sum, the sum is default to 0.

# My attempt
def positive_sum(arr):
    result = 0
    for num in arr:
        if num > 0:
            result += num
    return result

# Best Practice
def positive_sum(arr):
    return sum(x for x in arr if x > 0)

print(positive_sum([1,-4,7,12]))

# Reversed Strings: ---------------------------------------------------------- #
# Complete the solution so that it reverses the string passed into it.
# 'world'  =>  'dlrow'
# 'word'   =>  'drow'

# My attempt, Best Practice
def solution(string):
    return string[::-1]

print(solution("world"))

# Convert boolean values to strings 'Yes' or 'No'.: -------------------------- #
# Complete the method that takes a boolean value and return a "Yes" string for
# true, or a "No" string for false.

# My attempt, Best Practice
def bool_to_word(boolean):
    return "Yes" if boolean else "No"

print(bool_to_word(True))
print(bool_to_word(False))

# Convert a Number to a String!: --------------------------------------------- #
# We need a function that can transform a number (integer) into a string.
# What ways of achieving this do you know?
# Examples (input --> output):
# 123  --> "123"
# 999  --> "999"
# -100 --> "-100"

# My attempt, Best Practice
def number_to_string(num):
    return str(num)

print(type(number_to_string(123)))

# Opposite number: ----------------------------------------------------------- #
# Very simple, given a number (integer / decimal / both depending on the
# language), find its opposite (additive inverse).
# Examples:
# 1: -1
# 14: -14
# -34: 34

# My attempt, Best Practice
def opposite(number):
  return -number

print(opposite(14))
print(opposite(-34))

# Remove First and Last Character: ------------------------------------------- #
# It's pretty straightforward. Your goal is to create a function that removes
# the first and last characters of a string. You're given one parameter,
# the original string. You don't have to worry about strings
# with less than two characters.

# My attempt, Best Practice
def remove_char(s):
    return s[1:-1]

print(remove_char('eloquent'))
print(remove_char('country'))

# Square(n) Sum: ------------------------------------------------------------- #
# Complete the square sum function so that it squares each number passed into it
# and then sums the results together.
# For example, for [1, 2, 2] it should return 9

# My attempt, Best Practice
def square_sum(numbers):
    return sum(x**2 for x in numbers)

print(square_sum([1, 2, 2]))