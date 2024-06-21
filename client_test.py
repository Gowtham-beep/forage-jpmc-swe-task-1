import unittest
from client3 import getDataPoint
from client3 import getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote),(quote['stock'],quote['top_bid']['price'],quote['top_ask']['price'],(quote['top_bid']['price']+quote['top_ask']['price'])/2))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote),(quote['stock'],quote['top_bid']['price'],quote['top_ask']['price'],(quote['top_bid']['price']+quote['top_ask']['price'])/2))


  """ ------------ Add more unit tests ------------ """
  def test_positive_prices(self):
        self.assertEqual(getRatio(120.48, 119.2), 120.48 / 119.2)
        self.assertEqual(getRatio(150, 75), 2.0)
        self.assertEqual(getRatio(100, 50), 2.0)
    
  def test_zero_price_b(self):
        self.assertEqual(getRatio(100, 0), None)
    
  def test_zero_price_a(self):
        self.assertEqual(getRatio(0, 100), 0.0)
    
  def test_both_zero_prices(self):
        self.assertEqual(getRatio(0, 0), None)

  def test_negative_prices(self):
        self.assertEqual(getRatio(-100, 50), -2.0)
        self.assertEqual(getRatio(100, -50), -2.0)
        self.assertEqual(getRatio(-100, -50), 2.0)
      
    
if __name__ == '__main__':
    unittest.main()
