class List:
    primaryList = [[3, "spasdf"],[3, "sparf"],[ 4, "asafd"]]
    isActive = True

    def removeItem(self, item):

        print(self.printList())
        for element in enumerate(self.primaryList):
            successful = True
            #"this whole while loop is a dirty way of fixing the for loop issues of skipping elements b/c I deleted an index"
            while successful:
                print(self.primaryList[element[0]][1])
                print(element)
                if item.upper() == self.primaryList[element[0]][1].upper():
                    print(self.primaryList[element[0]])
                    del self.primaryList[element[0]]
                else:
                    successful = False
    ##def printList(self):

      ##  for element in enumerate(self.primaryList):
      ##      print(self.primaryList[element[0]])

