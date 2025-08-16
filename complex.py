real1=float(input("Enter the real part of the first complex number:"))
image1=float(input("Enter the imaginary part of the first complex number:"))
real2=float(input("Enter the real part of the second complex number:"))
image2=float(input("Enter the imaginary part of the second complex number:"))

c1=complex(real1,image1)
c2=complex(real2,image2)

sum_result=c1+c2
product_result=c1*c2

print(f"The sum of {c1} and{c2}is {sum_result}")
print(f"The product of {c1} and{c2}is {product_result}")
