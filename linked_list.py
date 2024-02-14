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
        if current is None:
            return 0
        n = 1
        while current.next:
            current = current.next
            n+=1 
        return n 
    
    def remove_first(self):
        current = self.head
        if current is None:
            raise ValueError('Список пуст')
        self.head = current.next

    def remove_last(self):
        current = self.head
        if current is None:
            raise ValueError('Список пуст')
        if self.head.next is None:
            self.head = None
            return
        current1 = current
        while current.next is not None:
            current1 = current
            current = current.next
        current1.next = None
    
    def remove_at(self, index):
        current = self.head
        if current is None:
            raise ValueError('Список пуст')
        n = 0
        if index == 0:
            self.head = None
            return
        while current.next and n!=index-1:
            current = current.next
            n += 1
        if current.next is None:
            raise ValueError('Нет элемента с таким индексом')
        current1 = current.next
        current.next = current1.next
    
    def remove_first_value(self, value):
        current = self.head
        if current is None:
            raise ValueError('Список пуст')
        if self.head.next is None:
            if self.head.value == value:
                self.head = None
                return
            else:
                raise ValueError('Такого значения не существует')
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
        if current is None:
            raise ValueError('Список пуст')
        if self.head.next is None:
            if self.head.value == value:
                self.head = None
                return
            else:
                raise ValueError('Такого значения не существует')
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

