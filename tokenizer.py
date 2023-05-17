from reader import Reader


class Tokenizer:
    def __init__(self, reader: Reader) -> None:
        self._current = ''
        self._reader = reader
        self.next()

    def next(self):

        while self._reader.current == ' ':
            self._reader.next()

        if self._reader.current == '-':
            self._current = 'minus'
            self._reader.next()

        elif self._reader.current == '+':
            self._current = 'plus'
            self._reader.next()

        elif self._reader.current == '*':
            self._current = 'asterisk'
            self._reader.next()

        elif self._reader.current == '/':
            self._current = 'slash'
            self._reader.next()

        elif self._reader.current == '(':
            self._current = 'l_brace'
            self._reader.next()

        elif self._reader.current == ')':
            self._current = 'r_brace'
            self._reader.next()

        elif self._reader.current.isdigit():
            number = ''
            while self._reader.current.isdigit():
                number += self._reader.current
                self._reader.next()
            if self._reader.current == '.':
                number += self._reader.current
                self._reader.next()
                if self._reader.current.isdigit():
                    while self._reader.current.isdigit():
                        number += self._reader.current
                        self._reader.next()
                else:
                    raise RuntimeError('Invalid number')
            self._current = ('number', float(number))

        elif self._reader.current is self._reader.EOF:
            self._current = 'eof'

    @property
    def current(self):
        return self._current
