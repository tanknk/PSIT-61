"""Filter"""
import json
def main():
    """Sort ID and Check all values"""
    dic = json.loads(input())
    key_filter = float(input())
    value = []
    idstudent = []
    for i in dic:
        if dic[i] >= key_filter:
            value.append(dic[i])
    for keys, values in dic.items():
        if key_filter <= values:
            idstudent.append(int(keys))
    idstudent.sort()
    if idstudent == []:
        print('Nope')
    for j in range(len(idstudent)):
        print(idstudent[j], '%.2f'%dic.get(str(idstudent[j])), sep='\t')
main()
