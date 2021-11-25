"""Demonstrates working with lists.
"""


def demonstrate_lists():
    """Using just the simplest operations with lists.
    - create a non-empty list with different kinds of elements
    - accessing/slicing a list
    - comparing 2 lists (== vs. is)
    - concatenating 2 lists (the + operator)
    - looping through a list
    """

    imagine = ['Imagine', True, 1971]
    print(imagine)
    print(imagine[1:])
    print(imagine[0:2])
    print(imagine == ['Imagine', True, 1971])
    print(imagine is ['Imagine', True, 1971])
    print(imagine + ['John', True, 2021])
    for item in imagine + ['John', True, 2021]:
        print(item)




def demonstrate_list_methods():
    """Using
    append() # ubaci u listu
    insert() # dodaj na poziciju .insert(pozicija, STA)
    remove() # izbacuje zadati el iz liste
    pop()    # izbacuje poslednji a moze i .pop(broj) izbacuje broj -1.element iz liste
    extend()
    count()
    index()
    reverse()
    len()
    ...
    Also, "in" and "not in" operators can be used to search lists
    for the occurrence of a given element.
    """
    imagine = ['Imagine', True, 1971]
    print(imagine.append('John Lennon'))
    print(imagine)
    imagine.insert(2,'Klaus')
    print( imagine.insert(2,'Klaus'))
    imagine.remove('Klaus')
    print(imagine)
    imagine.pop()
    print(imagine)
    imagine.extend(["Imagine"])
    print(imagine)
    print(imagine.count('Imagine'))
    print(imagine.index('Imagine'))
    print([i for i in range(len(imagine)) if imagine[i] == 'Imagine'])
    imagine.append('Mick')
    imagine.reverse()
    print(imagine)




def demonstrate_arrays():
    """Using array.array() to build list-based numeric arrays.
    Demonstrating that lists and arrays are different types.
    """

    from array import array
    a = array('i',[1,2,3,4])
    print(type(a))
    print(a)


def populate_empty_list():
    """Creating an empty list and populating it with random values
    using random.seed() and random.randint()
    """

    from random import randint, seed
    seed(23)
    l = []
    for i in range(100):
        l.append(randint(0,1000))
    print(l[34:36])


def duplicate_list():
    """Duplicating lists (carefully :)).
    Don't use l2 = l1, but either of the following:
    - l2 = l1.copy()
    - l2 = l1 + []
    - l2 = l1[:]
    """
    imagine = ['Imagine', True, 1971]
    l = imagine # bukvalno iste liste i adrese
    print(id(l), id(imagine))
    l = imagine.copy() # kopira samo sadrzaj
    print(id(l), id(imagine))
    print(l)


def demonstrate_list_comprehension():
    """Showing examples of list comprehension.
    - list comprehension over an array.array()
    - list comprehension over a list of strings
    - list comprehension with enumerate(), to find indices of all occurrences of an element in a list
    Using str() and join() in printing results.
    """

    # songs = ['Imagine a Man', 'There\'s a Place', 'No Expectations', 'Heaven Knows']

    from array import array
    a = array('i', [1, 2, 3, 4])
    print([i for i in a])
    print([i for i in a if i % 2])

    songs = ['Imagine a Man', 'There\'s a Place', 'No Expectations', 'Heaven Knows']
    print([song for song in songs if song.startswith('Imagine')])

    #Izdvaja prve reci iz naslova
    fw = [song.split()[0] for song in songs] # napravi mi listu koja uzima sve prve reci svakog elementa iz songs
    print(fw)
    fw = fw[0] + ' ' + ' '.join([fwl.lower() for fwl in fw[1:]])
    print(fw)

if __name__ == '__main__':

    # demonstrate_lists()
    # demonstrate_list_methods()
    # demonstrate_arrays()
    # populate_empty_list()
    # duplicate_list()
    demonstrate_list_comprehension()

