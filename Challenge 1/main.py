
# define 2 arrays one being the original array 
# and the second being an updated array
first_array = [1,2,3,4,5,6,7,8,9,10]
second_array = [1,10,9,11,22,23]

def check_array(original_array, updated_array):
    added_array = []
    deleted_array = []

    # Find new items
    # Loop through the updated array
    # if the item is not in the original array
    # then add it to the new items array
    for item in updated_array:
        found = False
        for i in original_array:
            if(item == i):
                found = True
                continue
        if not found:
            added_array.append(item)

    # find deleted items
    # Loop through the original array
    # if the item is in the updated array then it is not deleted
    # else add it to the deleted items array
    for item in original_array:
        deleted = True
        for i in updated_array:
            if(item==i):
                deleted = False
                continue
        if deleted:
            deleted_array.append(item)

    return deleted_array, added_array
                

del_items, new_items = check_array(first_array, second_array)
print(f'Deleted items are: {del_items}')
print(f'Newly added items are: {new_items}')