from flask import Flask, render_template, url_for, redirect, request, flash, session
from utils.UserForm import UserForm
from utils.SaveDataBase import SaveForm, SaveImgInfo
from utils.ProcessData import age_for_save, profession_for_save, living_for_save, travel_for_save
from utils.ImagesSetTools import dataset_generator, GenerateRandom
from wsgiref.simple_server import make_server
from datetime import timedelta
from werkzeug.middleware.proxy_fix import ProxyFix
import json
import numpy as np

app = Flask(__name__)
app.send_file_max_age_default = timedelta(seconds=1)
app.config["SECRET_KEY"] = 'ab292e7dd1374d3185286270cac2bb18'
# 数据库配置
# 数据集
graph_set_1 = []
graph_set_2 = []
graph_name_1 = []
graph_name_2 = []


# 用于将numpy数组序列化成json
class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(NpEncoder, self).default(obj)


# 开始界面
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


# 过滤器
@app.template_filter('get_name')
def get_name(str):
    length2 = len("images/data_set_test1.0/") + 1
    return str[length2:-1] + "g"


# 城市安全测试界面(正常用户）
@app.route('/test', methods=['GET', 'POST'])
def test():
    src_path = "./static/images/data_set_test1.0"
    generator = GenerateRandom()
    cur_id = generator.process()
    path = src_path + "/" + str(cur_id)
    session['judge_num'] = json.dumps(cur_id, cls=NpEncoder)
    graph_set_1, graph_set_2, graph_name_1, graph_name_2, count = dataset_generator(path)
    ls_1 = []
    ls_2 = []
    for i in graph_set_1:
        i = i[26:-7] + i[-5]
        ls_1.append(i)
    for i in graph_set_2:
        i = i[26:-7] + i[-5]
        ls_2.append(i)
    if request.json:
        # 对传回的数据进行处理，存入数据库
        data = request.json
        db = SaveImgInfo()
        # 处理被认为是安全的图片
        for i in range(len(data)):
            img_safe = (data[i]['name'].split('.')[0][0:-3] + data[i]['name'].split('.')[0][-1])[1:]
            if img_safe in ls_1:
                # 安全处理
                safe_info = db.get_data(img_safe)
                safe = safe_info[1] + 1
                db.update_data_safe(safe, img_safe)
                # 不安全处理
                img_unsafe = ls_2[i]
                unsafe_info = db.get_data(img_unsafe)
                unsafe = unsafe_info[2] + 1
                db.update_data_unsafe(unsafe, img_unsafe)
            else:
                safe_info = db.get_data(img_safe)
                safe = safe_info[1] + 1
                db.update_data_safe(safe, img_safe)
                # 不安全处理
                img_unsafe = ls_1[i]
                unsafe_info = db.get_data(img_unsafe)
                unsafe = unsafe_info[2] + 1
                db.update_data_unsafe(unsafe, img_unsafe)
    return render_template('image_test.html', set_1=graph_set_1, set_2=graph_set_2, name_set_1=graph_name_1,
                           name_set_2=graph_name_2)


# 测试界面二 接口
@app.route('/test_spec', methods=['GET', 'POST'])
def test_spec():
    src_path = "./static/images/data_set_test"
    generator = GenerateRandom()
    cur_id = generator.process()
    path = src_path + "/" + str(cur_id)
    session['judge_num'] = json.dumps(cur_id, cls=NpEncoder)

    # path = './static/images/data_set_test'
    graph_set_1, graph_set_2, graph_name_1, graph_name_2 = dataset_generator(path)
    res1 = dict.fromkeys(graph_name_1, 0)
    res2 = dict.fromkeys(list(reversed(graph_name_2)), 0)
    if request.json:
        # 对传回的数据进行处理，存入数据库
        data = request.json
        db = SaveImgInfo()
        for i in range(len(data)):
            # 处理被认为是安全的图片
            # print("-"*10)
            # print(data)
            img = data[i]['name'].split('.')[0].split('/')[1]
            # print(img)
            number = "".join(list(filter(str.isdigit, img)))
            if "-" in img:
                # print("为负的！")
                number = number + str(1)
            # db.get_data(number) #当把图片文件夹建好，图片和文件夹数据库初始化好之后，把622180换成number
            info = db.get_data(number)
            safe = info[1] + 1
            unsafe = info[2]
            skip = info[3]
            db.update_data(safe, number)
        # print("data", request.json)

    return render_template('image_test_spec.html', set_1=graph_set_1, set_2=graph_set_2, name_set_1=graph_name_1,
                           name_set_2=graph_name_2)


# 用户提交信息界面
@app.route('/forms', methods=['GET', 'POST'])
def forms():
    form = UserForm()
    if request.method == 'POST' and form.validate():
        # 获取前台传来的表单
        gender = request.form.get('gender')  # 1为男性，2为女性
        age = request.form.get('age')
        profession = request.form.get('profession')
        earthquake_checkbox_1 = request.form.get('earthquake_checkbox_1')
        earthquake_checkbox_2 = request.form.get('earthquake_checkbox_2')
        earthquake_checkbox_3 = request.form.get('earthquake_checkbox_3')
        earthquake_checkbox_4 = request.form.get('earthquake_checkbox_4')
        living = request.form.get('living')
        travel = request.form.get('travel')
        advice = request.form.get('feedback')
        judge_num = session.get('judge_num', None)

        # 处理数据
        earthquake = []
        earthquake_checkbox = [earthquake_checkbox_1, earthquake_checkbox_2, earthquake_checkbox_3,
                               earthquake_checkbox_4]
        for i in range(4):
            if earthquake_checkbox[i] == "y":
                earthquake.append(1)
            else:
                earthquake.append(0)
        a = [str(i) for i in earthquake]
        b = int(''.join(a))
        form = (judge_num, int(gender), age_for_save(age), profession_for_save(profession), b, living_for_save(living),
                travel_for_save(travel), advice)
        user_info = SaveForm()
        user_info.add_form(form)
        flash(u'调查问卷已成功提交，感谢您的参与！')
        return redirect(url_for('index'))

    return render_template('page_form.html', form=form)


if __name__ == '__main__':
    server = make_server('127.0.0.1', 5000, app)
    server.serve_forever()
    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.run()
