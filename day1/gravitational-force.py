# Gravitational force is the attractive force that exists between two masses. 
# Calculate the gravitational force between Earth and the Moon

G = 6.67 * (10 ** -11)
r = 3.84 * (10 ** 8)

# Earth mass
M = 6.0 * (10 ** 24)

# Moon mass
m = 7.34 * (10 ** 22)

grav_force = (G * M * m) / (r ** 2)
print(grav_force)