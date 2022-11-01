from model.Ingredient import Ingredient
import mysql.connector

class DbAccess:
    
    def userInList():
        pass

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
        l=[]
        return l

