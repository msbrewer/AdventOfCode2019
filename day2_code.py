import sys
originp = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,1,19,5,23,
            2,9,23,27,1,5,27,31,1,5,31,35,1,35,13,39,1,39,9,43,
            1,5,43,47,1,47,6,51,1,51,13,55,1,55,9,59,1,59,13,
            63,2,63,13,67,1,67,10,71,1,71,6,75,2,10,75,79,2,
            10,79,83,1,5,83,87,2,6,87,91,1,91,6,95,1,95,13,99,
            2,99,13,103,1,103,9,107,1,10,107,111,2,111,13,115,
            1,10,115,119,1,10,119,123,2,13,123,127,2,6,127,131,
            1,13,131,135,1,135,2,139,1,139,6,0,99,2,0,14,0]


def op1(inp1, inp2):
    return inp[inp1] + inp[inp2]

def op2(inp1, inp2):
    return inp[inp1] * inp[inp2]

def output(inpList):
    if inpList[0] == 1:
        return op1(inpList[1], inpList[2])
    elif inpList[0] == 2:
        return op2(inpList[1], inpList[2])

def run(inp, i=0):
    while True:
        inpList = [inp[i], inp[i+1], inp[i+2], inp[i+3]]
        inp[inpList[3]] = output(inpList)
        i = i + 4
        if inp[i] == 99:
            return inp

#for i in range(100):
#    inp = originp
#    inp[1] = i
#    for p in range(100):
#        inp[2] = p
inp = originp
inp[1] = 12
inp[2] = 2
print(run(inp))

#        if inp[0] == 19690720:
#            print(100 * inp[1] + inp[2])
#            sys.exit()
