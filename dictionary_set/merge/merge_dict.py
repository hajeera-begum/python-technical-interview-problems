d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'b': 5, 'd': 4}

print("Overwriting Logic: ",d1|d2) 

merge=d1.copy()
for k,v in d2.items():  #Why items because we need both key and value. See below table to remember
    merge[k]=merge.get(k,0)+v

print("Adding both dictionary logic: ",merge)
'''
| Method       | Gives              |
| ------------ | ------------------ |
| `d.keys()`   | keys               |
| `d.values()` | values             |
| `d.items()`  | (key, value) pairs |
'''
