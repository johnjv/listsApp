class List:
    primaryList = [[3, "spasdf"],[3, "sparf"],[ 4, "asafd"]]
    isActive = True

    def removeItem(self, item):
        print(self.printList())
        for element in enumerate(self.primaryList):
            successful = True
            "this whole while loop is a dirty way of fixing the for loop issues of skipping elements b/c I deleted an index"
            while successful:
                print(element)
                if item == self.primaryList[element[0]][0]:
                    del self.primaryList[element[0]]
                else:
                    successful = False
    ##def printList(self):

      ##  for element in enumerate(self.primaryList):
      ##      print(self.primaryList[element[0]])

