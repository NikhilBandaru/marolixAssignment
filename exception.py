def addtocart(db,name,productnameandquentite,addtocart,electronics):
    userNamesList = list(db.values())
    
    if name not in userNamesList :
        print('welcome to our smart mart')
        db[len(db)+1]=name
    try:
        for itemName in list(productAndQuantity.keys()):
                if itemName not in electronics.keys():
                    raise Exception("Product not present in our inventory")
                else:
                    for item in list(electronics.keys()):
                        if itemName == item:
                            if productAndQuantity[itemName] > electronics[item]:
                                raise Exception("Product Quantity is out of stock")
                            else:
                                addTOCart.append(itemName)
                                print({
                                    "message":f"{itemName} of {productAndQuantity[itemName]} is added by user {name}",
                                    "data":addTOCart
                                })

    except Exception as ex:
        return({
            "message":str(ex),
            "data":None
        })


db = {
    1:"raja",
    2:"Sandhya",
    3:"Vamshi",
    4:"bhargava",
    5:"gopi",
    6:"pusgpavati"
}

addTOCart = []
electronics = {"samsung":10, "onepluse":15, "huweai":20, "iphone":100, "mi":20, "vivo":30, "oppo": 50, "nokia": 200, "iqoo":20, "10or":30}

currentCustomerUserName = "nikhil"
productAndQuantity = {'iphone': 25, 'samsung': 5}
res = addtocart(db, currentCustomerUserName, productAndQuantity, addTOCart, electronics)
print(res)