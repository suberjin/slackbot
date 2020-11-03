# Slackbot
--------------------------------------

## Description

This is a PoC of Slackbot that uses python [slack-bolt](https://slack.dev/bolt-python/tutorial/getting-started) library and [Fastapi](https://fastapi.tiangolo.com/tutorial/first-steps/)
The project gather information from  Currency Conversion service [currencyfreaks.com](https://api.currencyfreaks.com)
In order to use it you should create your own environment variables that are necessary for Slack `SLACK_SIGNING_SECRET`, `SLACK_SIGNING_SECRET` and you API key `API_KEY` for exchange service.


## Project structure

The project has the following files:

- example -- examples for Kubernetes that uses Docker image on docker hub
- Dockerfile -- Dockerfile in order to create your own Docker image
- app.py -- the project itself
- requirements.txt -- list of requrenment
