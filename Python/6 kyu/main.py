# # Multiples of 3 or 5: ------------------------------------------------------- #
# # If we list all the natural numbers below 10 that are multiples of 3 or 5, we
# # get 3, 5, 6 and 9. The sum of these multiples is 23.
# # Finish the solution so that it returns the sum of all the multiples of 3 or 5
# # below the number passed in.


# # My attempt
# def solution(number):
#     if number <= 0:
#         return 0
#     return sum(n for n in range(number) if n % 3 == 0 or n % 5 == 0)


# # Best Practice
# def solution(number):
#     return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)


# print(solution(10)). # 23

# # Stop gninnipS My sdroW!: --------------------------------------------------- #
# # Write a function that takes in a string of one or more words, and returns the
# # same string, but with all words that have five or more letters reversed
# # Just like the name of this Kata). Strings passed in will consist of only letters
# # and spaces. Spaces will be included only when more than one word is present.


# # My attempt
# def spin_words(sentence):
#     new_sentence = ""
#     for word in sentence.split():
#         print(word)
#         if len(word) >= 5:
#             new_sentence += " " + word[::-1]
#         else:
#             new_sentence += " " + word
#     return new_sentence[1:]


# # Best Practice
# def spin_words(sentence):
#     return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])


# print(spin_words("Hey fellow warriors"))  # "Hey wollef sroirraw"
