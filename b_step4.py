def search_idx(k):
    idx = next_ptr[start_idx]
    target_idx = 0
    prev_target_idx = 0
    counter = 1
    while counter <= k+1:
        if counter == k:
            target_idx = idx
        elif counter == k+1:
            prev_target_idx = idx
        idx = next_ptr[idx]
        counter += 1

    return target_idx, prev_target_idx

n, k = map(int, input().split())
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

target_idx, prev_target_idx = search_idx(k)

next_ptr[start_idx] = prev_target_idx
prev_ptr[prev_target_idx] = start_idx

print_idx = next_ptr[start_idx]
while print_idx != end_idx:
    print(value[print_idx])
    print_idx = next_ptr[print_idx]