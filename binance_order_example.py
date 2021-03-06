###################### EXAMPLE FOR THE ALGO:

## Calculating the quantity of the trade:

equity = 2000
num_currencies = 13

size_per_currency = equity/num_currencies

# If the currency is not traded and the condition of the signal: enter a trade:
crypto = 'BTCUSDT'
orders = client.get_open_orders(symbol=crypto)
## Check what type of data orders is
if signal and orders:
	## Make the trade:

	if signal is a buy:
		# Calculate position sizing
		currency_price = get_last_price(crypto)
		## If the base currency is USDT:
		if crypto[-4:] == 'USDT':
			number_currencies_to_trade = size_per_currency/currency_price
			order = client.order_market_buy(
	    			symbol=crypto,
	    			quantity=number_currencies_to_trade)

		## If the base currency is BTC:
		if crypto[-3:] == 'BTC':
			bitcoin_last_price = get_las_price('BTCUSDT')
			number_currencies_to_trade = size_per_currency/(currency_price*bitcoin_last_price)
			order = client.order_market_buy(
	    			symbol=crypto,
	    			quantity=number_currencies_to_trade)

	if signal is a sell:
		# Calculate position sizing
		currency_price = get_last_price(crypto)
		## If the base currency is USDT:
		if crypto[-4:] == 'USDT':
			number_currencies_to_trade = size_per_currency/currency_price
			order = client.order_market_sell(
	    			symbol=crypto,
	    			quantity=number_currencies_to_trade)

		## If the base currency is BTC:
		if crypto[-3:] == 'BTC':
			bitcoin_last_price = get_las_price('BTCUSDT')
			number_currencies_to_trade = size_per_currency/(currency_price*bitcoin_last_price)
			order = client.order_market_sell(
	    			symbol=crypto,
	    			quantity=number_currencies_to_trade)
