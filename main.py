# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val=val
#         self.next=next
#
#
# class LinkedList:
#     def __init__(self, head=None):
#         self.head=head
#
#
#     def insert(self,val):
#         new_node = ListNode(val)
#         if self.head==None:
#             self.head=new_node
#             return
#         else:
#             curr=self.head
#         while curr.next!=None:
#             curr=curr.next
#         curr.next=new_node
#
#
#     def __str__(self):
#         res=""
#         curr=self.head
#         while curr != None:
#             print(curr.val)
#             curr=curr.next
#
#
#
#
#
# list1=LinkedList()
# list1.insert(3)
# list1.insert(1)
# list1.insert(4)
# print(list1)


"""
Класс ForeignPassport является производным от класса Passport. Метод PrintInfo
существует в обоих классах. PassportList представляет собой список, содержащий объекты
обоих классов. Вызов метода PrintInfo для каждого элемента списка демонстрирует его
полиморфное поведение.
"""


class Passport:
    def __init__(self, first_name, last_name, birthday, number, country):
        self.first_name=first_name
        self.last_name=last_name
        self.birthday=birthday
        self.number=number
        self.country=country


    def print_info(self):
        print(self.first_name, self.last_name, self.birthday, self.number, self.country)


class ForeignPassport(Passport):
    def __init__(self, first_name, last_name, birthday, number, country, visa):
        self.visa=visa
        super().__init__(first_name, last_name, birthday, number, country)


    def print_info(self):
        super().print_info()
        print(self.visa)


passportlist=[]
foreignpassport=ForeignPassport("David","Azdza","13.07.2023", 13432, "Russia", "есть")
passport=Passport("David","Azdza","13.07.2023", 23432, "Russia")
passportlist.append(foreignpassport)
passportlist.append(passport)
print(passportlist)
print(passportlist[0].number)