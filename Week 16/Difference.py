"""Difference"""
import json
def main(lis_1, lis_2):
    """Test"""
    result = []
    for i in range(len(lis_1)):
        if lis_1[i] not in lis_2:
            result.append(lis_1[i]+' '+str(lis_1.count(lis_1[i])))
        elif lis_1[i] in lis_2:
            if lis_1.count(lis_1[i]) == lis_2.count(lis_1[i]):
                pass
            else:
                nub = lis_1.count(lis_1[i]) - lis_2.count(lis_1[i]) if lis_1.count(lis_1[i])\
                 > lis_2.count(lis_1[i]) else lis_2.count(lis_1[i]) - lis_1.count(lis_1[i])
                result.append(lis_1[i]+' '+str(nub))
    for i in range(len(lis_2)):
        if lis_2[i] not in lis_1:
            result.append(lis_2[i]+' '+str(lis_2.count(lis_2[i])))
        elif lis_2[i] in lis_1:
            if lis_1.count(lis_2[i]) == lis_2.count(lis_2[i]):
                pass
            else:
                nub = lis_1.count(lis_2[i]) - lis_2.count(lis_2[i]) if lis_1.count(lis_2[i]) \
                > lis_2.count(lis_2[i]) else lis_2.count(lis_2[i]) - lis_1.count(lis_2[i])
                result.append(lis_2[i]+' '+str(nub))
    result = sorted(list(set(result)))
    if sorted(lis_1) == sorted(lis_2):
        print('ONAJI DAYO!')
    else:
        print(*result, sep='\n')
main(json.loads(input()), json.loads(input()))
