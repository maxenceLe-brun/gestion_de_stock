import mysql.connector

connection_params = {
    'host': "localhost",
    'user': "root",
    'password': "root",
    'database': "boutique",
}

db = mysql.connector.connect(**connection_params)
c = db.cursor()



def check(c, ID:int = None, name:str = None, price:int = None, quantity:int = None):
    mark = [["id", "name", "prix", "quantite"],[ID, name, price, quantity]]
    if (None,)*4 != (ID, name, price, quantity):
        fit = ()
        for a in range(len(mark[1])):
            if mark[1][a] != None:
                fit += ((mark[0][a] + " = " + str(mark[1][a])))
        c.execute(("SELECT * FROM produit WHERE {}"+ (len(fit)-1)*" AND {}" + ";").format(fit))
        print(c.fetchall())
                

def add(c, name:str = None, description:str = None, price:int = None, quantity:int = None, id_categorie:int = None):
    
    if None not in (name, description, price, quantity, id_categorie):
        c.execute("SELECT * FROM produit")
        X = 1
        for i in c.fetchall():
            if name == i[1]:
                X = 0
        if X:
            c.execute("INSERT INTO produit (name, description, prix, quantite, id_categorie) VALUES('{}', '{}', {}, {}, {});".format(name, description,price, quantity, id_categorie))
        else:
            print("This name is already used, please pick another one")
    
    #Here's all the errors that has already been viewed
    elif None in (name, description, price, quantity, id_categorie):
        print("Empty slot, please furfil all the required informations")
    
    elif type(name) == str and len(name) > 255:
        print("Please, change the name within 255 characters")
        
    else:
        print("Please, enter correctly the name, the description, the price, the quantity and the id_category")

def remove(c, ID:int = None, name:str = None):
    if (None,None) != (ID,name):
        
        c.execute("SELECT * FROM produit")
        X = 0
        duply = [ID,name]
        for i in c.fetchall():
            if (name == i[1] or ID == i[0]) and None not in (ID, name):
                print("Wrong name/ID")
            elif name == i[1] or ID == i[0] and None in (ID, name):
                duply.remove(None)
                X = 1
                break
        
        if X:
            c.execute("DELETE FROM boutique WHERE id = "+ duply[0] + " OR name = " + duply[-1] + ";")
        else:
            print("Wrong name/ID")
    elif type(ID) != int or type(name) != str:
        print("Please, enter the ID and the name correctly")
    else:
        print("please, select an ID or a name to remove an article")

def rework(c, ID:int = None, name:str = None, newName:str = None, newDescription:str = None, newPrice:int = None, newQuantity:int = None, newId_categorie:int = None):
    if (None,None) != (ID,name):
        for i in c.fetchall():
            if (name == i[1] or ID == i[0]) and None not in (ID, name):
                print("Wrong name/ID")
            elif name == i[1] or ID == i[0] and None in (ID, name):
                #duply.remove(None)
                X = 1
                break
        
        if X:
            pass
            #c.execute("DELETE FROM boutique WHERE ID = "+duply[0])
        else:
            print("Wrong name/ID")
    pass
