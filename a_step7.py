n, p = map(int, input().split())
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

for _ in range(n):
    a = int(input())
    value[empty_min_idx] = a
    next_ptr[back] = empty_min_idx
    next_ptr[empty_min_idx] = end_idx

    empty_min_idx += 1
    back += 1

pre_del_idx = next_ptr.index(p)
post_del_idx = next_ptr[p]

next_ptr[pre_del_idx] = post_del_idx

out_index = next_ptr[start_idx]
while out_index != end_idx:
    print(value[out_index])
    out_index = next_ptr[out_index]