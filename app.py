#!/usr/bin/env python
# coding: utf-8
import cyclone.web
import sys

from twisted.internet import reactor
from twisted.python import log


class MainHandler(cyclone.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


if __name__ == "__main__":
    application = cyclone.web.Application([
        (r"/", MainHandler)
    ])

    log.startLogging(sys.stdout)
    open('/tmp/app-initialized', 'w').close()
    reactor.listenUNIX('/tmp/nginx.socket', application)
    reactor.run()
