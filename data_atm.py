import mysql.connector
import sys

all_args =sys.argv
args = all_args[1:]


conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="atm"
        )
cursor = conn.cursor()


if  args[0] == "--login":
    cursor.execute("SELECT username, password FROM atm")
    myresult = cursor.fetchall()

    for i in myresult:
        x =list(i)

        if args[1] == x[0] and args[2] == x[1]:
                print(f"Welcome {x[0]}!!")
                exit()

    os.exit("No user avalible Register first\nOR\nWrong password")



elif args[0] == "--register":
    cursor.execute("SELECT username, password FROM atm")
    myresult = cursor.fetchall()

    for i in myresult:
        x =list(i)
        if args[2] == x[0]:
            os.exit("already user avalible\n try anothrer user name")


    query = "INSERT INTO atm (Name, username, password, amount) VALUES (%s,%s,%s,%s)"
    cursor.execute(query, (args[1], args[2],args[3],"0"))
    conn.commit()
    print("Registeration succesful!!")

elif args[0] == "--delete":
    cursor.execute("SELECT Name,username, password FROM atm")
    myresult = cursor.fetchall()

    query = "DELETE FROM atm WHERE username=%s and password=%s"
    cursor.execute(query, (args[1], args[2]))
    conn.commit()

elif args[0] == "--update":
    cursor.execute("SELECT Name,username, password FROM atm")
    myresult = cursor.fetchall()

    query = "UPDATE atm SET amount=%s,password=%s WHERE id =%s"
    cursor.execute(query, (args[1], args[2], args[3]))
    conn.commit()

