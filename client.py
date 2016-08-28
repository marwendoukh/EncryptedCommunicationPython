from twisted.internet import reactor, ssl
from twisted.internet.protocol import ClientFactory
from twisted.protocols.basic import LineReceiver
import sys


##################################### The functions to handle the data  ########################
class TLSClient(LineReceiver):

    def connectionMade(self):
            self.transport.startTLS(ssl.CertificateOptions())
            self.sendLine("Hi")

    def lineReceived(self, line):
        print(line)            
        self.sendLine("TLS starts")
        self.sendLine("user")
        self.transport.loseConnection()

   
##################################### The functions to handle the connection  ########################


class TLSClientFactory(ClientFactory):
    protocol = TLSClient

    def clientConnectionFailed(self, connector, reason):
        print "connection failed: ", reason.getErrorMessage()
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        print "connection lost: ", reason.getErrorMessage()
        reactor.stop()



if __name__ == "__main__":
    factory = TLSClientFactory()
    #Change the server IP Address
    reactor.connectTCP('localhost', 8028, factory)
    reactor.run()
    
    
