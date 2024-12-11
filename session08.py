import mysql.connector

#kết nối mysql
def connectMySQL(db=''):
    if(db==''):
        con=mysql.connector.connect(
            host='localhost',
            user='root',
            password=''
        )
        print('Connect success, database not exists')
    else:
        con=mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database=db
        )
        print('Connect success with',db)
    return con

def createDatabase(db):
    con=connectMySQL()
    cursor=con.cursor()
    cursor.execute('create database if not exists '+db)
    print('Tạo database',db,' thành công!')
    con.close()
    cursor.close()

def createTable(tbname):
    con=connectMySQL(db='C2309LM2')
    cursor=con.cursor()
    cursor.execute('create table if not exists '+tbname+'(productid varchar(10) primary key,productname varchar(100),price int)')
    print('Tạo table',tbname,' thành công!')
    con.close()
    cursor.close()

def insertProduct():
    con=connectMySQL(db='C2309LM2')
    cursor=con.cursor()
    insert_sql="insert into product values(%s,%s,%s)"
    productid=input('Nhập mã sản phẩm:')
    productname=input('Nhập tên sản phẩm:')
    price=input('Nhập giá sản phẩm:')
    cursor.execute(insert_sql,(productid,productname,price))
    con.commit()
    print('Thêm thành công')
    con.close()
    cursor.close()
    
def updateProduct():
    con=connectMySQL(db='C2309LM2')
    cursor=con.cursor()
    update_sql="update product set productname=%s,price=%s where productid=%s"
    productid=input('Nhập mã sản phẩm cần sửa:')
    productname=input('Nhập tên sản phẩm cần sửa:')
    price=input('Nhập giá sản phẩm cần sửa:')
    cursor.execute(update_sql,(productname,price,productid))
    con.commit()
    print('Sửa thành công')
    con.close()
    cursor.close()

def deleteProduct():
    con=connectMySQL(db='C2309LM2')
    cursor=con.cursor()
    delete_sql="delete from product where productid=%s"
    productid=input('Nhập mã sản phẩm cần xóa:')
    cursor.execute(delete_sql,(productid,))
    con.commit()
    print('Xóa thành công')
    con.close()
    cursor.close()

def searchProduct():
    con=connectMySQL(db='C2309LM2')
    cursor=con.cursor()
    search_sql="select * from product where productname like %s"
    productname=input('Nhập tên sản phẩm cần tìm:')
    cursor.execute(search_sql,('%'+productname+'%',))
    records=cursor.fetchall()
    for row in records:
        print(row[0],':',row[1],':',row[2])
    con.close()
    cursor.close()
    
def showProduct():
    con=connectMySQL(db='C2309LM2')
    cursor=con.cursor()
    search_sql="select * from product"
    cursor.execute(search_sql)
    records=cursor.fetchall()
    for row in records:
        print(row[0],':',row[1],':',row[2])
    con.close()
    cursor.close()

choose=0
while(True):
    print('1. Tạo cấu trúc dữ liệu')
    print('2. Thêm mới')
    print('3. Sửa')
    print('4. Xóa')
    print('5. Hiển thị tất cả')
    print('6. Tìm kiếm')
    print('7. Thoát')
    choose =int(input('Mời bạn chọn 1 chức năng'))

    if choose==7:
        break
    elif choose==1:
        createDatabase(db='C2309LM2')
        createTable('Product')
    elif choose==2:
        insertProduct()
    elif choose==3:
        updateProduct()
    elif choose==4:
        deleteProduct()
    elif choose==5:
        showProduct()
    elif choose==6:
        searchProduct()
    else:
        print('Chọn tiếp đi')