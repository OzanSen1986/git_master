def file_maker(list1 = None):
    if list1 == None:
        list1 = []
    list1.append(input('amount: '))
    list1.append(input('category: '))
    list1.append(input('date: '))
    list1.append(input('optionalnote: '))
    print("saved: ",list1)
    print(f"newest test:{list1}")

file_maker()

