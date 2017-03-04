from utils.ports_used import get_used_ports

def port():
    ports = [x.to_dict() for x in get_used_ports()]

    return {
        "code": 0,
        "items": ports
    }
