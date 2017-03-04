from models import UsedPort
import psutil

def get_used_ports():
    all_conns = psutil.net_connections()

    listening = [UsedPort.from_ps_util_sconn(conn)
                 for conn in all_conns
                 if conn.status == 'LISTEN' ]

    return listening
