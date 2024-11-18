import math


def calculate_density():
    mass = float(input("Enter mass (kg): "))  # Get mass input
    volume = float(input("Enter volume (m^3): "))  # Get volume input
    density = mass / volume
    print(f"Value of Density (Density = mass / volume): {density} kg/m³")


def calculate_gravitational_force():
    g = 6.67430e-11  # Gravitational constant in N(m^2/kg^2)
    m1 = float(input("Enter mass of first object (kg): "))  # Get mass of first object
    m2 = float(input("Enter mass of second object (kg): "))  # Get mass of second object
    r = float(input("Enter distance between the two objects (m): "))  # Get distance between objects
    force = g * (m1 * m2) / r**2
    print(f"Value of Gravitational Force (F = G * (m1 * m2) / r^2): {force} N")


def calculate_hypotenuse():
    a = float(input("Enter side a (m): "))  # Get side 'a' input
    b = float(input("Enter side b (m): "))  # Get side 'b' input
    c = (a**2 + b**2)**0.5
    print(f"Value of Hypotenuse (a^2 + b^2 = c^2): {c} m")


def calculate_quadratic_roots():
    a = float(input("Enter coefficient a: "))  # Get coefficient a input
    b = float(input("Enter coefficient b: "))  # Get coefficient b input
    c = float(input("Enter coefficient c: "))  # Get coefficient c input
    discriminant = b**2 - 4 * a * c
    if discriminant >= 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print(f"Value of Quadratic Roots (x = (-b ± sqrt(b^2 - 4ac)) / 2a): {x1}, {x2}")
    else:
        print("No real solutions for the quadratic equation.")


def calculate_kinetic_energy():
    mass = float(input("Enter mass (kg): "))  # Get mass input
    velocity = float(input("Enter velocity (m/s): "))  # Get velocity input
    ke = 0.5 * mass * velocity**2
    print(f"Value of Kinetic Energy (KE = 0.5 * m * v^2): {ke} J")

# Call all the functions to display results:
calculate_density()
calculate_gravitational_force()
calculate_hypotenuse()
calculate_quadratic_roots()
calculate_kinetic_energy()