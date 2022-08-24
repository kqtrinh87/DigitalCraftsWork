
# name = "ada lovelace" # Variable into string
# print(name.title()) # Print name with title format, which capitalize each word
# print(name.upper()) # Print name with upper format, which captialize every letters.
# print(name.lower()) # Print name with lower format, which lowercase all letters.


# first_name = "ada"
# last_name = "lovelace"
# full_name = first_name + " " + last_name
# print(full_name)

# print("Python")
# print("\tPython") # \t is Tab
# print("Languages:\n\tPython\n\tC\n\tJavaScript")

# age = 23
# message = "Happy " + str(age) + "rd Birthday!"
# print(message)

# bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# print(bicycles)
# print(bicycles[0].title()) # Typing .title with variable help captialize it.
# print(bicycles[-1]) # Negative starts from the end
# message = "My first bicycle was a " + bicycles[0].title() + "."
# print(message)

# motorcycles = ['honda','yamaha','suzuki','ducati']
# print(motorcycles)
# motorcycles.remove('yamaha')
# print(motorcycles)

# vacationSpots = ['Tokyo', 'Paris', 'Washington D.C.', 'Mumbai', 'Cape Town']
# print('Original List: ' + str(vacationSpots))
# print('Sort List: ' + str(vacationSpots.sort()))
# print('Reserve Sort List: ' + str(vacationSpots.sort() reverse=True))

cars = ['bmw','subaru', 'toyoya', 'audi']

print("Here's the original list:")
print(cars)

print("\nHereis the sorted list:")
print(sorted(cars))

print("\nHere's the reserved list:")
print(sorted(cars.reverse())) # Need to reverse individually
cars.reverse()
