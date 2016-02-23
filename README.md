# ipmisim

IPMI simulator based on [Conpot](http://conpot.org/) and `pyghmi`.
Created for supporting feature testing in Apache CloudStack.

Default users and passwords:

    admin : password
    opuser : oppassword
    user : userpassword


Installation:

    pip install ipmisim


Usage in integration tests:

    from ipmisim import IpmiServer

    ipmi_server = IpmiServer(9001)
    ipmi_server.start('0.0.0.0', 9001)


Testing with ipmitool:

    ipmitool -I lanplus -H localhost -p 9001 -R1 -U admin -P password chassis power status
