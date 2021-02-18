
def show_all_elems_in_voc(voc):
  for j in voc:
    print(j,voc[j])

def add_book_by_its_name(voc,book_name):
  for i in voc:
    if book_name in voc[i]:
      voc[i][2] += 1  

def rename_book(voc,old_books_name,new_books_name):
  for j in voc:
    if old_books_name in voc[j]:
      voc[j][0] = new_books_name

def add_book_by_its_number(voc,num_of_book):
    voc[num_of_book][2] += 1 

def change_books_author(voc,book_name,author_name):
    for i in voc:
      if book_name in voc[i]:
        voc[i][1] = author_name 

LIST_OF_BOOKS = [[13,"BookOne","Vasily Yakovlev",10],[2,"BookTwo","Petr Podbelskiy",15],[6,"BookThree","Dmitry Polyakov",3],
                 [1,"BookThree","Senya Burdenko",111],[8,"BookFour","Sergey Denisov",2],[3,"BookFive","Vitya Yakovlevenko",2],
                 [5,"BookSix","Evgeniy Dashchenko",6],[4,"BookSix","Anton Gnatechenko",10],[7,"BookSeven","Semyon Radchenko",1],
                 [11,"BookEight","Vasily Demyanov",21],[12,"BookNine","Sergio Mussolini",19],[10,"BookTen","Adolf Riberg",10],
                 [9,"BookEleven","Ben Pavlikov",3]]
LIST_OF_BOOKS.sort()
voc = {}

for j in range(0,len(LIST_OF_BOOKS)):
  voc[LIST_OF_BOOKS[j][0]] = [LIST_OF_BOOKS[j][1],LIST_OF_BOOKS[j][2],LIST_OF_BOOKS[j][3]]

print("Hi! My name is Vittorio, I work with list of books. Tell me the name of your's dictionary: ")
dict_name = input()

while 1:
  print("Would would you like to do with " + dict_name + " ?")
  print(">>> 1.Increase number of books by name.")
  print(">>> 2.Rename book.")
  print(">>> 3.Increase number of books by number.")
  print(">>> 4.Show all elements in dictionary.")
  print(">>>0.Close program.")
  choosen_variant = int(input())
  if choosen_variant == 1:
    print("Input the name of book: ")
    books_name = input()
    add_book_by_its_name(voc,books_name)
    print("Succesful!")
  elif choosen_variant == 2:
    print("Var2")
  elif choosen_variant == 3:
    print("Var3")
  elif choosen_variant == 4:
    show_all_elems_in_voc(voc)
  elif choosen_variant == 0:
    print("Bye-bye!")
    break
  else:
    print("There is no command with that number!")
