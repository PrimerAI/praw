from ....const import API_PATH


class DictableMixin:
    DICTABLES = []
    def to_dict(self):
        result = {}
        for key in self.DICTABLES:
            result[key] = getattr(self, key) # TODO: support methods as the key
        return result
