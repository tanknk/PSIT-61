"""War"""
import json
def main(attack, defense):
    """ Calculate power """
    result = 0
    attack.sort(reverse=True)
    defense.sort(reverse=True)
    for i in defense:
        for j in attack:
            if j > i:
                result += j
                attack.remove(j)
            break
    print(result)

main(json.loads(input()), json.loads(input()))
