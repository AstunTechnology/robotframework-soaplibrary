# SOAP library for Robot Framework

## Introduction

This is a fork of the robotframework-sudslibrary but rather than using SUDS, it uses
[Zeep](https://github.com/mvantellingen/python-zeep) which is a current and maintained SOAP client.

## Installation

- Install VirtualEnv
```
python -m venv venv
```
- Activate VirtualEnv
```
.\venv\scripts\activate
```
- Install the pre-requisites
```
pip install -r requirements.txt
```
- [Download and install npm](https://nodejs.org/en/) (required for running local webservices)
- Install http-server (add *-g* option to install http-server for all users)
```
npm install http-server
```

## Running Tests
- Activate the local webservices
```
python ./Test/TestWebServices.py
```
- Run the tests
```
python ./Test/run_tests.py
```