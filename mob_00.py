""" Dictionary flipping demo, with Sam, Blake, and Me (UNFINISHED) """
from json import dumps


def flip(d: dict[str, int | list]) -> dict[int, str]:
    fd = dict()
    item_list = d.items()
    for i in item_list:
        if type(i[1]) is not list:
            if i[1] in fd:
                fd[i[1]] = fd[i[1]] + ', ' + i[0];
            else:
                # print(i)
                fd[i[1]] = i[0]
        else:
            if i[1][0] in fd:
                fd[i[1][0]] = fd[i[1][0]] + ', ' + i[0];
            else:
                # print(i)
                fd[i[1][0]] = i[0]


    # ... your code here
    return fd


if __name__ == "__main__":
    d1 = {
        "Paul": 1942,
        "John": 1940,
        "George": 1943,
        "Ringo": 1940
    }
    print(dumps(flip(d1), indent=4, sort_keys=True))

    d2 = {
        "Paul": [1942, {
            "Heather McCartney": 1962,
            "Mary McCartney": 1969,
            "Stella McCartney": 1971,
            "James McCartney": 1977,
            "Beatrice McCartney": 2003
        }],
        "John": [1940, {"Julian Lennon": 1963,
                        "Kyoko Chan Cox": 1963,
                        "Sean Lennon": 1975}],

        "George": [1943, {"Dhani Harrison": 1978}],
        "Ringo": [1940, {
            "Zak Starkey": 1965,
            "Jason Starkey": 1967,
            "Lee Starkey": [1970, {"Smokey": 2009, "Jakamo": 2009, "Ruby Tiger": 2009}]}]
    }
    print(dumps(flip(d2), indent=4, sort_keys=True))
