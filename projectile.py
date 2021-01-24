import math

gravity = 9.81
velocity = 44
angle = 80
distance = 0.5
height = 1

angle_in_radians = angle * (math.pi / 180)
y = height + distance * math.tan(angle_in_radians) - gravity * distance**2 \
    / (2 * velocity * math.cos(angle_in_radians))**2

print(y)
