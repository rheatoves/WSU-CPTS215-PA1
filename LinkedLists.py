##############################################
# Title: PA1 - Doubly Linked List
# Author: Rhea Toves
# Version: 1.0
# Date: February 4, 2022
#
# Description: This program creates a doubly
# linked list, in which we are able to add,
# remove, search for elements, and more.
##############################################

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def get_data(self):
        return self.data

    def set_data(self, new_data):
        self.data = new_data

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next

    def get_prev(self):
        return self.prev

    def set_prev(self, new_prev):
        self.prev = new_prev

    def __str__(self):
        return str(self.data)

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, item):
        temp = Node(item)
        temp.next = self.head
        if self.tail is None:
            self.tail = temp
        else:
            self.head.prev = temp
        self.head = temp

    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        current = None
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
        if found and current is not None:
            if previous is None:
                self.head = current.get_next()
                if current.get_next() is not None:
                    current.get_next().set_prev(None)
                current.set_next(None)
            else:
                previous.set_next(current.get_next())
                if current.get_next() is not None:
                    current.get_next().set_prev(previous)
                current.set_next(None)
                current.set_prev(None)
        current = None
        previous = None

    def size(self):
        current = self.head
        count = 0
        previous = None
        found = False
        while current is not None:
            count = count + 1
            current = current.get_next()
        return count

    def is_empty(self):
        return self.head is None

    def __str__(self):
        list_str = "None"
        current = self.head
        while current is not None:
            list_str += " <- " + str(current.get_data()) + " -> "
            current = current.get_next()
        list_str += "None"
        return list_str

    def append(self, item):
        temp = Node(item)
        temp.prev = self.tail
        if self.head is None:
            self.head = temp
        else:
            self.tail.next = temp
        self.tail = temp

    def insert(self, index, item):
        if index > self.size():
            print("The index is out of range!")
            return False
        if index == 0: # when index = 0, add item to front
            self.add(item)
        elif index == self.size(): # when index = size of list, put item at tail
            self.append(item)
        else:
            temp = Node(item)
            current = self.head
            while self.size() > index > 0:
                current = current.next
                index -= 1
            temp.next = current
            temp.prev = current.set_prev
            current.prev.next = temp
            current.prev = temp
        return True

    def pop(self, index=None):
        if index > self.size():
            print("The index is out of range!")
            return False
        item = None
        if 0 <= index < self.size():
            if index == 0:
                item = self.head.get_data()
                self.remove(item)
                if self.head is None:
                    self.tail = None
                else:
                    self.head.prev = None
            elif index == self.size():
                item = self.tail.get_data()
                self.remove(item)
            else:
                current = self.head
                while index > 0:
                    current = current.next
                    index -= 1
                item = current.get_data()
                current.prev.next = current.next
                current.next.prev = current.prev
        return item

    def __iter__(self):
        current = self.head
        while current:
            item = current.data
            current = current.next
        return item

def main():
    shoppinglist = DoublyLinkedList()
    shoppinglist.add("Guinea Pig Food")
    shoppinglist.add("Mochi Ice Cream")
    shoppinglist.add("Chocolate Bars")
    print("The Original Shopping List: ", shoppinglist)
    print("Searching for 'Mochi Ice Cream'. Result:", shoppinglist.search("Mochi Ice Cream"))
    print("Number of elements in the shopping list:", shoppinglist.size())
    print("Is the shopping list empty?:", shoppinglist.is_empty())
    print("Removing 'Mochi Ice Cream' from the grocery list.")
    shoppinglist.remove("Mochi Ice Cream")
    print("Shopping list without Mochi Ice Cream:", shoppinglist)
    shoppinglist.append("Chicken")
    print("New shopping list (append): ", shoppinglist)
    shoppinglist.insert(0, "Beans")
    print("New shopping list (insert): ", shoppinglist)
    shoppinglist.pop(2)
    print("New shopping list (pop): ", shoppinglist)

main()