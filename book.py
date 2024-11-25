# from fastapi import Body,FastAPI

# app=FastAPI()
# BOOKS = [
#     {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
#     {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
#     {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
#     {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
#     {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
#     {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
# ]

# @app.get("/books")
# async def sample():
#     return BOOKS

# @app.get("/books/{book_name}")
# async def sample2(book_name):
#     for book in BOOKS:
#         if book.get("title").casefold()==book_name.casefold():
#             return book

# # @app.get("/books/{dynamic_paramneter}")
# # async def sample2(dynamic_paranmeter):
# #     return {"dynamic_parameter":dynamic_paranmeter}


# @app.get("/book/{author}")
# async def book_call_by_query_perra(author :str,category: str):
#     book_out=[]
#     for book in BOOKS:
#         if book.get('author').casefold()==author.casefold() and book.get('category').casefold()==category.casefold():
#             book_out.append(book)
#     return(book_out)


# @app.post("/book/craete")
# async def create(new_book=Body()):
#     BOOKS.append(new_book)
# @app.put("/update")
# async def update_book(update=Body()):
#     for i in range(len(BOOKS)):
#         if BOOKS[i].get('title').casefold()== update.get('title').casefold():
#             BOOKS[i]=update
# @app.delete("/book/delete")
# async def delete(title: str):
#     for i in range(len(BOOKS)):
#         if BOOKS[i].get('title').casefold()==title.casefold():
#             BOOKS.pop(i)
#             break

# @app.get("/book/{category}")
# async def fetch_books(category):
#     out_put=[]
#     for book in BOOKS:
#         if book.get('category').casefold()== category.casefold():
#             out_put.append(book)
#     return out_put