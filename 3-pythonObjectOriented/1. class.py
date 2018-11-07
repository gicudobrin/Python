# The class keyword lets us define a class. We use it just like we do the def keyword for making functions. Class definitions are blocks like function definitions.

# class NewClass:
# Inside of the class, variables are called attributes.

# class NewClass:
#     name_attribute = "Kenneth"
# And functions that are defined inside of a class are called methods.

# class NewClass:
#     name_attribute = "Kenneth"

#     def name_method(self):
#         return self.name
# Whenever we call a class, it creates an instance. Each instance has full access to the all of the attributes and methods of the class.

# new_instance = NewClass()
# new_instance.name_method()


# Let's make a class:

# class NewClass:
#     name_attribute = "Kenneth"

#     def name_method(self):
#        print self.name_attribute

# new_instance = NewClass()
# new_instance.name_method()

import random

class Thief:
	sneaky = True

	def __init__(self, name, sneaky = True, **kwargs):
		self.name = name
		self.sneaky = sneaky

	def pickpocket(self):
		return self.sneaky and bool(random.randomint(0,1))
		
	def hide(self, light_level):
		return self.sneaky and light_level < 10