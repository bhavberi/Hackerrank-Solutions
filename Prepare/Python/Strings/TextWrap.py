

def wrap(string, max_width):
    l=textwrap.wrap(string,max_width)
    s=''
    for i in l:
        s+=i+'\n'
    
    return s

