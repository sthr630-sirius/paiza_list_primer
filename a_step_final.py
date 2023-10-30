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

'-------------------------------------'
' fanction search idex              '

'-------------------------------------'
' fanction insert                       '

'-------------------------------------'
' fanction delete                      '

'-------------------------------------'
' main                                      '
for _ in range(q):
    query = input()
    print(query[0])
    if int(query[0]) == 1:
        p = int(query.split()[1])
        x = int(query.split()[2])
        print("insert ", p, x)
        # insert()
    elif int(query[0]) == 2:
        p = int(query.split()[1])
        print("delete ", p)
        # delete()
'-------------------------------------'
' print                                      '

'-------------------------------------'
' test block                             '
print(value)
print(next_ptr)
