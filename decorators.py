## NOTE! This file will not run as-is, without errors. It is meant as a collection of examples. You will need to comment out various sections to make each section run. Each 'executable' section is bounded by *******

# Intro example of a higher-order function
def read_my_name(func):
  name = "Fred"
  name_thing = func(name)

  return name_thing


def make_a_phrase(name):
  return f'Hi. My name is {name}'

# Pass a reference to one function into another
print(read_my_name(make_a_phrase))

# This is a reference (just the name of the function)
# make_a_phrase
# This is executing the function.
# make_a_phrase()

# ********************************************************************

# Another example of using one function to call any other function that's passed to it as an argument
def add(num1, num2):
  return num1 + num2

def subtract(num1, num2):
  return num1 - num2

def calculator(func):
  return func(3, 4)

# Note that we do not execute 'add' before passing it into 'calculator'. We a passing in a reference to add, which allows 'caluclator' to call it later
# calculator can now be told to add or subtract based on the name (reference) of the function passed to it
result = calculator(add)
print(result)
difference = calculator(subtract)
print(difference)

# ********************************************************************

# The interior_decorator function below is known as a "higher-order" function because it takes a function as an arg and also returns a function. We can do this in Python (and JS) because the langauge treats functions as "first class objects", meaning functions are treated like any other variable. For example, a function can be passed as an argument to other functions, can be returned by another function and can be assigned as a value to a variable.

def interior_decorator(func):
  def add_curtains():
    func()
    print("now my house has purple curtains")

  return add_curtains


def move_in():
  print("My house was empty, but...")


# bind returned function from interiorDecorator to new variable
new_house = interior_decorator(move_in)
print("This is the function itself", new_house)
new_house()

# def interior_decorator(func):
  def add_curtains():
    func()
    print("now my house has purple curtains")

  return add_curtains

# # In this example you just have to call the decorated function to get the expected results. Using @foo tells python to use the function as a decorator and to decorate the function defined on the next line
@interior_decorator
def move_in():
  print("My house was empty, but...")

# Now we just have to call 'move_in()' and it will run as a decorated function, meaning interior_decorator will execute and pass move_in automagically to it
move_in()

# ********************************************************************

# Passing args to the decorated function. Here we define interior_decorator in a slightly different way, allowing the function passed to it to accept an argument
def interior_decorator(func):

  def add_curtains(color):
    if color == "orange":
      color = "ugly-ass"
    func(color)
    print(f'now my house has {color} curtains')

  return add_curtains


@interior_decorator
def move_in(color):
  print("My house was empty, but...")


move_in("orange")
move_in("brown")
