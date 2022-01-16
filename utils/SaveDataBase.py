import pymysql


class SaveForm:
    count = 0

    def __init__(self):
        self.db = pymysql.connect(
            host="localhost",
            user="root",
            passwd="13678422587",
            database="city")
        self.count += 1

    def add_form(self, form):
        # 使用 cursor() 方法创建一个 dict 格式的游标对象 cursor
        cursor = self.db.cursor()
        sql = "INSERT INTO user_info(judge_num,user_gender,user_age,user_profession,user_earthquake,user_living,user_travel,user_advice) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
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
        cursor.execute(sql, values)
        self.db.commit()
        self.db.close()


class SaveImgInfo:
    def __init__(self):
        self.db = pymysql.connect(
            host="localhost",
            user="root",
            passwd="13678422587",
            database="city")
        self.cursor = self.db.cursor()

    def get_data(self, id):
        sql = 'SELECT * FROM image_dic WHERE PID =' + str(id)
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        return result

    def update_data_safe(self, data, id):
        sql = 'UPDATE image_dic SET safe =' + str(data) + ' WHERE PID = ' + str(id)
        self.cursor.execute(sql)
        self.db.commit()
        print("update")

    def update_data_unsafe(self, data, id):
        sql = 'UPDATE image_dic SET unsafe =' + str(data) + ' WHERE PID = ' + str(id)
        self.cursor.execute(sql)
        self.db.commit()
        print("updated")

    # 关闭数据库连接
    def close(self):
        self.db.close()


class SaveImgSet:
    def __init__(self):
        self.db = pymysql.connect(
            host="localhost",
            user="root",
            passwd="13678422587",
            database="city")
        self.cursor = self.db.cursor()

    def update_data(self, data, id):
        sql = 'UPDATE image_set SET select_num =' + str(data) + ' WHERE PSID = ' + str(id)
        self.cursor.execute(sql)
        self.db.commit()
