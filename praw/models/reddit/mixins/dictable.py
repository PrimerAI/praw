from ....const import API_PATH


class DictableMixin:
    DICTABLES_METHODS = []
    def to_dict(self):
        result = {}
        for key in self.DICTABLES_METHODS:
            result[key] = getattr(self, key) # TODO: support methods as the key
        return result
