#BMI calculator
name_1= "Pedro"
height_m1= 2
weight_kg1= 67

name_2= "Pedro's sister"
height_m2= 1.7
weight_kg2= 56

name_3="Pedro's brother"
height_m3= 2.5
weight_kg3= 160

def bmi_calculator(name,height_m,weight_kg):
    bmi= weight_kg / (height_m**2)
    print ("bmi: ")
    print (bmi)
    if bmi<25:
        return name + " is not overweight"
    else:
        return name + " is overweight"
result1 = bmi_calculator(name_1,height_m1,weight_kg1)
result2 = bmi_calculator(name_2,height_m2,weight_kg2)
result3 = bmi_calculator(name_3,height_m3,weight_kg3)
        
print(result1)       
print(result2)       
print(result3)   
