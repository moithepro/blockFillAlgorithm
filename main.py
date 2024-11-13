from HamiltonPath import HamiltonPath
from utils import readfile, printarr, printarr_with_arrows

file = "./blocks2.txt"

arr = readfile(file)

printarr(arr)

path = HamiltonPath(arr)
for i in range(len(path)):
    if i == 0:
        continue
    arr[path[i][0]][path[i][1]] = i + 2
print("Hamiltonian Path:")
printarr_with_arrows(arr, path)
