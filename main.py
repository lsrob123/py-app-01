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
async def lines(keywords: str = "", output_json: str = "yes"):
    now = datetime.now()

    if output_json == "yes":
        lines = get_lines_from_file(keywords)
        return ORJSONResponse({"time": now, "response": lines})
    else:
        lines = get_lines_from_file(keywords, "<p />")
        return HTMLResponse(f"""
            <div>{now}</div>
            <div>{lines}</div>
        """)


def get_lines_from_file(keywords: str, line_break: str = ""):
    data_file = open("./data.txt", "r")
    lines = ""
    for line in data_file:
        lines += line
        lines += line_break
    data_file.close()

    return lines
