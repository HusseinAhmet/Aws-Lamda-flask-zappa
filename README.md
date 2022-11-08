# Aws-Lamda-flask-zappa

An example of creating very simple serverless web app on aws lambda using Python, Flask and Zappa.

```
mkdir zappa
cd zappa
python -m venv venv
source venv/bin/activate
# on windows: venv\Scripts\activate
pip install flask
pip install zappa
```



### Add or Python code 
```
app.py
```

### Run Zappa init

```
pip install flask zappa
# create app.py
zappa init
```

### Modify zappa_setting.json

profile name comes from .aws/credentials. aws_region needs to be set, all others from zappa init are OK

```
{
    "dev": {
        "app_function": "app.app",
        "profile_name": "default",
        "project_name": "flask-zappa-tut",
        "runtime": "python3.7",
        "s3_bucket": "zappa-9cf4j0c1h",
        "aws_region": "us-west-1"
    }
}
```

### Deploy 

```
zappa deploy dev
```

### Make changes and update

```
zappa update dev
```

### Delete the app

```
zappa undeploy dev
```
