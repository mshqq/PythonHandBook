N = int(input())
N_num1 = N // 100
N_num2 = N % 100 // 10
N_num3 = N % 10

M = int(input())
M_num1 = M // 100
M_num2 = M % 100 // 10
M_num3 = M % 10

pair1 = M_num1 + N_num1
pair2 = M_num2 + N_num2
pair3 = M_num3 + N_num3

fin = str(pair1 % 10) + str(pair2 % 10) + str(pair3 % 10)

print(int(fin)) 