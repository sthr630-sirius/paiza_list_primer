n = int(input())
size_array = 1024
start_idx = 0
end_idx = 1023
value = [None]*size_array
next_ptr = [None]*size_array
value[start_idx] = -1
value[end_idx] = -1
next_ptr[start_idx] = 1023
next_ptr[end_idx] = -1
back = 0
empty_min_idx = 1

for _ in range(n):
    i_num = int(input())
    value[empty_min_idx] = i_num
    'add element in front index'
    next_ptr[empty_min_idx] = next_ptr[start_idx]
    next_ptr[start_idx] = empty_min_idx
    '--------------------------'
    empty_min_idx += 1
    back += 1

print(value)
print(next_ptr)

print_idx = next_ptr[0]

for _ in range(size_array):
    print(value[print_idx])
    print_idx = next_ptr[print_idx]
    if print_idx == 1023:
        break