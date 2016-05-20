#!/usr/bin/env python

from flask import Flask
import socket,os,redis
from mc import lookup_service

redis_service = lookup_service('leader.mesos', 'dcos-green-redis.marathon.mesos')

redis_ip = redis_service[0]
redis_port = redis_service[1]

r=redis.Redis(host=(redis_ip),port=(redis_port))
r.set("count",0)

app = Flask(__name__)

@app.route("/nwi")
def nwi():
        r.incr("count")
	return "GREEN APP: Visit number %d\nHostname: %s\n" % (int(r.get("count")),socket.gethostname())

if __name__ == "__main__" :
        app.run(host="0.0.0.0")
