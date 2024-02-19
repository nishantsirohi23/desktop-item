class Node:
    def __init__(self,data):
        self.data =data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def traversal(self):
        current_node = self.head
        while(current_node):
            print(current_node.data)
            current_node = current_node.next

    def insertatbegin(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    def insertatindex(self,data,index):
        new_node = Node(data)
        curr_node = self.head
        count = 0
        while (count+1!=index and curr_node!=None):
            curr_node = curr_node.next
            count+=1
        new_node.next = curr_node.next
        curr_node.next =  new_node

    def insertatend(self,data):
        new_node = Node(data)
      
        curr_node = self.head
        while(curr_node.next!=None):
            curr_node = curr_node.next
        curr_node.next = new_node
    def remove_at_index(self, index):
        if self.head == None:
            return
 
        current_node = self.head
        position = 0
        if position == index:
            self.remove_first_node()
        else:
            while(current_node != None and position+1 != index):
                position = position+1
                current_node = current_node.next
 
            if current_node != None:
                current_node.next = current_node.next.next
            else:
                print("Index not present")

    def deletefirst(self):
        if (self.head==None):
            return 
        self.head = self.head.next
    def deletedata(self,data):
        dummy = Node(0)
        dummy.next = self.head
        current = dummy

        # Iterate through the linked list
        while current.next:
            # Check if the next node has the target value
            if current.next.data == data:
                # Skip the node with the target value
                current.next = current.next.next
            else:
                # Move to the next node
                current = current.next

        # Return the updated linked list
        return dummy.next
    def callength(self) -> int:
        if self.head is None:
            return 0
        curr_node = self.head
        count = 0
        while(curr_node!=None):
            count+=1
            curr_node = curr_node.next

        return count
    
    def remove_dupes(self):
        if self.head is None:
            return

        before = self.head
        after = before.next

        while after is not None:
            if before.data == after.data:
                print("Duplicate found, removing:", after.data)
                before.next = after.next
            else:
                before = before.next

            after = after.next

    def find_duplicates(self):
        seen_set = set()
        duplicates = set()
        current = self.head

        while current is not None:
            if current.data in seen_set:
                duplicates.add(current.data)
            else:
                seen_set.add(current.data)
            current = current.next

        return list(duplicates)


        
    


        
        


linkedlist = LinkedList()
linkedlist.insertatbegin('1')
linkedlist.insertatend('1')
linkedlist.insertatend('2')
linkedlist.insertatend('3')
linkedlist.insertatend('3')
linkedlist.insertatend('4')
linkedlist.insertatend('4')
linkedlist.insertatend('5')
linkedlist.traversal()

print("asfdasdf")
linkedlist.traversal()
mylist = linkedlist.find_duplicates()
print(mylist)
linkedlist.deletedata('1')
print("hey")
linkedlist.traversal()
for num in mylist:
    linkedlist.deletedata(num)



linkedlist.traversal()