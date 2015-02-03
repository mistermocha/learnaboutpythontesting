from classlib import SampleClass
import sys

if __name__ == '__main__':
    sc = SampleClass()
    sc.set_value(sys.argv[1])
    print(sc)
