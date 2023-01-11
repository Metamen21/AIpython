myList = ["Earth", "revolves", "around", "Sun"]
print(myList)
print(len(myList))
print(myList[0])
print(myList[3])
#Slice elements from a list
print(myList[1:3])
#Use negative index
print(myList[-1])
#print(myList[4])
#add element to a list
myList.insert(0,"The")
print(myList)
print(len(myList))
myList.insert(4,"the")
print(myList)
#append an element to a list
myList.append("continuously")
print(myList)
print(len(myList))
#When use extend the argument should be another list
#the elements of that list will be added
#to the current list as individual elements
myList.extend(["for", "sure"])
print(myList)
print(len(myList))
#you can append a sublist to the current list using append
myList.append(["The","earth","rotates"])
print(myList)
print(len(myList))
#delete a element in the list using element
myList.remove("The")
#delete a element in the list using index
myList.remove(myList[3])
print(myList)