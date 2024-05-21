
grid = [
    [9, 4],                                
    [6, 3],                                   
    [5, 8]                                    
]                                             
                                              
size = 0

for row in grid:
    size += 1


neighbordict = {}

for arr in grid:
    for elem in arr:
        if elem not in neighbordict:
            neighbordict[elem] = {}

        elem_index = arr.index(elem)
        arr_index = grid.index(arr)

        if elem_index - 1 < 0:
            # Sol üstteyim
            if arr_index - 1 < 0:
                if elem_index + 1 < len(arr):
                    neighbordict[elem][arr[elem_index + 1]] = 1
                if arr_index + 1 < len(grid):
                    neighbordict[elem][grid[arr_index + 1][elem_index]] = 1
            # Sol alttayım  
            elif arr_index + 1 >= len(grid):
                if elem_index + 1 < len(arr):
                    neighbordict[elem][arr[elem_index + 1]] = 1
                if arr_index - 1 >= 0:
                    neighbordict[elem][grid[arr_index - 1][elem_index]] = 1
            else:
                if arr_index + 1 < len(grid):
                    neighbordict[elem][grid[arr_index + 1][elem_index]] = 1
                if elem_index + 1 < len(arr):
                    neighbordict[elem][arr[elem_index + 1]] = 1
                if arr_index - 1 >= 0:
                    neighbordict[elem][grid[arr_index - 1][elem_index]] = 1

        elif elem_index + 1 >= len(arr):
            # Sağ alttayım
            if arr_index + 1 >= len(grid):
                if elem_index - 1 >= 0:
                    neighbordict[elem][arr[elem_index - 1]] = 1
                if arr_index - 1 >= 0:
                    neighbordict[elem][grid[arr_index - 1][elem_index]] = 1
            # Sağ üstteyim
            elif arr_index - 1 < 0:
                if elem_index - 1 >= 0:
                    neighbordict[elem][arr[elem_index - 1]] = 1
                if arr_index + 1 < len(grid):
                    neighbordict[elem][grid[arr_index + 1][elem_index]] = 1
            else:
                if elem_index - 1 >= 0:
                    neighbordict[elem][arr[elem_index - 1]] = 1
                if arr_index + 1 < len(grid):
                    neighbordict[elem][grid[arr_index + 1][elem_index]] = 1
                if arr_index - 1 >= 0:
                    neighbordict[elem][grid[arr_index - 1][elem_index]] = 1


keys_list = list(neighbordict.keys())

map_arr = [[]]

for elem in keys_list:
    map_arr.append([])
    
for elem in keys_list:
    map_arr[0].append(elem)
    
val = 0
for key in keys_list: #ex 9
    if key in neighbordict:
       for elem in keys_list:
            if elem in list(neighbordict[key].keys()):
                map_arr[keys_list.index(key)+1].append(val+1)
            else:
                map_arr[keys_list.index(key)+1].append(val)
for arr in map_arr:
    if map_arr.index(arr) != 0:
        if val < len(keys_list):
            arr.insert(0, keys_list[val])
            val += 1
        
        

print("  " + " ".join(map(str, keys_list)))
    

for arr in map_arr:
    if map_arr.index(arr) != 0:
        
        print(" ".join(map(str, arr)))


