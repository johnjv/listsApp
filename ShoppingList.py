from list import List

class ShoppingList(List):

    def addItem(self, quantity, item): ##I dont like how this handes duplicate entries. Should prompt for # to add/replace immediately
        newListItem = [quantity,item]  ## after duplicate thing is added
        matchingIndex = None
        isSame = False
        for index in enumerate(self.primaryList):
            if  item in self.primaryList[index[0]]:
                isSame = True
                matchingIndex = index[0]
                print("You already have {} on your shopping list!").format(item)
                print("You may replace the existing quantity of {}({}) with {}, or you may add to it".format(item,self.primaryList[index[0]][0],quantity))
                userInput = raw_input("Type ADD, REPLACE, or CANCEL\n").upper()
                print("\n")
                ##check if valid input,
                while True:
                    if userInput == "ADD":
                        self.primaryList[index[0]][0] += quantity
                        print("Adding {} to {} for a new total of {}").format(quantity, self.primaryList[index[0]][1],self.primaryList[index[0]][0])
                        #somestuff
                        break
                    elif userInput == "REPLACE":
                        self.primaryList[index[0]][0] = quantity
                        print("replacing existing quantity of {} with {}").format(item,quantity)
                        break
                    elif userInput == "CANCEL":
                        print("returning to main menu")
                        break
                    else:
                        print("\ninvalid selection, please try again")
                        userInput = raw_input("Type ADD, REPLACE, or CANCEL\n").upper()
        if isSame == False: ##if no dupes, adds new list item & quantity
            self.primaryList.append(newListItem) ##appends new list item & quantity to list


   ## "serach list to see if item is already there, For loop that searches first item of list it each index " \
   ## "ask user if they want to add to quantity)"
  ##  "if so, add quantity in argument to existing quantity"
   ## "else, create new item, quanitity pair, append to main list"


    def getUserInput(self):
        print("Thanks for using shopPro2015, the premier useless grocery list software\n\n")
        print("Your current list is as follows:")
        self.printList()
        print("\n")
        runApplication = True
        while runApplication == True: #does not yet handle invalid input for ind. selections
            print("Would you like to ADD or REMOVE an item from your list?\n You may also VIEW your current list or QUIT")
            actionSelection = raw_input("Type ADD, REMOVE, VIEW, or QUIT\n").upper()
            if actionSelection == "ADD":
                newItem = raw_input("What would you like to add to your list?\n")
                newQuantity = int(raw_input("How many?\n"))
                self.addItem(newQuantity,newItem)
            elif actionSelection == "REMOVE": #need to verify that seleciton is in list, valid input, etc
                removeSelection = raw_input("What would you like to remove?")
                self.removeItem(removeSelection)

            elif actionSelection == "VIEW":
                self.printList()
            elif actionSelection == "QUIT":
                break
            else:
                print("invalid selection")
                actionSelection = raw_input("Type ADD, REMOVE, VIEW, or QUIT\n").upper()


    ##"Displays list and prompts user for input--- add, remove, or quit"
    ##"calls printList() to display current list"
    ##"if user types DONE, isActive is set to False, terminating while loop"
    ##"if add, prompts user for name of item they want to add, searches current list for that, and if the item already" \
      ##  "is there, asks user if they want to add to quantity..."


    def printList(self):
        firstLine = True
        for index in enumerate(self.primaryList):
            ##'print first line. Attempt at emulating do while loop...'
            while firstLine == True:
                print("Quantity       Item") ##"7 spaces"
                print("******************") ##18
                firstLine = False
            ##now print out list
            print("{}           {}").format(self.primaryList[index[0]][0], self.primaryList[index[0]][1])##11 spaces
        print(" ")


