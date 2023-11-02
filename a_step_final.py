'-------------------------------------'
' define variant, array              '
n, q = map(int, input().split())
size_array = 1024
start_idx = 0
end_idx = 1023
value = [None]*size_array
next_ptr = [None]*size_array
value[start_idx] = -1
value[end_idx] = -1
next_ptr[start_idx] = 1023
next_ptr[end_idx] = -1
empty_min_idx = 1
back = 0

'-------------------------------------'
' initialize  variant, array          '
for _ in range(n):
    a = int(input())
    value[empty_min_idx] = a
    next_ptr[back] = empty_min_idx
    next_ptr[empty_min_idx] = end_idx
    empty_min_idx += 1
    back += 1

'-------------------------------------'
' function search index              '
def search_idx(next_ptr, p):
    idx = next_ptr[0]
    counter = 1
    while counter <= p+1:
        if counter == p-1:
            pre_target_idx = idx
        elif counter == p:
            target_idx = idx
        elif counter == p+1:
            post_target_idx = idx

        idx = next_ptr[idx]
        counter += 1

    return pre_target_idx, target_idx, post_target_idx

'-------------------------------------'
' function insert                      '
def insert_element(value, next_ptr, pre_target_idx, target_idx, post_target_idx, empty_min_idx, back, x):
    value[empty_min_idx] = x
    next_ptr[pre_target_idx] = empty_min_idx
    next_ptr[empty_min_idx] = post_target_idx

'-------------------------------------'
' function delete                      '
def delete_element(next_ptr, pre_target_idx, post_target_idx):
    next_ptr[pre_target_idx] = post_target_idx

'-------------------------------------'
' main                                      '
print(value)
print(next_ptr)
for _ in range(q):
    query = input()
    if int(query[0]) == 1:
        p = int(query.split()[1])
        x = int(query.split()[2])
        print("insert ", p, x)
        pre_target_idx, target_idx, post_target_idx = search_idx(next_ptr, p)
        #print(pre_target_idx, target_idx, post_target_idx)
        #print(value)
        #print(next_ptr)
        insert_element(value, next_ptr, pre_target_idx, target_idx, post_target_idx, empty_min_idx, back, x)
        empty_min_idx += 1
        back += 1
        #print(value)
        #print(next_ptr)
    elif int(query[0]) == 2:
        p = int(query.split()[1])
        print("delete ", p)
        pre_target_idx, target_idx, post_target_idx = search_idx(next_ptr, p)
        delete_element(next_ptr, pre_target_idx,  post_target_idx)

    print(value)
    print(next_ptr)
'-------------------------------------'
' print                                      '

'-------------------------------------'
' test block                             '
#print(value)
#print(next_ptr)
