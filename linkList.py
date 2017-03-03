class Box:
    def __init__(self, data, link):
        self.data = data
        self.link = link

    def getData(self):
        return self.data

    def setData(self,data):
        self.data = data

    def getLink(self):
        return self.link

    def setLink(self, link):
        self.link = link

head = Box(45,None)
head = Box(103,head)
curr = head
while curr != None:
    print(curr.getData())
    curr = curr.getLink()

box = Box('cat',None)
#find the last box in the current linked list
#link the new box up after the last box.


