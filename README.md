# python_snipets
A bunch of python folders with code scafolding for reuse in other projects  

## Setup  
Ideally a virtual environment shoud be setup for these projects.  
Using python 3.14, I found that the virtual environment should be in a file like .venv or .env  
```
py -m venv .env
.env\Scripts\activate.bat
```
Add dependencies for each example folder using pip install ....

## Running examples  
Make sure virtual environment is activated and dependencies are installed.  
Go in the example folder and run the app.py (this is usually the default name of the example)

## 001_Logging_example  
Useful logging advanced configuration for console, file rotation and json line logging using a config.json or config.yml file to setup the root logger for small to meduim sized projects.  

## 002_pyproject.toml (snakesay)  
A demo package configured using TOML configuration file. Comes from [Real Python Packaking](https://www.youtube.com/watch?v=v6tALyc4C10) video  
Go to folder and launch "pip installe -e ." to install the snakesay package and associated launch commands.  
Then type "snake hello world"  

## 003_fastapi  
A demo scafolding project to implement fastapi core features and a schema definition. It implements a basic CRUD (no delete) to store books in a memory dictionary.  

