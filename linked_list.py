class LinkedList:

    class Item:
        value = None
        next = None

        def __init__(self, value):
            self.value = value

    head:Item = None
    
    def append_begin(self, value):
        item = LinkedList.Item(value)
        item.next = self.head
        self.head = item

    def append_end(self, value):
        current = self.head
        if current is None:
            self.head = LinkedList.Item(value)
            self.head.value = value
            return
        
        while current.next:
            current = current.next
        
        item = LinkedList.Item(value)
        current.next = item


    def append_by_index(self, value, index):
       
        new_item = LinkedList.Item(value)
        if index == 0:
            new_item.next = self.head
            self.head = new_item
        else:
            current = self.head
            for i in range(index - 1):
                if current is None:
                    raise IndexError('Ошибка')
                current = current.next
            new_item.next = current.next
            current.next = new_item
    
   
    def __len__(self):
        current = self.head
        n = 1
        while current.next:
            current = current.next
            n+=1 
        return n 
    
    def remove_first(self):
        current = self.head
        self.head = current.next

    def remove_last(self):
        n = 0
        index = len(self)-1
        current = self.head
        while n != index-1:
            current = current.next
            n+=1 
        current.next = None
    
    def remove_at(self, index):
        current = self.head
        n = 0
        while current.next and n!=index-1:
            current = current.next
            n += 1
        if current.next is None:
            raise IndexError('Нет элемента с таким индексом')
        current1 = current.next
        current.next = current1.next
    
    def remove_first_value(self, value):
        current = self.head
        while current.next:
            current1 = current
            current = current.next
            if current.value == value:
                break
        else:
            raise ValueError('Такого значения не существует')
        current1.next = current.next
    
    def remove_last_value(self, value):
        current = self.head
        current1 = None
        next = None
        while current.next:
            next = current.next
            if next.value == value:
                current1 = current
            current = current.next
        if current1.value == None:
            raise ValueError("Значение не найдено")
        next = current1.next
        current1.next = next.next
        
my_list = LinkedList()
my_list.append_begin(0)
my_list.append_begin(1)
my_list.append_begin(1)
my_list.append_begin(2)
my_list.append_begin(3)
my_list.append_begin(4)
my_list.append_begin(1)
my_list.append_begin(5)
my_list.append_begin(1)
my_list.append_by_index(6, 1)
print(len(my_list))
my_list.remove_first()
print(len(my_list))
my_list.remove_last()
print(len(my_list))
my_list.remove_at(1)
print(len(my_list))
my_list.remove_first_value(3)
print(len(my_list))
my_list.remove_last_value(1)
print(len(my_list))
