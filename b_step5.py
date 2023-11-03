def search_idx(p):
    idx = next_ptr[start_idx]
    target_idx = 0
    prev_target_idx = 0
    next_target_idx = 0
    counter = 1
    while counter <= p+1:
        if counter == p-1:
            prev_target_idx = idx
        elif counter == p:
            target_idx = idx
        elif counter == p+1:
            next_target_idx = idx

        idx = next_ptr[idx]
        counter += 1

    return prev_target_idx, target_idx, next_target_idx

n, p, x = map(int, input().split())
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
    a  = int(input())
    value[empty_min_idx] = a
    next_ptr[empty_min_idx] = end_idx
    next_ptr[prev_ptr[end_idx]] = empty_min_idx
    prev_ptr[empty_min_idx] = prev_ptr[end_idx]
    prev_ptr[end_idx] = empty_min_idx
    empty_min_idx += 1

if p > n:
    value[empty_min_idx] = x
    next_ptr[empty_min_idx] = end_idx
    next_ptr[prev_ptr[end_idx]] = empty_min_idx
    prev_ptr[empty_min_idx] = prev_ptr[end_idx]
    prev_ptr[end_idx] = empty_min_idx

    empty_min_idx += 1

elif p <= n:
    prev_target_idx, target_idx, next_target_idx = search_idx(p)

    value[empty_min_idx] = x
    next_ptr[empty_min_idx] = target_idx
    next_ptr[prev_target_idx] = empty_min_idx
    prev_ptr[empty_min_idx] = prev_target_idx
    prev_ptr[target_idx] = empty_min_idx

    empty_min_idx += 1

print_idx = next_ptr[start_idx]
while print_idx != end_idx:
    print(value[print_idx])
    print_idx = next_ptr[print_idx]