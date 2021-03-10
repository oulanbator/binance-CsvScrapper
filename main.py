import requests, csv, time, os
from datetime import datetime

def get_timestamp():
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    return timestamp

# Create "/data" dir if not existing one
if not os.path.exists("data"):
    os.makedirs("data")

# Ask user for delay
delay = int(input("Please enter delay betwen requests (seconds) : "))

# Start looping on requests
while True:
    # Get current time, calculate next loop start
    now = datetime.now()
    next_loop_time = datetime.timestamp(now) + delay
    #  Get data
    r = requests.get('https://api.binance.com/api/v3/ticker/price')
    markets = r.json()
    # build file path
    date_time = now.strftime("%Y-%m-%d_%H-%M-%S")
    csv_filename = date_time + "_PriceTicker.csv" 
    path = os.path.join('data', csv_filename)
    # Build CSV
    with open(path, 'w', newline='') as csvfile:
        fieldnames = ['date_time', 'symbol', 'price']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=',')
        writer.writeheader()
        # Loop through market coins
        for market in markets:
            csv_date_time = now.strftime("%Y/%m/%d - %H:%M:%S")
            symbol = market.get('symbol')
            price = market.get('price')
            # write CSV row
            writer.writerow({
                "date_time": csv_date_time,
                "symbol": symbol,
                "price": price
            })
    # Alert success and wait for next loop
    print(csv_filename + " has been saved ! (infinite loop : CTRL + C to stop engines)")
    while get_timestamp() < next_loop_time:
        time.sleep(1/4)