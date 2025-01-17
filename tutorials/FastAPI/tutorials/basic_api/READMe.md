# Creating a basic app
***

## Goal
- Before creating our ML model lets start by creating a basic API that’s going to return us a simple message.
***

## Create a simple app
- This app will return a simple welcome message.
- This app will return a simple answer given a user input.
- Paste the following code in a file named: `basic-app.py`

```python
# Imports
from fastapi import FastAPI
import uvicorn

# Instaniate your FastAPI instance
app = FastAPI()

# Defining path operation for root endpoint
@app.get('/')
def main():
    return {'message': 'Welcome to kyaiooiayk!'}

# Defining path operation for /name endpoint
@app.get('/{name}')
def hello_name(name : str):
    # Defining a function that takes only string as input and output the following message.
    return {'message': f'Welcome to kyaiooiayk! Provided input:, {name}'}

```

## Firing your app
- Run your app with: `uvicorn basic-app:app --reload`
- `basic-app` refers to the name of the the `*.py` file
- `app` refers to the FastAPI instantiation name.
- `–reload` tells to restart the server every time we reload.
- Copy and past this address in yor browser: `http://127.0.0.1:8000/`
***

## Manual API app calls
- Calling the root path end point: `http://127.0.0.1:8000/`
- Calling a custom end point: `http://127.0.0.1:8000/hello again!`
***

## Interactive API app calls
- FastAPI comes with Interactive API docs which can access by adding `/docs` in your path as in: `http://127.0.0.1:8000/docs`. 
- Here you’ll get a webpage where you can test the endpoints of your API by seeing the output they’ll give for the corresponding inputs if any.
*** 

## Troubleshooting
- If you get an erro like this: `OSError: [Errno 48] Address already in use` then follow this [link](https://ishaileshmishra.medium.com/the-python-flask-problem-socket-error-errno-48-address-already-in-use-4d074847587e) to resolve it. Essentially this appens, when you fire the app for the first time, you kill the python thread and relaunching it again.
- Option #1:
   - Try to locate the PID of the process with: `ps -fA | grep python`
   - Then kill the PID with: `kill PID`
   - If the one above does not work try: `kill -s KILL <pid>` or `kill -9 <pid>`
- Option #2:
   - Locate the PID with: `lsof -i:8050`
   -  Then shut the process with: `kill PID`
***

## References
- [Deploying ML Models as API using FastAPI](https://www.geeksforgeeks.org/deploying-ml-models-as-api-using-fastapi/?ref=rp)
***
