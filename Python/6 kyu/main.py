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


# print(solution(10))
