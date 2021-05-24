from prometheus_client import Counter, Enum, Gauge

RX_PACKETS = Counter('bfd_rx_packets', 'Number of Rx packets', labelnames=['bfd_neighbor'])
TX_PACKETS = Counter('bfd_tx_packets', 'Number of Tx packets', labelnames=['bfd_neighbor'])
# BFD_STATE = Enum('bfd_conn_state', 'Current status of the BFD Session',
#                  states=['STATE_ADMIN_DOWN', 'STATE_DOWN', 'STATE_INIT', 'STATE_UP'])
BFD_STATE = Gauge('bfd_conn_state', 'Current status of the BFD Session', ['bfd_neighbor'])


def rx_count(func):
    def wrapper(*args, **kwargs):
        # print(args[0].remote)
        RX_PACKETS.labels(args[0].remote).inc()
        return func(*args, **kwargs)
    return wrapper


def tx_count(func):
    def wrapper(*args, **kwargs):
        # print(args[0].remote)
        TX_PACKETS.labels(args[0].remote).inc()
        return func(*args, **kwargs)
    return wrapper


# def bfd_state(state):
#     BFD_STATE.state(state)
def bfd_state(func):
    state = {
        0: 'STATE_ADMIN_DOWN',
        1: 'STATE_DOWN',
        2: 'STATE_INIT',
        3: 'STATE_UP'
    }

    def wrapper(*args, **kwargs):
        BFD_STATE.labels(args[0].remote).set(args[1])
        return func(*args, **kwargs)
    return wrapper
