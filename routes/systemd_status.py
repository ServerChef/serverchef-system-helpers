from utils.systemd_status import get_unit_status

def systemd_status(unit_name):
    status = get_unit_status(unit_name)

    return {
        "code": 0,
        "status": status.to_dict()
    }
