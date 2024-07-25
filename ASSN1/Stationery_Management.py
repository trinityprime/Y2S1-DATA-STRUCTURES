from Stationary import Stationary, Queue, RestockDetail

def main():
   prodList = []
   while (True):
                
        print("(1). Add a new Stationary")
        print("(2). Display all Stationary")
        print("(3). Sort Stationary via Bubble Sort on Category")
        print("(4). Sort Stationary via Insertion Sort on Brand")
        print("(5). Sort Stationary via Selection Sort on Prod Id")
        print("(6). Sort Stationary via Merge Sort on Category followed by stock in ascending order")
        print("(7). Restocking Menu")
        print("(8). Set number of records per row to display")
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
        elif user_input == "5":
            SortSelection(prodList)
        elif user_input == "6":
            SortMerge(prodList)
        elif user_input == "7":
            RestockingMenu(prodList)
        elif user_input == "8":
            per_row = int(input("Enter number of records per row: "))
            DisplayRecordsPerRow(prodList, per_row)
        elif user_input == "9":
            prodList = populateData()
        elif user_input.lower() == "0":
            exit()
        else:
            print("Invalid input.")

def RestockingMenu(prodList):
    while True:
        print("Restocking Menu:")
        print("(1). Add Restock Details")
        print("(2). View Restock Queue Size")
        print("(3). Handle Next Delivery")
        print("(0). Return to Main Menu")
        restock_input = input("Please enter your choice: ")
        print("------------------------")

        if restock_input == "1":
            AddRestock(prodList)
        elif restock_input == "2":
            ViewQueueSize()
        elif restock_input == "3":
            HandleNextDelivery(prodList)
        elif restock_input == "0":
            break
        else:
            print("Invalid input.")

def populateData():
    prodList = []
    newStudA = Stationary(prod_id="PD1020", prodname="Pastel Art Paper", category="Paper", brand="Faber-Castell", supp_year=2021, stock=2000)
    prodList.append(newStudA)
    newStudA = Stationary(prod_id="PD1025", prodname="Mars Lumograph Drawing Pencils", category="Pencils", brand="Staedtler", supp_year=2022, stock=320)
    prodList.append(newStudA)
    newStudA = Stationary(prod_id="PD1015", prodname="Water color Pencils", category="Pencils", brand="Faber-Castell", supp_year=2011, stock=150)
    prodList.append(newStudA)
    newStudA = Stationary(prod_id="PD1050", prodname="Noris 320 fiber tip pen", category="Pens", brand="Staedtler", supp_year=2021, stock=350)
    prodList.append(newStudA)
    newStudA = Stationary(prod_id="PD1001", prodname="Copier Paper (A4) 70GSM", category="Paper", brand="PAPERONE", supp_year=2021, stock=1500)
    prodList.append(newStudA)
    newStudA = Stationary(prod_id="PD1033", prodname="Scientific Calculator FX-97SG X", category="Calculator", brand="CASIO", supp_year=2022, stock=50)
    prodList.append(newStudA)
    newStudA = Stationary(prod_id="PD1005", prodname="P0P Bazic File Separator Clear", category="Office Supplies", brand="Popular", supp_year=2000, stock=500)
    prodList.append(newStudA)
    print("Data has been populated!\n")
    return prodList

def AddStationary(prodList):
    while True:
        prod_id = input("Enter Product ID: ").upper()
        while not prod_id or not prod_id.startswith("PD") or not prod_id[2:].isdigit() or len(prod_id) != 6:
            print("Invalid input. Product ID must start with 'PD' followed by 4 digits.\n")
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
        while not category or not category.isalpha():
            print("Invalid input. Category must contain only letters.\n")
            category = input("Enter Category: ")

        brand = input("Enter Brand: ")
        while not brand or not brand.isalpha():
            print("Invalid input. Brand must contain only letters.\n")
            brand = input("Enter Brand: ")
        
        supp_year = input("Enter Supplier Year: ")
        while not supp_year:
            print("Input cannot be empty.\n")
            supp_year = input("Enter Supplier Year: ")

        while not supp_year.isdigit() or int(supp_year) < 0 or len(supp_year) != 4:
            print("Invalid input. Supplier Year must be a four-digit number.\n")
            supp_year = input("Enter Supplier Year: ")

        stock = input("Enter Stock: ")
        while not stock.isdigit() or int(stock) < 0:
            print("Invalid input. Stock must be a non-negative integer.\n")
            stock = input("Enter Stock: ")
        stock = int(stock)


        newStudA = Stationary(prod_id, prodname, category, brand, supp_year, stock)
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
            print("Stock: ", i.get_stock())
            print("------------------------")


def SortBubble(prodList):
    n = len(prodList)
    for i in range(n-1):
        SwapTakenPlace = False;
        for j in range(0, n - i - 1):
        #Compares each item with its adjacent item
            if prodList[j].get_category() < prodList[j + 1].get_category():
            #Checks if the category of the current Stationary object is less than the category of the next Stationary object.
                prodList[j], prodList[j + 1] = prodList[j + 1], prodList[j]
                #Swaps the current Stationary object with the next one.
                SwapTakenPlace = True
        print("Pass", i + 1)
        print("------------------------")
        for stationary in prodList:
            print("Product ID:", stationary.get_prod_id())
        print("------------------------")
        if SwapTakenPlace == False: # there was no swapping at all, it means the list is already sorted, there no need to continue future pass
            break # so we end early

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


def SortSelection(prodList):
    n = len(prodList)
    for i in range(n):
        max_idx = i
        for j in range(i + 1, n):
            if prodList[j].get_prod_id() > prodList[max_idx].get_prod_id():
                max_idx = j
        prodList[i], prodList[max_idx] = prodList[max_idx], prodList[i]
        print(f"Pass {i + 1}:")
        print(f"------------------")
        for p in prodList:
            print(p.get_prod_id())
        print(f"------------------")

    for stationary in prodList:
        print(f"Prod id: {stationary.get_prod_id()}\nProd Name: {stationary.get_prodname()}\nCategory: {stationary.get_category()}\nBrand: {stationary.get_brand()}\nSupplier Since: {stationary.get_supp_year()}\nStocks: {stationary.get_stock()} \n")


def SortMerge(stationery_list):
    def merge_sort(arr, key=lambda x: x):
        if len(arr) > 1:
            mid = len(arr) // 2
            L = arr[:mid]
            R = arr[mid:]

            merge_sort(L, key=key)
            merge_sort(R, key=key)

            i = j = k = 0

            while i < len(L) and j < len(R):
                if key(L[i]) < key(R[j]):
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1

            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1

            print("New List:")
            print("---------------------")
            for stationery in arr:
                print(stationery.get_prod_id())
            print("---------------------") 

    merge_sort(stationery_list, key=lambda x: (x.get_category(), x.get_stock()))


    for stationary in stationery_list:
        print(f"Prod id: {stationary.get_prod_id()}\nProd Name: {stationary.get_prodname()}\nCategory: {stationary.get_category()}\nBrand: {stationary.get_brand()}\nSupplier Since: {stationary.get_supp_year()}\nStock: {stationary.get_stock()} \n")


def DisplayRecordsPerRow(prodList, per_row=1):
    def recursive_display(index):
        if index >= len(prodList):
            return
        print(f"Product ID: {prodList[index].get_prod_id()}")
        print(f"Product Name: {prodList[index].get_prodname()}")
        print(f"Category: {prodList[index].get_category()}")
        print(f"Brand: {prodList[index].get_brand()}")
        print(f"Supplier Year: {prodList[index].get_supp_year()}")
        print(f"Stock: {prodList[index].get_stock()}\n")
        if (index + 1) % per_row == 0:
            input("Press Enter to continue...")
        recursive_display(index + 1)

    recursive_display(0)


def AddRestock(prodList):
    prod_id = input("Enter Product ID for restocking: ").upper()
    quantity = int(input("Enter quantity: "))
    for prod in prodList:
        if prod.get_prod_id() == prod_id:
            restock_detail = RestockDetail(prod_id, quantity)
            Queue.enqueue(restock_detail)
            print("Restock details added to queue.\n")
            return
    print("Product ID not found in the system.\n")


def ViewQueueSize():
    print(f"Number of deliveries in queue: {Queue.size()}\n")


def HandleNextDelivery(prodList):
    if Queue.is_empty():
        print("No deliveries in queue.\n")
        return
    
    next_delivery = Queue.queue[0]
    print(f"Next delivery: Product ID: {next_delivery.prod_id}, Quantity: {next_delivery.quantity}")
    choice = input("Accept delivery? (y/n): ").lower()
    
    if choice == 'y':
        for prod in prodList:
            if prod.get_prod_id() == next_delivery.prod_id:
                prod.set_stock(prod.get_stock() + next_delivery.quantity)
                print(f"Stock updated for {next_delivery.prod_id}. New stock: {prod.get_stock()}\n")
                Queue.dequeue()
                print(f"Remaining deliveries in queue: {Queue.size()}\n")
                return
    
    Queue.enqueue(Queue.dequeue())
    print("Delivery sent to the back of the queue.\n")


if __name__ == "__main__":
     main()


     