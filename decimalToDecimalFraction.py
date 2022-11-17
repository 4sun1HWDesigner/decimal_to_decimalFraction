def DecimalToBinary(n, digit):
    n_temp = n
    result = 0
    for i in range(0, digit):     
        n_quotient = n_temp // 2
        n_remainder = n_temp %2
        n_temp = n_quotient
        n_remainder_mul_weight_of_digit = n_remainder * (2 ** -(digit-i))
        result = result + n_remainder_mul_weight_of_digit
        
    return result
    
    


arr = []
num_arr = []

f = open("decimal_value.txt", 'r')
f_2 = open("decimal_fraction_value.txt", 'w')

while True:
    line = f.readline()
    line = line.strip("\n")
    arr.append(line)
    if not line: break
             
num_arr = list(map(int, arr[0:len(arr)-1]))

for j in range(0, len(num_arr)):
    num_arr[j] = DecimalToBinary(num_arr[j], 12)

for i in range(0, len(num_arr)):    
    f_2.write(str(num_arr[i]))
    f_2.write("\n")
    
f.close()
f_2.close()