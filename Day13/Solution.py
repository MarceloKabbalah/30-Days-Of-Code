#!/bin/python
# compatible with python3

class MyBook(Book):
    def __init__(self, title, author, price):
        Book.__init__(self, title, author)
        self.price = price
        
    def display(self):
        print("Title: %s\nAuthor: %s\nPrice: %s" %(title, author, price))