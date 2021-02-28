# Python Builtins assignment #1

> Link to Python Builtin functions: \
> https://docs.python.org/3/library/functions.html

Write a script that joins two lists with numbers into a single string.

### The script
For a given 2 lists at `n` equal size:
1. Convert each number in the two lists to its `ascii` representation 
1. Concatenate all the values in the two lists by the order of their indexes  (e.g `the value in index 0 in list1` + `the value in index 0 in list2` + `the value in index 1 in list1` etc.).
1. Print out the entire concatenated string to screen.

```python
    def convert_numbers_to_sentence(list1, list2):
            # your implementation should be here
```
 
### Example
Given two lists:
* `list1 = [65,80]`
* `list2 =  [109,77]`

The `ascii` representation of the number 65 found in `list1` at index **0** is `A` \
The `ascii` representation of the number 109 found in `list2` at index **0** is `m`


The `ascii` representation of the number 80 found in `list1` at index **1** is `P` \
The `ascii` representation of the number 77 found in `list2` at index **1** is `M`

Hence the output that would be printed to screen would be: 

**"AmPM"**

And so forth...


### Testing the output

Done coding? in order to make sure your implementation actually you should run your function on the following 2 lists to get a **meaningful sentence**.

```python
    list1 = [79, 115, 99, 111, 108, 114, 99, 115, 97, 115]
    list2 =  [112, 83, 104, 111, 32, 111, 107, 116, 114, 33]

    convert_numbers_to_sentence(list1, list2)
```

If the output is not clear, something is wrong...check again.

# Python Builtins assignment #2

Write a function `tuple_loto` that receives two parameters:
1. a list of tuples (contain only numbers) 
1. A given number. 

Return `True` if **ANY** of these conditions are met:
- The max number in **ALL** tuples is equal to the given number
- The sum of th first 2 numbers in **ALL** the tuples is equal to the given number
- The one before last number in **ALL** the tuples is equal to the given number

> **HINT:** Most of the operations here (including the True/False checks) can be done by a Builtin method.
> We highly recommend you go through the different Builtin methods thoroughly before you decide to implement.

### Tests + Examples

Checkout the following inputs to make sure your implementations works:

```python
def tuple_loto(list_of_tuples, loto_number):
    # Your implementation here

has_max_of_8 = [(1, 5, 4, 8, 0, 2, 3), (2, 6, 2, 8, 8), (3, 8, 0, 4, 7)]
first_two_numbers_sum_is_8 = [(3, 5, 4), (2, 6, 2, 3, 5), (4, 4, 9, 4, 7)]
one_before_last_number_is_8 = [(3, 8, 4), (2, 6, 2, 8, 5), (8, 4)]
only_one_of_the_tuples_have_max_of_8 = [(3, 5, 4), (2, 8, 2, 3, 5), (4, 9, 8)]
nothing_is_true_in_this_list = [(3, 3, 9), (8, 6, 2), (4, 1, 9, 8)]

tuple_loto(has_max_of_8, 8) #will return True
tuple_loto(first_two_numbers_sum_is_8, 8) #will return True
tuple_loto(one_before_last_number_is_8, 8) #will return True
tuple_loto(only_one_of_the_tuples_have_max_of_8, 8) #will return False
tuple_loto(nothing_is_true_in_this_list, 8) #will return False

```

