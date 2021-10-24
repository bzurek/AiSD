from lista import *
from typing import Any


class Stack:
    _storage: LinkedList #storage ma atrybut linkedlisty

    def __init__(self, listas = LinkedList()): #listas to obiekt klasy linkedlist zastosowany w stosie
        self._storage = listas #przepisanie listy do stosu

    def push(self, element: Any): #dodanie elementu na szczyt stosu
        self._storage.append(element) #wykorzystanie funkcji append z linkedlisty

    def pop(self): #zdecie elementu ze stosu
        return self._storage.remove_last() #zwrocenie zdjetego elementu za pomoca funkcji remove_last z linkedlisty

def prints(stack): #funkcja wypisujaca elementy ze stosu w kolumnie
    tab = [] #deklaracja pustej tablicy
    temp = stack._storage.head #przypisanie heada do tempa
    while temp is not None: #petla spradzajaca czy temp jest pusty
        tab.append(temp.value) #wpisanie wartosci z tempa do taba
        temp = temp.next #przejscie do kolejnego elementu
    tab2 = tab[:: -1] #odwrocenie tablicy
    for x in tab2: #przejscie po odwroconej tablicy
        print(x) #wypisanie na ekranie elementow z tablicy

def len(stack): #funkcja zwracajaca wysokosc stacka
    return length(stack._storage) # wykorzystuje funkcje length z biblioteki listy

stack = Stack()
assert len(stack) == 0
stack.push(3)
stack.push(10)
stack.push(1)

assert len(stack) == 3
top_value = stack.pop()

assert top_value == 1
assert len(stack) == 2