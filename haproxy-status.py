#!/usr/bin/python

import argparse
import socket
import csv
import sys

RECV_SIZE = 1024
PRINT_COLS = {
    'pxname': 0,
    'svname': 1,
    'status': 17,
}
DEBUG = False

def execute(cmd, socket='/var/run/haproxy.sock'):
    try:
        client = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    except:
        print "Could not connect to socket: %s" % socket
        sys.exit(1)
    client.connect(socket)
    client.sendall('%s\n' % cmd)
    result = ''
    buf = ''
    buf = client.recv(RECV_SIZE)
    while buf:
        result += buf
        buf = client.recv(RECV_SIZE)
    client.close()
    return result

def get_stats(socket):
    if DEBUG:
        testdata_file = open('./testdata', 'r')
        raw_stats = testdata_file.read()
    else:
        raw_stats = execute('show stat', socket)
    return csv.reader(raw_stats.strip().split('\n'), delimiter=',')

def split_host(line):
    return line.split(',')

def is_host(line):
    svname = line[1]
    is_host = svname != "FRONTEND" and svname != "BACKEND"
    return is_host

def get_hosts(stats):
    return filter(is_host, stats)

def get_headers():
    return ['svname', 'pxname', 'status']

def print_table(table):
    table = strip_table(table)
    table.insert(0, get_headers())
    table = map(insert_table_spaces, table)

    col_widths = [max(len(x) for x in col) for col in zip(*table)]
    for row in table:
        print_row = ''
        for i in range(0, len(row)):
            print_row += row[i].ljust(col_widths[i])
        print print_row

def strip_table(table):
    kept = []
    for row in table:
        kept_row = []
        for i, item in enumerate(row):
            if i in PRINT_COLS.values():
                kept_row.append(item)
        kept.append(kept_row)
    return kept

def insert_table_spaces(row):
    rtn = []
    for i, item in enumerate(row):
        if i > 0:
            rtn.append(' | ' + item)
        else:
            rtn.append(item)
    return rtn

def main(socket):
    stats = get_stats(socket)
    hosts = get_hosts(stats)
    print_table(hosts)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Get HAProxy status information')
    parser.add_argument('--socket', help='path to haproxy socket', nargs='?', default='/var/run/haproxy.socket')

    args = parser.parse_args()
    main(args.socket)
