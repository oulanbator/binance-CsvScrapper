# Binance coin market

* A very simple script to get real-time data from Binance API.
* For each request, you get the last price of all coins on Binance Exchange.
* No analysis or other features implemented, it's just a real time scrapper !
* No API keys (or even an account) needed.
* No security implemented at all. It's highly recommended to read Binance API documentation to get aware of request limits. 
* Developped only for learning purpose. Use it at your own discretion and risk.

# Minimal Setup Example

No fancy way to install it. Follow the steps.

Just clone this repository :
> git clone https://github.com/oulanbator/binance-coinmarket

Go to the repo folder :
> cd binance-coinmarket

(Recommended) Create new virtual env and activate it. E.g :
> python -m venv env
>
> source env/bin/activate

Then install requirements :
> pip install -r requirements.txt

# How it works ?
Now, once your virtual env is active. You can run your data scrapper :
> python main.py

Just define a delay betwen requests (in seconds) and start getting data !
Your CSV files are stored in "/data" folder. 
Each CSV file represents a request and give you the last price (at request time) for all crypto currencies of the binance Exchange.

That's it !
