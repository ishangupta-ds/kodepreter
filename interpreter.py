import re
import os

def generate_lines(address):
	f_open=open(address, "r")
	arr=str(f_open.read()).split('\n')
	lines=[]
	for i in arr:
		if i.find('koderunners')!=-1:
			lines.append(i.lower())
		else:
			lines.append(i)
	return lines


def generate_opcode(lines):
	opcode=[]
	for i in lines:
		if i.find('koderunners')!=-1:
			opcode.append(len(re.findall(r'koderunners', i)))
		elif i.find('X')!=-1:
			opcode.append(len(re.findall(r'X', i)))
		elif len(i.strip())<1:
			opcode.append(0)
	return opcode


def interpret_opcode(opcode):
	i=0
	while i<len(opcode):

		# quit the program
		if opcode[i]==0:
			quit()

		# Add top 2 numbers
		elif opcode[i]==1:
			if len(memory)<2:
				print("ERROR: Stack UnderFlow!!!")
				quit()
			else:
				top=memory[len(memory)-1]
				topnext=memory[len(memory)-2]
				if top.isdigit() and topnext.isdigit():
					memory.append(str(float(top)+float(topnext)))
				else:
					print("ERROR: TypeError!!!")
					quit()

		# subtract top 2 numbers(top - topnext)
		elif opcode[i]==2:
			if len(memory)<2:
				print("ERROR: Stack UnderFlow!!!")
				quit()
			else:
				top=memory[len(memory)-1]
				topnext=memory[len(memory)-2]
				if top.isdigit() and topnext.isdigit():
					memory.append(str(float(top)-float(topnext)))
				else:
					print("ERROR: TypeError!!!")
					quit()

		# multiply top 2 numbers
		elif opcode[i]==3:
			if len(memory)<2:
				print("ERROR: Stack UnderFlow!!!")
				quit()
			else:
				top=memory[len(memory)-1]
				topnext=memory[len(memory)-2]
				if top.isdigit() and topnext.isdigit():
					memory.append(str(float(top)*float(topnext)))
				else:
					print("ERROR: TypeError!!!")
					quit()

		# divide top 2 numbers(top / topnext)
		elif opcode[i]==4:
			if len(memory)<2:
				print("ERROR: Stack UnderFlow!!!")
				quit()
			else:
				top=memory[len(memory)-1]
				topnext=memory[len(memory)-2]
				if top.isdigit() and topnext.isdigit():
					memory.append(str(float(top)/float(topnext)))
				else:
					print("ERROR: TypeError!!!")
					quit()

		# top % topnext
		elif opcode[i]==5:
			if len(memory)<2:
				print("ERROR: Stack UnderFlow!!!")
				quit()
			else:
				top=memory[len(memory)-1]
				topnext=memory[len(memory)-2]
				if top.isdigit() and topnext.isdigit():
					memory.append(str(float(top)%float(topnext)))
				else:
					print("ERROR: TypeError!!!")
					quit()

		# top == topnext
		elif opcode[i]==6:
			if len(memory)<2:
				print("ERROR: Stack UnderFlow!!!")
				quit()
			else:
				top=memory[len(memory)-1]
				topnext=memory[len(memory)-2]
				if top.isdigit() and topnext.isdigit():
					memory.append(str(float(top)==float(topnext)))
				else:
					memory.append(str(top==topnext))

		# top != topnext
		elif opcode[i]==7:
			if len(memory)<2:
				print("ERROR: Stack UnderFlow!!!")
				quit()
			else:
				top=memory[len(memory)-1]
				topnext=memory[len(memory)-2]
				if top.isdigit() and topnext.isdigit():
					memory.append(str(float(top)!=float(topnext)))
				else:
					memory.append(str(top!=topnext))

		# top < topnext
		elif opcode[i]==8:
			if len(memory)<2:
				print("ERROR: Stack UnderFlow!!!")
				quit()
			else:
				top=memory[len(memory)-1]
				topnext=memory[len(memory)-2]
				if top.isdigit() and topnext.isdigit():
					memory.append(str(float(top)<float(topnext)))
				else:
					memory.append(str(len(top)<len(topnext)))

		# top > topnext
		elif opcode[i]==9:
			if len(memory)<2:
				print("ERROR: Stack UnderFlow!!!")
				quit()
			else:
				top=memory[len(memory)-1]
				topnext=memory[len(memory)-2]
				if top.isdigit() and topnext.isdigit():
					memory.append(str(float(top)>float(topnext)))
				else:
					memory.append(str(len(top)>len(topnext)))

		# top & topnext
		elif opcode[i]==10:
			if len(memory)<2:
				print("ERROR: Stack UnderFlow!!!")
				quit()
			else:
				top=memory[len(memory)-1]
				topnext=memory[len(memory)-2]
				if top.isdigit() and topnext.isdigit():
					memory.append(str(float(top) & float(topnext)))
				else:
					print("ERROR: TypeError!!!")
					quit()

		# top ! topnext
		elif opcode[i]==11:
			if len(memory)<2:
				print("ERROR: Stack UnderFlow!!!")
				quit()
			else:
				top=memory[len(memory)-1]
				topnext=memory[len(memory)-2]
				if top.isdigit() and topnext.isdigit():
					memory.append(str(float(top) | float(topnext)))
				else:
					print("ERROR: TypeError!!!")
					quit()

		# not top
		elif opcode[i]==12:
			if len(memory)<1:
				print("ERROR: Stack UnderFlow!!!")
				quit()
			else:
				top=memory[len(memory)-1]
				topnext=memory[len(memory)-2]
				if top.isdigit() and topnext.isdigit():
					memory.append(str(not float(top)))
				else:
					print("ERROR: TypeError!!!")
					quit()

		# input
		elif opcode[i]==13:
			inp=str(input())
			memory.append(inp)

		# output
		elif opcode[i]==14:
			if len(memory)<1:
				print("ERROR: Stack UnderFlow!!!")
				quit()
			else:
				print(memory[len(memory)-1])

		i+=1


# Driver Code
memory=[]
print("Enter the address: ", end="")
address=input()
lines=generate_lines(address)
opcodes=generate_opcode(lines)
print(opcodes)
interpret_opcode(opcodes)