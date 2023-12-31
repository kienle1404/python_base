def combine_dict(dict1:dict, dict2:dict)->dict:
    d = {}
    for k,v in dict1.items():
        d[k] = [v]
    for k,v in dict2.items():
        if k in d:
            d[k].append(v)
        else:
            d[k] = [v]
    return d

# def function(a, b=10,c="a", *d, **e):

def combine_more_dict(*dicts)->dict:
    d = {}
    for dict_ in dicts:
        for k, v in dict_.items():
            if k in d:
                d[k].append(v)
            else:
                d[k] = [v]
    return d

d1 = {'w': 50, 'x': 100, 'y': 'Green', 'z': 400}
d2 = {'x': 300, 'y': 'Red', 'z': 600}
print(combine_more_dict(d1, d2, d2))
