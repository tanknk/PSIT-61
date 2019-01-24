"""input"""
def main():
    """output"""
    numa = float(input())
    numb = float(input())
    numc = float(input())
    numd = float(input())
    print(float(func1(func1(numa))))
    print(float(func2(func1(numa-numb))))
    print(float(func3((func1(numa+numb)), func1(numa+numc), func2(func1(numd**2)))))
    print(float(func4(func3(func1(numa+numb), func1(numa-numc), func2(func1(numd**2))),\
    	func2((func1(numa-numb))), func1(func1(func1(func1(func1(numc))))), (numd**8))))

def func1(x_1):
    """input"""
    return 2*x_1
def func2(x_1):
    """input"""
    return (3*(x_1**4))-(x_1**3)+2*(x_1**2)+10
def func3(x_1, y_1, z_1):
    """input"""
    return ((z_1+x_1)**2)-(x_1*y_1)+(y_1**2)
def func4(a_1, b_1, c_1, d_1):
    """input"""
    return ((a_1**2)+(b_1**2)-(c_1**2))/((d_1**2)-(2*(a_1*d_1))+(2*a_1))

main()
