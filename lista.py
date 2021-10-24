from typing import Any

class Node:
    value: Any
    next: 'Node'

    def __init__(self, value: Any, next=None): #konstruktor klasy Node
        self.value = value
        self.next = next

class LinkedList:
    head: Node
    tail: Node

    def __init__(self, head=None, tail=None): #konstruktor klasy LinkedList
        self.head = head
        self.tail = tail

    def push(self, value: Any):
        temp = Node(value)  # stworzenie nowego wezla
        temp.next = self.head  # referencja do starego heada
        self.head = temp  # przepiecie heada do nowego wezla
        while (temp.next is not None): #dopoki nie dojdzie do konca listy
            temp = temp.next
        self.tail = temp # przepiecie taila do ostatniego elementu
    def append(self, value: Any):
        temp = Node(value)  # stworzenie nowego wezla
        self.tail.next = temp  # podpiecie nowo stworzonego wezla pod ostatni element listy
        self.tail = temp  # przepiecie taila do nowego wezla

    def node(self, at: int):
        temp = self.head  # referencja do pierwszego elementu
        for x in range(0,at+1): #at+1 bo inaczej nie wejdzie w ifa, at to jak znak mniejszosci, bez rownosci
            if x == at:
                return temp
            temp = temp.next  # przejscie do kolejnego elementu

    def insert(self, value: Any, after: Node):
        temp = Node(value)  # stworzenie nowego wezla
        temp.next = after.next  # skopiowanie elementowi after referencji do nexta
        after.next = temp  # referencja poprzedniego elementu do nowo stworzonego

    def pop(self):
        temp = self.head  # stworzenie kopii pierwszego elementu
        self.head = self.head.next  # przepisanie heada do drugiego elementu
        return temp.value  # zwracanie straconego heada

    def remove_last(self):
        temp = self.tail  # kopia taila, zeby moc ja zwrocic
        temp2 = self.head  # poczatek listy
        while (temp2.next.next is not None):  # przechodzenie do przedostatniego elementu
            temp2 = temp2.next
        self.tail = temp2  # przepisanie taila do przedostatniego elementu
        self.tail.next = None #urwanie referencji do kolejnego elementu
        return temp.value

    def remove(self, after: Node):
        after.next = after.next.next  #przepiecie referencji do kolejnego elementu

def printlist(Llist):
    result = '' #pusty string
    temp = Llist.head #pierwszy element listy
    while(temp.next is not None): #petla iteracyjna po liscie az do przedostatniego elementu
        result = result + str(temp.value) + ' -> ' # dopisanie elementu i strzalki do stringa
        temp = temp.next #przejscie do kolejnego elementu w petli
    result = result + str(temp.value) #dodanie ostatniego elementu do stringa
    return result

def len(Llist):
    temp = Llist.head #pierwszy element listy
    counter = 0 #ustawienie licznika na zero
    while(temp.next is not None): #petla iteracyjna po liscie az do przedostatniego elementu
        counter += 1 #zwiekszenie licznika o jeden
        temp = temp.next #przejscie do kolejnego elementu w petli
    return counter+1 #dodanie ostatniego elementu i zwrocenie dlugosci

list_ = LinkedList()
assert list_.head == None
list_.push(1)
list_.push(0)

assert printlist(list_) == '0 -> 1'
list_.append(9)
list_.append(10)

assert printlist(list_) == '0 -> 1 -> 9 -> 10'
middle_node = list_.node(at=1)
list_.insert(5, after=middle_node)

assert printlist(list_) == '0 -> 1 -> 5 -> 9 -> 10'
first_element = list_.node(at=0)
returned_first_element = list_.pop()

assert first_element.value == returned_first_element
last_element = list_.node(at=3)
returned_last_element = list_.remove_last()

assert last_element.value == returned_last_element
assert printlist(list_) == '1 -> 5 -> 9'
second_node = list_.node(at=1)
list_.remove(second_node)

assert printlist(list_) == '1 -> 5'

assert len(list_) == 2
