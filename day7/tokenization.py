import tokenize
import io
tokens = tokenize.generate_tokens(io.StringIO("x = 10").readline)
for tok in tokens:
    print(tok)
    #output
    #  TokenInfo(type=55 (OP), string='=', start=(1, 2), end=(1, 3), line='x = 10')
""" TokenInfo(type=2 (NUMBER), string='10', start=(1, 4), end=(1, 6), line='x = 10')
TokenInfo(type=4 (NEWLINE), string='', start=(1, 6), end=(1, 7), line='x = 10')
TokenInfo(type=0 (ENDMARKER), string='', start=(2, 0), end=(2, 0), line='') """