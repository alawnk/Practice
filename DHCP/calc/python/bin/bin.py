import os,sys
BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASEDIR)

from my_module import main
if __name__ == '__main__':
    main.run()
    print(__name__)
    print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))