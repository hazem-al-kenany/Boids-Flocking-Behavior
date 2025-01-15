# Boids Simulation: Flocking Behavior in a 2D Space

This project simulates the flocking behavior of **boids** (bird-like agents) in a 2D space using simple rules for separation, alignment, and cohesion. The simulation showcases emergent behaviors such as flock formation and movement dynamics.

---

## Features

### Boid Behavior
- **Separation**:
  - Ensures boids maintain a safe distance from nearby boids.
- **Alignment**:
  - Aligns each boid's velocity with its neighbors to achieve collective movement.
- **Cohesion**:
  - Guides boids towards the center of mass of their neighbors to maintain group cohesion.

### Environment
- **2D Toroidal Grid**:
  - The simulation is bounded, with positions wrapping around the edges of the grid.
  - Grid size: `200x200`.
- **Dynamic Visualization**:
  - The movement of boids is visualized in real time using Matplotlib animations.

---

## Code Structure

### Key Classes and Functions

#### **Boid Class**
- **Attributes**:
  - `position`: The current position of the boid.
  - `velocity`: The current velocity of the boid.
- **Methods**:
  - `update_position`: Updates the boid's position based on its velocity and wraps around boundaries.

#### **Behavior Functions**
- **`separation(boid, boids)`**:
  - Calculates a steering force to avoid crowding by other nearby boids.
- **`alignment(boid, boids)`**:
  - Calculates a steering force to align the boid's velocity with its neighbors.
- **`cohesion(boid, boids)`**:
  - Calculates a steering force to move the boid towards the center of mass of its neighbors.

#### **Utility Functions**
- **`limit_speed(velocity)`**:
  - Limits a boid's speed to the maximum allowed value.

#### **Visualization**
- **Matplotlib Animation**:
  - Updates the positions of boids in real time and renders their movement.

---

## Simulation Parameters

- **Grid Size**: `200x200`.
- **Number of Boids**: `20`.
- **Maximum Speed**: `2` units per frame.
- **Perception Radius**: `20` units.
- **Weights**:
  - Separation: `1.5`.
  - Alignment: `1.0`.
  - Cohesion: `1.0`.

---

## How to Run

### Prerequisites
- Python 3.7 or higher.
- Required libraries:
  ```bash
  pip install matplotlib numpy
