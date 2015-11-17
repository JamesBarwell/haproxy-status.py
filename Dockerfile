FROM gliderlabs/alpine:3.1
MAINTAINER barwell

RUN apk-install python

WORKDIR /app
ADD haproxy-status.py /app/

ENTRYPOINT ["/app/haproxy-status.py"]
