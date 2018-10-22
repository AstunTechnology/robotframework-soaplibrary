# SOAP library for Robot Framework

##Introduction

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

## Running Tests
```
python ./Test/TestWebServices.py
python ./Test/run_tests.py
```