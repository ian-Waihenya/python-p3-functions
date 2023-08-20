#!/usr/bin/env python3

def greet_programmer():
  print("Hello, programmer!")
  
greet_programmer()


def greet(name):
  print(f"Hello, {name}!")
    
greet("Naureen")

def greet_with_default(name="programmer"):
  print(f"Hello, {name}!")
 
greet_with_default()

def add(num1, num2):
  print(f"{num1 + num2}")
add(1,2)
    

def halve(number):
    if not isinstance(number, (int, float)):
        return None
    
    return number / 2


input_number = 4
result = halve(input_number)
print("Half of", input_number, "is", result)

