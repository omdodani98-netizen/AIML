#simple interest calculator 
principal = float(input("Enter the main amount"))
rate = float(input("Enter Rate of interest"))
time = float(input("Enter duration"))

# formula used SI = ( principal * rate * time ) / 100
SI = (principal*rate*time)/100
print("The SI is " , SI)
