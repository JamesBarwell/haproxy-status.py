haproxy-status.py
======

A python script to display HAProxy status, by connecting to the management socket.

## Use cases

This script could be of use in the following circumstances:
* in an environment where it is not easy to connect to the HAProxy HTTP status page.
* when multiple HAProxy processes are run on the same host. In this case, only one process will bind to the port and serve the HTTP status page, which makes it difficult to view the status of the other processes.
* if running a batch command against multiple HAProxy hosts (e.g. via a config management tool), this allows all information to be easily collated and grepped.

## How to use

Ensure that the HAProxy [management socket is configured](http://cbonte.github.io/haproxy-dconv/configuration-1.5.html#9.2). You will need to configure one management socket per process.

```bash
./haproxy-status.py /var/run/haproxy.sock [/var/run/haproxy2.sock [/var/run/haproxy3.sock]]
```

## Example output

```bash
$ /opt/haproxy-status.py /var/run/haproxy1.sock /var/run/haproxy2.sock
# pxname | svname      | status | weight | chkdown | lastchg | rate | rate_max | check_status | rtime
web      | LIVE-WEB-01 | UP     | 1      | 0       | 163     | 0    | 0        | L7OK         | 0
web      | LIVE-WEB-02 | UP     | 1      | 0       | 163     | 0    | 0        | L7OK         | 0
api      | LIVE-API-01 | DOWN   | 1      | 1       | 163     | 0    | 0        | L4CON        | 0
api      | LIVE-API-02 | DOWN   | 1      | 1       | 163     | 0    | 0        | L4CON        | 0
# pxname | svname      | status | weight | chkdown | lastchg | rate | rate_max | check_status | rtime
web      | LIVE-WEB-01 | UP     | 1      | 0       | 163     | 0    | 0        | L7OK         | 0
web      | LIVE-WEB-02 | UP     | 1      | 0       | 163     | 0    | 0        | L7OK         | 0
api      | LIVE-API-01 | DOWN   | 1      | 1       | 163     | 0    | 0        | L4CON        | 0
api      | LIVE-API-02 | DOWN   | 1      | 1       | 163     | 0    | 0        | L4CON        | 0
```
