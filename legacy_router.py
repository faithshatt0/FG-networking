from mininet.net import Mininet
from mininet.node import Host, Node
from mininet.cli import CLI
from mininet.log import setLogLevel, info

def myNetwork():
    net = Mininet( topo=None,
    build=False,
    ipBase='10.26.1.0/24')
    
    info( '*** Adding controller\n' )
    info( '*** Add switches\n')
    r1 = net.addHost('r1', cls=Node, ip='10.26.1.1/24')
    r1.cmd('sysctl -w net.ipv4.ip_forward=1')
    
    info( '*** Add hosts\n')
    h1 = net.addHost('h1', cls=Host, ip='10.26.1.2/24', defaultRoute='via 10.26.1.1')
    h2 = net.addHost('h2', cls=Host, ip='10.26.2.2/24', defaultRoute='via 10.26.2.1')
    
    info( '*** Add links\n')
    net.addLink(h1, r1, intfName2='r1-eth1', params2={'ip' : '10.26.1.1/24'})
    net.addLink(h2, r1, intfName2='r1-eth2', params2={'ip' : '10.26.2.1/24'})
    
    info( '*** Starting network\n')
    net.build()
	
    info('*** Starting controllers\n')
    for controller in net.controllers:
	controller.start()

    info('*** Starting switches\n')

    info('*** Post configure switches and hosts\n')
        
    CLI(net)
    net.stop()
 
if __name__ == '__main__':
    setLogLevel( 'info' )

myNetwork()
