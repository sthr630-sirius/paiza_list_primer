n, l, r = map(int, input().split())
size_array = 1024
start_idx = 0
end_idx = 1023
value = [None]*size_array
next_ptr = [None]*size_array
value[start_idx] = -1
value[end_idx] = -1
next_ptr[start_idx] = end_idx
next_ptr[end_idx] = -1
empty_min_idx = 1
back = 0

' initialize value of array '
for _ in range(n):
    a = int(input())
    value[empty_min_idx] = a
    next_ptr[back] = empty_min_idx
    next_ptr[empty_min_idx] = end_idx

    empty_min_idx += 1
    back += 1

#print(value)
#print(next_ptr)

' main '
if l != r:
    pre_del_idx = next_ptr.index(l)
    post_del_idx = pre_del_idx
    for _ in range(r-l+1):
        post_del_idx = next_ptr[post_del_idx]
    next_ptr[pre_del_idx] = post_del_idx

' output value of array '
output_idx = next_ptr[start_idx]
while output_idx != end_idx:
    print(value[output_idx])
    output_idx = next_ptr[output_idx]

#print(value)
#print(next_ptr)