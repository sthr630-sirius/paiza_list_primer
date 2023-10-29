n, p, x = map(int, input().split())
size_array = 1024
start_idx = 0
end_idx = 1023
value = [None]*size_array
next_ptr = [None]*size_array
value[start_idx] = -1
value[end_idx] = -1
next_ptr[start_idx] = 1
next_ptr[end_idx] = 1023
empty_min_ptr = 1
back = 0

for _ in range(n):
    i_num = int(input())
    value[empty_min_ptr] = i_num
    next_ptr[empty_min_ptr] = end_idx
    next_ptr[back] = empty_min_ptr
    empty_min_ptr += 1
    back += 1

#print(value)
#print(next_ptr)

if p > n:
    next_zptr[next_ptr.index(end_idx)] = empty_min_ptr

    value[empty_min_ptr] = x
    next_ptr[empty_min_ptr] = end_idx

    empty_min_ptr += 1
    back += 1

else:
    value[empty_min_ptr] = x

    pre_insert_idx = next_ptr.index(p)
    post_insert_idx = next_ptr[pre_insert_idx]
    next_ptr[pre_insert_idx] = empty_min_ptr
    next_ptr[empty_min_ptr] = post_insert_idx

    empty_min_ptr += 1
    back += 1

out_idx = next_ptr[0]

while out_idx != end_idx:
    print(value[out_idx])
    out_idx = next_ptr[out_idx]
