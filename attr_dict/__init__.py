class AttrDict(dict):
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self

    @classmethod
    def recursive_walk(cls, d): 
        self = cls(d)
        for key, value in self.items():
            if type(value) is dict: 
                self[key] = cls.recursive_walk(value)
        return self

