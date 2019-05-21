import re


def extract_tokens(text):
    pat = re.compile(r'".*"|[a-zA-Z]+|\d+|[\(\)^v/\+\-\*\.]|[:=<>~]{1,2}|\s|.+')

    return re.findall(pat, text)
