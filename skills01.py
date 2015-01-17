# Things you should be able to do.

number_list = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
word_list = [ "What", "about", "the", "Spam", "sausage", "spam", "spam", "bacon", "spam", "tomato", "and", "spam"]

# Write a function that takes a list of numbers and returns a new list with only the odd numbers.
def all_odd(number_list):
    new_list = []
    for i in number_list:
        if i % 2 != 0:
            new_list.append(i)
    print new_list  
    return new_list

# # Write a function that takes a list of numbers and returns a new list with only the even numbers.
def all_even(number_list):
    new_list = []
    for i in number_list:
        if i % 2 == 0:
            new_list.append(i)
    print new_list
    return new_list

# Write a function that takes a list of strings and returns a new list with all strings of length 4 or greater.
def long_words(word_list):
    new_list = []
    for i in word_list:
        if len(i) >= 4:
            new_list.append(i)
    print new_list
    return new_list

# Write a function that finds the smallest element in a list of integers and returns it.
def smallest(number_list):
    smallest = min(number_list)
    print smallest
    return smallest

# Write a function that finds the largest element in a list of integers and returns it.
def largest(number_list):
    maximum = max(number_list) 
    print maximum
    return maximum

#largest(number_list)

# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(number_list):
    halved_list = []
    for each in number_list:
        int_number = float(each)
        halved_list.append(float(int_number / 2))
    print halved_list
    return halved_list

# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lengths(word_list):
    new_list = []
    for i in word_list:
        new_list.append(len(i))
    print new_list
    return new_list

#word_lengths(word_list)

# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(number_list):
    
    counter = 0

    for each in number_list:
        counter += each
    print counter
    return counter

#TODO with a list comprehension after finishing the exercises 
#Solving this with a list comprehension would require an additional lambda function,
#Don't worry about for now but do ask later
# counter = [____ for each in number_list]

#sum_numbers(number_list)

# Write a function that multiplies all the numbers in a list together.
def mult_numbers(number_list):
    counter = 1
    for each in number_list:
        counter *= each
    print counter
    return counter

#mult_numbers(number_list)

# Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
#Could iterate through the list and append each list item on to a new string
def join_strings(word_list):
    new_string = ""
    for each in word_list:
        new_string += each
    print new_string
    return new_string

# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(number_list):

    the_average = sum(number_list) / len(number_list)

    print the_average
    return the_average

average(number_list)