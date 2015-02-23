haproxy-status.py
======

A python script to display HAProxy status, by connecting to the management socket.

## Use cases

This script could be of use in the following circumstances:
* in an environment where it is not easy to connect to the HAProxy HTTP status page.
* when multiple processes are being run on the same host, as only one process will bind to the port and serve the HTTP status page, leaving the others invisible.
* if running a batch command against multiple HAProxy hosts (e.g. via Ansible), this allows all information to be easily collated.

## How to use

Ensure that the HAProxy [management socket is configured](http://cbonte.github.io/haproxy-dconv/configuration-1.5.html#9.2). You will need to configure one management socket per process.


```bash
./haproxy-status.py /var/run/haproxy.sock [/var/run/haproxy2.sock [/var/run/haproxy3.sock]]
```
