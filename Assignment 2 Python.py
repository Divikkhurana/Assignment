#!/usr/bin/env python
# coding: utf-8

# ###  Task 1

# #### 1.1 Write a Python Program to implement your own myreduce() function which works exactly like Python's built-in function reduce()  

# In[1]:


def myReduce(function,list1):
    mylist=[]
    for i in range(1,len(list1)):
        val=function(list1[i-1],list1[i])
        mylist.append(val)
        list1[i]=val
    return mylist[-1]
    
   

        


# In[2]:


print(myReduce(lambda x,y:x*y,[1,2,3,4,5]))


# In[3]:


print(myReduce(lambda x,y:x+y,[1,2,3,4,5,6,7,8,9,10]))


# #### Write a Python program to implement your own myfilter() function which works exactly like Python's built-in function filter() 

# In[4]:


def myFilter(function,list1):
    mylist=[]
    for i in range(len(list1)):
        if function(list1[i]):
            mylist.append(list1[i])
    return mylist


# In[5]:


print(myFilter(lambda x:x%2,[1,2,3,4]))


# In[6]:


print(myFilter(lambda x:x>2,[1,2,3,4]))


# #### 2.   
# Implement List comprehensions to produce the following lists.  
# Write List comprehensions to produce the following Lists  
# 

# #### 2.1 ['A','C','A','D','G','I','L',D']

# In[120]:


[i for i in 'ACADGILD']


# #### 2.2 ['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']

# In[7]:


[chr(j)*i for j in range(120,123) for i in range(1,5)]


# #### 2.3 ['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz'] 

# In[8]:


[chr(j)*i for i in range(1,5) for j in range(120,123) ]


# ####  2.4  [[2], [3], [4], [3], [4], [5], [4], [5], [6]] 

# In[9]:


[[j+i] for j in range(2,5) for i in range(3)]


# #### 2.5 [[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]

# In[10]:


[[j+i for j in range(2,6)] for i in range(4)]


# #### 2.6 [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]

# In[11]:


[(i+1,j+1)for j in range(3) for i in range(3)]


# ####  3.Implement a function longestWord() that takes a list of words and returns the longest one. 

# In[27]:


def longestWord(words):
    max=0
    val=''
    for i in words:
        if len(i)>maxValue:
            val=i
            max=len(i)
    return val


# In[29]:


print(longestWord(['I love tea', 'He hates tea', 'We love tea']))
        


# ###  Task 2

# #### 1.1
# Write a Python Program(with class concepts) to find the area of the triangle using the below formula.  
# area = (s*(s-a)*(s-b)*(s-c)) ** 0.5  
# Function to take the length of the sides of triangle from user should be defined in the parent class and function to calculate the area should be defined in subclass.

# In[103]:


class parent:
    def __init__(self):
        self.len1=0
        self.len2=0
        self.len3=0
        pass
    def takeLength(self):
        self.len1=int(input('Enter first length'))
        self.len2=int(input('enter 2nd length'))
        self.len3=int(input('enter 3rd length'))
        
class child(parent):
    def __init__(self):
        pass
    def calculateArea(self):
        perimeter=(self.len1+self.len2+self.len3)/2
        print(perimeter)
        area=(perimeter*(perimeter-self.len1)*(perimeter-self.len2)*(perimeter-self.len3))*0.5
        return area
    


# In[104]:


tri1=child()


# In[105]:


tri1.takeLength()


# In[107]:


tri1.calculateArea()


# #### 1.2 Write a function filter_long_words() that takes a list of words and an integer n and returns the list of words that are longer than n. 

# In[110]:


def filter_long_words(words,num):
    long_words=[]
    for i in words:
        if len(i)>num:
            long_words.append(i)
    return long_words
            


# In[111]:


print(filter_long_words(['This', 'is', 'a', 'string', 'with', 'words'],3))


# #### 2.1 Write a Python program using function concept that maps  list of words into a list of integers representing the lengths of the corresponding words​. 

# In[113]:


def my_map(seq):
    my_list=[]
    for i in seq:
        my_list.append(len(i))
    return my_list


# In[114]:


print(my_map(['this','is','my','map','function']))


# #### 2.2  Write a Python function which takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise. 

# In[115]:


def isVowel(char):
    char=char.lower()
    if char=='a' or char=='e' or char=='i' or char=='o' or char=='u':
        return True
    else: 
        return False


# In[117]:


print(isVowel('A'))


# In[118]:


print(isVowel('u'))


# In[119]:


print(isVowel('B'))


# In[ ]:




