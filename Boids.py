import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

grid_size = 200
num_boids = 20
max_speed = 2
perception_radius = 20
separation_weight = 1.5
alignment_weight = 1.0
cohesion_weight = 1.0

class boid:
    def __init__(self):
        self.position = np.random.rand(2) * grid_size
        self.velocity = (np.random.rand(2) - 0.5) * 2 #random positions and velocities

    def update_position(self):
        self.position += self.velocity
        self.position %= grid_size #wrap around boundary

def separation(boid, boids): #calculate separation force
    steer = np.zeros(2)
    for other in boids:
        distance = np.linalg.norm(boid.position - other.position)
        if 0 < distance < perception_radius / 2:
            steer += (boid.position - other.position) / distance
    return steer * separation_weight

def alignment(boid, boids): #calculate alignment force
    avg_velocity = np.zeros(2)
    total = 0
    for other in boids:
        distance = np.linalg.norm(boid.position - other.position)
        if distance < perception_radius:
            avg_velocity += other.velocity
            total += 1
    if total > 0:
        avg_velocity /= total
        return (avg_velocity - boid.velocity) * alignment_weight
    return np.zeros(2)

def cohesion(boid, boids): #calculate cohesion force
    center_of_mass = np.zeros(2)
    total = 0
    for other in boids:
        distance = np.linalg.norm(boid.position - other.position)
        if distance < perception_radius:
            center_of_mass += other.position
            total += 1
    if total > 0:
        center_of_mass /= total
        return (center_of_mass - boid.position) * cohesion_weight
    return np.zeros(2)

def limit_speed(velocity):
    speed = np.linalg.norm(velocity)
    if speed > max_speed:
        return (velocity / speed) * max_speed
    return velocity

boids = [boid() for _ in range(num_boids)] #initialize boids

fig, ax = plt.subplots() #visualization setup
scat = ax.scatter([], [], s=50, c='blue', marker='o')
ax.set_xlim(0, grid_size)
ax.set_ylim(0, grid_size)

def update(frame): #update function for animation
    global boids
    positions = []
    for b in boids:
        #calculate forces
        sep = separation(b, boids)
        ali = alignment(b, boids)
        coh = cohesion(b, boids)

        b.velocity += sep + ali + coh
        b.velocity = limit_speed(b.velocity)
        b.update_position() #update velocity and position

        positions.append(b.position)

    #update positions
    positions = np.array(positions)
    scat.set_offsets(positions)
    return scat,

ani = FuncAnimation(fig, update, interval=50, blit=True)
plt.show()