import pymysql as p

Conn = p.connect(host="localhost", user="root", passwd="chirag1234", database="Project")
Cur = Conn.cursor()

# Cur.execute("select * from ICC where Pname like '%kohli%'")
# for i in Cur.fetchall():
#     print(i)



a = 1
while a <= 1000:
    a+=2
else:
    print(a)
print(a)







