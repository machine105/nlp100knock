import plyvel
import sys

def getArea(name):
    db = plyvel.DB('kvs.ldb', create_if_missing=False)
    return db.get(name)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'missing argument'
        sys.exit()
    print('area: %s'%(getArea(sys.argv[1]), ))
