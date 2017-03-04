__all__ = ['SystemdUnitStatus', 'UsedPort']


class BaseModel(object):
    pass


class SystemdUnitStatus(BaseModel):
    active = True
    status = "active"

class UsedPort(BaseModel):
    port = 0
    program_name = "/dev/null"
    pid = 10
    protocol = "tcp6"
    bind_address = "0.0.0.0"
