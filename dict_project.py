#  ============mini_project_(dictionery)_start================
dit ={}

while True:
    print("/n Dictonery liberyare section")
    print("1: Add new word")
    print("2: Sarch for meaning")
    print("3: Display all words")
    print("4: Update meaning")
    print("5: Delete word")
    print("6: exit")

    choice = input("enter your choice: ")

    if choice=="1":
        word = input("enter the word: ").lower()
        meaning = input("enter the meaning: ")
        dit[word]=meaning
        print("succesfully added")
    elif choice=="2":
        word = input("enter the word: ").lower()
        print(dit[word])
    elif choice=="3":
        print(dit.keys())
    elif choice=="4":
         word = input("enter the word: ").lower()
         dit[word]=input("enter the new meaning: ")
         print(dit)
         print("update succesfully")
    elif choice=="5":
         word = input("enter the word: ").lower()
         obj=dit.pop(word)
         print(f"{obj} delete succes")
    elif choice=="6":
        print("exit in the list thank you")
        break
