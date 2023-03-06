# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC 
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>

# COMMAND ----------

# MAGIC %md
# MAGIC # COVID Demo
# MAGIC ## Data Analysis with **`pandas`**
# MAGIC 
# MAGIC ## ![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png) In this lesson you:<br>
# MAGIC  - Import the COVID-19 dataset
# MAGIC    * **`pd.read_csv()`**
# MAGIC  - Summarize the data
# MAGIC    * **`head`**, **`tail`**, **`shape`**
# MAGIC    * **`sum`**, **`min`**, **`count`**, **`mean`**, **`std`**
# MAGIC    * **`describe`**
# MAGIC  - Slice and munge data
# MAGIC    * Slicing, **`loc`**, **`iloc`**
# MAGIC    * **`value_counts`**
# MAGIC    * **`drop`**
# MAGIC    * **`sort_values`**
# MAGIC    * Filtering
# MAGIC  - Group data and perform aggregate functions
# MAGIC    * **`groupby`**
# MAGIC  - Work with missing data and duplicates
# MAGIC    * **`isnull`**
# MAGIC    * **`unique`**, **`drop_duplicates`**
# MAGIC    * **`fillna`**
# MAGIC  - Visualization
# MAGIC    * Histograms
# MAGIC    * Scatterplots
# MAGIC    * Lineplots
# MAGIC  
# MAGIC  Check out <a href="https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf" target="_blank">this cheetsheet</a> for help.
# MAGIC  
# MAGIC  See also the <a href="https://pandas.pydata.org/docs/" target="_blank">pandas docs</a>.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Import the COVID-19 dataset

# COMMAND ----------

# MAGIC %md
# MAGIC Use `%sh ls` to search the folder structure

# COMMAND ----------

# MAGIC %sh ls /dbfs/databricks-datasets/COVID/

# COMMAND ----------

# MAGIC %sh ls /dbfs/databricks-datasets/COVID/CSSEGISandData/csse_covid_19_data/csse_covid_19_daily_reports

# COMMAND ----------

# MAGIC %md
# MAGIC Use `%sh head` to see the first few lines of CSV file

# COMMAND ----------

# MAGIC %sh head /dbfs/databricks-datasets/COVID/CSSEGISandData/csse_covid_19_data/csse_covid_19_daily_reports/04-11-2020.csv

# COMMAND ----------

# MAGIC %md
# MAGIC Import **`pandas`**.  
# MAGIC 
# MAGIC Alias it as **`pd`**:

# COMMAND ----------

import pandas as pd

# COMMAND ----------

# MAGIC %md
# MAGIC Read the csv file. 
# MAGIC 
# MAGIC This creates a **`DataFrame`**.

# COMMAND ----------

pd.read_csv("/dbfs/databricks-datasets/COVID/CSSEGISandData/csse_covid_19_data/csse_covid_19_daily_reports/04-11-2020.csv")

# COMMAND ----------

# MAGIC %md
# MAGIC Now let's combine the lines of code and save the **`DataFrame`** to a variable so we can reuse it

# COMMAND ----------

import pandas as pd

df = pd.read_csv("/dbfs/databricks-datasets/COVID/CSSEGISandData/csse_covid_19_data/csse_covid_19_daily_reports/04-11-2020.csv")
df

# COMMAND ----------

# MAGIC %md
# MAGIC ### Summarize the data

# COMMAND ----------

# MAGIC %md
# MAGIC First, let's talk tab completion

# COMMAND ----------

# df. # Uncomment this and press 'tab' with your cursor after the "."

# COMMAND ----------

# MAGIC %md
# MAGIC Need help?

# COMMAND ----------

help(df.head())

# COMMAND ----------

# MAGIC %md
# MAGIC Take a peak at the first and last few rows of the data

# COMMAND ----------

df.head()

# COMMAND ----------

df.tail(2)

# COMMAND ----------

# MAGIC %md
# MAGIC How many records are in the dataset?

# COMMAND ----------

df.shape

# COMMAND ----------

# MAGIC %md
# MAGIC Summarize the data

# COMMAND ----------

# df.sum()
# df.min()
# df.max()
# df.count()
df.mean()
# df.std()

# COMMAND ----------

# MAGIC %md
# MAGIC These summary stats are aggregated for you...

# COMMAND ----------

df.describe()

# COMMAND ----------

# MAGIC %md
# MAGIC ### Slice and munge data

# COMMAND ----------

# MAGIC %md
# MAGIC Grab just the confirmed cases

# COMMAND ----------

df["Confirmed"]

# COMMAND ----------

# MAGIC %md
# MAGIC Grab the country and confirmed cases.

# COMMAND ----------

df.columns

# COMMAND ----------

df[["Country_Region", "Confirmed"]]

# COMMAND ----------

# MAGIC %md
# MAGIC Create a new column called **`Date`**

# COMMAND ----------

import datetime

df["Date"] = datetime.date(2020, 4, 11)

# COMMAND ----------

df["Date"].head()

# COMMAND ----------

# MAGIC %md
# MAGIC Slice the DataFrame to get the first 10 rows

# COMMAND ----------

df.loc[:10, ["Country_Region", "Confirmed"]]
# df.loc[0:10, ["Country_Region", "Confirmed"]] # Same thing

# COMMAND ----------

# MAGIC %md
# MAGIC Return just the first column from the first row

# COMMAND ----------

df.iloc[0, 0]

# COMMAND ----------

# MAGIC %md
# MAGIC How many regions to we have per country?

# COMMAND ----------

df["Country_Region"].value_counts()

# COMMAND ----------

# MAGIC %md
# MAGIC What's FIPS?

# COMMAND ----------

df = df.drop("FIPS", axis=1)

# COMMAND ----------

# MAGIC %md
# MAGIC Sort by confirmed cases

# COMMAND ----------

df.sort_values("Confirmed", ascending=False)

# COMMAND ----------

# MAGIC %md
# MAGIC Let's just look at what's going on in the US

# COMMAND ----------

df[df["Country_Region"] == "US"]

# COMMAND ----------

# MAGIC %md
# MAGIC Now let's look at what's going on in my county

# COMMAND ----------

df[(df["Country_Region"] == "US") & (df["Province_State"] == "California") & (df["Admin2"] == "San Francisco")]

# COMMAND ----------

# MAGIC %md
# MAGIC ### Group data and perform aggregate functions

# COMMAND ----------

# MAGIC %md
# MAGIC What country has the greatest number of confirmed cases?

# COMMAND ----------

df.groupby("Country_Region")

# COMMAND ----------

# MAGIC %md
# MAGIC Group and sum the data. **Note that an aggregate function return a scalar (single) value.**

# COMMAND ----------

df.groupby("Country_Region")["Confirmed"].sum().sort_values(ascending=False)

# COMMAND ----------

# MAGIC %md
# MAGIC Which US states have the most cases?

# COMMAND ----------

df[df["Country_Region"] == "US"].groupby("Province_State")["Confirmed"].sum().sort_values(ascending=False)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Work with missing data and duplicates

# COMMAND ----------

# MAGIC %md
# MAGIC Do we have null values?

# COMMAND ----------

df.isnull().tail()

# COMMAND ----------

df.isnull().sum()

# COMMAND ----------

# MAGIC %md
# MAGIC How many unique countries?

# COMMAND ----------

df["Country_Region"].unique().shape

# COMMAND ----------

# MAGIC %md
# MAGIC Another way to do the same thing.

# COMMAND ----------

df["Country_Region"].drop_duplicates()

# COMMAND ----------

df.fillna("NO DATA AVAILABLE").tail(3)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Visualization
# MAGIC    * Histograms
# MAGIC    * Scatterplots
# MAGIC    * Lineplots

# COMMAND ----------

us_subset_df = df[df["Country_Region"] == "US"]

# COMMAND ----------

# MAGIC %md
# MAGIC What is the _distribution_ of deaths by US states and territories?

# COMMAND ----------

us_subset_df.groupby("Province_State")["Deaths"].sum().hist()

# COMMAND ----------

us_subset_df.groupby("Province_State")["Deaths"].sum().hist(bins=30)

# COMMAND ----------

# MAGIC %md
# MAGIC How do confirmed cases compare to deaths?

# COMMAND ----------

us_subset_df.plot.scatter(x="Confirmed", y="Deaths")

# COMMAND ----------

us_subset_df[us_subset_df["Deaths"] < 1000].plot.scatter(x="Confirmed", y="Deaths")

# COMMAND ----------

# MAGIC %md
# MAGIC Import the data for all available days.

# COMMAND ----------

import glob

path = "/dbfs/databricks-datasets/COVID/CSSEGISandData/csse_covid_19_data/csse_covid_19_daily_reports"
all_files = glob.glob(path + "/*.csv")

dfs = []

for filename in all_files:
    temp_df = pd.read_csv(filename)
    temp_df.columns = [c.replace("/", "_") for c in temp_df.columns]
    temp_df.columns = [c.replace(" ", "_") for c in temp_df.columns]

    month, day, year = filename.split("/")[-1].replace(".csv", "").split("-")
    d = datetime.date(int(year), int(month), int(day))
    temp_df["Date"] = d

    dfs.append(temp_df)
    
all_days_df = pd.concat(dfs, axis=0, ignore_index=True, sort=False)
all_days_df = all_days_df.drop(["Latitude", "Longitude", "Lat", "Long_", "FIPS", "Combined_Key", "Last_Update"], axis=1)

# COMMAND ----------

all_days_df.head()

# COMMAND ----------

# MAGIC %md
# MAGIC How has the disease spread over time?

# COMMAND ----------

all_days_df.groupby("Date")["Confirmed"].sum().plot(title="Confirmed Cases over Time", rot=45)

# COMMAND ----------

# MAGIC %md
# MAGIC Break this down by types of cases.

# COMMAND ----------

all_days_df.groupby("Date")["Confirmed", "Deaths", "Recovered"].sum().plot(title="Confirmed, Deaths, Recovered over Time", rot=45)

# COMMAND ----------

# MAGIC %md
# MAGIC What is the growth in my county?

# COMMAND ----------

(all_days_df[(all_days_df["Country_Region"] == "US") & (all_days_df["Province_State"] == "California") & (all_days_df["Admin2"] == "San Francisco")]
 .groupby("Date")["Confirmed", "Deaths", "Recovered"]
 .sum()
 .plot(title="Confirmed, Deaths, Recovered over Time", rot=45))

# COMMAND ----------

# MAGIC %md
# MAGIC Wrap this up in a function and run it yourself!

# COMMAND ----------

def plot_my_country(Country_Region, Province_State, Admin2):
    (all_days_df[(all_days_df["Country_Region"] == Country_Region) & (all_days_df["Province_State"] == Province_State) & (all_days_df["Admin2"] == Admin2)]
     .groupby("Date")["Confirmed", "Deaths", "Recovered"]
     .sum()
     .plot(title="Confirmed, Deaths, Recovered over Time", rot=45))

plot_my_country("US", "New York", "New York City")

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2022 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>
