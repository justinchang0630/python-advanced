import requests,json
import matplotlib.pyplot as plt
from tkinter import *
base_url = "https://data.epa.gov.tw/api/v1/"
api_num = "aqx_p_432?"
offset = "0"
limit = "50"
api_key = "9be7b239-557b-4c10-9775-78cadfc555e9"
send_url = base_url
send_url += api_num
send_url += "offset="+offset
send_url += "&limit="+limit
send_url += "&api_key="+ api_key
response = requests.get(send_url)
info = response.json()
a_list = []
b_list =[]
c_list =[]
if "fields" in info.keys():
  for i in range(int(limit)):
    data = info["records"][i]["County"]
    if data == "新北市":
      print("City=" + info["records"][i]["County"])
      a_list.append(info["records"][i]["SiteName"])
      print("County=" + info["records"][i]["SiteName"])
      print("AQI=" + info["records"][i]["AQI"])
      b_list.append(info["records"][i]["AQI"])
      print("PM2.5=" + info["records"][i]["PM2.5"])
      c_list.append(info["records"][i]["PM2.5"])
      print("Status=" + info["records"][i]["Status"]+"\n")
print(a_list)
print(b_list)
plt.plot(a_list,b_list, "r-^", label="AQI")
plt.plot(a_list,c_list, "g-o", label="PM2.5")
plt.legend(loc="best")
plt.show()

win = Tk()
win.title("hi")
btn1 = Button(win, text="讀取七天，天氣預報", command=get_data)
btn1.pack()

put_day1=Label(win,text = "", fg = "#588795", bg = "#00FFFF")
put_day2=Label(win,text = "", fg = "#588795", bg = "#00FFFF")
put_day3=Label(win,text = "", fg = "#588795", bg = "#00FFFF")
put_day4=Label(win,text = "", fg = "#588795", bg = "#00FFFF")
put_day5=Label(win,text = "", fg = "#588795", bg = "#00FFFF")
put_day6=Label(win,text = "", fg = "#588795", bg = "#00FFFF")
put_day7=Label(win,text = "", fg = "#588795", bg = "#00FFFF")
input_lat=Entry(win)
input_lat.pack()
input_lon=Entry(win)
input_lon.pack()

put_day1.pack()
put_day2.pack()
put_day3.pack()
put_day4.pack()
put_day5.pack()
put_day6.pack()
put_day7.pack()
win.mainloop()

