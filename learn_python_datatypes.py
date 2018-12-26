#!/usr/bin/env python
# coding: utf-8

# # Data types

# In[1]:


# type of an object type()
type(1)


# In[2]:


type(1.0)


# In[3]:


type(1 + 1j)


# In[4]:


type(True)


# In[5]:


type("string")  # or type('string')


# In[6]:


type([1, 2])   


# In[7]:


type( (1,2) )


# In[8]:


type({1,2})


# In[9]:


type({'a': 1, "b": 2, (1,2): 3})


# # checking type() results

# In[13]:


type(int()) == int


# In[14]:


type(float()) == float


# In[15]:


type(complex()) == complex


# In[25]:


type(bool()) == bool


# In[24]:


type(str()) == str


# In[10]:


type(dict()) == dict


# In[11]:


type(list()) == list


# In[12]:


type(tuple()) == tuple


# # type conversion

# In[16]:


# converts 'set' data type to 'tuple'
tuple({1,3})


# In[17]:


# converts 'set' data type to 'list'
list({1,3})


# In[18]:


# converts 'list' data type to 'tuple'
tuple([1,3])


# In[19]:


# converts 'tuple' data type to 'list'
list((1,3))


# In[20]:


# converts 'tuple' data type to 'set'
set((1,3))


# In[21]:


# converts 'list' data type to 'set'
set([1,3])


# In[22]:


dict(a = 1, b = 3)

