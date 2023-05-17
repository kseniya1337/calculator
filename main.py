from reader import Reader
from tokenizer import Tokenizer
from token_parser import Parser

input_string = input('Enter a mathematical expression: ')
reader = Reader(input_string)
tokenizer = Tokenizer(reader)
parser = Parser(tokenizer)
print(parser.run())
