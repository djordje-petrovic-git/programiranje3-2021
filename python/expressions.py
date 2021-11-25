"""Demonstrates how operators and expressions work in Python.
"""

from settings import *    #ovim smo iz settings.py uveli neko podesavanje


def demonstrate_arithmetic_operators():
    """Working with arithmetic operators.
    Arithmetic operators in Python are pretty much the same as in other programming languages.
    The integer division operator: //  OPERATOR CELOBROJNOG DELJENJA
    """

    print((45 // 12) % 3 -234)


def demonstrate_relational_operators():
    """Working with relational operators.
    - simple comparisons
    - comparing dates (== vs. is)
    - comparing dates (>, <, etc. with dates)
    - None in comparisons, type(None)
    """

    print(12 > 34)
    print()

    if 12 > 34:
        print(True)
    else:
        print(False)
    if 0:
        print(True)
    else:
        print(False)
    print()

    from datetime import date
    d1 = date(1971,10,11)
    d2 = date(1971,10,11)
    if(d1 > d2):
        print('D1 > D2')
    else:
        print('D1 < D2')
    print(d1 == d2) # POREDJENJE SADRZAJA
    print(id(d1) == id(d2)) # POREDJENJE ADRESA  id()
    print(id(d2), id(d1))

    print(type(None))
    print()

def demonstrate_logical_operators(): # LOGICKI OPERATORE
    """Working with logical operators.
    - logical operations with True, False and None
    - logical operations with dates
        - make sure to read this: https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not !!!
          (or just this: https://stackoverflow.com/questions/44612144/logical-operators-in-python)
    - logical operations with None (incl. None and int, None and date, etc.)
    - None and date vs. None > date
    """

    print(True and False)
    print(1 or None)
    print()

    from datetime import date
    d1 = date(1971, 10, 11)
    d2 = date(1973, 10, 11)

    print(d1 and d2)
    print(False and d2)
    print(False or d2)
    print(False or not d2)
    print(not d2)
    print()

    print(None and d1)
    print(None or d1)
    print(None or not d1)
    print()


    print(d1.strftime(PREFERED_DATE_FORMAR))
if __name__ == '__main__':

    # demonstrate_arithmetic_operators()
    # demonstrate_relational_operators()
    demonstrate_logical_operators()

