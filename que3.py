# Write a program to input the marks of 5 subjects and display the total and average marks.
maths=int(input("Enter a Marks Obtain In Maths:"))
science=int(input("Enter a Marks  obtain in Science:"))
sst=int(input("Enter a maks obtain in SST:"))
marathi=int(input("Enter a marks obtain in Marathi:"))
hindi=int(input("Enter a marks obtain in Hindi:"))
total=maths + science + sst + marathi + hindi 
Average=total/5
print("The total Marks obtain is :",total,"Average Marks is :",Average)