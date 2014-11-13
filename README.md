RESTful access to ISC DHCPd leases
==================================

In some environents, such as when cloning VMs which do not have vm-tools installed, one might be able to retrieve a system’s MAC address but not its configured IP address.  In those cases, its helpful to have a simple way to lookup the IP address that was assigned to that MAC by the DHCP server.

There are 2 versions of this app included in this repository: a standalone server and a WSGI application.  As I have a web server already running on my DHCP server, I will primarily be maintaining the WSGI version.

Standalone
----------

The standalone app may be started from the commandline and will listen for HTTP connections on port 8080.

    ./standalone/dhcpd_leases.py
    http://0.0.0.0:8080/

WSGI
----

To setup the WSGI version:

    git clone https://github.com/jerearista/dhcpd_leases_info.git
    cd dhcpd_leases_info

    install -d /var/www/dhcpd_leases/wsgi
    install dhcpd_leases/wsgi/* /var/www/dhcpd_leases/wsgi/
    install -d /var/www/dhcpd_leases/static
    install dhcpd_leases/static/* /var/www/dhcpd_leases/static/
    install etc/httpd/conf.d/dhcp_leases.conf /etc/httpd/conf.d/
    sudo systemctl restart httpd

Example
-------

Request the IP of an active lease:

    GET http://<dhcp_server>/dhcpd_leases/ip_by_mac/00:50:56:9b:f5:28

Returns:

    192.0.2.10


