from app import mysql

#To access table in mysql
class Table():
    def __init__(self, table_name, *table_columns):
        self.table = table_name
        self.columns = "(%s)" %",".join(table_columns)
        self.columnlist = table_columns

        #if table is not present a new table will be created
        if isnewtable(table_name):
            create_data = ""
            for column in self.columnlist:
                create_data += "%s varchar(100)," %column
            cur = mysql.connection.cursor()
            cur.execute("create table %s(%s)" %(self.table,create_data[:len(create_data)-1]))
            cur = mysql.connection.cursor()
            cur.close()

    #Function to get all rows from a table
    def getall(self):
        cur = mysql.connection.cursor()
        cur.execute("select * from %s" %self.table)
        data = cur.fetchall()
        cur.close()
        return data

    #Function to get one row from a table
    def getone(self, search, value):
        data= {}
        cur = mysql.connection.cursor()
        result = cur.execute("select * from %s where %s =\"%s\"" %(self.table, search, value))
        if result > 0:
            data = cur.fetchone()
        cur.close()
        return data

    #Function to delete one row from a table
    def deleteone(self, search, value):
        cur = mysql.connection.cursor()
        cur.execute("delete from %s where %s =\"%s\"" %(self.table, search, value))
        mysql.connection.commit()
        cur.close()

    #Frunction to drop a table
    def drop(self):
        cur = mysql.connection.cursor()
        cur.execute("drop table %s" %self.table)
        cur.close()

    #Function to insert values into a table
    def insert(self, *args):
        data=""
        for arg in args:
            data += "\"%s\"," %(arg)
        cur = mysql.connection.cursor()
        cur.execute("insert into %s%s values(%s)" %(self.table, self.columns, data[:len(data)-1]))
        mysql.connection.commit()
        cur.close()

#Function to execute raw query in database
def sql_raw(query):
    cur = mysql.connection.cursor()
    cur.execute(query)
    mysql.connection.commit()
    cur.close()

#Function to check whether it is a new table or not
def isnewtable(table_name):
    cur = mysql.connection.cursor()
    try:
        result = cur.execute("select * from %s limit 1" %table_name)
        cur.close()
    except:
        return True
    else:
        return False

#Function to check whether the user is new or not
def isnewuser(username):
    users = Table("users", "name", "email", "username", "password")
    data = users.getall()
    usernames = [user.get('username') for user in data]
    return False if username in usernames else True
