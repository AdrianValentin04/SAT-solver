import fileinput
from itertools import product
import sys
from time import time

#begin_time = time()

f = open(sys.argv[1], "r")
data = f.read()
#data = input()
nr_rel = 1  	# nr de relatii(de paranteze)
max_lit = 0 	# nr de variabile
ok = 0

for i in data:
    if i == '^':
        nr_rel = nr_rel + 1 	# numaram relatiile

number = 0
# aflam nr de variabile
for i in range(len(data)): 		
    if data[i] >= "0" and data[i] <= "9":
        number = number * 10 + int(int(data[i]) - 0)
    else:
        max_lit = max(max_lit, number)
        number = 0

SAT = []
splitted = data.split(")^(")
number = 0
# generam matricea SAT 
for i in range(nr_rel):
    variables = [0 for j in range(max_lit)]
    lit_splitted = splitted[i].split("V")

    for j in range(len(lit_splitted)):
        for k in range(len(lit_splitted[j])):
            if(lit_splitted[j][k] == "~"):
                ok = 1
            if lit_splitted[j][k] >= "0" and lit_splitted[j][k] <= "9":
                number = number * 10 + int(int(lit_splitted[j][k]) - 0)
        if ok == 0:
            variables[number - 1] = 1
        else:
            variables[number - 1] = -1

        number = 0
        ok = 0

    SAT.append(variables)
# generam matricea de permutari
truth = [1, -1]
truth_matrix = list(product(truth, repeat = max_lit))

ok = 0
i = j = 0 	 # indicii pentru truth_matrix
# testam satisfiabilitatea formulei date ca input
while(ok == 0 and i < len(truth_matrix)):
    ok = 1
    for k in range(nr_rel):
        found = 0
        for l in range(max_lit):
            if(SAT[k - 1][l - 1] * truth_matrix[i][j] == 1):
                found = 1
                break
            j = j + 1
       
        if found == 0:
            ok = 0
            break
        
        j = 0

    i = i + 1
    j = 0

print(ok)

#duration = time() - begin_time
#print(duration)