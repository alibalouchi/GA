import numpy
i = [77.78, 85.00, 90.28, 85.28, 89.17, 78.61, 79.72, 76.11, 88.33, 74.44, 65.00, 82.22, 83.06, 74.72, 66.67]
cmin = [0.00, 0.00, 0.01, 0.01, 0.00, 0.00, 0.36, 0.00, 0.00, 0.00, 0.00, 0.34, 0.54, 0.05, 0.07]
cmax = [0.04, 0.04, 0.07, 0.04, 0.81, 0.42, 1.25, 0.10, 0.21, 0.51, 0.43, 0.83, 1.88, 0.16, 0.50]
#Defining Random function for weights
def Random(cmin, cmax, size):
    weights = []
    num = 0
    while num < size:
        new_weight = numpy.random.uniform(low=cmin[num], high=cmax[num])
        weights.append(new_weight)
        num=num+1
    return weights

#Defining a function that creates numbers of weight matrixes
def NumWeights(number, cmin, cmax, size):
    weights = []
    for i in range(number):
        new_matrix = Random(cmin, cmax, size)
        weights.append(new_matrix)
    return weights
    

#Defining fitness function
def FitnessFunction(list1, weights, size):
    num = 0
    fitness = []
    while num < size:
        fitness_var = list1[num] * weights[num]
        fitness.append(fitness_var)
        num += 1
    fitneses = sum(fitness)
    print fitneses
    return fitneses
#Defining function that calculate all the fittnesses
def FitnessAll(list1, weights, weights_size, size):
    num = 0
    fitnessall = []
    while num < weights_size:
        fitnessall.append(FitnessFunction(list1, weights[num], size))
        num += 1
    return fitnessall

#Defining a function that find the best fitness in list
def FindWeightsOfFitnesses():
    weights = NumWeights(15, cmin, cmax, 15)
    fitneses = FitnessAll(i, weights, 15, 15)
    print fitneses
    maximum_index = 0
    for index in range(len(fitneses)):
        if fitneses[index] == max(fitneses):
            maximum_index = index
            print maximum_index
    best_weight = weights[maximum_index]
    return maximum_index
    return best_weight

#Defining a function that create childrens
def MakingChild(list_a, list_b):
    child1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    child2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for index in range(len(list_a)):
        if index%2==0:
            child1[index] = list_a[index]
        else:
            child1[index] = list_b[index]
        if index%2 ==0:
            child2[index] = list_b[index]
        else:
            child2[index] = list_a[index]
    return list_a, list_b, child1, child2

#Defining a function that create all childrens
def CreateChildAll(list1, number_of_list_in_list1):
    num = 0
    childs = []
    for index in range(number_of_list_in_list1):
        for index1 in range(number_of_list_in_list1):
            if index != index1:
                childs.append(MakingChild(list1[index], list1[index1]))
    return childs
child = CreateChildAll(NumWeights(15, cmin, cmax, 15), 15)
#Defining mutations
m=[]
def Mutation(list1):
    random_number = int(numpy.random.uniform(low=0, high=50))
    random_index = int(numpy.random.uniform(low=0, high=14))
    random_array = int(numpy.random.uniform(low=0, high=210))
    random_matrix = int(numpy.random.uniform(low=0, high=4))
    for index in range(random_number):
        child[random_array][random_matrix][random_index] = numpy.random.uniform(low=cmin[random_index], high=cmax[random_index])
    return child


Mutation(child)

print child