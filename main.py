# HTTP METHOD GET
from fastapi import FastAPI
from typing import Optional

# Baris ini membuat instance aplikasi FastAPI.
app = FastAPI()

# Mendefinisikan endpoint - Ini disebut decorator.
@app.get("/")
def read_root():
    # return {"Message" : "Hello World"}
    return {"Message" : "Hello Sam"}

@app.get("/greet") # Tidak perlu sama dengan nama fungsi
def greet():
    return {"Message" : "Hello Wonwoo"}


# PATH & QUERY PARAMETER
# 1. Path Parameter
# @app.get("/greet/{name}") # {name} disebut path parameter, yaitu nilai yang diambil langsung dari URL.
# def greet_name(name:str):
# # def greet_name(name:int):
#     return {"Message" : f"Hello {name}"}

# 2. Query Parameter
# @app.get("/greet/{name}")
@app.get("/greet/") # http://127.0.0.1:8000/greet/?name=sam&age=20
def greet_name(name: str, age:Optional[int] = None):
    return {"Message": f"Hello {name} and you are {age} years old"}
# http://127.0.0.1:8000/greet/Yuri?age=20 


# HTTP METHOD POST


