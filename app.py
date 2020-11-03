import requests
import json
import os

from fastapi import FastAPI, Request, HTTPException, Response
from slack_bolt import App
from slack_bolt.adapter.fastapi import SlackRequestHandler


app = App()
app_handler = SlackRequestHandler(app)
api = FastAPI()

api_key = os.environ['API_KEY']


@app.event("app_mention")
def handle_app_mentions(body, say, logger):
    logger.info(body)
    say("What's up?")


@app.command("/show_my_exchange")
def command(ack, body, say):
    ack()
    response = requests.get(f"https://api.currencyfreaks.com/latest?apikey={api_key}")
    result_json = response.json()
    say(f"Date: {result_json['date']}, UAH: {result_json['rates']['UAH']}, EUR: {result_json['rates']['EUR']}" )


@api.post("/slack/events")
async def endpoint(req: Request):
    return await app_handler.handle(req)


@api.get("/healthz")
def check_api():
  response = requests.get("https://api.currencyfreaks.com")
  if response.status_code != 200:
    raise HTTPException(status_code=response.status_code, detail=response.text)
  else:
    return {"message": "OK"}


@api.get("/readinez")
async def test():
  return {"message": "OK"}
