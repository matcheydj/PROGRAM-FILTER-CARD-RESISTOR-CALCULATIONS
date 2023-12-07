pip install pygame
# pip install pygame
# In this version, the program checks the direction of each axis (x, y, z, a, b, c, d) and prints a message accordingly. It also checks if the keys Y, N, and M (represented as buttons 0, 1, and 2) are pressed.

import pygame

pygame.init()

# Initialize the joystick
pygame.joystick.init()

try:
    # We assume that you have only one joystick maybe plugged
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
except pygame.error:
    print("Couldn't detect any joystick")
    exit()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # Assume axis 0 for x, 1 for y, 2 for z, 3 for a, 4 for b, 5 for c, and 6 for d
    axes = ['x', 'y', 'z', 'a', 'b', 'c', 'd']
    for i in range(7):
        direction = joystick.get_axis(i)
        try:
            if direction > 0:
                print(f"Not Bad! ({axes[i]}-axis)")
            elif direction < 0:
                print(f"Not Dad! ({axes[i]}-axis)")
        except Exception as e:
            print(f"An error occurred: {e}")

    # Assume button 0 for Y, 1 for N, and 2 for M
    keys = ['Y', 'N', 'M']
    for i in range(3):
        if joystick.get_button(i):
            print(f"Key {keys[i]} pressed!")

# Trial period over trying some more
print "Trying Something!"
          
import subprocess
import pygame

# Try to import pygame, and install it if it's not found
try:
    import pygame
except ImportError:
    subprocess.check_call(["python", '-m', 'pip', 'install', 'pygame'])
    import pygame

pygame.init()

# Initialize the joystick
pygame.joystick.init()

try:
    # We assume that you have only one joystick
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
except pygame.error:
    print("Couldn't detect any joystick")
    exit()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # Assume axis 0 for x, 1 for y, 2 for z, 3 for a, 4 for b, 5 for c, and 6 for d
    axes = ['x', 'y', 'z', 'a', 'b', 'c', 'd']
    for i in range(7):
        direction = joystick.get_axis(i)
        try:
            if direction > 0:
                print(f"Not Bad! ({axes[i]}-axis)")
            elif direction < 0:
                print(f"Not Dad! ({axes[i]}-axis)")
        except Exception as e:
            print(f"An error occurred: {e}")

    # Assume button 0 for Y, 1 for N, and 2 for M
    keys = ['Y', 'N', 'M']
    for i in range(3):
        if joystick.get_button(i):
            print(f"Key {keys[i]} pressed!")

          # Get Pressed!
          # Please note that running pip install within a script requires the appropriate permissions. If you’re running this script in an environment where you don’t have permission to install packages, this will fail. Always make sure you have the necessary permissions when attempting to install Python packages.
elif set x=1
try:
  x/0 = y
y/x = 1
x = 1/0
except ThereIsNoTry:
print("You can't try!")
      exit()
