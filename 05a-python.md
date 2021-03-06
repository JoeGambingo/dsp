 # Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Both list and tuples are sequences of values. However tuples are immutable - they cannot be changed.

>> The keys to a dictionary must be immutable, but the values can change. So lists can be values in a dictionary, but not keys. Tuples, however, can be used as keys.

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Lists and sets are both collections of values. Lists are ordered, and contain mutable objects. Sets are unordered, and contain immutable objects. Lists can contain duplicate values. Sets automatically simplify to only contain unique values.

>> Lists could be used when performing calculations, so that the values can be changed. Sets could be used to collect and protect data.

>> Sets are faster when determining if a value exists in the sequence, but slower when iterating over each value.

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> `Lambdas` are anonymous functions (functions not formerly declared with a name) that are often written for a one-off purpose. They are useful for passing one function through another function.

>>Using a `lambda` as the key in the `sorted` function, would allow a list to be sorted by a function rather than a static key. For an example, see the snippet included below, from Stack Overflow

```
>> to_be_sorted = [1, 2, 3, 4, 5, 6, 7, 8, 9]
>> sorted(to_be_sorted, key = lambda x: abs(5-x))

[5, 4, 6, 3, 7, 2, 8, 1, 9]
```

---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> A list comprehension is method of building a sequence much like sequences are described in mathematics. The basic syntax of a list is: `[expression for item in list if conditional]`

>> The following example, adapted from the link below, demonstrates how list comprehensions can acheive the same results as `map` and `filter`. The list comprehension is much more readable than the map and filter approach.
```
>> words = 'The quick brown fox jumps over the lazy dog'.split()
>> print(words)
['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']

>> test = [[w.upper(), w.lower(), len(w)] for w in words if len(w) > 3]
>> for i in test:
      print(i)
['QUICK', 'quick', 5]
['BROWN', 'brown', 5]
['JUMPS', 'jumps', 5]
['OVER', 'over', 4]
['LAZY', 'lazy', 4]

>> stuff = map(lambda w: [w.upper(), w.lower(), len(w)], words)
>> stuff = list(filter(lambda x: x[2] > 3, stuff))
>> for i in test:
      print(i)
['QUICK', 'quick', 5]
['BROWN', 'brown', 5]
['JUMPS', 'jumps', 5]
['OVER', 'over', 4]
['LAZY', 'lazy', 4]
```
>> Source: http://www.secnetix.de/olli/Python/list_comprehensions.hawk

>> Set comprehensions work just like list comprehensions.
```
>> s = {x for x in range(1,11) if x%2 == 0}
>> print(s)
{2, 4, 6, 8, 10}
```

>> Dictionary comprehensions are similar and take the form `{key: value for (key, value) in iterable}'. See this example from Stack Overflow:

```
>> {n: n**2 for n in range(0,5)}
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```
>> Source: https://stackoverflow.com/questions/14507591/python-dictionary-comprehension

>> A common approach is to form a dictionary from two equal length lists, matching key and value for the elements at the same position in each list. The `zip` function creates tuples of these position matched pairs.

```
>> squares = [x**2 for x in range(0,5)]
>> cubes = [x**3 for x in range(0,5)]
>> {k:v for (k,v) in zip(squares, cubes)}
{0: 0, 1: 1, 4: 8, 9: 27, 16: 64}
```




---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513

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
