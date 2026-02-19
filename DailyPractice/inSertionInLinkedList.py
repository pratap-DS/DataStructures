class Node:
    def __init__(self,info,link=None):
        self.info = info
        self.link = link


class LinkedList:

    def __init__(self):
        self.head = None

    def insertionAtBeginning(self,info):
        
        newNode = Node(info)
        if self.head != None:
            newNode.link = self.head
            self.head = newNode
        else:
            self.head = newNode

    def insertionAtEnd(self, info):
        
        newNode = Node(info)
        if self.head != None:
            current = self.head
            while (current.link != None):
                current = current.link
            current.link = newNode
        else:
            self.head = newNode

    def printElements(self):

        if self.head != None:
            currentHead = self.head
            while currentHead != None:
                print(currentHead.info)
                currentHead = currentHead.link
        else:
            print("No elements found in LL")


    def insertAtposition(self,info, position):

        count = 1
        newNode = Node(info)
        if self.head != None:
            current = self.head

            while (current.link != None):
                # print("Is he?",count,position)
                if count == position:
                    # print("Is here?")
                    saveLink = current.link
                    current.link = newNode
                    newNode.link = saveLink
                    break
                count += 1
                current = current.link


        else:

            pass



            

                










LL = LinkedList()
LL.insertionAtBeginning(10)
LL.insertionAtBeginning(123)
LL.insertionAtBeginning(1234)
LL.printElements()
LL.insertionAtEnd(9)
LL.insertionAtEnd(8)
LL.insertAtposition(9999,0)
LL.printElements()









        




        


         
            

