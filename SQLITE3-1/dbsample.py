import sqlite3
import random
first_name = ['Ali' , 'Reza' , 'Mamad' , 'Javad' , 'Gholam' , 'faeze' , 'Mozgan' , 'Marzie' , 'Tahere']


for i in range(1,10) :
    with sqlite3.connect('db_sample.db') as conn:
        #Create
        names = random.choice(first_name)
        garde = input("Garde --->  ")
        cur = conn.cursor()
        cur.execute("INSERT INTO students (id,grade,name) VALUES (?, ?, ?)" , (i,garde,names))
        conn.commit()
        i+=1
    
    
    #Read
    cur.execute("SELECT id,grade,name FROM students")
    st = cur.fetchall()
    print(st)
    
    
    #Update
    # cur.execute("UPDATE students SET grade = ? WHERE id = ?" , (2,12))
    # conn.commit()