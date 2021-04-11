from Token import tokens

class PrePro():

    def __init__(self):
        return

    def filter(self, cf):
        
        for token in tokens:
            if token.value.match('/'): token_div = token
            elif token.value.match('*'): token_mult = token

        open_comment = None
        close_comment = None
        cut_in = []
        for e in range(len(cf)):
            if open_comment is None:
                if token_div.value.match(cf[e]) and e != (len(cf) - 1):
                    if token_mult.value.match(cf[e+1]):
                        open_comment = e
            
            elif close_comment is None:
                if token_mult.value.match(cf[e]) and e != (len(cf) - 1):
                    if token_div.value.match(cf[e+1]):
                        close_comment = e + 2

            if open_comment is not None and close_comment is not None:
                cut_in.append((open_comment, close_comment))
                open_comment = None
                close_comment = None

        for e in range(len(cut_in)):
            pos = cut_in.pop()
            cf = cf[0:pos[0]] + cf[pos[1]:]

        cf = cf.strip()
        
        return cf
        