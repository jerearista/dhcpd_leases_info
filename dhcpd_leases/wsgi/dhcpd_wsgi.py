#!/usr/bin/env python
"""Simple RESTful interface to request the IP leased to a given MAC address

    Sample Apache Configuration:
        LoadModule wsgi_module modules/mod_wsgi.so
        WSGIScriptAlias /dhcpd_leases /var/www/dhcpd_leases/wsgi/dhcpd_wsgi.py/
        AddType text/html .py

    Example:
        GET http://<dhcp_server>/dhcpd_leases/ip_by_mac/00:50:56:9b:f5:28

    Returns:
        a.b.c.d

"""

# References:
# http://www.dreamsyssoft.com/blog/blog.php?/archives/6-Create-a-simple-REST-web-service-with-Python.html
# http://webpy.org/
# https://github.com/MartijnBraam/python-isc-dhcp-leases

import web
from isc_dhcp_leases.iscdhcpleases import IscDhcpLeases

leasefile = "/var/lib/dhcpd/dhcpd.leases"

urls = (
    '/ip_by_mac/(.*)', 'get_ip_by_mac',
)

leases = IscDhcpLeases(leasefile)
cur_leases = leases.get_current()

class get_ip_by_mac:
    def GET(self, mac):
        if mac not in cur_leases.keys():
            return "None"
        this_lease = cur_leases[mac]
        return str(this_lease.ip)

application = web.application(urls, globals()).wsgifunc()
