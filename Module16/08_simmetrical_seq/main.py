def is_palindrome(num_list):
    reverse_list = []
    for i_num in range(len(num_list)-1, -1, -1):
        reverse_list.append(num_list[i_num])
    if num_list == reverse_list:
        return True
    else:
        return False


nums = []
new_nums = []
answer = []

count_nums = int(input('Количество чисел: '))
for i in range(count_nums + 1):
    num = int(input('Число: '))
    nums.append(num)
for i_nums in range(0, len(nums)):
    for j_elem in range(i_nums, len(nums)):
        new_nums.append(nums[j_elem])
    if is_palindrome(new_nums):
        for i_answer in range(0, i_nums):
            answer.append(nums[i_answer])
        answer.reverse()
        break
    new_nums = []

print(f'Исходный список: {nums}')
print(f'Нужно чисел для палиндрома: {len(answer)}')
print(f'Список этих чисел: {answer}')
