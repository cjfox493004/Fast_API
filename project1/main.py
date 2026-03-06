from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import random
import os

app = FastAPI()

@app.get("/randint")
def get_randint():
    n1 = random.randint(0,12)
    n2 = random.randint(0,12)
    return({"n1": n1, "n2": n2})

@app.get("/product")
def get_product(n1: int, n2: int):
    return(n1 * n2)


# serve the frontend from the "static" folder; using an absolute path makes
# it work regardless of the current working directory when uvicorn is
# started.
static_dir = os.path.join(os.path.dirname(__file__), "static")
app.mount("/", StaticFiles(directory=static_dir, html=True), name="static")


#shows a random multiplication problem, click button to show result