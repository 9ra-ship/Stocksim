import os
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame 

API_KEY = ("PK04738MQ0VKKJRYSKGY")
SECRET_KEY = ("IYhz0yHeP9zWsUV5VkdCbB4DFIrkKwcm4sAM651Z")
client = StockHistoricalDataClient(api_key=API_KEY, secret_key=SECRET_KEY)
