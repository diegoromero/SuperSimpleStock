# Super Simple Stocks
Super Simple Code for Super Simple Stocks: JP Morgan assessment assignement

## Description
The source code that will :

- For a given stock, 
    - calculate the dividend yield
    - calculate the P/E Ratio
    - record a trade, with timestamp, quantity of shares, buy or sell indicator and price
    - Calculate Stock Price based on trades recorded in past 15 minutes
- Calculate the GBCE All Share Index using the geometric mean of prices for all stocks

## Requirements

- Python 3.x (tested on 3.4)

## Run

```
from supersimplestock import SuperSimpleStock, Market

sss = SuperSimpleStock('POP')

sss.trade('BUY', 100, 5.25)
sss.dividend_yield()
sss.pe_ratio()
sss.price()

sss.set_stock('GIN')

sss.trade('SELL', 1000, 3.14)
sss.dividend_yield()
sss.pe_ratio()
sss.price()

market = Market()

market.gbce()
```

