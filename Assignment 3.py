#!/usr/bin/env python
# coding: utf-8

# # Q1. Which keyword is used to create a function? Create a function to return a list of odd numbers in the range of 1 to 25.

# 'def' keyword is used to create a function

# In[25]:


def get_odd_numbers():
    odd_numbers = []
    for num in range(1, 26):
        if num % 2 != 0:
            odd_numbers.append(num)
    return odd_numbers


# In[27]:


result = get_odd_numbers()
print(result)


# # Why *args and **kwargs is used in some functions? Create a function each for *args and **kwargs to demonstrate their use. 

# The *args and **kwargs are used in Python functions to handle variable-length arguments.
# 
# The *args parameter allows a function to accept any number of positional arguments as a tuple.
# The **kwargs parameter allows a function to accept any number of keyword arguments as a dictionary. 

# In[28]:


def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total


# In[29]:


result = sum_numbers(1,2,3)


# In[30]:


print(result)


# In[31]:


def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(name="John", age=25, city="New York")


# # Q3. What is an iterator in python? Name the method used to initialise the iterator object and the method used for iteration. Use these methods to print the first five elements of the given list [2, 4, 6, 8, 10, 12, 14, 16, 18, 20].

# In Python, an iterator is an object that implements the iterator protocol, which consists of the __iter__() and __next__() methods. Iterators are used to iterate over elements in a container or sequence, such as a list, tuple, or dictionary, one at a time.

# The __iter__() method is used to initialize the iterator object. It is called when the iterator is created and should return the iterator object itself.
# 
# The __next__() method is used for iteration. It is called to get the next item from the iterator. 

# In[32]:


numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
iterator = iter(numbers)

for _ in range(5):
    element = next(iterator)
    print(element)


# # Q4. What is a generator function in python? Why yield keyword is used? Give an example of a generator function.

# In Python, a generator function is a special type of function that generates a sequence of values using the yield keyword instead of the return keyword. When a generator function is called, it returns an iterator object that can be iterated over to retrieve the generated values one at a time. The generator function can pause its execution and remember its state between iterations, making it memory-efficient and suitable for generating large or infinite sequences.

# In[33]:


def square_generator(n):
    for i in range(n):
        yield i ** 2


# In[34]:


squares = square_generator(5)

for num in squares:
    print(num)


# # Q5. Create a generator function for prime numbers less than 1000. Use the next() method to print the first 20 prime numbers.

# In[36]:


def prime_generator():
    primes = []
    num = 2

    while True:
        if all(num % prime != 0 for prime in primes):
            yield num
            primes.append(num)
        num += 1


# In[37]:


prime_gen = prime_generator()

for _ in range(20):
    prime = next(prime_gen)
    print(prime)


# # Q6. Write a python program to print the first 10 Fibonacci numbers using a while loop.
# 

# In[38]:


def fibonacci_sequence(n):
    fibonacci = [0, 1]
    while len(fibonacci) < n:
        next_num = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(next_num)
    return fibonacci

n = 10
fibonacci_numbers = fibonacci_sequence(n)

for num in fibonacci_numbers:
    print(num)


# # Q7. Write a List Comprehension to iterate through the given string: ‘pwskills’.
# # Expected output: ['p', 'w', 's', 'k', 'i', 'l', 'l', 's']
# 

# In[39]:


string = 'pwskills'
result = [char for char in string]
print(result)


# # Q8. Write a python program to check whether a given number is Palindrome or not using a while loop.
# 

# In[41]:


def is_palindrome(number):
    original_number = number
    reverse = 0

    while number > 0:
        remainder = number % 10
        reverse = (reverse * 10) + remainder
        number = number // 10

    if original_number == reverse:
        return True
    else:
        return False

number = int(input("Enter a number: "))
if is_palindrome(number):
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")


# # Q9. Write a code to print odd numbers from 1 to 100 using list comprehension.
# # Note: Use a list comprehension to create a list from 1 to 100 and use another List comprehension to filter out odd numbers.

# In[42]:


odd_numbers = [num for num in range(1, 101) if num % 2 != 0]
print(odd_numbers)

