import adafruit_dht
import board
import time

# DHT11センサーをGPIO17に接続
dhtDevice = adafruit_dht.DHT11(board.D17)

# 1回データを取得
try:
    temperature = dhtDevice.temperature
    humidity = dhtDevice.humidity
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
except Exception as e:
    print(f"Error reading sensor: {e}")
