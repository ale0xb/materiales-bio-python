def inv(secuencia):
    return secuencia[::-1]

def comp(secuencia):
    ret_str = ''
    secuencia = secuencia.upper()
    for c in secuencia:
        if c == 'A':
            ret_str += 'T'
        elif c == 'C':
            ret_str += 'G'
        elif c == 'T':
            ret_str += 'A'
        elif c == 'G':
            ret_str += 'C'
        else:
            ret_str += c
     
    return ret_str
            
def inv_comp(secuencia):
    return comp(inv(secuencia))