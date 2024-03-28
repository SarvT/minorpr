# # import numpy as np
# # import pickle
# # import pandas as pd

# # p = np.array([[0,67,145,84,116,128,98,97.8]])
# # pickled_model = pickle.load(open('hhcs_rfc.sav', 'rb'))
# # print(pickled_model.predict(p))

# fah = 104
# cel = (fah-32)/1.8

# print(cel)

# f=96
# temp = f*9/5+32
# print(temp)


import requests
import json

url = "https://newsapi.org/v2/everything?q=health&sortBy=publishedAt&apiKey=3212fb5d74dc43009ca1cb717557acff"


response = requests.request("GET", url)
res = response.text

print(res[0])