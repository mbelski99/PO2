def __repr__(self):
    values = ",".join (f"{k.strip("_")}={v!r}" for k,v in self.__dict__.items())
    return f"{type(self).__name__}({values}})"

print(repr(x))