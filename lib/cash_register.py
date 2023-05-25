#!/usr/bin/env python3


class CashRegister:
  def __init__(self, discount= 0):
    self.discount = discount
    self.total = 0.0
    self.items =[]
    self.price = []


  def add_item(self, title, price, quantity= 1):
    self.total += price * quantity
    for _ in range(0, quantity):
        self.items.append(title)
        self.price.append(price)

  def apply_discount(self):
    if self.discount > 0:
        self.total -= self.total * self.discount//100
        print(f"After the discount, the total comes to ${self.total}.")

    else:
      print("There is no discount to apply.")

  def void_last_transaction(self):
      last_item_price =self.price.pop()
      if self.discount > 0:
          self.total -= last_item_price * self.discount//100
          self.items.pop()
          if len(self.items) == 0:
              self.total = 0.0

      else:
         self.total -= last_item_price
         self.items.pop()
         if len(self.items) == 0:
            self.total = 0.0
      
     
     
      
