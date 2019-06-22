def merge(lList, rList, byRatings, reverse):

    final = []

    while lList or rList:

        if len(lList) and len(rList):
            
            if byRatings == True:
                left = lList[0].meanRat
                right = rList[0].meanRat
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


def mergesort(list, byRat = False, rev = False):

    if len(list) <= 1: return list
    mid = int(len(list)/2)
    return merge(mergesort(list[:mid], byRat, rev), mergesort(list[mid:], byRat, rev), byRat, rev)
