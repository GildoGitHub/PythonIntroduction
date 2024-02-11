people = ['Gildo', 'Maria', 'Teresa', 'Joao', 'Louren']

#Printting elements of list
print(people)
print() #Jumping one line

#Printting singular values 
for element in people:
    print(element.title())
print() #Jumping one line

#Sortting list
people.sort()
print(people)
print() #Jumping one line

#Reverse sort
people.sort(reverse=True)
print(people)
print() #Jumping one line

people.append('Jorge') #Adding one element in list
print(people)
print() #Jumping one line

people.pop() #Deleting one element on top
print(people)
print() #Jumping one line

sorted(people) #Using method sorted to sort list temporarity

lista = ['A','S','K']

l=sorted(lista,reverse=True) #Using sorted method to reverse sort list temporarity
print(l)







