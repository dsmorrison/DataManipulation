#!/usr/bin/env python
# coding: utf-8

# # Welcome to the Data Manipulation Lesson.
# ## Notebook 1
# 
# In this lesson, we will be using this workbook in tandum with the reading assignments.
# 
# The workbook has been broken up into three sections.  Each section has reading assignments and is followed by questions and prompts for you to work through.
# 
# In [your Canvas](https://launchcode.instructure.com/courses/14/quizzes/569), you will find the reading quiz.  

# In[1]:


import pandas as pd
import numpy as np

data= pd.read_csv("titanic.csv")


# ## Before You Get Started
# 
# We are going to be using the Titanic Dataset. Make sure to run a head() before you start working with manipulation methods.

# In[2]:


# Run the head of your data set here:
data.head()


# In[3]:


# check for duplicates
data.duplicated().sum()


# In[4]:


# if there are, go ahead and drop them:
data.drop_duplicates()


# ### Cleaning Note:
# 
# While the columns are not the "prettiest", don't adjust any of them yet. We are going to update some values and add some values as we workthrough this notebook. Applologies for the extra visual "noise" on your screen. You will be given the option to tidy up the columns at the end of this notebook.

# ## Running Tables Note:  
# If your tables don't appear to have accepted your changes, try the "Run All" option in the "Cell" section of the menu bar.  

# <span style="background-color:dodgerblue; color:dodgerblue;">- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -</span> 

# # A. Aggregation
# 
# 1. Please read the following:
#     - [Python | Pandas dataframe.aggregate()](https://www.geeksforgeeks.org/python-pandas-dataframe-aggregate/)
#     - [Python | Pandas dataframe.groupby()](https://www.geeksforgeeks.org/python-pandas-dataframe-groupby/)
# 1. Answer the Check Your Understanding Questions in your Canvas account.
# 1. Work through the section Exercises.  
#     - There are 4 sections in part A:
#         - Groupby
#         - Aggregation Methods
#         - Groupby and Basic Math
#         - Groupby and Multiple Aggregations
# 

# #### Creating Variables.
# 
# As we begin to manipulate our data, create new variables to store your work in.  This will keep your original data in tact.  Having the original dataset available will save you time with each manipulation.  You can also create variable names that inform you of the purpose of the manipulation.  

# ### 1: Groupby <span style="color:dodgerblue;"> - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - </span> 

# #### Groupby "embark_town"
# 
# 1. Using the titanic data set, groupby "embark_town".
# 1. Create a variable that will represent the grouping of data. 
# 1. Intitalize it using the groupby() function and pass it the column.
# 

# In[6]:


# Code your groupby "embark_town" here:
data_group = data.groupby("embark_town")


# In[7]:


# To view the grouped data as a table, use the variable_name.first():
data_group.first()


# #### Groupby "survived"
# 
# Did you know that you can also chain on some of our exploratory methods to the groupby method?
# 
# 1. Create & initalize a new variable to hold a table that will groupby "survived" 
# 1. Use method chaining to tack on the describe method

# In[8]:


# Code your groupby "survived" table here:
survived_group = data.groupby("survived").describe()

# run your table below:


# In[58]:


# run your table with describe


# In[59]:


# How is this table organized?  Why are there 40 columns now?


# ### 2. Aggregation Methods <span style="color:dodgerblue;"> - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - </span> 

# Note: **agg()** and **aggregate()** are identical [source](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.aggregate.html)

# #### Method Chaining
# 
# 1. Create a variable to method chain **head()** and **agg()** togehter.
# 1. Pass one of the following statistical values to **agg()**
#    - "mean", "median", "mode", "min", "max", "std", "var", "first", "last", "sum"

# In[10]:


# Code your method chain here:
mean_data = data_group.head().agg("mean")  
    


# In[12]:


# Create a variable to method chain head() with agg("sum")
sum_data = data_group.head().agg("sum")
# run your table:


# In[62]:


# Explain the sum table.  What is going on with the "sex", "class", and "alive" columns?
#error. will not sum a string. "concatenated"


# #### Using a Dictionary <span style="color:darkorange;"> - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - </span> 
# ##### A dictionary is a Python collection type.  
# 
# Is a collection type that stores **key-value pairs**.  A key-value pair is an orgainzation system that is made up of a single *key* that has one or more *values* paired with it.  
# Think of it like your contacts list.  The contacts list is the dictionary object.  
# Each contact is organized by a key, usually name.  And attached to each name is contact information, or the values.
# Some contacts might have email address, phone number, home or work address, etc. Other contacts may just be a name and phone number.  This is a very simple example, but understanding this orgainzational structure will be helpful as you learn to manipulate tables.  
# 
# *Here is a dictionary example with 3 keys:*
# >**contacts_dictionary = {"name1": ["email", 555-5552, "work info"], 
#       "name2": ["email", 555-5554],
#       "name3": 555-5555}**
#                      
# *Here is a dictionary example with a single key-value pair*
# **study_group_dictionary = {"name1": 555-5557}**   
# 
# It has a single key, and a list of values. The organization of this structure is called a "Key-Value Pair".
# Using the contact list example, the key would be the name of the person and the values would be their contact information.  The key is a single item (the person's name) and the values can be a single item (an email address) or mulitple items (email, phone number, address, work info, etc).
# Keys and values can be any data type, but must use correct data type syntax.  The keys do not have to be strings, but they do need to be a single value.  
# 
# For more information, you can read more on dictionary objects [here](https://www.w3schools.com/python/python_dictionaries.asp).
# 

# #### Aggregation across muliple columns using dictionary functionality
# 
# ##### Syntax Example:
# 
# **age_dictionary={"age":["sum", "max"]}**
# 
# We are creating a new dictionary (**age_dictionary**).  The key is **age** and the values we want are **"sum""** and **"max"**.  This dictionary object has now become a tempate for the aggregations we want to preform.  However, on it's own, it does nothing.  Once passed to the **agg()** method, it will pick out the specific location of data we want to examine.  Making a subset table.  
# 
# The code is contained in the box below.  Run it and see what happens.
# 
# 
# For syntax examples, review [this webpage](https://www.geeksforgeeks.org/python-pandas-dataframe-aggregate/).
# #### <span style="color:coral;"> - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - </span>

# In[63]:


# Predict the table output before you uncomment the code below.

# age_dictionary={"age":["sum", "max"]}
# dictionary_agg=data.agg(age_dictionary)
# dictionary_agg


# 1. What if we want to look at more than one column at a time?  We pass more dictionaries to the agg function.
# 1. Create a variable to hold at least 3 columns.  Use the syntax from the "Syntax Example" as a guide.
#     - Aggregate the following:  survived: "sum" & "count"; age: "std" & "min", and sibsp: "count" & "sum"

# In[14]:


# Code your dictionary here:
test_dictionary={"survived": ["sum", "count"],
                "age": ["std", "min"],
                "sibsp": ["count", "sum"]
                }
dictionary_agg=data.agg(test_dictionary)


# ### 3. Groupby and Basic Math <span style="color:dodgerblue;"> - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - </span> 
# 
# 1. Groupby "pclass".  Make sure you use a variable to hold your grouped data.

# In[20]:


# # Run your table using first() here instead of head():

passenger_class = data.groupby(['pclass'])  
passenger_class.first()


# ### 4. Groupby and Multiple Aggregations <span style="color:dodgerblue;"> - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - </span> 

# #### Group with a List<span style="color:dodgerblue;"> - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - </span>

# 1. We want to do muliple aggregation functions to our newly grouped data set.  We created a variable to hold a list of functions we want to perform.  These functions are part of the agg method.  When we pass our list to the method, the method will iterate through each item and perform that function for the entire table.

# In[22]:


# our list of functions
agg_func_list = ['sum', 'mean', 'median', 'min', 'max', 'std', 'var', 'first', 'last', 'count']


#Apply the agg method to our passenger_class variable (made in the Groupby Basic Math section).  
# Pass our list to the function and run your table.
passenger_class.agg(agg_func_list)

  


# #### Group with a Dictionary<span style="color:dodgerblue;"> - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - </span>
# 
# Using only a list provides us with the entire table.  What if we only want to look at age vs pclass?  
# 
# we can create a dictionary to hold the age column for us.  The *key* would be the name of our column, and the values our list of functions to preform on that column.  The code would look like this:

# In[23]:


agg_func_dict = {
    'age':
    ['sum', 'mean', 'median', 'min', 'max', 'std', 'var', 'first', 'last', 'count']
}
# We would run our table like this:
passenger_class.agg(agg_func_dict)  


# Looking at the *age_func_dict* syntax, create a dictionary variable for the "survived" column and pass it to **passenger_class.agg()** in the box below.

# In[24]:


# Code it here:

passenger_class.agg(agg_func_dict)  


# <span style="background-color:dodgerblue; color:dodgerblue;">- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -</span> 

# # B. Recoding and Creating New Values and Variables 
# 
# 1. Please read the following:
#     1. [How to create new columns derived from existing columns?](https://pandas.pydata.org/docs/getting_started/intro_tutorials/05_add_columns.html)
#     1.[Recode Data](https://pythonfordatascienceorg.wordpress.com/recode-data/)
# 1. Answer the Check Your Understanding questions in your Canvas Account.
# 1. Work through the Part B, there are 2 sections
# 
# Suggested Reading:
# - [How to manipulate textual data?](https://pandas.pydata.org/docs/getting_started/intro_tutorials/10_text_data.html)

# ### Create a New Column <span style="color:dodgerblue;"> - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - </span> 
# As questions arrise during your data exploring and cleaning, you might want to test them out.  In this instance, we want to make sure the values we want to manipulate remain untouched. One thing we can do is to add a new column that will contain our manipulations.
# 
# In the box below:
# 1. Create a new column by manipulating the values of different column.  Specifically, create a new column, "fare_2021" that allows us to compare the cost of fare in pounds back in 1912 to 2021.  [This website](https://www.in2013dollars.com/uk/inflation/1912) can help you find the 2021 fare amount. 

# In[26]:


# Code your new "fare_2021" column here:
data["fare_2021"]=(data["fare"] * 117.17)
# Run the head of your table to see your new column:
data.head()


# ### Replacing Values <span style="color:dodgerblue;"> - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - </span> 
#  
# Replace the values in the "alive" coloum from string "yes" or "no" to bools, where "yes" becomes True and "no" becomes False.

# In[27]:


# Code your updated values here:

data
data["alive"]=data["alive"].replace({"yes":True, "no":False})


# We can also use functions to update values.
# 
# 1. Create a function that will set the alive values as bools. Apply it to your table and run your table here:

# In[28]:


# Code your function here:
def set_alive_to_number(series):
    if series == "yes":
        return True
    else: 
        return False
data["alive"] = data["alive"].apply(set_alive_to_number)


# ### Using a function to create a new column <span style="color:dodgerblue;"> - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - </span> 
# 
# Sometimes you might want to create a new column based on combining multiple columns together.
# 
# 1. create an "age_group" column that breaks years up as 0-19, 20-29, 30-39, etc until all given ages are covered.  Make sure you check to see where you can stop counting by 10s.

# In[29]:


# Write your max age check here:
age_check = data["age"].agg("max")
age_check


# In[31]:


# Code the new "age_group" column function here:
def age_groups(series):
    if series <20:
        return "0-19 years"
    elif 20 <= series < 30:
        return "20-29 years"
    elif 30 <= series < 40:
        return "30-39 years"
    elif 40 <= series < 50:
        return "40-49 years"
    elif 50 <= series < 60:
        return "50-59 years"
    elif 60 <= series < 70:
        return "60-69 years"
    elif 70 <= series < 80:
        return "70-79 years"
    elif 80 <= series < 90:
        return "80-89 years"
    else:
        return "no data"
    
data["age_group"] = data["age"].apply(age_groups) 


# <span style="background-color:dodgerblue; color:dodgerblue;">- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -</span> 

# # C. Reshaping Tables
# 
# 1. Please read the following:
#     1. [How to reshape the layout of tables?](https://pandas.pydata.org/docs/getting_started/intro_tutorials/07_reshape_table_layout.html)
# 1. Answer the Check Your Understanding in your Canvas account
# 1. Work through Part C, there are 4 sections
# 
# 
# Suggested Reading:
# 1. [pandas.pivot_table](https://pandas.pydata.org/docs/reference/api/pandas.pivot_table.html)
# 1. [pandas.melt](https://pandas.pydata.org/docs/reference/api/pandas.melt.html)
# 1. [pandas.pivot](https://pandas.pydata.org/docs/reference/api/pandas.pivot.html)

# ### Sort_values <span style="color:dodgerblue;"> - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - </span> 

# Use **sort_values()** to answer the following question:
# > What is the age of the person who paid the highest fare?
# 
# Hint: We want to see the highest fare value first. What order would we want? ascending or descending?  Check the [documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html?highlight=sort_values#pandas.DataFrame.sort_values) for the syntax.

# In[33]:


# Code your sort_values here:
sort_data = data.sort_values(by=["who", "age"], ascending =  False)

# Run your table here:
print(sort_data)


# ### pivot_table <span style="color:dodgerblue;"> - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - </span> 
# 1. pivot the table of the summed data where the values are "fare", index is "who" and "age_group", and the columns are "survived"
# 
# Hint: set the aggfunc parameter to np.sum
# 
# 
# 

# In[41]:


# Code your pivot_table here:
data_pt = data.pivot_table("fare", ["who", "age_group"], "survived", aggfunc=np.sum)

# Run your table here:
print(data_pt)


# ### Wide to Long <span style="color:dodgerblue;"> - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - </span> 
# 
# 1. Create a table where the columns are "who" and the values are "pclass"
# 1. Answer the question:  How does this table differ from the pivot_table above?  Specifically, how is "who" different?

# In[42]:


# Code your table here:
wide_long = data.pivot(columns="who", values="age_group")

# Run your table here:

print(wide_long)
# Answer the question here:
#


# ### Melt <span style="color:dodgerblue;"> - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - </span> 

# 1.  What does **melt** to the data? 

# In[77]:


# What does melt do?
#converts a wide table to a long table


# 2. Melt to your data.  Be sure to store the output in a new variable.  What is the new shape of your table?

# In[39]:


# Create your default melt table here with the following syntax:  new_name = pd.melt(data_set)
data_m=pd.melt(data)
# Run your table here:

# Check the shape of your new table.
data_m.shape


# 3. Create a melt table where the index variables are "embarked", and the values are "fare" and "deck"

# In[40]:


# Create your melt table here:
data_melt = pd.melt(data, id_vars=["embarked"], value_vars=["fare", "deck"])
 
# Run your table here:

# Check the shape
data_melt.shape


# # Optonal Challenges:
# 
# 1. Clean and Explore the table.  
#     1. How would you handle any missing data?
#     1. Would you keep all of the columns?
#     1. Would you want to manipulate any data?

# In[ ]:




