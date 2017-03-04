import json
import psutil

__all__ = ['SystemdUnitStatus', 'Use']


class BaseModel(object):
    def to_dict(self):
        return {name: getattr(self, name) for name in self.get_keys()}

    def get_keys(self):
        return [name for name in dir(self) if
            not name.startswith('__')
            and not callable(getattr(self, name))]

    def __init__(self, **kwargs):
        keys = self.get_keys()
        for kwarg, value in kwargs.items():
            if kwarg in keys:
                setattr(self, kwarg, value)

    def __repr__(self):
        print(json.dumps(self.to_dict()))

class SystemdUnitStatus(BaseModel):
    active = True
    status = "active"

class UsedPort(BaseModel):
    port = 0
    program_name = "/dev/null"
    pid = 10
    protocol = "tcp6"
    bind_address = "0.0.0.0"

    @classmethod
    def from_ps_util_sconn(cls, conn):
        ret = cls()

        ret.program_name = psutil.Process(conn.pid).name()
        ret.bind_address, ret.port = conn.laddr
        ret.pid = conn.pid

        return ret

