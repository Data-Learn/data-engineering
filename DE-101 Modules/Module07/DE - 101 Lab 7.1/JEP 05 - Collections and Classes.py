# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC 
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>

# COMMAND ----------

# MAGIC %md
# MAGIC # Collections & Classes
# MAGIC ## ![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png) In this lesson you:<br>
# MAGIC - Use list methods and syntax to append, remove, or replace elements of a list
# MAGIC - Define dictionaries
# MAGIC - Use list and dictionary comprehensions to efficiently transform each element of each data structure
# MAGIC - Define classes and methods

# COMMAND ----------

# MAGIC %md
# MAGIC ### 1) Lists
# MAGIC 
# MAGIC We've seen that a list is an ordered sequence of items. The items may be of any type, though in practice you'll usually create lists where all of the values are of the same type. You typically create a list by providing comma-separated values enclosed by square brackets. You can then access elements in the list via 0-based indexing.

# COMMAND ----------

breakfast_list = ["pancakes", "apple", "eggs"]
print(f"The first breakfast item is {breakfast_list[0]}")

# COMMAND ----------

# MAGIC %md
# MAGIC #### Updating Lists
# MAGIC 
# MAGIC Lists are _mutable_ collections, meaning that we can change the contents of the list with operations like updating, appending, and deleting elements.

# COMMAND ----------

# Replace pancakes with waffles
breakfast_list[0] = "waffles"
print(f"After the update: {breakfast_list}")

# Append an item to the end of the list
breakfast_list.append("oatmeal")
print(f"After the append: {breakfast_list}")

# Remove the eggs to go vegan
del breakfast_list[2]
print(f"After the delete: {breakfast_list}")

# COMMAND ----------

# MAGIC %md
# MAGIC #### Determining Whether an Item is in a List
# MAGIC 
# MAGIC You can test for the presence or absence of an item in a list using the **`in`** and **`not in`** operations, respectively.

# COMMAND ----------

if "apple" in breakfast_list:
    print("You had an apple for breakfast")

if "congee" not in breakfast_list:
    print("You did not have congee for breakfast")

# COMMAND ----------

# MAGIC %md
# MAGIC #### Built-in Functions for Lists
# MAGIC 
# MAGIC Python has built-in functions for determining the length, minimum, and maximum of a collection.

# COMMAND ----------

item_count = len(breakfast_list)
print(f"You had {item_count} items for breakfast")

nums = [-7, 5, 1, 8, -3, 2]
print(f"The lowest value in the list is {min(nums)}")
print(f"The highest value in the list is {max(nums)}")

# COMMAND ----------

# MAGIC %md
# MAGIC ### 2) List Comprehensions
# MAGIC 
# MAGIC A common task is to take a collection of values and create a new collection that is a transformation of the original values. 
# MAGIC 
# MAGIC You can do this explicitly with a **`for`** loop.

# COMMAND ----------

# Create a capitalized list of breakfast items
caps_list = []  # Initialize an empty list
for item in breakfast_list:
    caps_list.append(item.capitalize())

print(f"Transformed results: {caps_list}")

# COMMAND ----------

# MAGIC %md
# MAGIC A more compact and efficient technique to accomplish the same thing is a _list comprehension_. 
# MAGIC 
# MAGIC The following is equivalent to the example above:

# COMMAND ----------

caps_list = [item.capitalize() for item in breakfast_list]
print(f"Result of list comprehension: {caps_list}")

# COMMAND ----------

# MAGIC %md
# MAGIC A comprehension can also include a filter expression to process only the items that match a condition.

# COMMAND ----------

# Take all positive values of the original list and generate a list of their squares
print(f"Original list: {nums}")

square_positives = [i * i for i in nums if i > 0]
print(f"Square of positives list: {square_positives}")

# COMMAND ----------

# MAGIC %md
# MAGIC ### 3) Dictionaries
# MAGIC 
# MAGIC A Python <a href="https://www.w3schools.com/python/python_dictionaries.asp" target="_blank">_dictionary_</a> is a mutable collection of elements where each element is a key-value pair.
# MAGIC 
# MAGIC * All of the keys in a dictionary must be unique.
# MAGIC * The keys must be of an immutable type, typically strings or integers.
# MAGIC * The values may be mutable and of any type.
# MAGIC * Prior to Python 3.6, dictionaries are _unordered_ collections. The order of elements can change as you add and delete elements.
# MAGIC * In Python 3.6 and later, dictionaries are _ordered_ collections, which means that they keep their elements in the same order in which they were originally inserted.
# MAGIC 
# MAGIC You can create a dictionary like this:

# COMMAND ----------

breakfast_dict = {
    "eggs": 160, # Corresponds to number of calories
    "apple": 100,
    "pancakes": 400,
    "waffles": 300,
}
print(breakfast_dict)

# COMMAND ----------

# MAGIC %md
# MAGIC #### Accessing Dictionary Values
# MAGIC 
# MAGIC Once created, you can retrieve the value corresponding to a given key like this:

# COMMAND ----------

apple_calories = breakfast_dict["apple"]
print(f"Your apple had {apple_calories} calories.")

# COMMAND ----------

# MAGIC %md
# MAGIC However, if the dictionary does not contain an element with that key, Python raises a **`KeyError`**.

# COMMAND ----------

# Uncomment the following line and run this cell
# breakfast_dict["oatmeal"]

# COMMAND ----------

# MAGIC %md
# MAGIC Alternatively, you can use the dictionary **`get()`** method. This returns the value for the given key if present. 
# MAGIC 
# MAGIC If the key is not present in the dictionary, **`get()`** returns either a given default value if specified or the **`None`** value otherwise.

# COMMAND ----------

# get() with a given default of 0
result1 = breakfast_dict.get("oatmeal", 0)
print(f"{result1}")

# get() with an implicit default of None
result2 = breakfast_dict.get("muesli")
print(f"{result2}")

# COMMAND ----------

# MAGIC %md
# MAGIC #### Determining Whether a Key is in a Dictionary
# MAGIC 
# MAGIC You can test for the presence or absence of a key in a dictionary using the **`in`** and **`not in`** operations, respectively.

# COMMAND ----------

if "pancakes" in breakfast_dict:
    print(f"pancakes have {breakfast_dict['pancakes']} calories")

if "orange" not in breakfast_dict:
    print("I couldn't find an orange in the dictionary")

# COMMAND ----------

# MAGIC %md
# MAGIC #### Updating Dictionaries
# MAGIC 
# MAGIC Because a dictionary is a mutable collection, we can change its contents with operations like inserting, updating, and deleting elements.

# COMMAND ----------

print(f"Original dictionary: {breakfast_dict}")

# Insert orange juice
breakfast_dict["orange juice"] = 110
print(f"After insert: {breakfast_dict}")

# Update the calorie count for waffles
breakfast_dict["waffles"] = 350
print(f"After update: {breakfast_dict}")

# Delete the pancakes
del breakfast_dict["pancakes"]
print(f"After delete: {breakfast_dict}")

# COMMAND ----------

# MAGIC %md
# MAGIC #### Iterating Over the Elements of a Dictionary
# MAGIC 
# MAGIC You can use a simple **`for`** loop to iterate over the elements of a dictionary like this:

# COMMAND ----------

print("Food          Calories")
for food in breakfast_dict:
    print(f"{food:13} {breakfast_dict[food]}") # :13 is used for spacing

# COMMAND ----------

# MAGIC %md
# MAGIC Alternatively, you can unpack the key-value pairs while iterating over a dictionary as follows:

# COMMAND ----------

print("Food          Calories")
for food, calories in breakfast_dict.items():
    print(f"{food:13} {calories}")

# COMMAND ----------

# MAGIC %md
# MAGIC ### 4) Functions with Arbitrary Arguments
# MAGIC 
# MAGIC You can define a function in Python that accepts an arbitrary number of arguments with syntax like this:
# MAGIC 
# MAGIC <code><b>
# MAGIC def my_func(*args):<br/>
# MAGIC &nbsp; &nbsp; ...
# MAGIC </b></code>
# MAGIC 
# MAGIC The parameter name **`args`** is not required, but it is a common convention. 
# MAGIC 
# MAGIC The **`args`** parameter is treated as a sequence containing all of the arguments passed to the function.

# COMMAND ----------

def calculate_sum(*args):
    total = 0
    for value in args:
        total += value
    return total

print(f"sum(1, 2, 3, 4, 5) = {calculate_sum(1, 2, 3, 4, 5)}")
print(f"sum(1) = {calculate_sum(1)}")
print(f"sum() = {calculate_sum()}")

# COMMAND ----------

# MAGIC %md
# MAGIC ### 5) Functions with Arbitrary Keyword Arguments
# MAGIC 
# MAGIC A Python function can also accept arbitrary named arguments, which are referred to a _keyword arguments_, with syntax like this:
# MAGIC 
# MAGIC <code><b>
# MAGIC def my_func(**kwargs):<br/>
# MAGIC &nbsp; &nbsp; ...
# MAGIC </b></code>
# MAGIC 
# MAGIC The parameter name **`kwargs`** is not required, but it is a common convention. 
# MAGIC 
# MAGIC The **`kwargs`** parameter is treated as a dictionary containing all of the argument names and values passed to the function.

# COMMAND ----------

def my_func(**kwargs):
    print("Arguments received:")
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

print("First Example\n=============")
my_func(first_name="James", last_name="Bond", drink="Martini - shaken, not stirred")

print("\nSecond Example\n==============")
my_func(movie_title="Casino Royale", release_year=2006)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 6) Classes
# MAGIC 
# MAGIC A <a href="https://www.w3schools.com/python/python_classes.asp" target="_blank">_class_</a> is a custom type that you can define that is in essence a custom data structure.
# MAGIC 
# MAGIC * The class definition itself serves as a "template" that you can use to create any number of individual _objects_ (also known as _instances_ in object oriented programming).
# MAGIC * These objects will have the same characteristics and behaviors, but their own data values (also known as _attributes_ or _properties_ in OOP).
# MAGIC 
# MAGIC As an analogy, you can think of a class as though it were a blueprint for a house.
# MAGIC 
# MAGIC * The blueprint isn't a house itself, but it describes how to build a house.
# MAGIC * From one blueprint (class), a developer could build any number of houses (objects/instances).
# MAGIC * Each house would have the same floorplan, but each house could have its own unique paint colors, floor tiling, etc. (attributes/properties).
# MAGIC 
# MAGIC NOTE: We've already encountered and used classes in this course. For example, Python has a built-in **`str`** class that defines the capabilities of all strings. Similarly, **`list`** and **`dict`** are built-in classes defining the capabilities of lists and dictionaries, respectively. You can see that for yourself by using the **`help()`** function on these types:

# COMMAND ----------

help(dict)

# COMMAND ----------

# MAGIC %md
# MAGIC #### Class Methods
# MAGIC 
# MAGIC A class definition usually consists of one or more function definitions, which are also called _methods_.
# MAGIC 
# MAGIC * These methods are automatically associated with each object created using the class.
# MAGIC * When you invoke a method, Python automatically passes a reference to the associated object as the first argument, followed by any other arguments that you passed explicitly.
# MAGIC * By convention, **`self`** is used as the parameter name for the object reference.
# MAGIC 
# MAGIC Here's a simple example of a class definition and its use:

# COMMAND ----------

class Thing:
    def greet(self, greeting="Hello!"):
        print(f"{self} says, '{greeting}'")

thing1 = Thing()  # Create an instance of Thing
thing2 = Thing()  # Create another Thing

thing1.greet()                # Call the greet() method on thing1
thing2.greet("Guten Tag!")    # Call the greet() method on thing2

# COMMAND ----------

# MAGIC %md
# MAGIC Wow, that's ugly. 
# MAGIC 
# MAGIC We can see that the value of **`self`** is different for **`thing1`** and **`thing2`** because each is a separate instance of **`Thing`**. 
# MAGIC 
# MAGIC But the string representation of **`self`** is not informative to us as programmers. 
# MAGIC 
# MAGIC To make things more interesting and useful, we need to define some class properties.

# COMMAND ----------

# MAGIC %md
# MAGIC #### Class Properties and the Constructor Method
# MAGIC 
# MAGIC Class properties are usually defined in a special method called a _constructor_.
# MAGIC 
# MAGIC * The constructor method **must** be named **`__init__()`**.
# MAGIC * Python calls the constructor method automatically whenever you create an instance of the class.
# MAGIC * The purpose of the constructor is to initialize the newly created instance, most typically by setting the initial values of the object's properties.
# MAGIC 
# MAGIC The following is an example of a more interesting class that includes a constructor method that sets two properties and two additional methods:

# COMMAND ----------

class Person:
  
    # Defining the class constructor method
    def __init__(self, first_name, last_name):
        # Here we create the properties on self with the values provided in the constructor
        self.first_name = first_name
        self.last_name = last_name

    # Defining other class methods
    def greet(self, greeting="Hello!"):
        print(f"{self.first_name} says, '{greeting}'")

    def full_name(self):
        return self.first_name + " " + self.last_name

person1 = Person("Michelle", "Robinson")
person2 = Person(first_name="Barack", last_name="Obama")

person1.greet()
person2.greet("Hi!")

print(f"person1's current name: {person1.full_name()}")
person1.last_name = "Obama"  # You can change the value of object properties
print(f"person1's updated name: {person1.full_name()}")

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2022 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>
