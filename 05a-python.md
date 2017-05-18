# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Lists and tuples can store elements of any type, and preserve the ordering of elements.  Lists can be changed, and values can be appended to lists while tuples are immutable and cannot be changed once they are initialized.  For this reason tuples can be used as dictionary keys while lists cannot

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Like lists, sets store elements of any type.  However, sets store an unordered collection of unique elements.  Because sets use hashing to store values, finding an element in a set is faster than it is for finding an element in a list.

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> `lambda` is a construct for creating anonymous functions.  It is used for defining functions inline, usually functions that are simple or only used once.

>> ex:  
>> `sq = lambda x: x**2`  
>> `sq(2) => 4`
>>  
>>  `sorted([1,5,2,4], key=lambda x: x%2==0)` sorts by the output of the lambda function in the key argument, which is whether the value is odd/even.  
>> So this will return an array with odd values at the beginning and even values at the end


---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions are used to construct lists inline, instead of using a loop to fill a list with the appropriate elements.  

>> `map(lambda x: x+2, [i**2 for i in range(1,10)])` adds 2 to the first 9 squares

>> `filter(lambda x: x>0, [i for i in range(-10,10)])` returns all positive elements in the input list  

>> set comprehension:  `{i%2 for i in range(10)}` returns `{0,1}`

>> dict comprehension: `{ch: ch.upper() for ch in string.ascii_lowercase}` returns a dictionary with lowercase keys and uppercase values

---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937 Days

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513 Days

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Write a script as indicated (using the football data) in [q8_parsing.py](python/q8_parsing.py)
