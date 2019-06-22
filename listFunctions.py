def merge(lList, rList, key, reverse):

    final = []

    while lList or rList:

        if len(lList) and len(rList):
            
            if key != None:

                if key == "meanRat":
                    left = lList[0].meanRat
                    right = rList[0].meanRat
                elif key == "count":
                    left = lList[0].count
                    right = rList[0].count
            else:
                left = lList[0]
                right = rList[0]
           
            if reverse:
                if left > right:
                    final.append(lList.pop(0)) 
                else: final.append(rList.pop(0))

            else:
                if left < right:
                    final.append(lList.pop(0)) 
                else: final.append(rList.pop(0))

        if not len(lList):
             if len(rList): final.append(rList.pop(0))

        if not len(rList):
           if len(lList): final.append(lList.pop(0))

    return final


def mergesort(list, key = None, rev = True):

    if len(list) <= 1: return list
    mid = int(len(list)/2)
    return merge(mergesort(list[:mid], key, rev), mergesort(list[mid:], key, rev), key, rev)
