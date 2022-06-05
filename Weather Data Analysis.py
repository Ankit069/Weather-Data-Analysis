#!/usr/bin/env python
# coding: utf-8

# # Import basic libraries

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# # Import the data set

# In[2]:


weather=pd.read_csv("Weather Data.csv")
weather.head()


# In[3]:


weather.isnull().sum()


# In[4]:


weather.info()


# In[5]:


weather.index


# In[6]:


weather.columns


# In[7]:


weather["Weather"].unique()


# In[8]:


weather.nunique()


# In[9]:


weather.count()


# In[10]:


weather["Weather"].value_counts()


# # Find all the unique "Wind Speed" values in data

# In[11]:


weather["Wind Speed_km/h"].unique()


# # Find the number of times when the "Weather is exactly clear"

# In[12]:


weather[weather.Weather=="Clear"]


# In[13]:


weather.groupby("Weather").get_group("Clear")


# # Find the no. of timeswhen the "Wind speed was exactly 4km/h"

# In[14]:


weather[weather["Wind Speed_km/h"]==4]


# # Rename the column name "Weather" of the dataframe to  "Weather Condition"

# In[15]:


weather.rename(columns={"Weather":"Weather Condition"},inplace=True)


# In[16]:


weather


# # What is the mean "Visibility"?

# In[17]:


weather.Visibility_km.mean()


# # What is the Standard deviation of "Pressure " in the data

# In[18]:


weather.Press_kPa.std()


# # What is the variance of  "Realtive Humadity"

# In[19]:


weather["Rel Hum_%"].var()


# 
# # Find the instances when "Snow" was recorded

# In[20]:


weather[weather["Weather Condition"]=="Snow"]


# # Find all instances when "Wind Speed is above 24" and "Visibility is 25"

# In[21]:


weather[(weather["Wind Speed_km/h"]>24) & (weather["Visibility_km"]==25)]


# # what is the mean value of each columns against "weather condition"

# In[22]:


weather.groupby("Weather Condition").mean()


# # What is the minimum and maximum value of each column against each "Weather Condition"

# In[23]:


weather.groupby("Weather Condition").min()


# In[24]:


weather.groupby("Weather Condition").max()


# # Show all the records where condtion is "Fog"

# In[25]:


weather[weather["Weather Condition"]=="Fog"]


# # Find all instances when  "Weather is Clear" or "Visibility is above 40"

# In[26]:


weather[(weather["Weather Condition"]=="Clear") | ( weather["Visibility_km"]>40)]


# In[29]:


weather["Visibility_km"]=weather["Visibility_km"].astype(int)
weather["Rel Hum_%"]=weather["Rel Hum_%"].astype(int)
weather["Wind Speed_km/h"]=weather["Wind Speed_km/h"].astype(int)


# In[30]:


weather.head()


# In[31]:


weather.info()


# # Data Visualization

# In[32]:


weather["Visibility_km"].unique()


# In[127]:


plt.figure(figsize=(10,5))
plt.hist(data=weather,x="Visibility_km",color="g")
plt.show()


# In[123]:


weather["Visibility_km"].mean()


# In[121]:


plt.figure(figsize=(14,7))
plt.hist(data=weather,x="Rel Hum_%",bins=10)
plt.show()


# In[ ]:





# In[122]:


plt.figure(figsize=(14,7))
plt.hist(data=weather,x="Wind Speed_km/h",color="c")
plt.show()


# In[41]:


weather["Wind Speed_km/h"].mean()


# # Pairplot between the  all the Columns

# In[43]:


sns.pairplot(weather)


# # Relation Between "Visibility_km" and "Press_kPa"

# In[87]:


sns.barplot(x="Visibility_km",y="Press_kPa",color="green",data=weather)


# In[70]:


weather.columns


# In[99]:


weather1=weather.drop(["Weather Condition","Date/Time"],axis=1)


# # Plot Heatmap

# In[98]:


plt.figure(figsize=(14,6))
corr=weather.corr()
heatmap=sns.heatmap(corr,annot=True)
heatmap.set_title("Correlation Heatmap Between Variables",fontsize=18)
plt.show()


# #                                     THANK YOU
