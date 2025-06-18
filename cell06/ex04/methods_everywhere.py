import sys

def shrink(s):
    print(s[8])

def enlarge(s):
    print(s + 'Z' * (8 - len(s)))

for arg in sys.argv[1:]:
    if len(arg) > 8:
        enlarge(arg)
    elif len(arg) < 8:
        enlarge(arg)
    else:
        print(arg)