from twisted.internet import reactor,protocol

class Echo(protocol.Protocol):
    """This is just about the simplest possible protocol"""
    def dataReceived(self,data):
        "As soonas any data is received,write it back."
        self.transport.write(data)
        print(data)


def main():
    """This runs the protocol on port 8000"""
    factory = protocol.ServerFactory()
    factory.protocol = Echo
    reactor.listenTCP(8000,factory)
    reactor.run()

if __name__ == '__main__':
    main()
