# format message
import logging


def strokeRedNumLagMess(newLagMess):
    try:
        oldLagMess = list()
        sCut = list()
        for i in newLagMess:
            strings = str(i)
            sCut.extend(strings.split())
            sCut.pop(-3)
            sCut.pop(-3)
            sCut[-2] = "`" + sCut[-2] + "`"
            result = ''
            for s in sCut:
                result += ' ' + s
            result = result.strip(')')
            oldLagMess.append(result)
            sCut.clear()
            return oldLagMess
    except Exception as e:
            logging.basicConfig(filename='../static/format.log', filemode='a+', format='%(name)s - %(levelname)s - %(message)s')
            logging.warning(e)
            print("Format.py strokeRedNumLagMess expection: ", e)

def breakLine(lagTopic):
    try:
        braekLineA = ''
        for s in lagTopic:
            braekLineA += '\n' + s + '\n'
        return braekLineA
    except Exception as e:
            logging.basicConfig(filename='../static/format.log', filemode='a+', format='%(name)s - %(levelname)s - %(message)s')
            logging.warning(e)
            print("Format.py breakLine expection: ", e)

