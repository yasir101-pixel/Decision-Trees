#!/usr/bin/env python
# coding: utf-8

# # Import Necessary Libraries

# In[4]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# # Ensuring Data is properly Loaded

# In[5]:


file = open('WISDM_ar_v1.1_raw_updated')
lines = file.readlines()

processedList = []

for i, line in enumerate(lines):
    try:
        line = line.split(',')
        last = line[5].split(';')[0]
        last = last.strip()
        if last == '':
            break;
        temp = [line[0], line[1], line[2], line[3], line[4], last]
        processedList.append(temp)
    except:
        print('Error at line number: ', i)


# In[6]:


columns = ['UserID', 'activity', 'Time', 'X', 'Y', 'Z']
data = pd.DataFrame(data = processedList, columns = columns)
data.head()


# In[7]:


data.info()


# In[8]:


data['UserID']=data['UserID'].astype('float')
data['Time']=data['Time'].astype('int64')
data['X']=data['X'].astype('float')
data['Y']=data['Y'].astype('float')
data['Z']=data['Z'].astype('float')


# In[9]:


data.info()


# In[10]:


data.shape


# # Exploration of Activities

# In[11]:


activity_counts = data['activity'].value_counts()
activity_counts


# In[12]:


activity_counts.plot(kind='bar',title='Training Examples by activity Type', figsize=(14,8) );


# # No of Samples belong to each volunteer

# In[13]:


countofactivityperperson=data['UserID'].value_counts()
print(countofactivityperperson)


# In[14]:


countofactivityperperson.plot(kind='bar',title='Maximum samples per userid', figsize=(14,8) );


# # No of Actvities performed by each UserID

# In[15]:


import pandas as pd

# Assuming your data is stored in a DataFrame called 'data'

# Group data by 'UserID' and aggregate the unique activities performed by each user
user_activities = data.groupby('UserID')['activity'].unique()

# Print out the mapping of UserID to activities
for user_id, activities in user_activities.items():
    print(f"UserID {user_id} performs activities: {', '.join(activities)}")


# In[16]:


import pandas as pd
import matplotlib.pyplot as plt

# Assuming your data is stored in a DataFrame called 'data'

# Group data by 'UserID' and count the number of unique activities performed by each user
user_activity_counts = data.groupby('UserID')['activity'].nunique()

# Plotting
plt.figure(figsize=(10, 6))
user_activity_counts.plot(kind='bar')
plt.title('Number of Unique Activities by UserID')
plt.xlabel('UserID')
plt.ylabel('Number of Unique Activities')
plt.xticks(rotation=45)
plt.show()


# # Plot all the activities of UserID36

# In[17]:


import matplotlib.pyplot as plt

def plot_user_acceleration(user_id, data, sampling_frequency, num_samples):
    user_data = data[data['UserID'] == user_id]
    walking_data = user_data[user_data['activity'] == 'Walking']
    walking_data = walking_data[['X', 'Y', 'Z']]
    walking_data = walking_data[:num_samples]
    
    # Calculate the time values based on sampling frequency
    timestamps = [i / sampling_frequency for i in range(len(walking_data))]
    
    plt.figure(figsize=(16, 6))
    plt.plot(timestamps, walking_data)
    plt.title(f'Acceleration Data for UserID {user_id} - Walking (First {num_samples} Samples)')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Acceleration')
    plt.legend(['X', 'Y', 'Z'])
    plt.show()

# Example usage
# Assuming you have 'data' containing the dataset, a 'sampling_frequency' value, and a 'num_samples' value
plot_user_acceleration(user_id=36, data=data, sampling_frequency=20, num_samples=200)


# In[18]:


import matplotlib.pyplot as plt

def plot_user_acceleration(user_id, data, sampling_frequency, num_samples):
    user_data = data[data['UserID'] == user_id]
    walking_data = user_data[user_data['activity'] == 'Jogging']
    walking_data = walking_data[['X', 'Y', 'Z']]
    walking_data = walking_data[:num_samples]
    
    # Calculate the time values based on sampling frequency
    timestamps = [i / sampling_frequency for i in range(len(walking_data))]
    
    plt.figure(figsize=(16, 6))
    plt.plot(timestamps, walking_data)
    plt.title(f'Acceleration Data for UserID {user_id} - Jogging (First {num_samples} Samples)')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Acceleration')
    plt.legend(['X', 'Y', 'Z'])
    plt.show()

# Example usage
# Assuming you have 'data' containing the dataset, a 'sampling_frequency' value, and a 'num_samples' value
plot_user_acceleration(user_id=36, data=data, sampling_frequency=20, num_samples=200)


# In[19]:


import matplotlib.pyplot as plt

def plot_user_acceleration(user_id, data, sampling_frequency, num_samples):
    user_data = data[data['UserID'] == user_id]
    walking_data = user_data[user_data['activity'] == 'Upstairs']
    walking_data = walking_data[['X', 'Y', 'Z']]
    walking_data = walking_data[:num_samples]
    
    # Calculate the time values based on sampling frequency
    timestamps = [i / sampling_frequency for i in range(len(walking_data))]
    
    plt.figure(figsize=(16, 6))
    plt.plot(timestamps, walking_data)
    plt.title(f'Acceleration Data for UserID {user_id} - Upstairs (First {num_samples} Samples)')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Acceleration')
    plt.legend(['X', 'Y', 'Z'])
    plt.show()

# Example usage
# Assuming you have 'data' containing the dataset, a 'sampling_frequency' value, and a 'num_samples' value
plot_user_acceleration(user_id=36, data=data, sampling_frequency=20, num_samples=200)


# In[20]:


import matplotlib.pyplot as plt

def plot_user_acceleration(user_id, data, sampling_frequency, num_samples):
    user_data = data[data['UserID'] == user_id]
    walking_data = user_data[user_data['activity'] == 'Downstairs']
    walking_data = walking_data[['X', 'Y', 'Z']]
    walking_data = walking_data[:num_samples]
    
    # Calculate the time values based on sampling frequency
    timestamps = [i / sampling_frequency for i in range(len(walking_data))]
    
    plt.figure(figsize=(16, 6))
    plt.plot(timestamps, walking_data)
    plt.title(f'Acceleration Data for UserID {user_id} - Downstairs (First {num_samples} Samples)')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Acceleration')
    plt.legend(['X', 'Y', 'Z'])
    plt.show()

# Example usage
# Assuming you have 'data' containing the dataset, a 'sampling_frequency' value, and a 'num_samples' value
plot_user_acceleration(user_id=36, data=data, sampling_frequency=20, num_samples=200)


# In[21]:


import matplotlib.pyplot as plt

def plot_user_acceleration(user_id, data, sampling_frequency, num_samples):
    user_data = data[data['UserID'] == user_id]
    walking_data = user_data[user_data['activity'] == 'Sitting']
    walking_data = walking_data[['X', 'Y', 'Z']]
    walking_data = walking_data[:num_samples]
    
    # Calculate the time values based on sampling frequency
    timestamps = [i / sampling_frequency for i in range(len(walking_data))]
    
    plt.figure(figsize=(16, 6))
    plt.plot(timestamps, walking_data)
    plt.title(f'Acceleration Data for UserID {user_id} - Sitting (First {num_samples} Samples)')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Acceleration')
    plt.legend(['X', 'Y', 'Z'])
    plt.show()

# Example usage
# Assuming you have 'data' containing the dataset, a 'sampling_frequency' value, and a 'num_samples' value
plot_user_acceleration(user_id=36, data=data, sampling_frequency=20, num_samples=200)


# In[22]:


import matplotlib.pyplot as plt

def plot_user_acceleration(user_id, data, sampling_frequency, num_samples):
    user_data = data[data['UserID'] == user_id]
    walking_data = user_data[user_data['activity'] == 'Standing']
    walking_data = walking_data[['X', 'Y', 'Z']]
    walking_data = walking_data[:num_samples]
    
    # Calculate the time values based on sampling frequency
    timestamps = [i / sampling_frequency for i in range(len(walking_data))]
    
    plt.figure(figsize=(16, 6))
    plt.plot(timestamps, walking_data)
    plt.title(f'Acceleration Data for UserID {user_id} - Standing (First {num_samples} Samples)')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Acceleration')
    plt.legend(['X', 'Y', 'Z'])
    plt.show()

# Example usage
# Assuming you have 'data' containing the dataset, a 'sampling_frequency' value, and a 'num_samples' value
plot_user_acceleration(user_id=36, data=data, sampling_frequency=20, num_samples=200)


# # Create a table of each UserId performing each Activity

# In[23]:


import pandas as pd
from IPython.display import display

# Assuming your data is stored in a DataFrame called 'data'

# Group data by 'UserID' and 'activity' and count the number of samples
user_activity_counts = data.groupby(['UserID', 'activity']).size().reset_index(name='sample_count')

# Pivot the table for better readability
user_activity_pivot = user_activity_counts.pivot(index='UserID', columns='activity', values='sample_count')

# Fill NaN values with 0
user_activity_pivot = user_activity_pivot.fillna(0).astype(int)

# Calculate the total sum of activities for each UserID
user_activity_pivot['Total'] = user_activity_pivot.sum(axis=1)

# Calculate the total number of samples for each activity
activity_sample_totals = user_activity_pivot.sum(axis=0)
activity_sample_totals.name = 'Total'

# Concatenate the total sample counts as a new row to the user_activity_pivot DataFrame
user_activity_pivot = pd.concat([user_activity_pivot, pd.DataFrame(activity_sample_totals).T])

# Apply color formatting
def color_negative_red(val):
    color = 'red' if val < 0 else 'black'
    return f'color: {color}'

styled_table = user_activity_pivot.style.applymap(color_negative_red, subset=user_activity_pivot.columns[1:-1]) \
                                        .background_gradient(cmap='coolwarm', subset=user_activity_pivot.columns[1:-1]) \
                                        .format(None, na_rep="-")

# Display the styled table
display(styled_table)


# # Label the activities of Data

# In[24]:


from sklearn.preprocessing import LabelEncoder
label = LabelEncoder() 
data['label'] = label.fit_transform(data['activity'])
data.head()


# In[25]:


data.shape


# # Create Dependent and Independent Feature

# In[26]:


data = data.drop(['activity','UserID'], axis = 1) # we drop the activity colum from independent variables


# In[27]:


data.head()


# In[28]:


columns = data.columns.tolist()
columns= [c for c in columns if c not in ["label"]]
target =  "label"
state = np.random.RandomState(42)
X = data[columns]
Y = data[target]


# In[29]:


X.shape,Y.shape


# # Exploratory Data Anlysis

# In[30]:


count_classes = pd.value_counts(data['label'],sort=True)
count_classes.plot(kind='bar',rot=0,figsize=(14,8))
plt.title("Label Distribution")
plt.xlabel("Label")
plt.ylabel("Frequency of Records")


# In[31]:


walking = data[data['label']==5]
Jogging = data[data['label']==1]
Upstairs = data[data['label']==4]
Downstairs = data[data['label']==0]
Sitting = data[data['label']==2]
Standing = data[data['label']==3]


# In[32]:


print(walking.shape,Jogging.shape,Upstairs.shape,Downstairs.shape,Sitting.shape,Standing.shape)


# # Performing the Undersampling

# In[33]:


from imblearn.under_sampling import NearMiss
nm = NearMiss()
X_res, Y_res = nm.fit_resample(X, Y)
X_res.shape, Y_res.shape


# In[34]:


from collections import Counter
print('original dataset shape{}'.format(Counter(Y)))
print('Resampled dataset shape{}'.format(Counter(Y_res)))


# # Standardize the FeatureSet

# In[35]:


from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X = scaler.fit_transform(X)

scaled_X = pd.DataFrame(data = X, columns = ['Time','X', 'Y', 'Z'])


scaled_X.head()


# # Decision Trees

# In[47]:


from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,classification_report


# Split dataset into training set and test set
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=1) # 70% training and 30% test


# In[48]:


# Create Decision Tree classifer object
clf = DecisionTreeClassifier()

# Train Decision Tree Classifer
clf = clf.fit(X_train,Y_train)

#Predict the response for test dataset
y_pred = clf.predict(X_test)


# In[49]:


accuracy = accuracy_score(Y_test, y_pred)


# In[50]:


accuracy


# In[51]:


class_report = classification_report(Y_test, y_pred)
print('Classification Report:\n', class_report)


# In[52]:


pip install mlxtend 


# In[53]:


from mlxtend.plotting import plot_confusion_matrix
from sklearn.metrics import confusion_matrix,classification_report,accuracy_score
confusion=confusion_matrix(Y_test, y_pred)
print ("Confusion Matrix", confusion)
plot_confusion_matrix(conf_mat=confusion, class_names=label.classes_, show_normed=True, figsize=(7,7))


# # Cross Validation

# In[68]:


import numpy as np
from sklearn.model_selection import cross_val_score
results=cross_val_score(KNN,X,Y,cv=10)
print(results)


# In[69]:


print(np.mean(results))


# In[ ]:




