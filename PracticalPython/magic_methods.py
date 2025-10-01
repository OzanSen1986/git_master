class InventoryItem:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def __repr__(self):
        return f"InventoryItem(name='{self.name}', quantity={self.quantity})"

    def __add__(self, other):
        if isinstance(other, InventoryItem) and self.name == other.name:
            return InventoryItem(self.name, self.quantity + other.quantity)
        raise ValueError('Can not add items of different type')

    def __sub__(self, other):
        if isinstance(other, InventoryItem) and self.name == other.name:
            if self.quantity >= other.quantity:
                return InventoryItem(self.name, self.quantity - other.quantity)
            raise ValueError('Can not subtract more than the available quantity')
        raise ValueError('Can not subtract items of different type')
    
    def __mul__(self, factor):
        if isinstance(factor, (int, float)):
            return InventoryItem(self.name, int(self.quantity * factor))
        raise ValueError('Multiplication factor must be a number')

    def __truediv__(self, factor):
        if isinstance(factor, (int, float)) and factor != 0:
            return InventoryItem(self.name, int(self.quantity / factor))
        raise ValueError('Division Factor must be a non-zero number.')

    def __eq__(self, other):
        if isinstance(other, InventoryItem):
            return self.name == other.name and self.quantity == other.quantity
        return False
    
    def __lt__(self, other):
        if isinstance(other, InventoryItem) and self.name == other.name:
            return self.quantity < other.quantity
        raise ValueError('Can not compare items of different types.')
    
    def __gt__(self, other):
        if isinstance(other, InventoryItem) and self.name == other.name:
            return self.quantity > other.quantity
        raise ValueError('Can not compare items of different types.')


item1 = InventoryItem("Apple", 50)
item2 = InventoryItem("Apple", 30)
item3 = InventoryItem("Orange", 20)

result_add = item1 + item2
print(result_add)

result_sub = item1 - item2
print(result_sub)

result_mul = item1 * 2
print(result_mul)

# comparing items
print(item1 > item2)
print(item1 == InventoryItem("Apple", 50))

# trying to add items of different types
try:
    result_invalid = item1 + item3
except ValueError as e:
    print(e)

# trying to subtract more than available quantity
try:
    result_invalid = item2 - item1
except ValueError as e:
    print(e)


class Counter:
    def __init__(self):
        self.value = 1

    def count_up(self):
        self.value += 1
    
    def count_down(self):
        self.value -= 1

    def __str__(self):
        return f'Count= {self.value}'

    def __add__(self, other):
        if isinstance(other, Counter):
            return self.value + other.value
        raise Exception('Invalid Type')

class CountDown:
    def __init__(self, start):
        self.current = start
    
    def __iter__(self):
        # Returns the iterator object itself.
        return self
    
    def __next__(self):
        """Returns the next value in the countdown"""
        if self.current > 0:
            value =self.current
            self.current -=1
            return value
        else:
            raise StopIteration

for number in CountDown(3):
    print(number)  







count1= Counter()
count2 = Counter()


count1.count_up()
count2.count_up()

#print(count1, count2)
#print(count1 + count2)







