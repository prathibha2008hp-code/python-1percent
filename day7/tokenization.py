import tokenize
import io
tokens = tokenize.generate_tokens(io.StringIO("x = 10").readline)
for tok in tokens:
    print(tok)