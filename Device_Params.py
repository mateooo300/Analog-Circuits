task = int(input("Choose a Calculation: \n1: Width \n2: Gm  \n3: Go \n4: Cdb \n5: Cgd \n"))
			    
			   
if task == 1:
	W_C = input("PMOS or NMOS?")

	if W_C == "P":
		A_in = float(input("Enter Current: "))
		A = A_in*.000001
		Kin = float(input("Enter uCox/2 (Converts whole number to u): "))
		K = Kin * .000001
		V_ov = float(input("Enter Vov: "))
		Lin = float(input("Enter device length(Converts whole number to u): "))
		L = Lin * .000001
		Width_X = (A*L)/((V_ov*V_ov)*K)
		Width = "{:e}".format(Width_X)

	M = input("Mirror: Y/N?")

	if M == "Y":
		Multiplier = float(input("Enter multiplier: "))
		Width_M = Width_X*Multiplier
		print("{:e}".format(Width_M))
	if M == "N":
		print (Width)


	if W_C == "N":
		A_in = float(input("Enter Current: "))
		A = A_in*.000001
		Kin = float(input("Enter uCox/2 (Converts whole number to u): "))
		K = Kin * .000001
		V_ov = float(input("Enter Vov: "))
		Lin = float(input("Enter device length(Converts whole number to u): "))
		L = Lin * .000001
		Width_X = (A*L)/((V_ov*V_ov)*K)
		Width = "{:e}".format(Width_X)

	M = input("Mirror: Y/N?")

	if M == "Y":
		Multiplier = float(input("Enter multiplier: "))
		Width_M = Width_X*Multiplier
		print("{:e}".format(Width_M))
	if M == "N":
		print (Width)

elif task == 2:
	A_in = float(input("Enter Current: "))
	A = A_in*.000001
	Multiplier = float(input("Enter multiplier(if none enter '1': "))
	A_M = A*Multiplier
	V_ov = float(input("Enter Vov: "))
	Gm_X = (2*A_M)/(V_ov)
	Gm = "{:e}".format(Gm_X)
	print ("gm: " + Gm)



elif task == 3:
	A_in = float(input("Enter Current: "))
	A = A_in*.000001
	Multiplier = float(input("Enter multiplier(if none enter '1': "))
	A_M = A*Multiplier
	Lambda = float(input("Enter Lambda: "))
	Go_X = A_M*Lambda
	Go = "{:e}".format(Go_X)
	print ("go: " + Gm)


elif task == 4:
	Cjo = float(input("Enter Cjo(standard notation): "))
	Lin = float(input("Enter device length(Converts whole number to u): "))
	L = Lin * .000001
	Win = float(input("Enter device Width(Converts whole number to u): "))
	W = Win * .000001
	Vr = float(input("Enter Reverse Voltage: "))
	Pb = float(input("Enter PB (if unknown enter .7): "))
	Mj = float(input("Enter MJ (If unknown enter .5): "))
	Cdbx = (Cjo*W*L)/((1+(Vr/Pb))^Mj)

	Cdb = "{:e}".format(Cdbx)
	print ("Cdb: " + Cdb)


elif task == 5:
	Cdgo = float(input("Enter Cdgo(standard notation): "))
	Win = float(input("Enter device Width(Converts whole number to u): "))
	W = Win * .000001
	Cgdx = Cdgo*W

	Cdg = "{:e}".format(Cgdx)
	print("Cdg: " + Cdg)


