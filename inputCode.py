import csv

file=open(r"/Users/adrielgenao/Documents/GitHub/Python-Projects/eBay/InputFile","r")
fileList=list(file)
x=0
while x<len(fileList):
    if 'Buy' in fileList[x]:
        fileList.pop(x)
    if 'Research' in fileList[x]:
        fileList.pop(x)
    if 'Promote' in fileList[x]:
        fileList.pop(x)     
    if 'EditLink' in fileList[x]:
        fileList.pop(x)
    if 'recommended' in fileList[x]:
        fileList.pop(x)
    if 'Eligible' in fileList[x]:
        fileList.pop(x)
    if 'photo' in fileList[x]:
        fileList.pop(x)
    if 'Suggested' in fileList[x]:
        fileList.pop(x) 
    if 'volume' in fileList[x]:
        fileList.pop(x)
    if 'Respond' in fileList[x]:
        fileList.pop(x)
    if 'variations' in fileList[x]:
        fileList.pop(x)
    if 'Best Offer' in fileList[x]:
        fileList.pop(x)    
    #if '$' in fileList[x]:
    #    fileList.pop(x+2)                                                                                                                               
    x+=1        
file=open(r"/Users/adrielgenao/Documents/GitHub/Python-Projects/eBay/InputFile","w")
for a in fileList:
    file.write(a)
file.close()
b=0
while b<len(fileList):
    current=list(fileList[b])
    current.pop(len(current)-1)
    fileList[b]=current
    b+=1
productsList=[]
a=0
while a<len(fileList):
    product=""
    for m in fileList[a]:
        product+=m
    productsList.append(product)   
    a+=1
a=0
while a<len(productsList):
    if productsList[a]=='':
        productsList.pop(a)
    a+=1            
productsArray=[['Name','Price','Quantity']]
currentList=[]       
a=0
while a<len(productsList):
    currentList=[productsList[a],productsList[a+1],productsList[a+2]]
    productsArray.append(currentList)
    a+=3
with open(r"/Users/adrielgenao/Documents/GitHub/Python-Projects/eBay/Products.csv", 'w') as csvfile:  # File as written mode
    csvwriter = csv.writer(csvfile)  # Create csv writing function
    rows = 0
    while rows < len(productsArray):
        csvwriter.writerow(productsArray[rows])  # Rewrite 2d array back into file
        rows += 1    
