Discover Constraints
====================

WSGI middleware for OpenStack Swift that makes cluster constraints
discoverable. This middleware responds to GET requests to /.constraints and
returns a json-encoded mapping of the cluster constraints.

----

INSTALL
=======

1) Download the source and run `sudo python ./setup.py install` or build a
package and install it.

2) Add to your proxy-server.conf::

    [pipeline:main]
    pipeline = dc proxy-server

    [filter:dc]
    use = egg:discover_constraints#discover_constraints

3) Restart your proxy server
