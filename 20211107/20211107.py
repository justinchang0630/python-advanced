import requests, json
import matplotlib.pyplot as plt
from tkinter import *

base_url = "https://tcgbusfs.blob.core.windows.net/blobyoubike/YouBikeTP.json"
send_url = base_url
print("%s\n" % send_url)
response = requests.get(send_url)
info = response.json()
print(info)
