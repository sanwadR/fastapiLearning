'''
When you declare other function parameters that are not part of the path parameters, they are automatically interpreted as "query" parameters !!!!
'''
from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get('/items/')
async def read_item(skip: int = 0, limit:int=10):
    return fake_items_db[skip: skip + limit] # This just defines the range from skip to the limit of the fake_items_db

'''
Optional parameters : 
The same way, you can declare optional query parameters, by setting their default to None
'''
# @app.get('/items/{item_id}')
# async def read_item(item_id: int,q: str = None):
#     if q:
#         return {"item_id": item_id, "q": q}
#     return {"item_id": item_id}

'''
REQUIRED query parameters :
If you want to declare a required query parameter, you can do it with the Query class,
'''
@app.get("/items/{item_id}")
async def read_user_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item

'''
Here the query parameter needy is a required query parameter of type str.

If you open in your browser a URL like:


http://127.0.0.1:8000/items/foo-item
...without adding the required parameter needy, you will see an error like:


{
  "detail": [
    {
      "type": "missing",
      "loc": [
        "query",
        "needy"
      ],
      "msg": "Field required",
      "input": null
    }
  ]
}
'''