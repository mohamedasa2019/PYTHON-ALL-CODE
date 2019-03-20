



import sqlite3
def main():
    db=sqlite3.connect("information.db")
    db.row_factory=sqlite3.Row     # هذا السطر لتحويل البيانات بشكل ديكشنري لاستطيع قرائتها
    db.execute("create table if not exists admin(Name text,age int)")
    db.execute("insert into admin ( name,age ) values ( ?,?)", ("mohamed",48))    # db.execute نفذ امر
    db.execute("insert into admin ( name,age ) values ( ?,?)", ("MOUSTAFA",9))  #  insert اضف
  # db.execute("delete from admin where name='mohamed'")   #  لحذف بيانات
    db.execute("update admin set age = 10 where name = 'MOUSTAFA'")   # لتعديل بيانات
    db.commit()



    cusror=db.execute("select * from admin")
    for row in cusror:
        print("name : {} , age : {}".format(row["name"],row["age"]))

















if __name__ == '__main__': main()
