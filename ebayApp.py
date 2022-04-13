import pandas as pd
import csv

df=pd.read_csv(r"C:\Users\Adriel\OneDrive\Documents\GitHub\Python-Projects\eBay\Products.csv",encoding='windows-1252', header=0)
df.index+=1
products=df[['Name','Price','Quantity']].values
products=products.tolist()

def Selection(Option,products,df):
    if Option.lower()=='v':  # View function
        View(df)
    if Option.lower()=='e':  # Editing Quantity function
        Edit(products,df)

def View(df):  # Viewing all products
    print(df.to_string(columns=['Name','Price','Quantity']))

def Edit(products,df):
    View(df)
    Choice=input("Enter item row number (Type 'h' to go back to home):\n")
    if Choice=='h':  # If user wants to return back to selection function
        return
    a=0
    while a<len(products):
        if a==int(Choice)-1:  # Printing details of product; -1 as the products are listed/indexed by one instead of zero
            print("Name: "+products[a][0]+"\n")
            print("Price: "+products[a][1]+"\n")
            print("Quantity: "+str(products[a][2])+"\n")
            break
        a+=1
    change=input("Enter quantity change (Type 'h' to go back home): \n")
    if(change=='h'): # If user wants to return back to selection function
        return
    products[a][2]=int(change)  # Changing quantity to that specified   


while True:  # While loop for choosing functions
    Option = input("View Products(Type 'v')/Edit Quantities(Type 'e')/Quit(Type 'q')\n")
    if Option.lower()=='q':
        break  # Quiting program
    with open(r"C:\Users\Adriel\OneDrive\Documents\GitHub\Python-Projects\eBay\Products.csv", 'w') as csvfile:  # Saving product array to main products file
        products.insert(0,['Name','Price','Quantity'])
        csvwriter = csv.writer(csvfile)
        rows = 0
        while rows < len(products):
            csvwriter.writerow(products[rows])  # Rewriting entire file with new products array
            rows += 1
    df=pd.read_csv(r"C:\Users\Adriel\OneDrive\Documents\GitHub\Python-Projects\eBay\Products.csv",encoding='windows-1252', header=0)
    df.index+=1
    products=df[['Name','Price','Quantity']].values
    products=products.tolist()
    Selection(Option,products,df)


    


