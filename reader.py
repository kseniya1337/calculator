class Reader:
    EOF = '\0'

    def __init__(self, string):
        self._string = string
        self._position = 0

    def next(self):
        self._position += 1

    @property
    def current(self):
        if self._position >= len(self._string):
            return self.EOF
        return self._string[self._position]

    @property
    def position(self):
        return self._position
