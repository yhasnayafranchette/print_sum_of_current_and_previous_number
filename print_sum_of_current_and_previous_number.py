#Exercise 2: Print the sum of the current number and the previous number
#Write a program to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.

def sum_of_current_and_previous_number():
    previous_number = 0

    for current_number in range(0,10):
        sum_of_two_numbers = current_number + previous_number
        print(f"The sum of current number {current_number} and previous number {previous_number} is: {sum_of_two_numbers}")
        previous_number = current_number

sum_of_current_and_previous_number()