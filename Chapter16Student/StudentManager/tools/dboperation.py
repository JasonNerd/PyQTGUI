import pymysql

def open():
    return pymysql.connect(host="localhost", 
                           user="root", 
                           password="21X#T31;S51Q02L",
                           database="db_student",
                           charset="utf8")

def exec(sql, values):
    db = open()
    cursor = db.cursor()
    try:
        cursor.execute(sql, values)
        db.commit()
        return 1
    except Exception as err:
        print(err)
        db.rollback()
        return 0
    finally:
        cursor.close()
        db.close()

def query(sql, *keys):
    db = open()
    cursor = db.cursor()
    cursor.execute(sql, keys)
    res = cursor.fetchall()
    cursor.close()
    db.close()
    return res

def query_(sql):
    db = open()
    cursor = db.cursor()
    cursor.execute(sql)
    res = cursor.fetchall()
    cursor.close()
    db.close()
    return res