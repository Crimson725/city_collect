# 项目用数据收集网站

## 更改数据集

- 将数据集文件夹放置于 `/static/images/`
- 数据集文件夹子文件夹命名从0开始
- 根据要求修改 `app.py`，`init_db.py`，`ImageSetTools.py`，`SaveDataBase.py`中的相关代码（数据库连接，文件名截取等）
- 若参考本项目的数据集配置方式，启动前首先执行 `init_db.py`

## 执行/debug

本项目使用Flask框架

**本地执行**

```bash
git clone https://github.com/Crimson725/city_collect.git
git checkout stable
cd city_collect
flask run
```


若在执行时启用热加载调试需在 `app.py 进行修改`

```python

if __name__ == '__main__':
    server = make_server('127.0.0.1', 5000, app)
    server.serve_forever()
    app.wsgi_app = ProxyFix(app.wsgi_app)
# 修改此处 debug=True
    app.run(debug=True)

```

## 安装依赖

```
pip install -r requirements.txt
```

## 网站部署启动

```
gunicorn app:app -c gunicorn.py       
```

### 部署注意

- 需要自行配置nginx
- 修改 `gunicorn.py`内的部署设置
