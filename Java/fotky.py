# Tuto funkci implementuj.
def is_face_on_photo(photo):
    mask = [[0, 0], [0, 1], [1, 0], [1, 1]]
    check = 1
    dictionary = {
        'f': 2,
        'a': 3,
        'c': 5,
        'e': 7
    }

    for i in range(0,len(photo) - 1):
        for j in range(0, len(photo[0]) - 1):
            if photo[i][j] == 'f' or 'a' or 'c' or 'e':
                for k in range(4):
                    check *= dictionary.get(photo[i + mask[k][0]][j + mask[k][1]], 1)
                if check == 2*3*5*7:
                    return(True)
                else:
                    check = 1
    return(False)

# Testy:
print(is_face_on_photo([['f', 'a'], ['c', 'e']]))  # True
print(is_face_on_photo([['f', 'a', 'c', 'e']]))  # False
print(is_face_on_photo([['e', 'c', 'x'], ['a', 'f', 'x'], ['x', 'x', 'x']]))  # True
print(is_face_on_photo([['f', 'f', 'x'], ['a', 'a', 'x'], ['x', 'x', 'x']]))  # False
print(is_face_on_photo([['x', 'f', 'c'], ['x', 'a', 'e'], ['x', 'x', 'x']]))  # True
