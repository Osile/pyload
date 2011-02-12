# -*- coding: utf-8 -*-

import sys
from socket import error
from os.path import dirname, abspath, join

try:
    import thrift
except ImportError:
    sys.path.append(abspath(join(dirname(abspath(__file__)), "..", "..", "lib")))

from thrift.transport import TTransport
from Socket import Socket
from Protocol import Protocol

from thriftgen.pyload import Pyload

class WrongLogin(Exception):
    pass

class NoConnection(Exception):
    pass

class NoSSL(Exception):
    pass

class ThriftClient():
    def __init__(self, host="localhost", port=7228, user="", password=""):

        self.createConnection(host, port)
        try:
            self.transport.open()
        except error, e:
            if e.args and e.args[0] == 111:
                raise NoConnection

        try:
            correct = self.client.login(user, password)
        except error, e:
            if e.args and e.args[0] == 104:
                #connection reset by peer, probably wants ssl
                try:
                    self.createConnection(host, port, True)
                    #set timeout or a ssl socket will block when query none ssl server
                    self.socket.setTimeout(10)

                except ImportError:
                    #@TODO untested
                    raise NoSSL
                try:
                   self.transport.open()
                   correct = self.client.login(user, password)
                finally:
                    self.socket.setTimeout(None)

        if not correct:
            self.transport.close()
            raise WrongLogin

    def createConnection(self, host, port, ssl=False):
        self.socket = Socket(host, port, ssl)
        self.transport = TTransport.TBufferedTransport(self.socket)

        protocol = Protocol(self.transport)
        self.client = Pyload.Client(protocol)


    def __getattr__(self, item):
        return getattr(self.client, item)

if __name__ == "__main__":

    client = ThriftClient(user="User", password="pyloadweb")

    print client.getServerVersion()
    print client.statusServer()
    print client.statusDownloads()
    q = client.getQueue()

    for p in q:
      data = client.getPackageData(p.pid)
      print data
      print "Package Name: ", data.name