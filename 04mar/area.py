
import shape as s
# Main program
area = True
while area:
	print("Enter 1 to calculate the area of a circle")
	print("Enter 2 to calculate the area of a triangle")
	print("Enter 3 to calculate the area of a square")
	print("Enter 4 to calculate the area of a rectangle")
	print("Enter 5 to terminate the program")

	choice = int(input("Enter your choice: "))

	if choice == 1:
		radius = float(input("Enter radius: "))
		print("Area of circle =", s.circle_area(radius))
	elif choice == 2:
		base = float(input("Enter base: "))
		height = float(input("Enter height: "))                                                
		print("Area of triangle =", s.triangle_area(base, height))
	elif choice == 3:
		side = float(input("Enter side length: "))
		print("Area of square =", s.square_area(side))
	elif choice == 4:
		length = float(input("Enter length: "))
		breadth = float(input("Enter breadth: "))
		print("Area of rectangle =", s.rectangle_area(length, breadth))
	elif choice == 5:
		area = False
	else:
		print("Invalid Choice")

print("Program terminated")
