#!/usr/bin/env python

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

def main():
    # Instantiate a dummy authorizer for managing 'virtual' users
    authorizer = DummyAuthorizer()
    # Define a new user having full r/w permissions and a read-only
    # anonymous user
    #authorizer.add_user('user', '12345', '.', perm='elradfmwM')
    #authorizer.add_user('user', '12345', '/home/user/tmp/rom', perm='elradfmw')
    #authorizer.add_anonymous('/home/user/tmp/rom')
    #authorizer.add_user('user', '12345', '/', perm='elradfmw')
    #authorizer.add_anonymous('/')
    authorizer.add_user('user', '12345', '/home/archermind/', perm='elradfmw')
    #authorizer.add_anonymous('/home/user/tmp/rom')
    authorizer.add_anonymous('/home/archermind/tmp/shared')
    
    # Instantiate FTP handler class
    handler = FTPHandler
    handler.authorizer = authorizer
    
    # Define a customized banner (string returned when client connects)
    handler.banner = "ftp filesystem ready."
    # Specify a masquerade address and the range of ports to use for
    # passive connections.  Decomment in case you're behind a NAT.
    #handler.masquerade_address = '151.25.42.11'
    #handler.passive_ports = range(60000, 65535)
    
    # Instantiate FTP server class and listen on 0.0.0.0:2121
    address = ('0.0.0.0', 2121)
    server = FTPServer(address, handler)
    
    # set a limit for connections
    #server.max_cons = 256
    #server.max_cons_per_ip = 5
    
    # start ftp server
    server.serve_forever()
    
if __name__ == '__main__':
    main()
