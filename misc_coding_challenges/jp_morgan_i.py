s = "I am using hackerrank to improve programming"
t = "am hackerrank to improve"
s_list = s.split(" ")
t_list = t.split(" ")
t_len = len(t_list)
t_counter = 0
ans_list = s_list
rem_positions_list = list()

for i in range(len(s_list)):
    if s_list[i] == t_list[t_counter]:
        rem_positions_list.append(i)
        t_counter += 1
        if t_counter == t_len:
            break

for i in range(len(rem_positions_list)):

    ans_list.pop(rem_positions_list[i] - i)
print(ans_list)
# print(ans)
# print(s_list[:ans] + s_list[ans + 1 : :])
