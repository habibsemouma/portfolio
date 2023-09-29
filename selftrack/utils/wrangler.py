import json
import os
import re

import numpy as np
import pandas
from pandasql import sqldf

hour_pattern = r"^(\d{2}):\d{2}:\d{2}$"


def convert_hour(time_data):
    return re.match(hour_pattern, time_data).group(1)


def activity_extract():
    for record in os.listdir("data"):
        if "Activity" in record:
            activity_df = pandas.read_csv("data/" + record)

    activity_df.rename(columns={"App name": "name"}, inplace=True)
    dates = activity_df["Date"].unique()
    duration_by_hour = {}

    for date in dates:
        if type(date) == str:
            df = sqldf(
                f"select * from activity_df where date='{date}' and name!='Screen off (locked)'"
            )
            df["Hour"] = df["Time"].apply(convert_hour)
            df["Duration"] = (
                pandas.to_timedelta(df["Duration"])
                .dt.total_seconds()
                .apply(lambda x: np.round(x / 60, 2))
            )
            df = sqldf(
                "select Hour as hour,sum(Duration) as duration from df group by Hour"
            )
            df["duration"] = df["duration"].apply(lambda x: np.round(x, 2))
            df["hour"] = df["hour"].astype(int)

            for hour in np.arange(0, 24):
                if hour not in list(df.hour):
                    df.loc[hour + 0.5] = hour, 0
            df = df.sort_values("hour")

            df = df.to_dict(orient="list")
            duration_by_hour[date[0:5]] = df
    with open("cleaned/activity.json", "w") as f:
        f.write(json.dumps(duration_by_hour, indent=4))


def activity_by_app():
    for record in os.listdir("data"):
        if "Activity" in record:
            activity_df = pandas.read_csv("data/" + record)
    activity_df.rename(columns={"App name": "name"}, inplace=True)
    df = activity_df
    df["Duration"] = pandas.to_timedelta(df["Duration"]).dt.total_seconds()
    df = (
        sqldf("select name,sum(duration) as duration from df group by name")
        .dropna()
        .sort_values("duration")
    )
    df["duration"] = df["duration"].apply(lambda x: np.round(x / 3600))
    df = df[df["name"] != "Screen off (locked)"][-9:]
    with open("cleaned/activity_by_app.json", "w") as f:
        f.write(json.dumps(df.to_dict(orient="list"), indent=4))


def phone_check():
    for record in os.listdir("data"):
        if "Check" in record:
            df = pandas.read_csv("data/" + record)
            break
    df.rename(
        columns={
            "Date": "date",
            "Screen on time": "screentime",
            "Check phone count": "checkcount",
        },
        inplace=True,
    )
    df["screentime"] = (
        pandas.to_timedelta(df["screentime"])
        .dt.total_seconds()
        .apply(lambda x: np.round(x / 3600, 2))
    )
    df = df.dropna()
    df["date"] = df["date"].apply(lambda x: x[0:5])
    df = df.to_dict(orient="list")
    with open("cleaned/check_count.json", "w") as log:
        log.write(json.dumps(df, indent=4))
