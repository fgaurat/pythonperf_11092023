import sqlite3

from Todo import Todo

class TodoDAOContext:


    def __init__(self,db_file):
        self._con = sqlite3.connect(db_file)
    
    def __enter__(self):
        print("__enter__(self)")
        return self

    def __exit__(self,*exc):
        print('def __exit__(self,*exc)')
        self._con.close()


    def findAll(self):

        cur =self._con.cursor()
        res = cur.execute("SELECT * FROM todos_tbl")
        for id,title,completed in res.fetchall():
            t = Todo(id,title,completed)
            yield t
        # for row in res.fetchall():
        #     t = Todo(*row)

    def __del__(self):
        self._con.close()
