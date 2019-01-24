""" Additive """
import math as m
def main():
    """ output """
    print((m.sin(m.radians(90))+m.sin(m.radians(60))**2)\
        /(m.cos(m.radians(245**2))+m.cos(m.radians(45+135))))
    print((m.factorial(16)*m.factorial(4))/m.factorial(8))
    print((15+25)/(m.sqrt(((25-12)**2)+((12-15)**2))))
    print(m.log10(1234**4))
    print((m.log(4234, 5) + m.log(8191, 2) + 71*m.log10(156154)) / \
        (m.log(777, 7) - m.log(888, 8) - m.log(999, 9)))

main()
