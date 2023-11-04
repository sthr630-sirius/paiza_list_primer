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

n, l, r = map(int, input().split())
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

for _ in range(n):
    a = int(input())
    value[empty_min_idx] = a
    next_ptr[empty_min_idx] = end_idx
    next_ptr[prev_ptr[end_idx]] = empty_min_idx
    prev_ptr[empty_min_idx] = prev_ptr[end_idx]
    prev_ptr[end_idx] = empty_min_idx
    empty_min_idx += 1

del_start_idx = search_idx(l)
del_end_idx = search_idx(r-1)

next_ptr[prev_ptr[del_start_idx]] = next_ptr[del_end_idx]
prev_ptr[next_ptr[del_end_idx]] = prev_ptr[del_start_idx]

print_idx = next_ptr[start_idx]
while print_idx != end_idx:
    print(value[print_idx])
    print_idx = next_ptr[print_idx]