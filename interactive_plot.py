import csv
import matplotlib.pyplot as plt
import numpy as np

#x = []
#y = []

#with open("sample_data.csv", "r") as file:
#    reader = csv.reader(file)
#    next(reader)
#    for row in reader:
#        x.append(float(row[0]))
#        y.append(float(row[1]))

#plt.figure(figsize=(8,5))
#plt.plot(x, y, marker="o", color='red', linestyle='-', linewidth=2)
##plt.ylabel("y-values")
#plt.grid(True)


#plt.show()


#--- To create a code for generating prime numbers ---

# 1. to write a function to check if the number is prime. 

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** (1 / 2) + 1)):
        if n % i == 0:
            return False
    return True



def get_primes():
    primes = []

    for idx in range(1, 351):
        if is_prime(idx):
            primes.append(idx)
    #print(primes)

    with open("result.txt", "w") as file:
        file.write("Primes numbers between 1 and 350:\n")
        for j in primes:
            file.write(str(j) + "\n")

    print("The primes numbers are written in to the file")


if __name__ == "__main__":
    get_primes()
