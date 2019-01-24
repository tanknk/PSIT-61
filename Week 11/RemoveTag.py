"""RemoveTag"""
def main():
    """Find < and > then remove"""
    text = input()
    while "<" in text:
        pos1 = text.find("<")
        pos2 = text.find(">")
        text = text.replace(text[pos1:pos2+1], " ")
    ans = text.split()
    print(ans)

main()
