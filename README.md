# Jymon -- JSON output for Xymon

The Xymon/Hobbit/BB monitoring system is still widely used. A problem with it however is that it is old.
This project provides JSON output to a Xymon server, either scripted to a file or as a web service

## Getting Started


### Prerequisites

This requires Python 2.7, Flask,a handful of python packages and an Xymon-client and for the python files to be executable

```
pip install -r requirements.txt
chmod +x ./*.py
```
### Debugging

Instead of writing a lengthy post here, the code is heavily commented and serves as its own documentation

### Files

jymon.py
a small python application that uses the xymon-client to query a Xymon server, parses it to JSON and prints it to stdout.
can be implemented directly into scripts for example to output the JSON to a file


jymon_server.py
A flask server that runs jymon.py when an http request is made. By default it caches the response for 3 seconds so
the Xymon server doesn't get flooded with requests if the jymon_server is being called too freqently 




### xymon-client

The Xymon client can be downloader from the [Xymon project page](https://sourceforge.net/projects/xymon/)

On ubuntu it can be installed with

```
$ sudo apt-get install xymon-client
```

On RHEL/Centos it can be downloaded directly [Here](https://sourceforge.net/projects/xymon/files/Xymon/4.3.10/RHEL6/xymon-client-4.3.10-1.x86_64.rpm/download)

and installed with
```
$ sudo yum install ~/xymon-client*rpm
```

### Speed

To test the effiency of the system I tested it against a Xymon server containing 17K entities being reported

xymon-client speed: 0.3 seconds

jymon-client speed: 0.9 seconds 

While jymon triples the speed it takes to deliver the data, doing it under a second with 17K entries feels acceptable

## Authors

* **Gbit** - [Gbit-is](https://github.com/gbit-is)


## License

This project is licensed under the MIT License
