import pymysql


class SaveForm:
    count = 0

    def __init__(self):
        self.db = pymysql.connect(
            host="localhost",
            user="root",
            passwd="13678422587",
            database="city_test")
        self.count += 1

    def add_form(self, form):
        # 使用 cursor() 方法创建一个 dict 格式的游标对象 cursor
        cursor = self.db.cursor()
        sql = "INSERT INTO user_info(judge_num,user_gender,user_age,user_profession,user_earthquake,user_living,user_travel,user_advice) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        # sql = "INSERT INTO user_info(user_id,judge_num,user_gender,user_age,user_profession,user_earthquake,user_living,user_travel,user_advice) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        # SQL = """INSERT INTO user_info(user_id,judge_num) VAULES(0, 1)"""
        # SQL = "INSERT INTO user_info(user_id,judge_num,user_gender,user_age,user_profession,user_earthquake,user_living,user_travel,user_advice) VALUES(111,2,1,2,3,1000,3,3,'我爱编程')"
        # SQL ="""INSERT INTO user_info(user_id,,judge_num,user_gender,user_age,user_advice) VALUES(%s,%s,%s,%s,%s)"""#有问题
        # SQL = """INSERT INTO user_info(user_id,judge_num,user_gender,user_age,user_profession,user_earthquake,user_living,user_travel,user_advice) VALUES form"""
        # SQL = """INSERT INTO user_info(user_id,judge_num,user_gender,user_age,user_profession,user_earthquake,user_living,user_travel,user_advice) VALUES form"""
        # 使用 execute()  方法执行 SQL 查询
        user_id = self.count
        judge_num = form[0]
        user_gender = form[1]
        user_age = form[2]
        user_profession = form[3]
        user_earthquake = form[4]
        user_living = form[5]
        user_travel = form[6]
        user_advice = form[7]
        values = (judge_num, user_gender, user_age, user_profession, user_earthquake, user_living, user_travel,
                  user_advice)
        # values = (user_id,judge_num,user_gender,user_age,user_profession,user_earthquake,user_living,user_travel,user_advice)
        cursor.execute(sql, values)
        self.db.commit()
        # 使用 fetchone() 方法获取单条数据.
        # data = cursor.fetchone()
        # print("successfully!")
        # 关闭数据库连接
        self.db.close()


class SaveImgInfo:
    def __init__(self):
        self.db = pymysql.connect(
            host="localhost",
            user="root",
            passwd="13678422587",
            database="city_test")
        self.cursor = self.db.cursor()

    def start(self):

        sql = "INSERT INTO image_dic(PID,safe,unsafe,skip,rate,image_name) VALUES (%s,%s,%s,%s,%s,%s)"
         # 使用 execute()  方法执行 SQL 查询
        PID = 622270
        safe = 0
        unsafe =0
        skip = 0
        rate = 0
        P_PSID =1
        image_name = '622(180)'
        values = (PID,safe,unsafe,skip,rate,image_name)
        self.cursor.execute(sql, values)
        self.db.commit()
        # 使用 fetchone() 方法获取单条数据.
        # data = cursor.fetchone()
        # print("successfully!")

    def get_data(self, id):
        sql = 'SELECT * FROM image_dic WHERE PID ='+str(id)
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        # print("Get data successfully!")
        return result

    def update_data(self, data, id):
        sql = 'UPDATE image_dic SET safe ='+str(data)+ ' WHERE PID = '+str(id)
        self.cursor.execute(sql)
        self.db.commit()
        # print("Update image_dic successfully!")
    # 关闭数据库连接
    def close(self):
        self.db.close()


class SaveImgSet:
    def __init__(self):
        self.db = pymysql.connect(
            host="localhost",
            user="root",
            passwd="13678422587",
            database="city_test")
        self.cursor = self.db.cursor()

    def update_data(self, data, id):
        sql = 'UPDATE image_set SET select_num ='+str(data)+' WHERE PSID = '+str(id)
        self.cursor.execute(sql)
        self.db.commit()
        # print("Update image_set successfully!")


