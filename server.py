from twisted.internet import reactor, ssl
from twisted.internet.protocol import ServerFactory
from twisted.protocols.basic import LineReceiver
import os

###########################################################################################################################################################    
###########################################################  FUNCTIONS   ##################################################################################   
###########################################################################################################################################################    

def User():
        return ("I'm %s " %(os.popen("whoami").read(),))
    

###########################################################################################################################################################          


class TLSServer(LineReceiver):
  
    def connectionMade(self):
            self.transport.startTLS(self.factory.contextFactory)
            self.sendLine("Hi")

    def connectionLost(self, reason):
           print("connection lost ")


    def lineReceived(self, command):
           print(command)
           self.sendLine("Okey, I received the following command : %s " % (command,))



#    SWITCH COMMAND : DO 
           if str(command) == 'user':             
                    self.sendLine(User())
           
       
#######################################################################          
   


if __name__ == '__main__':
    with open("myowncertif/server.key") as keyFile:
        with open("myowncertif/server.crt") as certFile:
            cert = ssl.PrivateCertificate.loadPEM(
                keyFile.read() + certFile.read())

    factory = ServerFactory()
    factory.protocol = TLSServer
    factory.contextFactory = cert.options()
    reactor.listenTCP(8028, factory)
    reactor.run()
