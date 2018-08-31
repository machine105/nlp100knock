import plyvel
import sys

def numArea(area):
    db = plyvel.DB('kvs.ldb', create_if_missing=False)
    cnt = 0
    for key, val in db:
        if val == area:
            cnt += 1
    return cnt

if __name__ == '__main__':
    print numArea('Japan')
