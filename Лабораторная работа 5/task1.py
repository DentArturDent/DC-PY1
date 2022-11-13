from pprint import pprint

n = 15

num_list = [{'dec': i, 'bin': bin(i), 'oct': oct(i), 'hex': hex(i)} for i in range(n+1)]

pprint(num_list)
