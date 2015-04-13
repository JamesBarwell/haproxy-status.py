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

The output table is designed to be easily filtered by grep.

## Example output

```bash
$ /opt/haproxy-status.py /var/run/haproxy1.sock /var/run/haproxy2.sock
socket                 | # pxname | svname        | status | weight | chkdown | lastchg | rate | rate_max | check_status | rtime
/var/run/haproxy1.sock | web      | live-web-01   | UP     | 1      | 1       | 165     | 0    | 0        | L7OK         | 0
/var/run/haproxy1.sock | web      | live-web-02   | UP     | 1      | 0       | 2534    | 0    | 0        | L7OK         | 0
/var/run/haproxy1.sock | api      | live-api-01   | UP     | 1      | 2       | 165     | 0    | 0        | L7OK         | 0
/var/run/haproxy1.sock | api      | live-api-02   | UP     | 1      | 0       | 2534    | 0    | 0        | L7OK         | 0
/var/run/haproxy1.sock | int      | live-int-01   | UP     | 1      | 1       | 164     | 0    | 0        | L4OK         | 0
/var/run/haproxy1.sock | int      | live-int-02   | UP     | 1      | 0       | 2534    | 0    | 0        | L4OK         | 0
/var/run/haproxy1.sock | admin    | live-admin-01 | UP     | 1      | 2       | 163     | 0    | 0        | L7OK         | 0
/var/run/haproxy1.sock | admin    | live-admin-02 | UP     | 1      | 0       | 2534    | 0    | 0        | L7OK         | 0
socket                 | # pxname | svname        | status | weight | chkdown | lastchg | rate | rate_max | check_status | rtime
/var/run/haproxy2.sock | web      | live-web-01   | UP     | 1      | 1       | 165     | 0    | 0        | L7OK         | 0
/var/run/haproxy2.sock | web      | live-web-02   | UP     | 1      | 0       | 2534    | 0    | 0        | L7OK         | 0
/var/run/haproxy2.sock | api      | live-api-01   | UP     | 1      | 2       | 165     | 0    | 0        | L7OK         | 0
/var/run/haproxy2.sock | api      | live-api-02   | UP     | 1      | 0       | 2534    | 0    | 0        | L7OK         | 0
/var/run/haproxy2.sock | int      | live-int-01   | UP     | 1      | 1       | 164     | 0    | 0        | L4OK         | 0
/var/run/haproxy2.sock | int      | live-int-02   | UP     | 1      | 0       | 2534    | 0    | 0        | L4OK         | 0
/var/run/haproxy2.sock | admin    | live-admin-01 | UP     | 1      | 2       | 163     | 0    | 0        | L7OK         | 0
/var/run/haproxy2.sock | admin    | live-admin-02 | UP     | 1      | 0       | 2534    | 0    | 0        | L7OK         | 0
```
