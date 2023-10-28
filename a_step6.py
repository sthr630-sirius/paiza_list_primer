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

if p > n:
    next_ptr[next_ptr.index(end_idx)] = empty_min_ptr

    value[empty_min_ptr] = x
    next_ptr[empty_min_ptr] = end_idx

    empty_min_ptr += 1
    back += 1

else:
    print("作成中")
    print("github 確認")

print(value)
print(next_ptr)