Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 17:00:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> a=2
>>> type(a)
<class 'int'>
>>> d=2.457
>>> type(d)
<class 'float'>
>>> a=17+79j
>>> type(a)
<class 'complex'>
>>> a=8
>>> s=8
>>> a+s
16
>>> a=10/3
>>> a
3.3333333333333335
>>> a*3
10.0
>>> a
3.3333333333333335
>>> a='yukti'
>>> b=' singh'
>>> a+b
'yukti singh'
>>> 
>>> 
>>> 
>>> 
>>> a='yukti'
>>> s='is'
>>> d='reading'
>>> a+s+d
'yuktiisreading'
>>> 
>>> 
>>> 
>>> 
>>> len(a)
5
>>> o=a[1]
>>> o
'u'
>>> print(om chutiya h)
SyntaxError: invalid syntax
>>> print(a)
yukti
>>> print(a+s+d)
yuktiisreading
>>> 
>>> 

>>> 
>>> 
>>> 
>>> 
>>> print(a[0])
y
>>> print(a[0]+ ukti)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    print(a[0]+ ukti)
NameError: name 'ukti' is not defined
>>> print(a[0]+ 'ukti')
yukti
>>> print(a[0]+ 'ukt'+a[4])
yukti
>>> print(a[0]+ a[1:3]+ a[4])
yuki
>>> 
>>> 
>>> 
>>> 
>>> 

>>> 


>>> 

>>> 


>>> a[2][1]
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    a[2][1]
IndexError: string index out of range
>>> a='yukti'
>>> a[2][1]
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    a[2][1]
IndexError: string index out of range
>>> a=[2][0]
>>> a
2
>>> a=
SyntaxError: invalid syntax
>>> 

>>> 

>>> 

>>> 
>>> a=(10,5.77,'yukti')
>>> a=[10,5.77,'yukti']
>>> b=[10,5.77,'yukti']
>>> b.append('hi')
>>> b.insert(2,'hi')
>>> b
[10, 5.77, 'hi', 'yukti', 'hi']
>>> b.remove('hi')
>>> b
[10, 5.77, 'yukti', 'hi']
>>> b.remove('hi')
>>> b
[10, 5.77, 'yukti']
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> b.pop(4)
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    b.pop(4)
IndexError: pop index out of range
>>> b.pop(2)
'yukti'
>>> b
[10, 5.77]
>>> #pop- can be removed and added as well
>>> #remove-complete removal of character
>>> '''DICTIONERIES'''
'DICTIONERIES'
>>> 
>>> 
>>> 
>>> 
>>> 
>>> a={'om':'stupid','yukti':'thebest'}
>>> a
{'om': 'stupid', 'yukti': 'thebest'}
>>> a={'om':[badwa,chutiya,pagal],'yukti':'good'}
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    a={'om':[badwa,chutiya,pagal],'yukti':'good'}
NameError: name 'badwa' is not defined
>>>  a={'om':['badwa','chutiya','pagal'],'yukti':'good'}
SyntaxError: unexpected indent
>>> a={'om':['badwa','chutiya','pagal'],'yukti':'good'}
>>> a['om']
['badwa', 'chutiya', 'pagal']
>>> a['om']='idiot'
>>> a
{'om': 'idiot', 'yukti': 'good'}
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> a['omkrish']='mc'
>>> a
{'om': 'idiot', 'yukti': 'good', 'omkrish': 'mc'}
>>> a={'om':['badwa','chutiya','pagal'],'yukti':'good'}
>>> a
{'om': ['badwa', 'chutiya', 'pagal'], 'yukti': 'good'}
>>> a['omkrish']='mc'
>>> a
{'om': ['badwa', 'chutiya', 'pagal'], 'yukti': 'good', 'omkrish': 'mc'}
>>> a={'channel':[12345,{'id':'ashish','feed':'h123','names':['ankush','IITR'],'branch':['EC','cs','IT'],349.0:56},'no'],'feedname':[{'1st feed':'h789','2nd feed':'h749'},'hi']}
>>> 
>>> 
>>> a['channel']
[12345, {'id': 'ashish', 'feed': 'h123', 'names': ['ankush', 'IITR'], 'branch': ['EC', 'cs', 'IT'], 349.0: 56}, 'no']
>>> a={'channel':[12345,{'id':'ashish','feed':'h123','names':['ankush','IITR'],'branch':['EC','cs','IT'],349.0:56},'no'],'feedname':[{'1st feed':'h789','2nd feed':'h749'},'hi']}
>>> a['channel'][2]
'no'
>>> len(a['feedname'])
2
>>> a['feedname'][0]
{'1st feed': 'h789', '2nd feed': 'h749'}
>>> 
>>> 
>>> 
>>> 

>>> 
>>> #session2
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> a='yukti singh deshlan'
>>> a='56'
>>> int(a)
56
>>> 
>>> tuple(a)
('5', '6')
>>> list(a)
['5', '6']
>>> dict(a)
Traceback (most recent call last):
  File "<pyshell#142>", line 1, in <module>
    dict(a)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> float(a)
56.0
>>> a='59.9'
>>> a
'59.9'
>>> float(a)
59.9
>>> 
