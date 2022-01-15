# 本文件存储对于数据格式转换以及数据保存读取等操作
# 将age改成对应的字符串形式，以下均为此功能
def age_for_save(age):
    if age == '1':
        return '未满16岁'
    elif age == '2':
        return '16-30岁'
    elif age == '3':
        return '30-55岁'
    else:
        return '55岁以上'


def profession_for_save(profession):
    if profession == 1:
        return '党政机关工作人员'
    elif profession == 2:
        return '社会生产服务和生活服务人员'
    elif profession == 3:
        return '农、林、牧、渔业生产及辅助人员'
    elif profession == 4:
        return '生产制造及有关人员'
    elif profession == 5:
        return '科学研究工作者'
    elif profession == 6:
        return '教育互联网从业者'
    elif profession == 7:
        return '青少年及在校学生'
    elif profession == 8:
        return '不便分类的其他从业人员'
    else:
        return '失业、无业或退休人员'


def earthquake_for_save(earthquake):
    s1 = '经历过512大地震'
    s2 = '在震中'
    s3 = '在震源附近'
    s4 = '未经历过大地震'


def living_for_save(living):
    if living == '1':
        return '从未居住过'
    elif living == '2':
        return '现在在都江堰'
    elif living == '3':
        return '曾经居住过'
    else:
        pass


def travel_for_save(travel):
    if travel == '1':
        return '从未到访'
    elif travel == '2':
        return '最近五年曾到访'
    elif travel == '3':
        return '五年之前曾到访'
    else:
        pass
