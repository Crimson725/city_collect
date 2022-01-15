# 项目用数据收集网站
## 安装依赖
```
pip install -r requirements.txt
```
## 网站启动
```
gunicorn app:app -c gunicorn.py         
```
**注意**
- 需要自行配置nginx
- 修改gunicorn.py内的部署设置
- 更多问题自行Google，在此不再赘述


