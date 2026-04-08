from dataclasses import dataclass
@dataclass
class Book:
    title:str
    author:str
    pages:int
b1=Book("O'tkan kunlar","A.Qodiriy",450)
b2=Book("O'tkan kunlar","A.Qodiriy",450)
print(b1)
print(b1==b2)