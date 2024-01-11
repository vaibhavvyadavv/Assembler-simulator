regs = {"000": 0, "001": 0, "010": 0, "011": 0,"100": 0, "101": 0, "110": 0, "111": "0" * 16,"PC": 0}
memAddress = {}
#initialise memAddress dictionary with keys of 128 memory addresses starting from '0000000'
for i in range(128):
    memAddress[bin(i)[2:].zfill(7)] = '0000000000000000'

instructions = []

lines = []
while True:
    try:
        line = input()
    except EOFError:
        break
    lines.append(line)

for inst in lines:
    inst.strip()
    instructions.append(inst[:16])

for i in range(len(instructions)):
    memAddress[bin(i)[2:].zfill(7)] = instructions[i]


def clearFlag():
    regs["111"] = "0" * 16

def setOverflow():
    regs["111"] = "0" * 12 + "1" + "000"

def setLess():
    regs["111"] = "0" * 13 + "1" + "00"

def setGreater():
    regs["111"] = "0" * 14 + "1" + "0"

def setEqual():
    regs["111"] = "0" * 15 + "1"

def add(inst):
    reg1 = inst[7:10]
    reg2 = inst[10:13]
    reg3 = inst[13:16]
    regs[reg1] = regs[reg2] + regs[reg3]
    if regs[reg1] > 65535:
        setOverflow()
        regs[reg1] = 0
    else:
        clearFlag()
    print(bin(regs['PC'])[2:].zfill(7), end = "        ")
    for i in regs:
        print(bin(regs[i])[2:].zfill(16), end = " ")
        if i == "110":
            break
    print(regs['111'])
    regs["PC"] += 1
    return regs["PC"]

def sub(inst):
    reg1 = inst[7:10]
    reg2 = inst[10:13]
    reg3 = inst[13:16]
    regs[reg1] = regs[reg2] - regs[reg3]
    if regs[reg1] < 0:
        setOverflow()
        regs[reg1] = 0
    else:
        clearFlag()
    print(bin(regs['PC'])[2:].zfill(7), end = "        ")
    for i in regs:
        print(bin(regs[i])[2:].zfill(16), end = " ")
        if i == "110":
            break
    print(regs["111"])    
    regs["PC"] += 1
    return regs["PC"]

def movi(inst):
    reg1 = inst[6:9]
    imm = inst[9:16]
    regs[reg1] = int(imm, 2)
    print(bin(regs['PC'])[2:].zfill(7), end = "        ")
    for i in regs:
        print(bin(regs[i])[2:].zfill(16), end = " ")
        if i == "110":
            break
    print(regs["111"])
    regs["PC"] += 1
    return regs["PC"]

def mov(inst):
    reg1 = inst[10:13]
    reg2 = inst[13:16]
    print(bin(regs['PC'])[2:].zfill(7), end = "        ")
    if reg2 != "111":
        regs[reg1] = regs[reg2]
        for i in regs:
            print(bin(regs[i])[2:].zfill(16), end = " ")
            if i == "110":
                break
    else:
        regs[reg1] = regs[reg2]
        for i in regs:
            if i != reg1:
                print(bin(regs[i])[2:].zfill(16), end = " ")
            else:
                print(regs[i], end = " ")
                regs[i] = int(regs[i],2)
                clearFlag()
            if i == "110":
                break
    
    print(regs["111"])
    regs["PC"] += 1
    return regs["PC"]

def ld(inst):
    reg1 = inst[6:9]
    mem_addr = inst[9:16]
    regs[reg1] = int(memAddress[mem_addr],2)
    #print the memory address at which inst is stored from dictionary memAddress
    print(bin(regs['PC'])[2:].zfill(7), end = "        ")
    for i in regs:
        print(bin(regs[i])[2:].zfill(16), end = " ")
        if i == "110":
            break
    print(regs["111"])
    regs["PC"] += 1
    return regs["PC"]

def st(inst):
    reg1 = inst[6:9]
    mem_addr = inst[9:16]
    memAddress[mem_addr] = bin(regs[reg1])[2:].zfill(16)
    print(bin(regs['PC'])[2:].zfill(7), end = "        ")
    for i in regs:
        print(bin(regs[i])[2:].zfill(16), end = " ")
        if i == "110":
            break
    print(regs["111"])
    regs["PC"] += 1
    return regs["PC"]

def mul(inst):
    reg1 = inst[7:10]
    reg2 = inst[10:13]
    reg3 = inst[13:16]
    regs[reg1] = regs[reg2] * regs[reg3]
    if regs[reg1] > 65535:
        setOverflow()
        regs[reg1] = 0
    else:
        clearFlag()
    print(bin(regs['PC'])[2:].zfill(7), end = "        ")
    for i in regs:
        print(bin(regs[i])[2:].zfill(16), end = " ")
        if i == "110":
            break
    print(regs["111"])
    regs["PC"] += 1
    return regs["PC"]

def div(inst):
    reg3 = inst[10:13]
    reg4 = inst[13:16]
    if regs[reg4] == 0:
        setOverflow()
        regs['000'] = 0
        regs['001'] = 0
    else:
        regs['000'] = regs[reg3] // regs[reg4]
        regs['001'] = regs[reg3] % regs[reg4]
        clearFlag()
    print(bin(regs['PC'])[2:].zfill(7), end = "        ")
    for i in regs:
        print(bin(regs[i])[2:].zfill(16), end = " ")
        if i == "110":
            break
    print(regs["111"])
    regs["PC"] += 1
    return regs["PC"]

def rs(inst):
    reg1 = inst[6:9]
    imm = inst[9:16]
    regs[reg1] = regs[reg1] >> int(imm, 2)
    print(bin(regs['PC'])[2:].zfill(7), end = "        ")
    for i in regs:
        print(bin(regs[i])[2:].zfill(16), end = " ")
        if i == "110":
            break
    print(regs["111"])
    regs["PC"] += 1
    return regs["PC"]

def ls(inst):
    reg1 = inst[6:9]
    imm = inst[9:16]
    regs[reg1] = regs[reg1] << int(imm, 2)
    print(bin(regs['PC'])[2:].zfill(7), end = "        ")
    for i in regs:
        print(bin(regs[i])[2:].zfill(16), end = " ")
        if i == "110":
            break
    print(regs["111"])
    regs["PC"] += 1
    return regs["PC"]

def xor(inst):
    reg1 = inst[7:10]
    reg2 = inst[10:13]
    reg3 = inst[13:16]
    regs[reg1] = regs[reg2] ^ regs[reg3]
    print(bin(regs['PC'])[2:].zfill(7), end = "        ")
    for i in regs:
        print(bin(regs[i])[2:].zfill(16), end = " ")
        if i == "110":
            break
    print(regs["111"])
    regs["PC"] += 1
    return regs["PC"]

def or_op(inst):
    reg1 = inst[7:10]
    reg2 = inst[10:13]
    reg3 = inst[13:16]
    regs[reg1] = regs[reg2] | regs[reg3]
    print(bin(regs['PC'])[2:].zfill(7), end = "        ")
    for i in regs:
        print(bin(regs[i])[2:].zfill(16), end = " ")
        if i == "110":
            break
    print(regs["111"])
    regs["PC"] += 1
    return regs["PC"]

def and_op(inst):
    reg1 = inst[7:10]
    reg2 = inst[10:13]
    reg3 = inst[13:16]
    regs[reg1] = regs[reg2] & regs[reg3]
    print(bin(regs['PC'])[2:].zfill(7), end = "        ")
    for i in regs:
        print(bin(regs[i])[2:].zfill(16), end = " ")
        if i == "110":
            break
    print(regs["111"])
    regs["PC"] += 1
    return regs["PC"]

def not_op(inst):
    reg1 = inst[10:13]
    reg2 = inst[13:16]
    regs[reg1] = ~regs[reg2]
    print(bin(regs['PC'])[2:].zfill(7), end = "        ")
    for i in regs:
        print(bin(regs[i])[2:].zfill(16), end =" ")
        if i == "110":
            break
    print(regs["111"])
    regs["PC"] += 1
    return regs["PC"]

def cmp_op(inst):
    reg1 = inst[10:13]
    reg2 = inst[13:16]
    if regs[reg1] < regs[reg2]:
        setLess()
    elif regs[reg1] > regs[reg2]:
        setGreater()
    else:
        setEqual()
    print(bin(regs['PC'])[2:].zfill(7), end = "        ")
    for i in regs:
        print(bin(regs[i])[2:].zfill(16),end = " ")
        if i == "110":
            break
    print(regs["111"])
    regs["PC"] += 1
    return regs["PC"]


def jmp(inst):
    mem_addr = inst[9:]
    #store int value in PC
    regs["PC"] = int(mem_addr, 2)
    for key in memAddress:
        if memAddress[key] == inst:
            print(key, end = "        ")
            break
    for i in regs:
        print(bin(regs[i])[2:].zfill(16),end = " ")
        if i == "110":
            break
    print(regs["111"])
    return regs["PC"]


def jlt(inst):
    mem_addr = inst[9:]
    #if less than flag is set
    if regs["111"][-3] == "1":
        regs["PC"] = int(mem_addr, 2)
        clearFlag()
    else:
        regs["PC"] += 1
        clearFlag()
    for key in memAddress:
        if memAddress[key] == inst:
            print(key, end = "        ")
            break
    for i in regs:
        print(bin(regs[i])[2:].zfill(16),end = " ")
        if i == "110":
            break
    print(regs["111"])
    return regs["PC"]

def jgt(inst):
    mem_addr = inst[9:]
    #if greater than flag is set
    if regs["111"][-2] == "1":
        regs["PC"] = int(mem_addr, 2)
        clearFlag()
    else:
        regs["PC"] += 1
        clearFlag()
    for key in memAddress:
        if memAddress[key] == inst:
            print(key, end = "        ")
            break
    for i in regs:
        print(bin(regs[i])[2:].zfill(16),end = " ")
        if i == "110":
            break
    print(regs["111"])
    return regs["PC"]

def je(inst):
    mem_addr = inst[9:]
    #if equal flag is set
    if regs["111"][-1] == "1":
        regs["PC"] = int(mem_addr, 2)
        clearFlag()
    else:
        regs["PC"] += 1
        clearFlag()
    for key in memAddress:
        if memAddress[key] == inst:
            print(key, end = "        ")
            break
    for i in regs:
        print(bin(regs[i])[2:].zfill(16),end = " ")
        if i == "110":
            break
    print(regs["111"])
    return regs["PC"]

def halt(inst):
    for key in memAddress:
        if memAddress[key] == inst:
            print(key, end = "        ")
            break
    for i in regs:
        print(bin(regs[i])[2:].zfill(16),end = " ")
        if i == "110":
            break
    print(regs["111"])
    return regs["PC"]


k = "0000000"
for key in memAddress:
    inst = memAddress[key]
    opcode = inst[:5]
    if opcode == "00000" and k == key:
        k = bin(add(inst))[2:].zfill(7)
    elif opcode == "00001" and k == key:
        k = bin(sub(inst))[2:].zfill(7)
    elif opcode == "00010" and k == key:
        k = bin(movi(inst))[2:].zfill(7)
    elif opcode == "00011" and k == key:
        k = bin(mov(inst))[2:].zfill(7)
    elif opcode == "00100" and k == key:
        k = bin(ld(inst))[2:].zfill(7)
    elif opcode == "00101" and k == key:
        k = bin(st(inst))[2:].zfill(7)
    elif opcode == "00110" and k == key:
        k = bin(mul(inst))[2:].zfill(7)
    elif opcode == "00111" and k == key:
        k = bin(div(inst))[2:].zfill(7)
    elif opcode == "01000" and k == key:
        k = bin(rs(inst))[2:].zfill(7)
    elif opcode == "01001" and k == key:
        k = bin(ls(inst))[2:].zfill(7)
    elif opcode == "01010" and k == key:
        k = bin(xor(inst))[2:].zfill(7)
    elif opcode == "01011" and k == key:
        k = bin(or_op(inst))[2:].zfill(7)
    elif opcode == "01100" and k == key:
        k = bin(and_op(inst))[2:].zfill(7)
    elif opcode == "01101" and k == key:
        k = bin(not_op(inst))[2:].zfill(7)
    elif opcode == "01110" and k == key:
        k = bin(cmp_op(inst))[2:].zfill(7)
    elif opcode == "01111" and k == key:
        k = bin(jmp(inst))[2:].zfill(7)
    elif opcode == "11100" and k == key:
        k = bin(jlt(inst))[2:].zfill(7)
    elif opcode == "11101" and k == key:
        k = bin(jgt(inst))[2:].zfill(7)
    elif opcode == "11111" and k == key:
        k = bin(je(inst))[2:].zfill(7)
    elif opcode == "11010" and k == key:
        k = bin(halt(inst))[2:].zfill(7)
    else:
        continue

for key in memAddress:
    print(memAddress[key])