#Create a function with multiple names
def my_funct(input):
    print(input)

my_var = my_funct
my_funct("spam-a-lot")
my_var("Spam-more")

#Create a function that uses one or more functions as arguments
def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def math(external_func, x, y):
    result = external_func(x, y)
    return result

math(add, 3, 8)
math(sub, 9, 4)

#Nest one or more functions
def person(name):
    def greeting():
        return "Surely, you can't be "
    greet = greeting() + name + "."
    return greet

print(person("King Arthur"))

# Use a function as a parameter for another function
def greeting(name):
    return "Surely, you can't be {}.".format(name)

def person(ext_func):
    title = "King of the Great Britain"
    return ext_func(title)

print(person(greeting))

#Use a function as a return value for a variable
def a_new_funct():
    def display_results():
        return "Blessed are the Greeks"
    return display_results

wise_saying = a_new_funct()
print(wise_saying())

#Use nested functions to utilize closure
def closure_example(name):
    def greet_me():
        return "Hail. " + name
    return greet_me

greet = closure_example("Bwian")
print(greet())




