'---------------------------------'
'    function push_back           '
def push_back(empty_min_idx, start_idx, end_idx, x):
    value[empty_min_idx] = x
    next_ptr[empty_min_idx] = end_idx
    next_ptr[prev_ptr[end_idx]] = empty_min_idx
    prev_ptr[empty_min_idx] = prev_ptr[end_idx]
    prev_ptr[end_idx] = empty_min_idx

'---------------------------------'
'    function search_idx          '
def search_idx(p):
    idx = next_ptr[start_idx]
    target_idx = 0
    counter = 1
    while counter <= p:
        if counter == p:
            target_idx = idx
        idx = next_ptr[idx]
        counter += 1
    return target_idx

'---------------------------------'
'  function insert_element '

'---------------------------------'
' function delete_element  '

'---------------------------------'
'   function print_array      '

'---------------------------------'
'     definition variant          '
n, q = map(int, input().split())
size_array = 1024
start_idx = 0
end_idx = 1023
value = [None]*size_array
next_ptr = [None]*size_array
prev_ptr = [None]*size_array
value[start_idx] = -1
value[end_idx] = -1
next_ptr[start_idx] = 1023
next_ptr[end_idx] = -1
prev_ptr[start_idx] = -1
prev_ptr[end_idx] = 0
empty_min_idx = 1

print(value)
print(next_ptr)
print(prev_ptr)

'---------------------------------'
'    initialization array          '
for _ in range(n):
    a = int(input())
    push_back(empty_min_idx, start_idx, end_idx, a)
    empty_min_idx += 1
print("value:", value)
print("next_ptr:", next_ptr)
print("prev_ptr", prev_ptr)
'---------------------------------'
'                main                  '
for _ in range(q):
    query = input()
    print(query)
    if query[0] == 1:
        p = query[1]
        x = query[2]
        #target_idx = search_idx(p)
        #insert_element(target_idx, x)
    elif query[0] == 2:
        p = query[1]
        #target_idx = search_idx(p)
        #delete_element(target_idx)

#print_array()