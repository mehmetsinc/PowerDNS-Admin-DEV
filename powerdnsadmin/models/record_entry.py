class RecordEntry(object):
    """
    This is not a model, it's just an object
    which will store records entries from PowerDNS API
    """
    def __init__(self,
                 name=None,
                 type=None,
                 status=None,
                 ttl=None,
                 data=None,
                 maskedip01=None,
                 maskedip02=None,
                 maskedswitchstatus=None,
                 comment=None,
                 is_allowed_edit=False):
        self.name = name
        self.type = type
        self.status = status
        self.ttl = ttl
        self.data = data
        self.maskedip01 = maskedip01
        self.maskedip02 = maskedip02
        self.maskedswitchstatus = maskedswitchstatus
        self.comment = comment
        self._is_allowed_edit = is_allowed_edit
        self._is_allowed_delete = is_allowed_edit and self.type != 'SOA'

    def is_allowed_edit(self):
        return self._is_allowed_edit

    def is_allowed_delete(self):
        return self._is_allowed_delete
