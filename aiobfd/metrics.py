from prometheus_client import Counter, Gauge, Info

CONFIG = Info('bfd_client_config', 'BFD client configuration settings')
RX_PACKETS = Counter('bfd_rx_packets', 'Number of Rx packets', labelnames=['local_ip', 'remote_ip'])
TX_PACKETS = Counter('bfd_tx_packets', 'Number of Tx packets', labelnames=['local_ip', 'remote_ip'])
# BFD_STATE = Enum('bfd_conn_state', 'Current status of the BFD Session',
#                  states=['STATE_ADMIN_DOWN', 'STATE_DOWN', 'STATE_INIT', 'STATE_UP'])
BFD_STATE = Gauge('bfd_conn_state', 'Current status of the BFD Session', ['local_ip', 'remote_ip'])


def client_config(local, remotes, tx_interval, rx_interval, detect_mult):
    CONFIG.info({'local_ip': local, 'remote_ip': ','.join(remotes), 'tx_interval': str(tx_interval), 'rx_interval': str(rx_interval), 'detect_mult': str(detect_mult)})


# The functions below decorate methods from the aiobfd.session.Session class
def rx_count(func):
    def wrapper(*args, **kwargs):
        RX_PACKETS.labels(args[0].local, args[0].remote).inc()
        return func(*args, **kwargs)
    return wrapper


def tx_count(func):
    def wrapper(*args, **kwargs):
        TX_PACKETS.labels(args[0].local, args[0].remote).inc()
        return func(*args, **kwargs)
    return wrapper


def bfd_state(func):
    state = {
        0: 'STATE_ADMIN_DOWN',
        1: 'STATE_DOWN',
        2: 'STATE_INIT',
        3: 'STATE_UP'
    }

    def wrapper(*args, **kwargs):
        BFD_STATE.labels(args[0].local, args[0].remote).set(args[1])
        return func(*args, **kwargs)
    return wrapper
