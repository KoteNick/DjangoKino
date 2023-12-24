import json


def strToList(string: str) -> list:
    s = "[" + string + "]"
    return json.loads(s)


def listToStr(l: list, nospaces = False) -> str:
    s = str(l)
    if nospaces:
        s = s.replace(' ', '')
    return s[1:-1]

if __name__=="__main__":
    print(listToStr(list(range(1, 21)), True))
