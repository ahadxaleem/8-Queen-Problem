import random
no_of_chromo = 4
len_of_chromo = 8


def horiz(arr):
    act_fit = 0
    for ind in range(len_of_chromo-1):
        for i in range(ind+1, len_of_chromo):
            if arr[ind] == arr[i]:
                act_fit += 1
    return act_fit


def diagonal(arr):
    act_fit = 0
    temp = 1
    for ind in range(len_of_chromo-1):
        for i in range(ind+1, len_of_chromo):
            if arr[ind]+temp > len_of_chromo-1:
                break
            if arr[ind]+temp == arr[i]:
                act_fit += 1
            temp += 1
        temp = 1
        for i in range(ind+1, len_of_chromo):
            if arr[ind]-temp < 0:
                break
            if arr[ind]-temp == arr[i]:
                act_fit += 1
            temp += 1
    return act_fit


def createchrome():

    temp = []
    for i in range(len_of_chromo):
        temp.append(random.randint(0, 7))
    return temp


def calfitness(a):
    tempfit = 28
    tempfit = tempfit-horiz(a)
    tempfit = tempfit-diagonal(a)
    return tempfit


def selection(a):
    ratio = []
    rolw = []
    select = []
    total = 0
    for i in range(no_of_chromo):
        total += a[i].fitness
    for i in range(no_of_chromo):
        ratio.append((a[i].fitness/total)*100)
    rolw.append(ratio[0])
    for i in range(1, no_of_chromo):
        rolw.append(rolw[i-1]+ratio[i])
    for i in range(no_of_chromo):
        assig = 0
        temp = random.randrange(0, 99)
        while 1:
            if temp > rolw[assig]:
                assig += 1
            else:
                select.append(assig)
                break
    return select


def crossOver(list, a):
    for i in range(0, no_of_chromo, 2):
        b = []
        c=[]
        temp = random.randrange(2, 6)
        for j in range(temp):
            b.append(list[a[i]].chrome[j])
            c.append(list[a[i+1]].chrome[j])
        for j in range(temp,len_of_chromo):
            b.append(list[a[i+1]].chrome[j])
            c.append(list[a[i]].chrome[j])
        list[i].chrome=b
        list[i+1].chrome=c

def mutate(list, a):
    for i in range(no_of_chromo):
        temp = random.randrange(0, 9)
        temp1 = random.randrange(0, 8)
        if temp > 7:
            continue
        else:
            list[a[i]].chrome[temp] = temp1


class chromosome:
    def __init__(self) -> None:
        self.chrome = createchrome()
        self.fitness = calfitness(self.chrome)


list = []
totalfit = 0
generation = 1
for i in range(no_of_chromo):
    list.append(chromosome())
for i in range(no_of_chromo):
    totalfit += list[i].fitness
print("Generation#"+str(generation))
for i in range(no_of_chromo):
    print("Chromosome "+str(i+1)+" " +
          str(list[i].chrome)+" Fitness = "+str(list[i].fitness))
generation += 1
print("Total Fitness = "+str(totalfit))
done = 1
while done:
    for i in range(no_of_chromo):
        if list[i].fitness > 27:
            print("Chromosome "+str(i+1)+" " +
                  str(list[i].chrome)+" Fitness = "+str(list[i].fitness))
            print("solution found.....")
            done = 0
            break
    if done == 1:
        a = selection(list)
        crossOver(list, a)
        mutate(list, a)
        for i in range(no_of_chromo):
            list[i].fitness = calfitness(list[i].chrome)
        totalfit = 0
        for i in range(no_of_chromo):
            totalfit += list[i].fitness
        print("\nGeneration#"+str(generation))
        for i in range(no_of_chromo):
            print("Chromosome "+str(i+1)+" " +str(list[i].chrome)+" Fitness = "+str(list[i].fitness))
        generation += 1
        print("Total Fitness = "+str(totalfit))
