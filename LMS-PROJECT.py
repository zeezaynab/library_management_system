#Part1)
#inventory:
library=[]

#Part2)
#add book:
def add_book():
  title=input("enter title of book here: ").lower()
  author=input("enter name of author here: ").lower()
  publicationyear=(input("enter year of publication here: "))
  status=input("is it available or checked out? ").lower()
  new_book=[title,author,publicationyear,status]
  library.append(new_book)
  print(f"Book {title} by {author} published in{publicationyear}has been added to the library.")   
  print()

#Part3)
#display book:
def display_book():       
  for book in library:
     print(book)

#Part4)
def check_out_book(title):
    checked_book=None
    for book in library:
        if book[0]==title:
            checked_book=book
    if checked_book==None:
        print(f"{title} does not exist.")
    else:
        if checked_book[3]=="available":
           checked_book[3]="checked out"
           print(f"Book {title} has now been checked out.Happy reading♡")
        else:
           print(f"Book {title} is already checked out.better luck next time:(")
        
#Part5)
#search book:
def search_book(search_term):
    found=0
    for book in library:
        if book[0]==search_term or book[1]==search_term or book[2]==search_term:  
            found+=1
            break
    if found!=0:
        print(f"The book you are searching for is {book[0]}.")
    else:
        print(f"The book you are searching for doesnt exit in this library:(")
            
#Part6)
#count books:
def count_books():
  return len(library) 

#Part 7)
#Delete books:
def delete_books(search_term):
    found=None
    for book in library:
        if book[0]==search_term or book[1]==search_term or book[2]==search_term:  
            found=book
            break
    if found==book:
        library.remove(found)
        print(f"The book {found[0]} has now been removed from the library.")
    else:
        print(f"The book you are searching for doesnt exit in this library:(")

#Part 8)
#Main loop for the library management system:
print("\n˚♡ Welcome to Opulent library ♡˚")
for _ in range(999):                                          
    print("\nLibrary Management System Menu:\n")          
    print("1.Add a book")                               
    print("2.Display all books")
    print("3.Check out a book")
    print("4.Search for a book")
    print("5.Count the number of books")
    print("6.Delete books")
    print("7.Exit")
    choice = input("Enter your choice (1-7):")
    if choice=="1":
        add_book()
    elif choice=="2":
        display_book()
    elif choice=="3":
        title = input("enter book title: ")
        check_out_book(title)
    elif choice=="4":
        search_book(input("enter search term: "))
    elif choice=="5":
        print(f"Book count: {count_books()}")
    elif choice=="6":
        delete_books(input("enter search term: "))
    elif choice=="7":
        print("♡Goodbye♡")
        break
    else:
        print("chose a number between 1 and 7.")