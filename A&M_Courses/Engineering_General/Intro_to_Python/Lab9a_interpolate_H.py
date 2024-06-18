# 	     By submitting this assignment I agree to the following
#          “Aggies do not, lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
#Name			Hunter Spier, Vishruth Balaji, Michael Camacho, Liliana Salgado
#Section		501
#Assignment		Lab9a_interpolate
#Date			10/19/2020

user_temp = float(input('Enter a temperature between 0 and 260 C: '))
user_pressure = float(input('Enter a pressure between 5 and 10 MPa: '))

f = open('Lab9a_ThermoProperties.csv', 'r')

values_list = []

values_list_P5 = []

values_list_P10 = []

# Create list of rows

for i in range(33):
    values_list.append(f.readline())

# Create list of rows coresponding to each temperature

for row in range(2,16):
    values_list_P5.append(values_list[row])


for row in range(19,33):
    values_list_P10.append(values_list[row])

# Separate rows into columns

for row in range(len(values_list_P5)):
    rows = values_list_P5[row].split(',')
    values_list_P5[row] = []
    for i in range(len(rows)):
        rows[i] = float(rows[i])
    for i in range(len(rows) - 1):
        values_list_P5[row].append(rows[i +1])
    
for row in range(len(values_list_P10)):
    rows = values_list_P10[row].split(',')
    values_list_P10[row] = []
    for i in range(len(rows)):
        rows[i] = float(rows[i])
    for i in range(len(rows) - 1):
        values_list_P10[row].append(rows[i +1])

# Linearly Interpolate for Temperature

def lin_int_temp(Plist):
    lin_int = []
    for variable in range(4):
        i = int(user_temp//20)
        m = user_temp % 20
        print(m)
        lin_int.append(((m * (Plist[i+1][variable] - Plist[i][variable]))/20) + Plist[i][variable])
    return lin_int


# Linearly Interpolate for Pressure
P5_interpolated_values = lin_int_temp(values_list_P5)

P10_interpolated_values = lin_int_temp(values_list_P10)

final_list = []

for variable in range(4):
    final_list.append((user_pressure * (P10_interpolated_values[variable] - P5_interpolated_values[variable]))/10 + P5_interpolated_values[variable])
    
# Print final answer

print('Properties at {} C and {} MPa are:\nSpecific volume (m^3/kg): {:.7f}\nSpecific internal energy (kJ/kg): {:.2f}\nSpecific enthalpy (kJ/kg): {:.2f}\nSpecific entropy (kJ/kgK): {:.4f}'.format(user_temp, user_pressure, final_list[0], final_list[1], final_list[2], final_list[3]))

f.close()










