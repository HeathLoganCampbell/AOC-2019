
ADD_OPCODE = 1
MULTI_OPCODE = 2
HALT_OPCODE = 99;

with open('input.txt') as f:
    inputData = map(int, f.read().split(","))

# 1 = add (adds 2 following numbers)
# 2 = times
# 
# 99 = finish


def boot(inputData):
  memory = inputData[:]
  pc = 0
  lastValue = 0

  for x in range(0, len(memory)):
    opcode = memory[pc]
    if(opcode == ADD_OPCODE):
      memory[memory[pc + 3]] = lastValue= memory[memory[pc + 1]] + memory[memory[pc + 2]]
      pc = pc + 4
    elif(opcode == MULTI_OPCODE):
      memory[memory[pc + 3]] = lastValue = memory[memory[pc + 1]] * memory[memory[pc + 2]] 
      pc = pc + 4
    elif(opcode == HALT_OPCODE):
      # Halt
      break
    else:
      #something went wrong
      break
  print("Answer:", lastValue)

print("Test 1 (Should be 2)")
boot([1,0,0,0,99])
print("Test 2 (Should be 3)")
boot([2,3,0,3,99])
print("Test 3 (Should be 9801)")
boot([2,4,4,5,99,0])
print("Test 4 (Should be 30)")
boot([1,1,1,4,99,5,6,0,99])

print("Real test")

inputData[1] = 12
inputData[2] = 2
boot(inputData)