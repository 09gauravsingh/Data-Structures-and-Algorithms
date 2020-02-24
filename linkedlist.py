class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.start=None
    def viewList(self):
        if self.start==None:
            print("list is empty")
        else:
            temp=self.start
            while temp!=None:
                print(temp.data,end= ' ')
                temp=temp.next
    def deleteFirst(self):
        if self.start==None:
            print("linked list is empty")
        else:
            self.start=self.start.next
    def insertList(self,value):
        newNode=node(value)
        if(self.start==None):
            self.start = newNode
        else:
            temp=self.start
            while temp.next!=None:
                temp=temp.next
            temp.next=newNode

mylist=LinkedList()
mylist.insertList(40)
mylist.insertList(80)
mylist.insertList(30)
mylist.viewList()
print()
mylist.deleteFirst()
mylist.viewList()
input()



