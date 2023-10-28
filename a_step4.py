n, k = map(int, input().split())
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

'add element in back index'
for _ in range(n):
    i_num = int(input())
    value[empty_min_idx] = i_num
    next_ptr[empty_min_idx] = end_idx
    next_ptr[back] = empty_min_idx
    empty_min_idx += 1
    back +=1

#print(value)
#print(next_ptr)

'delete element'
for _ in range(k):
    value[back] = None
    next_ptr[next_ptr.index(back)] = next_ptr[back]
    next_ptr[back] = None
    empty_min_idx -= 1
    back -= 1
#print(value)
#print(next_ptr)

print_idx = next_ptr[0]

while value[print_idx] != -1:
    print(value[print_idx])
    print_idx = next_ptr[print_idx]
