
# ICT2103 Workshop

This application allow the user to create, retrieve, update and delete records using python and couchbase.
 
## Enviroment Setup
1. Download [Couchbase server](https://docs.couchbase.com/server/4.1/install/installation.html)
2. Download [Python 3](https://www.python.org/downloads/release/python-380/)
3. Ensure that the the environment variables is setup correctly for python. You can check by opening the command prompt and enter the following commands.
```
python --version
```
It should show the following
```
Python 3.X.X
```

4. Ensure that the the environment variables is setup correctly for pip. You can check by opening the command prompt and enter the following commands.

```
pip --version
```
It should show the following
```
pip 19.2.3 from c:\program files\python38\lib\site-packages\pip (python 3.8)
```

5. Open index.py. Go to line 47. Update the database credential
```
bucketname = 'ICT2103'
cluster = Cluster('couchbase://localhost')
authenticator = PasswordAuthenticator('Administrator', 'password')
```

6. To run the program, Open command prompt and change the directory to the place where you save the repo. Enter the following command
```
cd C:\<path-to>\ICT2103Workshop 
python index.py
```
