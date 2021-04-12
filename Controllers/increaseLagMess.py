from Controllers import getLagMess, LagMessBefore,format
import logging

#  Search topics in excel file and test link have more than " increment " lag message (ex: 1000)
def alertOverMess(increment=0, allLagMess=getLagMess.countMesLag()):
    try:
        oldLagMess = LagMessBefore.readMess()
        increment = int(increment)
        comparingMess = list()
        differenceRes = [x for x in allLagMess + oldLagMess if x not in oldLagMess]
        for i in differenceRes:
            dif = 0
            sCut = list()
            sCut.extend(i.split())
            if int(sCut[-2]) >= increment:
                l4 = sCut[0]
                sCut2 = list()
                for d in oldLagMess:
                    sCut2.extend(d.split())
                    if sCut2[0] == sCut[0]:
                        if (int(sCut[-2]) - int(sCut2[-2])) >= increment:
                            result = ' '.join(sCut)
                            comparingMess.append(result)
                            sCut2.clear()
                            break
                        else:
                            sCut2.clear()
                            break
                    elif d.find(l4) == -1:
                        dif = dif + 1
                    if dif >= len(oldLagMess):
                        result2 = ' '.join(sCut)
                        comparingMess.append(result2)
                        sCut2.clear()
                        break
            sCut.clear()
        if len(differenceRes) > 0:
            LagMessBefore.saveMess(allLagMess)
            comparingMess = format.strokeRedNumLagMess(comparingMess)
        return comparingMess
    except Exception as e:
            logging.basicConfig(filename='../static/increaseLagMess.log', filemode='a+', format='%(name)s - %(levelname)s - %(message)s')
            logging.warning(e)
            print("increaseLadMEss.py alertOverMess expection:", e)

if __name__ == '__main__':
    alertOverMess()