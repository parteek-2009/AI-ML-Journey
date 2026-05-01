"""in this we will add single element in an array 
that single element will be added one by one to all
the elements in array"""
"""lets take a case in which we have a grossery prices and we have
to apply 10 percent on each"""
import numpy as np
product_prices = np.array([100,200,300,400,500])
discount = 10
after_discount_prices = product_prices - (product_prices*discount/100)
print(after_discount_prices)