from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from openai import OpenAI

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def instant():
    client = OpenAI(
        # increase default timeout to 15 minutes (from 10 minutes)
        timeout=900.0
    )
    message = """
    You are on a website that has been just deployed to production.
    Write an enthusiastic announcement to welcome a technical visitor for the first time, explaining that it is live on production.
    """
    messages = [{"role": "user", "content": message}]
    response = client.chat.completions.create(model="gpt-5-nano", messages=messages, service_tier="flex")
    reply = response.choices[0].message.content.replace("\n", "<br/>")
    html = (
        f"<html><head><title>Live in an Instant!</title></head><body><p>{reply}</p></body></html>"
    )

    return html