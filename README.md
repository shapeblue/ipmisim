# ipmisim

A fake ipmi server for testing purposes both as a tool and a library.
The code is forked from [Conpot](http://conpot.org/) and based on `pyghmi`.

![version badge](https://badge.fury.io/py/ipmisim.png) ![download badge](http://img.shields.io/pypi/dm/ipmisim.png)

This was created for testing IPMI related features in [Apache CloudStack](http://cloudstack.apache.org).

The tool ships with default sets of users for ease of use:

    ID  Name       Callin  Link Auth  IPMI Msg   Channel Priv Limit
    1   admin            true    true       true       ADMINISTRATOR
    2   operator         true    false      false      OPERATOR
    3   user             true    true       true       USER

The default passwords are:

    admin  : password
    opuser : oppassword
    user   : userpassword

Installation:

    pip install --upgrade ipmisim

Running:

    ipmisim 3000  # Runs on custom port 3000, else 9001 by default

For, usage in integration tests you can import the server module and create a server:

    from ipmisim.ipmisim import IpmiServer
    import socketserver

    port = 3000
    server = SocketServer.UDPServer(('0.0.0.0', port), IpmiServer)
    server.serve_forever()

For testing BMC power state, you can inspect `IpmiServerContext().bmc.powerstate`
For more details see server usage `ipmisim/ipmisim.py`

Testing with ipmitool:

    ipmitool -I lanplus -H localhost -p 9001 -R1 -U admin -P password chassis power status
