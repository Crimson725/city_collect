import pymysql
import os

host = 'localhost'
db = 'city_test'
user = 'root'
password = '13678422587'


# ---- 用pymysql 操作数据库
def get_connection():
    conn = pymysql.connect(host=host, db=db, user=user, password=password)
    return conn


def check_it():
    db = pymysql.connect(
        host="localhost",
        user="root",
        passwd="20010316",
        database="web_test")

    cursor = db.cursor()
    SQL = """INSERT INTO user_info(user_id,user_advice) VALUES(1111111111,'红米手机')"""

    cursor.execute(SQL)
    db.commit()
    db.close()


path = "../static/images/data_set_test1.0/"


def init_image_dic():
    select_num = 0
    for i in range(0, 7):
        # 对于每一个文件夹下的内容
        sql = "INSERT INTO image_dic(PID,safe,unsafe,skip,rate,P_PSID,image_name) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        cur_dic = path + str(i)
        P_PSID = i
        for file in os.listdir(cur_dic):
            image_name = file.split('.')[0]
            PID = image_name[0:-3] + image_name[-1]

            safe = 0
            unsafe = 0
            skip = 0
            rate = 0
            print(image_name, PID)
            values = (PID, safe, unsafe, skip, rate, P_PSID, image_name)

            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(sql, values)
            conn.commit()


def init_image_set():
    select_num = 0
    for i in range(7):
        # 对于每一个文件夹下的内容
        sql = "INSERT INTO image_set(PSID,name,select_num) VALUES (%s,%s,%s)"
        PSID = i
        name = i
        values = (PSID, name, select_num)
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()


if __name__ == '__main__':
    init_image_dic()
    pass
