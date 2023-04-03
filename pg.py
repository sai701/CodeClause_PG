import random
import array




num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
lc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
					'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
					'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
					'z']

uc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
					'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
					'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
					'Z']

spl = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
		'*', '(', ')', '<']





rand_num = random.choice(num)
rand_uc = random.choice(uc)
rand_lc = random.choice(lc)
rand_spl = random.choice(spl)


temp = rand_num + rand_uc + rand_lc + rand_spl
print(temp)



