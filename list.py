class List:
    primaryList = [[3, "apples"],[4, "corn"], [5, "dive"]]
    isActive = True

    def removeItem(self, item):

        self.printList()
        found = None
        for element in enumerate(self.primaryList):
            #"this whole while loop is a dirty way of fixing the for loop issues of skipping elements b/c I deleted an index"
            if self.primaryList.__len__() > 0:
                if item.upper() == self.primaryList[element[0]][1].upper():
                    del self.primaryList[element[0]]
                    found = True
        if found != True:
            print("You don't have that item on your list!")
        ##def printList(self):

          ##  for element in enumerate(self.primaryList):
          ##      print(self.primaryList[element[0]])

