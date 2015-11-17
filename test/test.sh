#!/bin/bash
set -e

echo "Bring up test infrastructure"
docker-compose up -d

# Get haproxy container ID
ID=$(docker ps | grep tutum/haproxy | awk '{print $1}')

echo "Waiting for haproxy to check backend status"
sleep 5

echo "Run haproxy-status container"
docker run --rm --volumes-from $ID barwell/haproxy-status /run/haproxy.stats

echo "Shut down infrastructure"
docker-compose stop
docker-compose rm -f

echo "Done"
