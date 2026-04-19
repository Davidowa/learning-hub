# Bonus - Arrays
# Arrays are used to store multiple values in one single variable
# We use arrays when we want to work with many values of the same type
# Arrays can only contain values of the same type
# For 90% of the cases, you will use lists instead of arrays
# But if you see performance issues in your code, you can use arrays

# To use arrays, you need to import the array module
# https://docs.python.org/3/library/array.html
# According to the documentation of the array module, the following types are available:
# Type code	C Type	            Python Type	            Minimum size in bytes
# 'b'	        signed char	        int	                    1
# 'B'	        unsigned char	    int	                    1
# 'u'	        Py_UNICODE	        Unicode character	    2
# 'h'	        signed short	    int	                    2
# 'H'	        unsigned short	    int	                    2
# 'i'	        signed int	        int	                    2
# 'I'	        unsigned int	    int	                    2
# 'l'	        signed long	        int	                    4
# 'L'	        unsigned long	    int	                    4
# 'q'	        signed long long	int	                    8
# 'Q'	        unsigned long long	int	                    8
# 'f'	        float	            float	                4
# 'd'	        double	            float	                8

import array as array
array1 = array.array('i', [1, 2, 3, 4, 5])

# In this example, we are creating an array of signed integers, that means that the values can be positive or negative

# To add an item to an array, you can use the append() method
# Example
array1.append(6)
print(array1)  # array('i', [1, 2, 3, 4, 5, 6])

# Or you can use the insert() method
# Example
array1.insert(0, 0)
print(array1)  # array('i', [0, 1, 2, 3, 4, 5, 6])

# We also have pop() and remove() methods as lists
# Example
array1.pop(0)
print(array1)  # array('i', [1, 2, 3, 4, 5, 6])

array1.remove(6)
print(array1)  # array('i', [1, 2, 3, 4, 5])

# You can access the elements of an array by referring to the index number
# Example
print(array1[0])  # 1

# If you try to add a value of a different type to an array, you will get an error
# Example
# array1.append("7") # an integer is required (got type str)
