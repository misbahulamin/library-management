class Aircraft:
    def __init__(self, make, code, type, flight_range):
        self.make = make
        self.code = code
        self.type = type
        self.flight_range = flight_range
    def get_make(self):
        return self.make
    def __repr__(self) -> str:
        return f'Aricraft make : {self.make} Code: {self.code} Type: {self.type} Flight Range : {self.flight_range}'
    