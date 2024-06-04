from Stationary import Stationary

def main():
   prodList = []
   while (True):
                print("(1). Add a new Stationary")
                print("(2). Display all Stationary")
                print("(3). Sort Stationary via Bubble Sort on Category")
                print("(4). Sort Stationary via Insertion sort on Brand")
                print("(9). Populate Data")
                print("(0). Exit Program")
                user_input = input("Please enter your choice: ")
                print("------------------------")

                if user_input == "1":
                    AddStationary(prodList)
                elif user_input == "2":
                    DisplayStationary(prodList)
                elif user_input == "3":
                    SortBubble(prodList)
                elif user_input == "4":
                    SortInsertion(prodList)
                elif user_input == "9":
                    prodList = populateData()
                elif user_input.lower() == "0":
                    exit()
                else:
                    print("Invalid input.")

def populateData():
    prodList = []
    newStudA = Stationary(prod_id="PD1020", prodname="Pastel Art Paper", category="Paper", brand="Faber-Castell", supp_year=2021)
    prodList.append(newStudA)
    newStudA = Stationary(prod_id="PD1025", prodname="Mars Lumograph Drawing Pencils", category="Pencils", brand="Staedtler", supp_year=2022)
    prodList.append(newStudA)
    newStudA = Stationary(prod_id="PD1015", prodname="Water color Pencils", category="Pencils", brand="Faber-Castell", supp_year=2011)
    prodList.append(newStudA)
    newStudA = Stationary(prod_id="PD1050", prodname="Noris 320 fiber tip pen", category="Pens", brand="Staedtler", supp_year=2021)
    prodList.append(newStudA)
    newStudA = Stationary(prod_id="PD1001", prodname="Copier Paper (A4) 70GSM", category="Paper", brand="PAPERONE", supp_year=2021)
    prodList.append(newStudA)
    newStudA = Stationary(prod_id="PD1033", prodname="Scientific Calculator FX-97SG X", category="Calculator", brand="CASIO", supp_year=2022)
    prodList.append(newStudA)
    newStudA = Stationary(prod_id="PD1005", prodname="P0P Bazic File Separator Clear", category="Office Supplies", brand="Popular", supp_year=2000)
    prodList.append(newStudA)
    print("Data has been populated!\n")
    return prodList

def AddStationary(prodList):
    while True:
        prod_id = input("Enter Product ID: ").upper()
        while not prod_id:
            print("Input cannot be empty.\n")
            prod_id = input("Enter Product ID: ").upper()

        for stationary in prodList:
            while stationary.get_prod_id() == prod_id:
                print("Product ID already exists. Enter a unique ID.\n")
                prod_id = input("Enter Product ID: ").upper()

        prodname = input("Enter Product Name: ")
        while not prodname:
            print("Input cannot be empty.\n")
            prodname = input("Enter Product Name: ")

        category = input("Enter Category: ")
        while not category:
            print("Input cannot be empty.\n")
            category = input("Enter Category: ")

        brand = input("Enter Brand: ")
        while not brand:
            print("Input cannot be empty.\n")
            brand = input("Enter Brand: ")
        
        supp_year = input("Enter Supplier Year: ")
        while not supp_year:
            print("Input cannot be empty.\n")
            supp_year = input("Enter Supplier Year: ")

        while not supp_year.isdigit() or int(supp_year) < 0 or len(supp_year) != 4:
            print("Invalid input. Supplier Year must be a four-digit number.\n")
            supp_year = input("Enter Supplier Year: ")

        newStudA = Stationary(prod_id, prodname, category, brand, supp_year)
        prodList.append(newStudA)
        print("Stationary added successfully!\n")
        break
            
def DisplayStationary(prodList):
    if not prodList:
        print("No Stationary in the list!\n")
    else:
        for i in prodList:
            print("Product ID: ", i.get_prod_id())
            print("Product Name: ", i.get_prodname())
            print("Category: ", i.get_category())
            print("Brand: ", i.get_brand())
            print("Supplier Year: ", i.get_supp_year())
            print("------------------------")

def SortBubble(prodList):
    n = len(prodList)
    for i in range(n-1):
        end = False;
        for j in range(0, n - i - 1):
        #Compares each item with its adjacent item
            if prodList[j].get_category() < prodList[j + 1].get_category():
            #Checks if the category of the current Stationary object is less than the category of the next Stationary object.
                prodList[j], prodList[j + 1] = prodList[j + 1], prodList[j]
                #Swaps the current Stationary object with the next one.
                end = True
        print("Pass", i + 1)
        print("------------------------")
        for stationary in prodList:
            print("Product ID:", stationary.get_prod_id())
        print("------------------------")
        if not end:
            break

    print()

    print("Final Sorted Stationary:")
    print("------------------------")
    for stationary in prodList:
        print("Product ID:", stationary.get_prod_id())
        print("Product Name:", stationary.get_prodname())
        print("Category:", stationary.get_category())
        print("Brand:", stationary.get_brand())
        print("Supplier Year:", stationary.get_supp_year())
        print("------------------------")

def SortInsertion(prodList):
    n = len(prodList)

    for i in range(1, n):
        key = prodList[i]  
        # Current element to be inserted at the correct position
        j = i - 1

        # Move elements of prodList[0..i-1], that are greater than key, to one position ahead of their current position
        while j >= 0 and prodList[j].get_brand() > key.get_brand():
            prodList[j + 1] = prodList[j]
            j -= 1

        prodList[j + 1] = key  
        # Insert the key at its correct position in the sorted sublist

        # Print the current pass and the list after each pass
        print("Pass", i)
        print("------------------------")
        for stationary in prodList:
            print("Product ID:", stationary.get_prod_id())
        print("------------------------")

    # Print the final sorted list
    print("Final Sorted Stationary:")
    print("------------------------")
    for stationary in prodList:
        print("Product ID:", stationary.get_prod_id())
        print("Product Name:", stationary.get_prodname())
        print("Category:", stationary.get_category())
        print("Brand:", stationary.get_brand())
        print("Supplier Year:", stationary.get_supp_year())
        print("------------------------")

if __name__ == "__main__":
     main()


     