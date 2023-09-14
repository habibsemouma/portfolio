import pandas
import os
from pandasql import sqldf
import numpy as np
import re
import json

hour_pattern=r'^(\d{2}):\d{2}:\d{2}$'

def convert_hour(time_data):
    return re.match(hour_pattern,time_data).group(1)

def activity_extract():

    for record in os.listdir("data"):
        if "Activity" in record:
            activity_df=pandas.read_csv("data/"+record)

    activity_df.rename(columns={'App name': 'name'}, inplace=True)
    dates=activity_df["Date"].unique()
    duration_by_hour={}

    all_hours = pandas.DataFrame({'hour': range(25)})
    for date in dates:
        if type(date)==str:

            df_slice=sqldf(f"select * from activity_df where date='{date}' and name!='Screen off (locked)'")
            df_slice["Hour"]=df_slice["Time"].apply(convert_hour)
            df_slice["Duration"]=pandas.to_timedelta(df_slice["Duration"]).dt.total_seconds().apply(lambda x:np.round(x/60,2))
            df_slice=sqldf("select Hour as hour,sum(Duration) as duration from df_slice group by Hour")
            
            print(all_hours)
            #df_slice = all_hours.merge(df_slice, on='hour', how='left').fillna(0)
            #print(df_slice)
            
            df_slice=df_slice.to_dict(orient="list")
            duration_by_hour[date]=df_slice
    with open('cleaned/activity.json',"w") as f:
        f.write(json.dumps(duration_by_hour,indent=4))
        
def activity_by_app():
    for record in os.listdir("data"):
        if "Activity" in record:
            activity_df=pandas.read_csv("data/"+record)
    activity_df.rename(columns={'App name': 'name'}, inplace=True)
    df_slice=activity_df
    df_slice["Duration"]=pandas.to_timedelta(df_slice["Duration"]).dt.total_seconds()
    df_slice=sqldf("select name,sum(duration) as duration from df_slice group by name").dropna()
    with open('cleaned/activity_by_app.json',"w") as f:
        f.write(json.dumps(df_slice.to_dict(orient="list"),indent=4))

def phone_check():
    for record in os.listdir('data'):
        if "Check" in record:
            df=pandas.read_csv("data/"+record)
            break
    df.rename(columns={'Date': 'date','Screen on time':"screentime","Check phone count":"checkcount"}, inplace=True)
    df["screentime"]=pandas.to_timedelta(df["screentime"]).dt.total_seconds().apply(lambda x:np.round(x/3600,2))
    df=df.dropna()
    df=df.to_dict(orient="list")
    with open("cleaned/check_count.json","w") as log:
        log.write(json.dumps(df,indent=4))
activity_extract()