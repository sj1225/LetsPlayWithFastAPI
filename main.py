### Let's Study FastAPI! ###
from typing import Optional, Union
from fastapi import FastAPI

app = FastAPI(
    # Specification API
    title="Let's Study FastAPI!",
    description="## Let's  Study FastAPI. \n Markdown is available here. **bold**, _italic_ ...",
    version="0.0.1",
    #terms_of_service="{terms_of_service_url}",
    contact={
        "name" : "m1ngmy0ng",
        #"url" : "{your_site_url}",
        #"email" : "{your_email}"
    },

    # License Informations
#    license_info={
#        "name" : "{license_name}",
#        "url": "{license_url}",
#    },

    # Tags
    openapi_tags=[
        {
            "name" : "tag01",
            "description" : "tag test 01"
        },
        {
            "name" : "tag02",
            "description" : "tag test 02"
        }
    ]
)

@app.get("/", tags=["tag01"], summary="Hello World!", description="Return 'Hello : World'")
def read_root():
    return {"Hello": "World"}

@app.get("/str", tags=["tag01"], summary="RETURN STRING", description="Return String")
def read_str():
    return "Hello?"

@app.get("/int", tags=["tag01"], summary="RETURN INTEGER")
def read_int():
    return 10

@app.get("/items/{item_id}", tags=["tag01"], summary="PARAMETER TEST")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

### Return HTML Page
from fastapi.responses import FileResponse

@app.get("/html", summary="HTML TEST")
def read_html():
    return FileResponse('index.html')

### Requests : POST, PUT, PATCH, DELETE
from pydantic import BaseModel

# Define data model
class User(BaseModel):
    name : str
    age : Optional[int] = 1

@app.post("/post", tags=["tag02"], summary="POST TEST")
def read_post(data : User):
    print("post ok")
    return data

@app.put("/put", tags=["tag02"], summary="PUT TEST")
def read_put(data : User):
    print("put ok")
    return data

@app.patch("/patch", tags=["tag02"], summary="PATCH TEST")
def read_patch(data : User):
    print("patch ok")
    return data

@app.delete("/delete", tags=["tag02"], summary="DELETE TEST")
def read_delete(data : User):
    print("delete ok")
    return data