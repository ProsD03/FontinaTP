from twisted.internet.protocol import Protocol, ClientFactory

class Fontina(Protocol):
  def connectionMade(self):
    print(self.transport.getPeer())

  def dataReceived(self, data: bytes):
    print(data)

class FontinaFactory(ClientFactory):
  def startedConnecting(self, connector):
    print('Started to connect.')

  def buildProtocol(self, addr):
    print('Connected.')
    return Fontina()

  def clientConnectionLost(self, connector, reason):
    print('Lost connection.  Reason:', reason)

  def clientConnectionFailed(self, connector, reason):
    print('Connection failed. Reason:', reason)