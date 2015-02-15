haproxy-status.py
======

A python script to display HAProxy status, by connecting to the management socket. This is useful in an environment where you cannot (easily) connect to HAProxy's HTTP status page.

## How to use

Ensure that the HAProxy [management socket is configured](http://cbonte.github.io/haproxy-dconv/configuration-1.5.html#9.2).


```bash
./haproxy-status.py [--socket /path/to/socket]
```
