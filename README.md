# Crowdsourced Data Collection Website for Urban Safety Perception

# Custom Dataset

- Place your dataset folder in `/static/images/`.
- Place your dataset folder in `/static/images/`.
- Subfolders of the dataset folder should be named starting from 0.
- Modify the relevant code in `app.py`, `init_db.py`, `ImageSetTools.py`, and `SaveDataBase.py` as per your requirements (database connections, file name truncation, etc.).
- If you are referencing the dataset configuration of this project, run `init_db.py` before starting.

## Execution/Debug

This project uses the Flask framework.

**Run Locally**

```bash
git clone https://github.com/Crimson725/city_collect.git
git checkout stable
cd city_collect
flask run
```

If you want to enable hot-reloading during execution, make the following modification in `app.py`:

```python

if __name__ == '__main__':
    server = make_server('127.0.0.1', 5000, app)
    server.serve_forever()
    app.wsgi_app = ProxyFix(app.wsgi_app)
    //...
    app.run(debug=True)

```

## Install Dependencies


```
pip install -r requirements.txt
```

## Deployment and Launch

```
gunicorn app:app -c gunicorn.py     
```

### Notes When Deploying

- Configure Nginx.
- Modify the deployment settings within gunicorn.py.
