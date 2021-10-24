from lista import *
from typing import Any


class Queue:
    _storage: LinkedList

    def __init__(self, listak= LinkedList()): #listak to obiekt klasy linkedlist zastosowany w kolejce
        self._storage = listak #przepisanie listy do kolejki

    def peek(self): # zwracanie wartosci pierwszego elementu
        return self._storage.node(0).value # zwrocenie wartosci elementu za pomoca funkcji node z linkedlisty

    def enqueue(self, element: Any): #umieszczenie elementu na koncu kolejki
        self._storage.append(element) #wykorzystanie funkcji append z linkedlisty

    def dequeue(self): #zwrocenie i usuniecie pierwszego elementu w kolejce
        return self._storage.pop() #wykorzystanie funkcji pop z linkedlisty

def printk(queue): #wypisanie na ekranie elementow w kolejce
    result = ''  # pusty string
    temp = queue._storage.head # pierwszy element kolejki
    while (temp.next is not None):  # petla iteracyjna po liscie az do przedostatniego elementu
        result = result + str(temp.value) + ', '  # dopisanie elementu i przecinka do stringa
        temp = temp.next  # przejscie do kolejnego elementu w petli
    result = result + str(temp.value)  # dodanie ostatniego elementu do stringa
    return result

def lenk(queue): #zwroci liczebnosc kolejki
    return length(queue._storage)  # wykorzystuje funkcje length z biblioteki listy

queue = Queue()
assert lenk(queue) == 0
queue.enqueue('klient1')
queue.enqueue('klient2')
queue.enqueue('klient3')

assert printk(queue) == 'klient1, klient2, klient3'
client_first = queue.dequeue()

assert client_first == 'klient1'
assert printk(queue) == 'klient2, klient3'
assert lenk(queue) == 2