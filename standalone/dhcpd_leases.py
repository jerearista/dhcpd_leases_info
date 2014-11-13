#!/usr/bin/env python
"""Simple RESTful interface to request the IP leased to a given MAC address

    Example:
        GET http://<dhcp_server>:8080/ip_by_mac/00:50:56:9b:f5:28

    Returns:
        a.b.c.d

"""

# Reference:
# http://www.dreamsyssoft.com/blog/blog.php?/archives/6-Create-a-simple-REST-web-service-with-Python.html
# http://webpy.org/
# https://github.com/MartijnBraam/python-isc-dhcp-leases

leasefile = "/var/lib/dhcpd/dhcpd.leases"

import web
from isc_dhcp_leases.iscdhcpleases import IscDhcpLeases  # Lease and IscDhcpLeases

# For SSL support:
#from web.wsgiserver import CherryPyWSGIServer
#CherryPyWSGIServer.ssl_certificate = "/path/to/ssl_certificate"
#CherryPyWSGIServer.ssl_private_key = "/path/to/ssl_private_key"

urls = (
    '/ip_by_mac/(.*)', 'get_ip_by_mac',
)

app = web.application(urls, globals())

leases = IscDhcpLeases(leasefile)
cur_leases = leases.get_current()

class get_ip_by_mac:
    def GET(self, mac):
        if mac not in cur_leases.keys():
            return "None"
        this_lease = cur_leases[mac]
        return str(this_lease.ip)

if __name__ == "__main__":
    app.run()
