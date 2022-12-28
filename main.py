# from fastapi import FastAPI, Query
# from fastapi.responses import HTMLResponse, ORJSONResponse
from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse, ORJSONResponse
from datetime import datetime
import os

app = FastAPI()


@app.get('/')
async def index():
    now = datetime.now()
    return HTMLResponse(f"""
        <div>This the index page</div>
        <div>{now}</div>
        <div>{__name__}</div>
    """)


@app.get('/lines/')
async def lines(keywords: str = ""):
    now = datetime.now()
    lines = get_lines_from_file(keywords)
    response = f"This the lines page - {now} {os.linesep} {lines}"
    return ORJSONResponse({"response": response})


def get_lines_from_file(keywords: str):
    return keywords
