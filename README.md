# 5 Things About Python Logging

This repository accompanies a talk given at the SFPython meet-up ([here](https://docs.google.com/presentation/d/1NsFebyAGkFQScrvoHLYguhgn3Dns6emsBJLOs8gVuZI/edit?usp=sharing)).

It is a collection of basic examples for how to use Python's logging API.


## Loggers

1. Simple logging: [loggers/simple/main.py](loggers/simple/main.py)
2. Using logger namespaces (or ancestry): [loggers/namespaces/main.py](loggers/namespaces/main.py)
3. Using \_\_name\_\_ for your namespaces: [loggers/free_namespaces/main.py](loggers/free_namespaces/main.py)


## Handlers

1. Simple stream handlers: [handles/streams/main.py](handlers/streams/main.py)
2. Simple file handlers: [handlers/files/main.py](handlers/files/main.py)
3. Handler levels vs. logger levels: [handlers/levels/main.py](handlers/levels/main.py)
4. Log messages over a network: [handlers/network/main.py](handlers/network/main.py)


## Formatters

1. Basic message formatting: [formatters/message/main.py](formatters/message/main.py) 
2. Date/Time formatting: [formatters/date_time/main.py](formatters/date_time/main.py)

BOOKMARK THESE SITES:
1. Python string format cheat-sheet: https://pyformat.info/
2. Python `LogRecord` attribute list: https://docs.python.org/2.7/library/logging.html#logrecord-attributes
3. Python `strftime` format strings: https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior


## Filters

1. Basic filtering: [filters/simple/main.py](filters/simple/main.py)
2. Injecting `LogRecord` attributes: [filters/inject/main.py](filters/inject/main.py)


## Configuration

1. Using `basicConfig`: [configuration/basicConfig/main.py](configuration/basicConfig/main.py)
2. Using `dictConfig`: [configuration/dictConfig/main.py](configuration/dictConfig/main.py)
3. Using `fileConfig`: [configuration/fileConfig/main.py](configuration/fileConfig/main.py)


### Example Configuration

1. `.ini`/`.conf` file: [configuration/fileConfig/config.ini](configuration/fileConfig/config.ini)
2. Native Python `dict`: [configuration/dictConfig/main.py](configuration/dictConfig/main.py)


## Bonus  - Python Log Config-Change Server

This is completely bonkers. 
Python has a built-in logging configuration update server.

This means you can change the logging config for an entire runtime on the fly, without restarting the process.

**NOTE**: This example uses Flask. If you want to run `main.py`, please be sure to `pip install Flask` first.

* Python Log Server: [log_server_WAT/main.py](log_server_WAT/main.py)
