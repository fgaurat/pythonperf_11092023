import csv
import sqlite3

def main():
    con = sqlite3.connect(r"tp07\todos_db.db")
    cur = con.cursor()
    a=2
    b=3
    l =[2,3]
    d = {
        "a":2,
        "b":3
    }
    s = "valeur de a:{0} valeur de b:{1}".format(*l)
    s = "valeur de a:{a} valeur de b:{b}".format(a=2,b=3)
    s = "valeur de a:{a} valeur de b:{b}".format(**d)

    with open("tp07\MOCK_DATA.csv", newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row['completed'] = True if row['completed']=='true' else False
            # sql = f"""INSERT INTO todos_tbl(title,completed) 
            # VALUES ('{row['title']}',{row['completed']})"""
            # print(sql)

            sql = "INSERT INTO todos_tbl(title,completed) VALUES ('{title}',{completed})".format(**row)
            print(sql)
            cur.execute(sql)
    con.commit()
    con.close()
if __name__=='__main__':
    main()
