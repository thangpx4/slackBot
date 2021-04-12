from Controllers import getLagMess
import logging

def saveMess(newString=getLagMess.countMesLag()):
    global f
    try:
        f = open("../static/lagMessBefore.txt", "w")
        for i in newString:
            i = str(i) + ";"
            f.write(i)
    except Exception as e:
        logging.basicConfig(filename='../static/lagMessBefore.log', filemode='a+',
                            format='%(name)s - %(levelname)s - %(message)s')
        logging.warning(e)
        print("LagMessBefore.py saveMess expection", e)
    finally:
        f.close()


def readMess():
    try:
        f = open("../static/lagMessBefore.txt", "r")
        oldMess2 = f.read()
        oldMess2 = oldMess2.split(";")
        return oldMess2
    except Exception as e:
        logging.basicConfig(filename='../static/lagMessBefore.log', filemode='a+',
                            format='%(name)s - %(levelname)s - %(message)s')
        logging.warning(e)
        print("LagMessBefore.py readMess expection: ", e)

if __name__ == '__main__':
    saveMess()
    readMess()
