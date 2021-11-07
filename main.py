import requests, json
import matplotlib.pyplot as plt
from tkinter import *


base_url="https://tcgbusfs.blob.core.windows.net/blobyoubike/YouBikeTP.json"
send_url = base_url
print("%s\n" % send_url)
response = requests.get(send_url)
info = response.json()


for i in info["retVal"]:
  print(i)
  print(info["retVal"][i])
  a_list.append(info["records"][i]["SiteName"])

  print("County=" + info["records"][i]["SiteName"])
  print("AQI=" + info["records"][i]["AQI"])
  b_list.append(info["records"][i]["AQI"])
                print("PM2.5=" + info["records"][i]["PM2.5"])
                c_list.append(info["records"][i]["PM2.5"])
                print("Status=" + info["records"][i]["Status"] + "\n")
                print("Status=" + info["records"][i]["Status"])
                show += "County=" + info["records"][i][
                    "SiteName"] + " AQI=" + info["records"][i][
                        "AQI"] + " PM2.5=" + info["records"][i][
                            "PM2.5"] + info["records"][i]["Status"] + "\n"
