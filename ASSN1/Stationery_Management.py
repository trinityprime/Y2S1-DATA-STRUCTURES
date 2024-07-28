from Stationary import Stationary, Queue, RestockDetail

queue = Queue()

def main():
   # per row stored as global var
   per_row = 1
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
            DisplayStationary(prodList, per_row)
        elif user_input == "3":
            SortBubble(prodList)
        elif user_input == "4":
            SortInsertion(prodList)
        elif user_input == "5":
            SortSelection(prodList, per_row)
        elif user_input == "6":
            SortMerge(prodList, per_row)
        elif user_input == "7":
            RestockingMenu(prodList)
        elif user_input == "8":
            per_row = int(input("Enter number of records per row: "))
        elif user_input == "9":
            prodList = populateData()
        elif user_input.lower() == "0":
            exit()
        else:
            print("Invalid input.")

def RestockingMenu(prodList):
    while True:
        print("Restocking Menu:")
        print("(1). Enter new stock arrival")
        print("(2). View Number of stock arrival")
        print("(3). Service next restock in queue")
        print("(0). Return to Main Menu")
        restock_input = input("Please enter your choice: ")
        print("------------------------")

        if restock_input == "1":
            AddRestock(prodList)
        elif restock_input == "2":
            ViewQueueSize()
        elif restock_input == "3":
            HandleNextRestock(prodList)
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
            
def DisplayStationary(prodList, per_row):
    if not prodList:
        print("No Stationary in the list!\n")
    else:
        DisplayRecordsPerRow(prodList, per_row)


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


def SortSelection(prodList, per_row):
    n = len(prodList)
    for i in range(n):
        max_idx = i
        for j in range(i + 1, n):
            if prodList[j].get_prod_id() > prodList[max_idx].get_prod_id():
                max_idx = j
        prodList[i], prodList[max_idx] = prodList[max_idx], prodList[i]
        print(f"Pass {i + 1}:")
        print(f"------------------")
        DisplayRecordsPerRow(prodList, per_row)
        print(f"------------------")


def SortMerge(stationery_list, per_row):
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
            DisplayRecordsPerRow(arr, per_row)
            print("---------------------") 

    merge_sort(stationery_list, key=lambda x: (x.get_category(), x.get_stock()))

    DisplayRecordsPerRow(stationery_list, per_row)


def DisplayRecordsPerRow(prodList, per_row=1):
    # Define labels and consistent widths for alignment
    labels = {
        'get_prod_id': ("Prod id", 45),        
        'get_prodname': ("Prod Name", 45),     
        'get_category': ("Category", 45),      
        'get_brand': ("Brand", 45),            
        'get_supp_year': ("Supplier Since", 45), 
        'get_stock': ("Stocks", 45)           
    }
    
    total_items = len(prodList)
    for start in range(0, total_items, per_row):
        end = min(start + per_row, total_items)
        
        for attribute, (label, width) in labels.items():
            for index in range(start, end):
                item = prodList[index]
                value = getattr(item, attribute)() if callable(getattr(item, attribute, None)) else ''
                # Print the label and value with consistent padding
                print(f"{label}: {value}".ljust(width), end=' ')
            print()  
        print()
        print()



def AddRestock(prodList):
    while True:
        prod_id = input("Enter Product ID for restocking: ").upper()
        for prod in prodList:
            if prod.get_prod_id() == prod_id:
                break
        else:
            print("Product ID not found in the system.\n")
            prod_id = input("Enter Product ID for restocking: ").upper()

        quantity = input("Enter quantity: ")
        while not quantity.isdigit() or int(quantity) < 0:
            print("Invalid input. Quantity must be a positive integer.\n")
            quantity = input("Enter quantity: ")
        quantity = int(quantity)

        restock_detail = RestockDetail(prod_id, quantity)
        queue.enqueue(restock_detail)
        print("Restocking arrival queued successfully!\n")
        break


def ViewQueueSize():
    print(f"Number of restocking in queue: {queue.size()}\n")


def HandleNextRestock(prodList):
    if queue.is_empty():
        print("No restock in queue.\n")
        return

    next_restock = queue.queue[0]
    restock_prod_id = next_restock.prod_id
    restock_quantity = next_restock.quantity

    # Find the corresponding stationary product details
    stationary_item = None
    for prod in prodList:
        if prod.get_prod_id() == restock_prod_id:
            stationary_item = prod
            break

    if stationary_item is None:
        print(f"Product ID {restock_prod_id} not found in inventory.\n")
        return

    print("Display Pending Stock Arrival:")
    print("----------------------------------")
    print(f"Product ID: {restock_prod_id}")
    print(f"Product Category: {stationary_item.get_category()}")
    print(f"Brand: {stationary_item.get_brand()}")
    print(f"Supplier Year: {stationary_item.get_supp_year()}")
    print(f"Stock remaining: {stationary_item.get_stock()}")
    print("----------------------------------")
    print(f"New Stock: {restock_quantity}")
    print("-----------------------------------")
    
    choice = input("Accept delivery? (y/n): ").lower()
    
    if choice == 'y':
        stationary_item.set_stock(stationary_item.get_stock() + restock_quantity)
        print(f"Stock updated for {stationary_item.get_prod_id()}. Updated stock: {stationary_item.get_stock()}\n")
        queue.dequeue()
        print(f"Remaining restock in queue: {queue.size()}\n")
    else:
        queue.enqueue(queue.dequeue())  # Send to the back of the queue
        print("Restock sent to the back of the queue.\n")

if __name__ == "__main__":
     main()


     