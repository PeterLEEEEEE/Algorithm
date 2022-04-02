from os import lseek


# dic = dict(type='lee', img=(3333,3333))

bbox = [[1,4], [3,1], [5, 6]]
bbox.sort(key=lambda x: x[0])

print(bbox)