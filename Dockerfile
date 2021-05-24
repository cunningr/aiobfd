FROM python:3.8-slim

RUN python -m pip install \
    bitstring \
    prometheus_client \
    json_log_formatter

COPY aiobfd/ /opt/aiobfd/aiobfd
COPY aiobfd_testing.py /opt/aiobfd/

WORKDIR /opt/aiobfd/