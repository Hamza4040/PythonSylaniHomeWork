print('-------------------------------------------------------')
print('\t\t\tMARK SHEET APP')
print('-------------------------------------------------------\n')
print('Enter your marks to generate marksheet')

Maths=float(input('Mathematics Marks(Total=100): '))
Physics=float(input('Physics Marks(Total=100): '))
Islamiat=float(input('Islamiat Marks(Total=100): '))
English=float(input('English Marks(Total=100): '))
Chemistry=float(input('Chemistry Marks(Total=100): '))
totalMarks=500

n=Maths+Physics+Islamiat+English+Chemistry
Percentage=(n/totalMarks)*100

if Percentage>=90:
    print("A-One Grade",Percentage,"%")
elif Percentage>=80:
    print("A Grade",Percentage,"%")
elif Percentage>=70:
    print("B Grade",Percentage,"%")
elif Percentage>=60:
    print("C Grade",Percentage,"%")
elif Percentage>=50:
    print("D Grade",Percentage,"%")
else:
    print("Fail",Percentage,"%")
