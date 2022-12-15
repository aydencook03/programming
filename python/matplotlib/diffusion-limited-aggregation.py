import numpy as np
import matplotlib.pyplot as plt

# sim parameters
grid_size = 400
particle_count = 100000
circle_radius = 180
distance_std = 360

# initialize grid
grid = np.zeros(shape=(grid_size, grid_size))
middle = int(grid_size/2 - 1)
grid[middle, middle] = 1

# release and simulate particles
for i in range(particle_count):
    angle = np.random.uniform(0, 2*np.pi)
    x, y = int(circle_radius * np.cos(angle) + middle), int(circle_radius * np.sin(angle) + middle)
    
    walking = True
    to_travel = int(np.random.normal(0, distance_std))
    traveled = 0
    
    while walking and (abs(traveled) < abs(to_travel)):
        # check neighboring cells. stick to any active ones
        if grid[x-1, y+1] or grid[x, y+1] or grid[x+1, y+1] or grid[x-1, y] or grid[x+1, y] or grid[x-1, y-1] or grid[x, y-1] or grid[x+1, y-1]:
            grid[x, y] = 1
            walking = False
        # pick travel direction
        if np.random.choice([0, 1]) == 0:
            xv = int(to_travel / abs(to_travel))
            yv = 0
        else:
            xv = 0
            yv = int(to_travel / abs(to_travel))
        x += xv
        y += yv
        traveled += int(to_travel / abs(to_travel))
        # stop walking if exiting the circle
        if (x-middle)**2 + (y-middle)**2 > circle_radius**2:
            walking = False
        
plt.imshow(grid)
plt.show()
