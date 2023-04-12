# import MetaTrader5 as mt5

# # platformaga ulanish
# if not mt5.initialize():
#     print("initialize() failed, error code =",mt5.last_error())
#     quit()

# # buyruq yuborish
# symbol = "EURUSD"
# lot = 0.1
# type = mt5.ORDER_TYPE_BUY
# price = mt5.symbol_info_tick(symbol).ask
# deviation = 20
# request = {
#     "action": mt5.TRADE_ACTION_DEAL,
#     "symbol": symbol,
#     "volume": lot,
#     "type": type,
#     "price": price,
#     "deviation": deviation,
#     "magic": 123456,
#     "comment": "Open Trade",
#     "type_time": mt5.ORDER_TIME_GTC, # Good Till Cancelled
#     "type_filling": mt5.ORDER_FILLING_FOK, # Fill or Kill
# }
# result = mt5.order_send(request)
# if result.retcode != mt5.TRADE_RETCODE_DONE:
#     print("Order failed, error:", result.comment)
# else:
#     print("Order placed:", result.order)
    
# # platformadan chiqish
# mt5.shutdown()



# -------------->   2 <---------------------------

# import alpaca_trade_api as tradeapi
# import time

# API_KEY = 'your_api_key'
# SECRET_KEY = 'your_secret_key'
# BASE_URL = 'https://paper-api.alpaca.markets'

# api = tradeapi.REST(API_KEY, SECRET_KEY, base_url=BASE_URL, api_version='v2')

# def make_order(symbol, qty, side, order_type, time_in_force):
#     try:
#         api.submit_order(
#             symbol=symbol,
#             qty=qty,
#             side=side,
#             type=order_type,
#             time_in_force=time_in_force
#         )
#         print(f"{side} order for {symbol} has been placed.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# def open_positions(symbols, target_qty):
#     for symbol in symbols:
#         make_order(symbol, target_qty, 'buy', 'market', 'gtc')
#         time.sleep(1)

# def main():
#     symbols = ['AAPL', 'GOOG', 'TSLA', 'AMZN', 'MSFT', 'NFLX', 'NVDA', 'FB', 'BRK.B', 'JPM']
#     target_qty = 10

#     for _ in range(10):  # 10 times the same set of symbols, you can modify this as per your requirements
#         open_positions(symbols, target_qty)
#         time.sleep(60)  # 1-minute interval between each set of orders

# if __name__ == '__main__':
#     main()







# -------------------> 3 <----------------------------------
import ccxt
from binance.client import Client
import tkinter as tk

API_KEY = 'your_binance_api_key'
SECRET_KEY = 'your_binance_secret_key'

binance_client = Client(API_KEY, SECRET_KEY)

def make_order(symbol, qty, side, order_type):
    try:
        binance_client.create_order(
            symbol=symbol,
            side=side,
            type=order_type,
            quantity=qty
        )
        print(f"{side} order for {symbol} has been placed.")
    except Exception as e:
        print(f"An error occurred: {e}")

def open_positions(symbols, target_qty):
    for symbol in symbols:
        make_order(symbol, target_qty, Client.SIDE_BUY, Client.ORDER_TYPE_MARKET)

def close_positions(symbols):
    for symbol in symbols:
        balance = float(binance_client.get_asset_balance(asset=symbol[:-3])['free'])
        if balance > 0:
            make_order(symbol, balance, Client.SIDE_SELL, Client.ORDER_TYPE_MARKET)

def handle_button_click():
    if not handle_button_click.positions_open:
        open_positions(symbols, target_qty)
        handle_button_click.positions_open = True
    else:
        close_positions(symbols)
        handle_button_click.positions_open = False

handle_button_click.positions_open = False

if __name__ == '__main__':
    symbols = ['BTCUSDT', 'ETHUSDT', 'BNBUSDT', 'LTCUSDT', 'LINKUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT', 'DOTUSDT', 'UNIUSDT']
    target_qty = 0.01  # Modify this value according to the minimum quantity allowed for each trading pair

    root = tk.Tk()
    root.title("Trading Bot")

    button = tk.Button(root, text="Toggle Positions", command=handle_button_click)
    button.pack()

    root.mainloop()
