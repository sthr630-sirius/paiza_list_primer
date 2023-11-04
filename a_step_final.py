'-------------------------------------'
' function search index              '
def search_idx(next_ptr, p):
    idx = next_ptr[0]
    counter = 1
    pre_target_idx = 0
    target_idx = 0
    post_target_idx = 0
    while counter <= p+1:
        #print("counter:", counter)
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
    next_ptr[empty_min_idx] = target_idx

'-------------------------------------'
' function delete                      '
def delete_element(next_ptr, pre_target_idx, post_target_idx):
    next_ptr[pre_target_idx] = post_target_idx

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
' main                                      '
for _ in range(q):
    query = input()
    if int(query[0]) == 1:
        p = int(query.split()[1])
        x = int(query.split()[2])
        pre_target_idx, target_idx, post_target_idx = search_idx(next_ptr, p)

        insert_element(value, next_ptr, pre_target_idx, target_idx, post_target_idx, empty_min_idx, back, x)
        empty_min_idx += 1
        back += 1

    elif int(query[0]) == 2:
        p = int(query.split()[1])
        pre_target_idx, target_idx, post_target_idx = search_idx(next_ptr, p)
        delete_element(next_ptr, pre_target_idx,  post_target_idx)

'-------------------------------------'
' print                                      '
print_idx = next_ptr[start_idx]
while print_idx != end_idx:
    print(value[print_idx])
    print_idx = next_ptr[print_idx]