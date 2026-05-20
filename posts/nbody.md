---
title: "N-BODY GRAVITY SIMULATION"
date: "2026-04-28"
summary: "Writing custom Euler integration methods for multi-body orbital tracks..."
thumbnail: "images/nbody_simulation.png"
---
# N-Body Gravity Simulation

Simulating gravitational interactions between multiple astronomical bodies (like stars and planets) is a classic problem in computational physics. This post covers the mathematical and algorithmic design behind our `NBSS.EXE` python simulation.

## Newtonian Mechanics

For any body $i$, the net gravitational force exerted by all other bodies $j$ is calculated as:

$$\vec{F}_i = G m_i \sum_{j \neq i} \frac{m_j (\vec{r}_j - \vec{r}_i)}{|\vec{r}_j - \vec{r}_i|^3}$$

To resolve acceleration and update positions, we can use numerical integration methods such as Euler-Cromer or Verlet.

## Code Design

Here is a look at the core integration loop implemented in Python:

```python
def update_bodies(bodies, dt):
    # Compute force vectors
    forces = [np.zeros(3) for _ in bodies]
    for i, b1 in enumerate(bodies):
        for j, b2 in enumerate(bodies):
            if i == j: continue
            diff = b2.pos - b1.pos
            dist = np.linalg.norm(diff)
            # Softening factor to avoid infinity at close range
            force_mag = G * b1.mass * b2.mass / (dist**2 + softening**2)
            forces[i] += force_mag * (diff / dist)
            
    # Update velocities and positions
    for i, b in enumerate(bodies):
        accel = forces[i] / b.mass
        b.vel += accel * dt
        b.pos += b.vel * dt
```

## Performance Scaling

![N-Body simulation screen](images/nbody_simulation.png)

Using naive $O(N^2)$ direct computation, the simulation handles up to a few thousand bodies in real-time. For higher counts, we can optimize by employing a **Barnes-Hut octree** which reduces complexity to $O(N \log N)$.
