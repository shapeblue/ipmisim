# ipmisim

IPMI simulator based on [Conpot](http://conpot.org/) and `pyghmi`.
Created for supporting feature testing in Apache CloudStack.

Default users and passwords:

    admin : password
    opuser : oppassword
    user : userpassword


Installation:

    pip install ipmisim


Running:

    ipmisim 3000  # Runs on custom port 3000, else 9001 by default

For, usage in integration tests you can do `from ipmisim.ipmisim import IpmiServer`.
For more details see ipmisim/ipmisim.py

Testing with ipmitool:

    ipmitool -I lanplus -H localhost -p 9001 -R1 -U admin -P password chassis power status
