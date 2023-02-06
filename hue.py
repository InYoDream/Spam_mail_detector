
# coding: utf-8

# In[1]:


from collections import Counter
import os


# In[2]:


fd='C:\Users\asus\Desktop\cybercrime\email/'


# In[3]:


files=os.listdir(fd)
#listdir is used o return files inside a folderin form of a list
len(files) 
#output would be 5172 as we have 5172 email files in our dataset


# In[4]:


emails=[fd + file for file in files] #a for loop
#This statement gives us a list named emails which has the concatenated folder location to its directory
emails #displays all strings in emails


# In[5]:


words=[]
for email in emails:
    obj=open(email,encoding='latin-1')#opens the email
    w=obj.read() #w stoores content of whole txt file in string format
    words+=w.split(" ")#splitting the string to lists wrt space


# In[6]:


len(words)
#displaying the no of words tored in the list named 'word'


# In[7]:


for it in range(len(words)):
    if not words[it].isalpha():
        words[it]=""
#here we remove alphanumeric words


# In[8]:


words_dict=Counter(words)
words_dict
#counts the frequency of each word in the list


# In[9]:


len(words_dict)


# In[10]:


"""we can see there are only 40,577 key value pairs
   we can further shrink the list with the most common words on basis of which we would do the analysis 
   first of all we will remove the spaces''
"""  
del words_dict[""]
words_dict=words_dict.most_common(3000)
#picking the 3000 most frequent words in dictionary and hence shrinking the dictionary
words_dict 
#displaying shrinked list of top 3000 elements


# In[11]:


feature=[]
label=[]
for email in emails:
    f=open(email,encoding='latin-1')
    b=f.read().split()
    data=[]
    for it in words_dict:
        data.append(b.count(it[0]))
    feature.append(data)#stores frequency of each word from every data file
    if 'spam' in email:
        label.append(1)
    if 'ham' in email:
        label.append(0)       


# In[12]:


import numpy as np


# In[13]:


feature=np.array(feature)
feature.shape


# In[14]:


label=np.array(label)
label.shape


# In[15]:


get_ipython().system('pip install scikit-learn')


# In[16]:


from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(feature,label,test_size=0.2,random_state=9)


# In[17]:


from sklearn.naive_bayes import MultinomialNB
classifiers=MultinomialNB()


# In[18]:


classifiers.fit(X_train,Y_train)


# In[19]:


sample_email="""
"""


# In[20]:


sample=[]
for it in words_dict:
    sample.append(sample_email.split(" ").count(it[0]))


# In[21]:


sample=np.array(sample)
sample.shape


# In[22]:


if((classifiers.predict(sample.reshape(1,3000)))==1):
    print('SPAM')
else:
    print('HAM')


# In[ ]:




