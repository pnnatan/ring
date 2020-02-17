from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel

class Ring( Topo ):
    "Ring topology example."
    
    def __init__( self ):
	"Create custom topo."
	#initialize
        Topo.__init__( self )

	#add
        HA1 = self.addHost( 'HA1' )
        HA2 = self.addHost( 'HA2' )
        HB1 = self.addHost( 'HB1' )
        HB2 = self.addHost( 'HB2' )
        HC1 = self.addHost( 'HC1' )
        HC2 = self.addHost( 'HC2' )
        HD1 = self.addHost( 'HD1' )
        HD2 = self.addHost( 'HD2' )
        HE1 = self.addHost( 'HE1' )
        HE2 = self.addHost( 'HE2' )
        HF1 = self.addHost( 'HF1' )
        HF2 = self.addHost( 'HF2' )
        HG1 = self.addHost( 'HG1' )
        HG2 = self.addHost( 'HG2' )
        HH1 = self.addHost( 'HH1' )
        HH2 = self.addHost( 'HH2' )
        S1 = self.addSwitch( 'S1' )
        S2 = self.addSwitch( 'S2' )
        S3 = self.addSwitch( 'S3' )
        S4 = self.addSwitch( 'S4' )
        S5 = self.addSwitch( 'S5' )
        S6 = self.addSwitch( 'S6' )
        S7 = self.addSwitch( 'S7' )
        S8 = self.addSwitch( 'S8' )


	#links
        self.addLink( S1, S2 )
        self.addLink( S2, S3 )
        self.addLink( S3, S4 )
        self.addLink( S4, S5 )
        self.addLink( S5, S6 )
        self.addLink( S6, S7 )
        self.addLink( S7, S8 )
        self.addLink( S8, S1 )
        self.addLink( S1, HA1 )
        self.addLink( S1, HA2 )
        self.addLink( S2, HB1 )
        self.addLink( S2, HB2 )
        self.addLink( S3, HC1 )
        self.addLink( S3, HC2 )
        self.addLink( S4, HD1 )
        self.addLink( S4, HD2 )
        self.addLink( S5, HE1 )
        self.addLink( S5, HE2 )
        self.addLink( S6, HF1 )
        self.addLink( S6, HF2 )
        self.addLink( S7, HG1 )
        self.addLink( S7, HG2 )
        self.addLink( S8, HH1 )
        self.addLink( S8, HH2 )
    print("Hosts criados e conectados")
topos = { 'Ring': ( lambda: Ring() ) }

def simpleTest():
    "Create and test a simple network"
    topo = SingleSwitchTopo(n=4)
    net = Mininet(topo)
    net.start()
    print "Dumping host connections"
    dumpNodeConnections(net.hosts)
    print "Testing network connectivity"
    net.pingAll()
    net.stop()

if __name__ == '__main__':
    # Tell mininet to print useful information
    setLogLevel('info')
    simpleTest()