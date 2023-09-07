# IDS706-python-template [![CI](https://github.com/jeremymtan/IDS706-python-template/actions/workflows/ci.yml/badge.svg)](https://github.com/jeremymtan/IDS706-python-template/actions/workflows/ci.yml)
This repo contains work for mini-project 1. It sets up an environment on codespaces and uses Github Actions to run a Makefile for the following: `make install`, `make test`, `make format`, `make lint`. 

Some important stuff included are:

* `Makefile`

* `Dockerfile`

* A base set of libraries for devops and web

* `githubactions` 

## Purpose of project
The purpose of this project is to create a python template to use for later projects. To make sure github actions is working properly, I use a Makefile to test various parts of my code. To clarify, I made a simple function in main.py and use various test cases in test_main.py to make sure my code works correctly.

## Prepration
1. open codespaces 
2. wait for container to be built and virtual environment to be activated with requirements.txt installed 

## Check format and test errors 
1. Format code `make format`
2. Lint code `make lint`

eg: check lint errors:

<img width="658" alt="Screenshot 2023-09-06 at 10 11 38 PM" src="https://github.com/jeremymtan/IDS706-python-template/assets/36715338/98471323-112d-4818-9c3b-7fc15b9b7927">

3. Test code `make test`

eg: check test cases:

<img width="1376" alt="Screenshot 2023-09-06 at 10 11 58 PM" src="https://github.com/jeremymtan/IDS706-python-template/assets/36715338/caf8d3dc-4da0-4f76-9fe5-20805ecafa1a">


## References 
https://github.com/nogibjj/python-template



