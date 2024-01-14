Contact ={}
def ShowFuntion():
    print(Contact.items())
    print("Name  \t Contact")
    for key in Contact:
        print("{} \t {} ". format(key,Contact.get(key)))

while True:
    choice = int(input("1. Add New Contact \n"
                   "2. Search Contact \n"
                   "3. Display the Contact \n"
                   "4. Edit the Contact \n"
                   "5. Delete the Contact \n"
                   "6. Exit \n"
                   "Please Write Number Between 1-6: "))

    if choice == 1:
        name = input("Add your Contact Name: ")
        phone = input("Add your Phone Number: ")
        Contact[name] = phone

    elif choice == 2:
        Contact_Name = input("Search the Contact: ")
        if Contact_Name in Contact:
            print(Contact_Name, "Contact Number is",Contact[Contact_Name])
        else:
            print("Not Found the Contact")

    elif choice == 3:
        if not Contact:
            print("Contact book is Empty")
        else:
            ShowFuntion()

    elif choice == 4:
        Edit_Contact = input("Edit your Contact: ")
        if Edit_Contact in Contact:
            phone = input("Change your Number: ")
            Contact[Edit_Contact] = phone
            print("Contact Updated Successfully")
            ShowFuntion()
        else:
            print("Name is Not Found")

    elif choice == 5:
        Delete_Contact = input("which Contact Number you want to Delete?: ")
        if Delete_Contact in Contact:
            DeleteConfirm = input("Do you want to delete this Contact y/n")
            if DeleteConfirm =="y" or DeleteConfirm =="Y":
                Contact.pop(Delete_Contact)
                ShowFuntion()
            else:
                print("The name is not found in the Contact")

    else:
        break
