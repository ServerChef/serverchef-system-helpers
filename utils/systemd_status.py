from models import SystemdUnitStatus
from exceptions import SystemdUnitNotFoundException
import subprocess

def get_unit_status(unit_name) -> SystemdUnitStatus:
    ret = SystemdUnitStatus()

    process = subprocess.Popen("systemctl status {} | grep Active | egrep -o \'\(.+\)\'".format(unit_name), shell=True, stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
    result = process.communicate()[0].decode('utf-8')

    if 'not be found' in result:
        raise SystemdUnitNotFoundException(result)

    result = result[1:-2]

    if result == 'running':
        ret.active = True

    ret.status = result

    return ret
