#
# Code from:
# http://rosettacode.org/wiki/Sierpinski_triangle#Python
#

def sierpinski(n):
    d = ["*"]
    for i in xrange(n):
        sp = " " * (2 ** i)
        d = [sp+x+sp for x in d] + [x+" "+x for x in d]
    return d
 
if __name__ == "__main__":
    print "\n".join(sierpinski(4))
