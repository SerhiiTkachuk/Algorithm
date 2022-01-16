def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


print(quicksort([11,1,23,4,25,0,3,11,2]))
print("="*30)

some_dict = {}
def check_keys(some_dict, key):
    if some_dict.get(key):
        print(f"Key {key} is in {some_dict} and his value is {some_dict.get(key)}")
    else:
        some_dict[key] = True
        print(f"Add {key} to dictionary {some_dict}.")

some_d = {1:True, 2:True}
check_keys(some_d, 2)
check_keys(some_d, 3)
check_keys(some_d, 3)
