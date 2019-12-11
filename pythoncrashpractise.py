# s=[value for value in range(0,20)]
# print(s)


# s=[value for value in range(0,10**6)]
# print(s)

# s=[value for value in range(1,20,2)]
# print(s)

# s=[value**3 for value in range(10)]
# print(s)
# for i in s[5:]:
#     print(i)

# alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
# print("Original x-position: " + str(alien_0['x_position']))


# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     alien_0['x_position'] = alien_0['x_position'] + 10
# else:
#     x_increment = 3
# print("New x-position: " + str(alien_0['x_position']))
# print(alien_0)

# my = {
#     "name":"sai",
#     "age":"23",
#     "city":"knr"
# }
# for key,value in my.items():
#     print("key :"+ key)
#     print("value :"+ value)
#     print()



# favorite_languages = {
#  'jen': 'python',
#  'sarah': 'c',
#  'edward': 'ruby',
#  'phil': 'python',
#  }
# for name, language in favorite_languages.items():
#     print(name.title() + "'s favorite language is " +
#  language.title() + ".")

# favorite_languages = {
#  'jen': 'python',
#  'sarah': 'c',
#  'edward': 'ruby',
#  'phil': 'python',
#  }
# friends = ['phil', 'sarah']
# for name in favorite_languages.keys():
#     print(name.title())
#     if name in friends:
#         print(" Hi " + name.title() +
#          ", I see your favorite language is " +
#          favorite_languages[name].title() + "!")

# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}
# aliens = [alien_0, alien_1, alien_2]
# for alien in aliens:
#     print(alien)

# pizza = {
#  'crust': 'thick',
#  'toppings': ['mushrooms', 'extra cheese'],
#  }
#  'edward': ['ruby', 'go'],
# print("You ordered a " + pizza['crust'] + "-crust pizza " + 
# "with the following toppings:"2)
# for topping in pizza['toppings']:
#     print("\t" + topping)


# favorite_languages = {
#  'jen': ['python', 'ruby'],
#  'sarah': ['c'],
#  'phil': ['python', 'haskell'],
#  }
# for name, languages in favorite_languages.items():
#     print("\n" + name.title() + "'s favorite languages are:")
#     for language in languages:
#         print("\t" + language.title())



# s1 = [
#     {
#         "age":18,
#         "weight": 35
#     },
#     {
#         "age":19,
#         "weight": 36
#     },
#     {
#         "age":18,
#         "weight": 34
#     },
#     {
#         "age":17,
#         "weight": 35
#     }

# ]
# s2=[]
# for i in s1:
#     for key,value in i.items():
#         if value == i["age"]:
#             print(i["age"])
        


        




# from collections import defaultdict
# intermediate = defaultdict(list)

# for subdict in s1:
#     for key, value in subdict.items():
#         intermediate[key].append(value)
# print(intermediate)


# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "

# active = True
# while active:
#     message = input(prompt)
#     if message == "quit":
#         active = False
#     else:
#         print(message)


# x = 1
# while x <= 5:
#  print(x)
#  x += 1


# unregistered = ["sai","krishna","chinni","saikrishna"]
# registered = [ ]
# while unregistered:
#     registeredone = unregistered.pop()
#     print("registering : " , registeredone)
#     registered.append(registeredone)

# print(registered)
# print(unregistered)    


# class dog():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def sitting(self):
#         sitting = self.name + " is sitting beside you"
#         age= "it is " + str(self.age )+ " old"
 

# my_dog = dog("wille",8)
# print(my_dog.sitting())

# class Car():
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year

#     def get_descriptive_name(self):
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name.title()

# my_new_car = Car('audi', 'a4', 2016)
# print(my_new_car.get_descriptive_name())


# class Car():
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0

#     def get_descriptive_name(self):
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name.title()
#     def read_odometer(self):
#         print("This car has " + str(self.odometer_reading) + " miles on it.")

    
#     def update_odometer(self, mileage):

#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")
    

#     def increment_odometer(self, miles):
#         self.odometer_reading += miles

# my_used_car = Car('subaru', 'outback', 2013)
# print(my_used_car.get_descriptive_name())
# my_used_car.update_odometer(23)
# my_used_car.read_odometer()
# my_used_car.increment_odometer(100)
# my_used_car.read_odometer()
# my_used_car.update_odometer(3)


# class Car():
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0

#     def get_descriptive_name(self):
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name.title()
#     def read_odometer(self):
#         print("This car has " + str(self.odometer_reading) + " miles on it.")

    
#     def update_odometer(self, mileage):

#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")
    

#     def increment_odometer(self, miles):
#         self.odometer_reading += miles
# class ElectricCar(Car):
#     def __init__(self, make, model, year):
#         super().__init__(make, model, year)
#         self.battery_size = 70
#     def describe_battery(self):
#         print("This car has a " + str(self.battery_size) + "-kWh battery.")


# my_tesla = ElectricCar('tesla', 'model s', 2016)
# print(my_tesla.get_descriptive_name())
# my_tesla.describe_battery()


# def beautifulDays(i, j, k):
#     count =0
#     for day in range(i,j):
#         d = (i-int(str(i)[::-1]))
#         if d == int(d):
#             count +=1
#     return count

# beautifulDays(20,23,6)


# from itertools import permutations
# a =  [''.join(p) for p in permutations('dkhc')]
# print(a)

# s = "lmno"
# for i in range(len(s)-1)[::-1]:
#     if (s[i] <s[i+1]) :
#         for j in range(i+1,len(s))[::-1]:
#             if (s[i]< s[j]):
#                 lis = list(s)
#                 lis[i],lis[j]=lis[j],lis[i]
#                 print("".join(lis[:i+1]+lis[i+1:][::-1]))

# s = "aaabccddd"
# s =list(s)
# for i in range(0,len(s)-2,2):
#     if s[i]==s[i+1]:
#         del s[i]
#         del s[i+1]
# print(s)
    

# #Recursive solution for N-Queens problem in Python
# from math import *
# import sys

# x = {}
# n = int(sys.argv[1])

# def place(k, i):
#     if (i in x.values()):
#         return False
#     j = 1
#     while(j < k):
#         if abs(x[j]-i) == abs(j-k):
#             return False
#         j+=1
#     return True
# def clear_future_blocks(k):
#     for i in range(k,n+1):
#        x[i]=None
# def NQueens(k):
#     for i in range(1, n + 1):
#         clear_future_blocks(k)
#         if place(k, i):
#             x[k] = i
#             if (k==n):
#                 for j in x:
#                     print( x[j])
#                 print ('---------')
#             else:
#                 NQueens(k+1)


# NQueens(1)

a = [[1,2],[3,4]]
print(sum(a,[]))