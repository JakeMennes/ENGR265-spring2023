**2.4.1 - An Odd List**
In this assignment you will be provided a list that has an odd length. Use the len() method and the built-in Python
operators to determine the index of the "middle" element of the list. Once the middle index has been identified, then
use a list index operation [] to final the value of that middle element. 
For example, if a list of length 3 contained [a, b, c] then the middle element would be located at index 1 and would have a value of "b".

Hint: you may with to use the [integer floor division operator](https://www.learndatasci.com/solutions/python-double-slash-operator-floor-division/)

**2.4.2 - An Even List**
In this assignment you will access two elements from a list and find their average. The list to be provided will be
of even length. The program will find the two elements closest to the numerical "middle" and compute their average.
For example, if a list of length 6 contains [2,4,5,9,10,12] the "middle two" elements are 5 and 9. Their average would
then be calculated as (5+9)/2 = 7. 

Store the final average of those middle elements in a variable called "middle_average".

Note: the `[]` can be fussy when there is a calculation for the list index inside the `[]`. For example my_list[some_num/2], 
may result in a floating point value that will cause a runtime error. It is suggested that any indices used be calculated
outside of the `[]` operator, and then cast into an integer via `int()`  or ensure the result is an integer, before being used. For example the two lines below may result in an error:

`some_index = (a + b) / 2`

`value = mylist[some_index]`

A safer method would be to manually convert the index to an integer:

`some_index = (a+b)/2`

`some_index = int(some_index)`

`value = mylist[some_index]`

or to use an operator that ensures the result is an integer:

`some_index = (a+b) // 2`

`value = mylist[some_index]`