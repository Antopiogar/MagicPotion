from model.Ingredient import Ingredient
from model.user import user
import mysql.connector
from model.potionLite import potionLite

class DbAccess:
    
    def userInList(us,psw):
        l = []
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="magicpotion"
        ) 
        mycursor = mydb.cursor()
        query=f"""SELECT * FROM Users ORDER BY id asc"""
        mycursor.execute(query)
        result=mycursor.fetchall()
        print(query)
        print(result)
        lst=[]
        users=[]
        for r in result:
            for i in range(0,3):
                lst.append(r[i])
            obj=user(lst[0],lst[1],lst[2])
            users.append(obj)
        logged=False
        for usr in users:
            if usr._is_logged(us,psw):        
                logged=True
        lst.clear()
        return logged

    def _add_ingredient(a):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="magicpotion") 
        mycursor = mydb.cursor()
        pippo=f""""{a._name}",{a._fire},{a._water},{a._air},{a._earth}"""
        query=f"INSERT INTO Ingredients (name,fire,water,air,earth) VALUES (%s,%s,%s,%s,%s)"
        mycursor.execute(query,pippo.split(","))
        result=mycursor.fetchall()
        mydb.commit()
        print(query)
        print(result)

    def _see_ingredients():
        l = []
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="magicpotion") 
        mycursor = mydb.cursor()
        query=f"""SELECT * FROM Ingredients ORDER BY Ingredients.id asc"""
        mycursor.execute(query)
        result=mycursor.fetchall()
        lst=[]
        for r in result:
            for i in range(0,6):
                lst.append(r[i])
            obj=Ingredient(lst[0],lst[1],lst[2],lst[3],lst[4],lst[5])
            l.append(obj.__str__())
            lst.clear()
        return l

    def _modify_ingredients(id,obj):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="magicpotion") 
        mycursor = mydb.cursor()
        pippo=f""""{obj._name}", {obj._fire}, {obj._water}, {obj._air}, {obj._earth}, {obj._id}"""
        query=f"""UPDATE Ingredients SET name=%s, fire=%s, water=%s, air=%s, earth=%s WHERE id=%s"""
        mycursor.execute(query,pippo.split(","))
        result=mycursor.fetchall()
        mydb.commit()
        print(query)
        print(result)

    def _delete_ingredients(id):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="magicpotion") 
        mycursor = mydb.cursor()
        pippo=[]
        pippo.append(id)
        query="""DELETE FROM Ingredients WHERE id=%s"""
        mycursor.execute(query,pippo)
        result=mycursor.fetchall()
        mydb.commit()
        print(query)
        print(result)

    def _see_potions():
        l = []
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="magicpotion") 
        mycursor = mydb.cursor()
        query="""SELECT * FROM Potions"""
        mycursor.execute(query)
        result=mycursor.fetchall()
        lst=[]
        for r in result:
            for i in range(0,3):
                lst.append(r[i])
            obj=potionLite(id=lst[0],name=lst[1],points=lst[2])
            l.append(obj.__str__())
            lst.clear()
        print(f"LISTA = {l}")
        return l
    
    def _see_Ingredients_of(id):
        l = []
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="magicpotion") 
        mycursor = mydb.cursor()
        lid=[]
        lid.append(id)
        query=f"""SELECT Ingredients.* FROM Ingredients,pozioni_ingredienti as pi WHERE pi.fk_potions=%s and pi.fk_ingredients=Ingredients.id ORDER BY Ingredients.id asc"""
        mycursor.execute(query,lid)
        result=mycursor.fetchall()
        lst=[]
        for r in result:
            for i in range(0,6):
                lst.append(r[i])
            obj=Ingredient(lst[0],lst[1],lst[2],lst[3],lst[4],lst[5])
            print(f"ingrediente QUERY: {obj}")
            l.append(obj.__str__())
            lst.clear()
        print(f"CONTENUTO DI l = {l}")
        return l
    
    def _modify_potions():
        pass
    def _delete_potions(id):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="magicpotion") 
        mycursor = mydb.cursor()
        pippo=[]
        pippo.append(id)
        query="""DELETE FROM Potions WHERE id=%s"""
        q2="""DELETE FROM pozioni_ingredienti WHERE fk_potions=%s"""
        mycursor.execute(q2,pippo)
        result=mycursor.fetchall()
        mydb.commit()
        mycursor.execute(query,pippo)
        result=mycursor.fetchall()
        mydb.commit()
        print(query)
        print(result)
    
    def _add_potion(name,lst,points):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="magicpotion") 
        mycursor = mydb.cursor()
        mycursor2=mydb.cursor()
        queryP=f"""INSERT INTO Potions (name,points) VALUES (%s,%s);"""
        ls=[]
        ls.append(name.__str__())
        ls.append(points.__str__()) 
        print(ls)
        mycursor.execute(queryP,ls)
        ls.pop(1)
        r=mycursor.fetchall().__str__()
        mydb.commit()
        queryId=f"""SELECT Potions.id FROM Potions WHERE Potions.name=%s"""
        mycursor2.execute(queryId,ls)
        r=mycursor.fetchall()
        print(f"r={r}")
        r=r.__str__()
        r=r.replace("[", " ").replace("(", " ").replace(","," ").replace(")"," ").replace("]"," ").strip()
        
        ls.clear()
        for i in range(0,len(lst)):
            query=f"""INSERT INTO Pozioni_Ingredienti (fk_potions,fk_ingredients) VALUES (%s,%s)"""
            p=f"{int(r)},{int(lst[i])}"
            print(p)    
            mycursor.execute(query,p.split(","))
            mycursor.fetchall()
            mydb.commit()
        