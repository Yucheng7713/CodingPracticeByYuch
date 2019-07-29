# Python Iterator :

# Iterator is an object which is used to iterate over an iterable object using __next__() method.
# Iterators have __next__() method, which returns the next item of the object
# !! If an object doesn't have __next__(), then it will not be considered as an Iterator (non-iterator type).

#######################################################################################################################

# Python Iterable :

# Iterable is an object, which one can iterate over.
# It generates an Iterator when when it is passed to __iter__() method.

# One can consider Iterable as a collection object which can be iterated over when its Iterator is created.

#######################################################################################################################

# Difference between Iterator and Iterable :

# Note that every iterator is also an iterable, but not every iterable is necessarily an iterator.
# For instance, a list is iterable but not an iterator, although itself has implemented __iter__()

#######################################################################################################################

# The below custom class is an iterable class which also consider as an iterator since it has __iter__() method.
# Try to comment out __iter__() method or __next__() to see what happens when running the code.

class MyList:
    def __init__(self, length):
        self.start = 0
        self.last = length - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.last:
            # When there reaches the limit or no more element left, raise StopIteration
            raise StopIteration
        else:
            # Update the current status of iterable
            self.start += 1
            return self.start - 1

# n_list is an iterable object
n_list = MyList(10)

#######################################################################################################################

# When a for loop is executed, for statement calls iter() on the object, which it's suppose to loop over.
# If the call is successful, the __iter__() will return an iterator object that defines the __next__() method,
# which access elements of the object one at a time.
# The __next__() will raise a StopIteration exception if there are no further elements available.
# The for loop will terminate as soon as it catches a StopIteration exception.

# !! Every time when for loop is called :
#   1. Call the iterator -> If there is no __iter__(), then the object is not iterable.
#   2. Call __next__() to get the elements from the iterable object. If there is no __next__(), then the object itself
#      will not be considered as an Iterator object

for i in n_list:
    print(i)

# How for loop actually works :
iter_obj = iter(iterable)

# Infinite loop
while 1:
    try:
        # get the next item
        element = next(iter_obj)
        # Do something which is specify in the for loop...
    except StopIteration:
        # if StopIteration is raised, break from loop
        break

#######################################################################################################################
