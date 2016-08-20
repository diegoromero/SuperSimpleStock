#! /usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
from functools import reduce
from operator import mul

STOCKS = {
        'TEA': {"symbol": 'TEA', "type": 'Common', "last_dividend": 0, "fixed_dividend": 0.0, "par_value": 100},
        'POP': {"symbol": 'POP', "type": 'Common', "last_dividend": 0.08, "fixed_dividend": 0.0, "par_value": 100},
        'ALE': {"symbol": 'ALE', "type": 'Common', "last_dividend": 0.23, "fixed_dividend": 0.0, "par_value": 60},
        'GIN': {"symbol": 'GIN', "type": 'Preferred', "last_dividend": 0.8, "fixed_dividend": 0.02, "par_value": 100},
        'JOE': {"symbol": 'JOE', "type": 'Common', "last_dividend": 0.13, "fixed_dividend": 0.0, "par_value": 250}
    }

trades = []

class SuperSimpleStock:
    """
    Common base class for stocks (class SuperSimpleStock)

    Constructor: SuperSimpleStock(symbol)
    """
    global STOCKS, trades
    
    def __init__(self, symbol):
        self.stock = STOCKS[symbol]
        
    def set_stock(self, symbol):
        """
        Sets the stock of the class to <symbol>
        
        :param symbol: symbol of the stock
        """
        self.stock = STOCKS[symbol]
        
    def dividend_yield(self):
        """
        Calculate dividend yield
        """
        price = self.price()
        if price:
            if self.stock['type'] == 'Common':
                return self.stock['last_dividend'] / price
            else:
                return (self.stock['fixed_dividend'] * self.stock['par_value']) / price
        else: 
            return None
    
    def pe_ratio(self):
        """
        Calculate P/E Ratio
        """
        dividend = self.dividend_yield()
        if dividend:
            return self.price() / dividend
        else:
            return None
    
    def trade(self, action, quantity, price):
        """
        Record a trade with timestamp == datetime.datetime.now()       

        :param action: SELL, BUY
        :param quantity: quantity of shares
        :param price: price of the share
        
        """
        trade = {
            'timestamp': datetime.datetime.now(),
            'action': action,
            'quantity': quantity,
            'price': price,
            'symbol': self.stock['symbol']
        }
        trades.append(trade)
        return trade
    
    def price(self):
        """
        Calculate Stock Price based on trades recorded in past 15 minutes
        """
        threshold = datetime.datetime.now() - datetime.timedelta(minutes=15)
        filtered = list(filter(lambda trade: trade['timestamp'] >= threshold and trade['symbol'] == self.stock['symbol'], trades))
        num = sum(map(lambda trade: trade['price'] * trade['quantity'], filtered))
        denum = sum(map(lambda trade: trade['quantity'], filtered))
        return num / denum if denum > 0 else None

    
class Market:
    """
    Common base class for the market (class Market)

    Constructor: Market()
    """
    global STOCKS
    
    def gbce(self):
        """
        Calculate the GBCE All Share Index using the geometric mean of prices for all stocks
        """
        prices = list(filter(lambda price: price != None, map(lambda stock: SuperSimpleStock(stock).price() ,STOCKS)))
        if prices:
            return pow(reduce(mul, prices), 1/len(prices))
        else:
            return None