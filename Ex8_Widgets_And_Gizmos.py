# Exercise 8:Widgets and Gizmos
# An online retailer sells two products: widgets and gizmos. Each widget weighs 75
# grams. Each gizmo weighs 112 grams. Write a program that reads the number of
# widgets and the number of gizmos in an order from the user. Then your program
# should compute and display the total weight of the order.
number_of_widgets = int(input("Enter the number of widgets: "))
number_of_gizmos = int(input("Enter the number of gizmos: "))
total_weight = int((number_of_widgets * 75) + (number_of_gizmos * 112))
print("Total weight (in grams):", total_weight)
