#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSKernelSwitch, OVSLegacyKernelSwitch, UserSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.link import Link, TCLink

def topology():

    "Create a network."
    net = Mininet( controller=RemoteController, link=TCLink, switch=OVSKernelSwitch )

    print "*** Creating nodes"

    h1 = net.addHost( 'h1', mac='00:00:00:00:00:01', ip='10.0.0.1/24' )
    h2 = net.addHost( 'h2', mac='00:00:00:00:00:02', ip='10.0.10.2/24' )
    h3 = net.addHost( 'h3', mac='00:00:00:00:00:03', ip='10.0.0.2/24' )
    c7 = net.addController( 'c7', controller=RemoteController, ip='127.0.0.1', port=6633 )

    print "*** Creating links"
    #net.addLink(h1, h2)
    Link(h1, h2)
    
    #net.addLink(h2, h3)
    Link(h2, h3)

    #net.addLink(s5, h2, 2, 0)
    Link(h3, h1)

    #net.addLink(h1, s5, 0, 1)

    h1.cmd('ifconfig h1-eth1 10.0.10.1 netmask 255.255.255.0')

    h2.cmd('ifconfig h2-eth1 10.0.20.1 netmask 255.255.255.0')

    h3.cmd('ifconfig h3-eth1 10.0.20.2 netmask 255.255.255.0')

    h1.cmd("sudo echo 1 > /proc/sys/net/ipv4/ip_forward")

    h2.cmd("sudo echo 1 > /proc/sys/net/ipv4/ip_forward")

    h3.cmd("sudo echo 1 > /proc/sys/net/ipv4/ip_forward")

    print "*** Starting network"

    net.build()

    c7.start()
 

    print "*** Running CLI"

    CLI( net )

 

    print "*** Stopping network"

    net.stop()

 

if __name__ == '__main__':

    setLogLevel( 'info' )

    topology()