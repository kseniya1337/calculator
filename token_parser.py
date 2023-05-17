from tokenizer import Tokenizer


class Parser:
    def __init__(self, tokenizer: Tokenizer):
        self._tokenizer = tokenizer

    def run(self):
        result = self._addition()
        if self._tokenizer.current != 'eof':
            raise RuntimeError('Invalid math expression')
        return result

    def _addition(self):
        result = self._multiplication()
        while self._tokenizer.current in {'plus', 'minus'}:
            operator = self._tokenizer.current
            self._tokenizer.next()
            value = self._multiplication()
            if operator == 'plus':
                result += value
            else:
                result -= value
        return result

    def _multiplication(self):
        result = self._simple_value()
        while self._tokenizer.current in {'asterisk', 'slash'}:
            operator = self._tokenizer.current
            self._tokenizer.next()
            value = self._simple_value()
            if operator == 'asterisk':
                result *= value
            else:
                result /= value
        return result

    def _simple_value(self):
        if self._tokenizer.current == 'l_brace':
            self._tokenizer.next()
            result = self._addition()
            if self._tokenizer.current != 'r_brace':
                raise RuntimeError('Invalid math expression')
            self._tokenizer.next()
            return result
        return self._number()

    def _number(self):
        negative = False
        if self._tokenizer.current == 'minus':
            negative = True
            self._tokenizer.next()

        if not self._is_number_token(self._tokenizer.current):
            raise RuntimeError('Invalid math expression')

        number = self._tokenizer.current[1]
        if negative:
            number *= -1

        self._tokenizer.next()
        return number

    def _is_number_token(self, token):
        return isinstance(token, tuple) and token[0] == 'number'
