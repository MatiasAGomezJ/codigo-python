def remove_html_markup(a):
    tag = False
    quote = False

    out = ''

    for c in a:
        if c == '<' and not quote:
            tag = True
        elif c == '>' and not quote:
            tag = False
        elif c == '"' or c == "'" and tag:
            quote = not quote
        elif not tag:
            out = out + c
    
    return out

print(remove_html_markup('"<b>foo</b>"'))