'''
objectives
-CRUD for pandas
create read update delete
-understanding set up jupyter notebooks
'''

import pandas as pd

'''
we always want to start by making a data frame
this creates the data frame (df) from csv
'''
df = pd.read_csv('final_website_stats 2.csv')

'''
the head function lets you see the first
5 rows of your dataframe.
we can also pass through any number we want in 
head(10) for example
'''
#print(df.head())

'''
#we can also create data frames from dictionaries
'''
#tempdict = {'col1':[1, 2, 3], 'col2':[4, 5, 6],}
#dictdf = pd.DataFrame.from_dict(tempdict)
#print(dictdf.head())

'''
we view our bottom 5 rows with the tail method
df.tail()
'''
#print(df.tail())

'''
viewing columns and data types
df.columns will show all columns in the dataframe
df.dtypes will show all columns' data types
'''
#print(df.columns)
#print(df.dtypes)

'''
summary statistics are necessary
the describe method will grab these
df.describe()
this will only work on ints and floats
to calculate summary stats on objects
we can pass df.describe(inlude=object)
booleans do not fit either of these 
categories well
we can pull summary statistics for all
columns using (include='all')
'''
#print(df.describe())
#print(df.describe(include=object))
#print(df.describe(include='all'))

'''
we can use the names of columns as keys. will show first and last 5 rows
df.columnname
this can get tricky if the column has spaces
if so, put the key in square brackets
df['column name']

to grab multiple columns, we pass an array of columns we want
df['column1', 'column2']

the unique method grabs unique values from a column
df.columnname.unique()
'''
#print(df.timestamp)
#print(df[['timestamp', 'page_views']])
#print(df.page_views.unique())

'''
to grab rows, we can use condition based filtering
for our csv, we have two boolean column
to select all false rows for one of them, 
we can do the following:

df[df['is_weekend'] == False]

this will check the column is_weekend 
for all False values and returns those rows

this works with other data types as well,
just pay attention to syntax. 
booleans need no ''

we can add multiple conditions as well.
lets find weekend holidays
we want is_weekend to be true
and is_holiday to be true

df[(df['is_weekend'] == True) & (df['is_holiday'] == True)]

we basically put all conditions in parenthesis
with ampersands
when we run this code, we find only 3 holiday weekends in our data set
highlights how useful this is
'''
#print(df[df['is_weekend'] == False])
#print(df[df['is_weekend'] == True])
#print(df[(df['is_weekend'] == True) & (df['is_holiday'] == True)])

'''
iloc is used for integer-location
based indexing

indexing lets us filter through a df
by using integers instead of conditions

lets say we want the 15th row of our df
df.iloc(14)
we usually 14 because df begins at row 0

we can extend iloc method
to only grab specific columns

we can slice using iloc as well
lets say we want rows 20-30
wed run df.iloc[20:30]
this will exclude 30. displays 20-29
'''

#print(df.iloc[14])
#print(df.iloc[14, 1])
#print(df.iloc[20:30])

'''
the loc method finds information through
keywords instead of integers

to do this, we need to index the df
choose a column to index to
for our example, lets use ad_spend

ad_spend = df.copy()
state.set_index('ad_spend', inplace=True)

the above code will essentially make a new df
indexed to the ad_spend column
the inplace modifier means to actually modify the df
instead of returning a modified copy

now, we can use the loc method to find 
specific value
lets say we only want to show rows where
the day of the week is tuesday
we will index again to day_of_week
next, we will use the loc method
day_of_week.loc['Tuesday']
this returns the 157 rows where the
day of the week is tuesday
'''
ad_spend = df.copy()
ad_spend.set_index('ad_spend', inplace=True)
#print(ad_spend)
#print(ad_spend.head())

day_of_week = df.copy()
day_of_week.set_index('day_of_week', inplace=True)
#print(day_of_week.loc['Tuesday'])

'''
when processing data, we will want to drop
null values
we can use two methods here

df.isnull().sum()

isnull() will find nulls
sum() will total them
for our data set, we actually have 0 null values

null values are represented as na in pandas
using the following will drop nulls

df.dropna(inplace=True)
'''
#print(df.isnull().sum())
#df.dropna(inplace=True)

'''
the drop() method will drop columns

lets say we want to drop is_holiday
we can run the following

df.drop()'is_holiday', axis=1)

we pass axis=1 because we are operating across columns
axis=0 would function along rows
for example, if we want to drop row 1:
df.drop[0, axis=0]
'''
#print(df.drop('is_holiday', axis=1).head())

'''
we can add column values
this doesnt make much sense for our data,
but lets demonstrate anyways
lets combine page views and ad spend

df['New Column'] = df['page_views'] + df['ad_spend']

'''
df['New Column'] = df['page_views'] + df['ad_spend']
#print(df['New Column'])

'''
lets say we dont like the values in our new column
we can set them to 100 with

df['New Column'] = 100
'''
#df['New Column'] = 100
#print(df['New Column'])

'''
we can use iloc to replace single values
to update just the first row of our new column

df.iloc[0, -1] = 10

here, we grab our first row (0)
the last column is -1, which is our new column
we then set it to -10
'''
#df.iloc[0, -1] = 10
#print(df.head())

'''
apply lets us do condition based updating
say we want to represent is_holiday with
1s and 0s in a new column called
holiday_binary

df['holiday_binary'] = df['is_holiday'].apply(lambda x: 1 if x==true else 0)

basically, we applied a lambda function to 
turn all trues to 1 and falses to 0

we now see two new columns at the end of our data frame
'''
df['holiday_binary'] = df['is_holiday'].apply(lambda x: 1 if x==True else 0)
#print(df.head())

'''
lets say we want to output our data to a new csv
we can output using the following

df.to_csv('output.csv')

this will output to the same directory
in our new output.csv, we see our new columns!

similarly, we can output to json and html

df.to_json()
df.to_html()

we can delete our data frame with

del df
'''
df.to_csv('output.csv')
df.to_json('output.json')
df.to_html('output.html')