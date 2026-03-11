import alchemy.elements
import alchemy

print("=== Sacred Scroll Mastery ===")

print("\nTesting direct module access:")
print("alchemy.elements.create_fire():", alchemy.elements.create_fire())
print("alchemy.elements.create_water():", alchemy.elements.create_water())
print("alchemy.elements.create_earth():", alchemy.elements.create_earth())
print("alchemy.elements.create_air():", alchemy.elements.create_air())
try:
    c_earth = alchemy.create_earth()
except AttributeError:
    c_earth = "AttributeError - not exposed"
try:
    c_air = alchemy.create_air()
except AttributeError:
    c_air = "AttributeError - not exposed"
print("\nTesting package-level acess (controlled by __init__.py):")
print("alchemy.create_fire():", alchemy.create_fire())
print("alchemy.create_water():", alchemy.create_water())
print("alchemy.create_earth():", c_earth)
print("alchemy.create_air():", c_air)

print("\nPackage metadata")
print("Version:", alchemy.__version__)
print("Author:", alchemy.__author__)
