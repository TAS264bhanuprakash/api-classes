from fastapi import FastAPI
from pydantic import BaseModel,Field

app=FastAPI()


class Book:
    id: int
    name: str
    author: str
    description: str
    rating: int
    def __init__(self,id,name,author,description,rating):
        self.id=id
        self.name=name
        self.author=author
        self.description=description
        self.rating=rating


BOOK=[
    Book(1,"Data Science1","Data Boy1","Normal",5),
    Book(2,"Data Science2","Data Boy2","Normal",4),
    Book(3,"Data Science3","Data Boy3","Normal",3),
    Book(4,"Data Science4","Data Boy4","Normal",2),
    Book(5,"Data Science5","Data Boy5","Normal",1)
]

def validation(BaseModel):
    id: int
    name: str
    author: str
    description: str
    rating: int

@app.get("/book_data/data")
async def data(data=validation):
    return BOOK
