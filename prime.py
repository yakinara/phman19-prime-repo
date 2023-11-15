prime_list = []
to_be_removed = []

for i in range(1,251):
  if (i == 2 or i == 3 or i == 5 or i==7):
    prime_list.append(i)
  if (i%2 == 0 or i%3 == 0 or i%5 == 0 or i%7 == 0 or i%(i**0.5)==0):
    #print(str(i) + ": not prime")
    continue
  else:
    prime_list.append(i)

for i in range(len(prime_list)):
  for j in range(len(prime_list)):
    if (prime_list[j] % prime_list[i] == 0 and prime_list[j] != prime_list[i]):
      #print(str(prime_list[j]) + ': not a prime')
      continue
      if (prime_list[j] not in to_be_removed):
        to_be_removed.append(prime_list[j])
      #prime_list.remove(prime_list[j])
    else: 
      continue

for i in range(len(to_be_removed)):
  prime_list.remove(to_be_removed[i])


print(prime_list)

primeFile = open("primeResult.txt", "w")
primeFile.write(str(prime_list))
primeFile.close()
#print(to_be_removed)
  