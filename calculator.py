import math

class Math:
    @staticmethod
    def add(x,y):
        return x+y
    @staticmethod
    def remove(x,y):
        return x-y
    @staticmethod
    def mulitiply(x,y):
        return x*y
    @staticmethod
    def divide(x,y):
        return x/y


def calculate():
    var = ("+","-","*","/")
    take = input("\n".join(var))
    if take == "+":
        num1 = int(input(">"))
        num2 = int(input(">"))
        print(Math.add(num1,num2))
    if take == "-":
        num1 = int(input(">"))
        num2 = int(input(">"))
        print(Math.remove(num1,num2))
    if take == "*":
        num1 = int(input(">"))
        num2 = int(input(">"))
        print(Math.mulitiply(num1,num2))
    if take == "/":
        num1 = int(input(">"))
        num2 = int(input(">"))
        print(Math.divide(num1,num2))


calculate()
