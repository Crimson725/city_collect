import os
import random
from utils.SaveDataBase import SaveImgSet



def dataset_generator(path):
    """
    获取目录下所有文件的路径,存入set中
    :param path:路径
    :return: 随机化的列表
    """
    ls = []
    set_1 = []
    set_2 = []
    name_set_1 = []
    name_set_2 = []

    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            dataset_generator(file_path)
        else:
            # 路径转换
            file_path = file_path.replace('\\', '/').lstrip(".").lstrip("/stati").lstrip("c/")
            ls.append(file_path)
    random.shuffle(ls)
    count = len(ls) // 2
    length = len("images/data_set_test2.0/") + 1
    ls_ret = []
    for i in ls:
        i = i.split('.')[1][4:-3] + i.split('.')[1][-1]
        ls_ret.append(i)
    for i in range(count):
        file = ls.pop()
        set_1.append(file)
        name_set_1.append(file[length:-1])
    for i in range(count):
        file = ls.pop()
        set_2.append(file)
        name_set_2.append(file[length:-1])
    # 每次取两个
    return set_1, set_2, name_set_1, name_set_2
