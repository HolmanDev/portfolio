---
title: "EXPLORING SHADER GRAPH"
date: "2026-05-10"
summary: "Custom vertex displacement shaders for fluid water surfaces..."
thumbnail: "images/physics_vehicles.png"
---
# Exploring Shader Graph

Procedural styling is a cornerstone of retro and modern games alike. This post details how to implement vertex displacement to simulate realistic water ripples using Unity's Shader Graph or raw HLSL.

## Vertex Displacement Formula

To simulate fluid wave dynamics, we displace the vertex position along its normal using a combination of sine waves:

$$y = A \sin(k \cdot x - \omega \cdot t)$$

Where:
- $A$ is the amplitude
- $k$ is the wave number (spatial frequency)
- $\omega$ is the angular frequency (speed)

## Implementation Steps

1. **Create the Time Node**: Connect it to a multiply node to control wave speed.
2. **Combine Noise Layers**: Combine a tiling gradient noise with simple sine waves to add complexity.
3. **Displace Vertices**: Multiply the noise output by the vertex normal vector and add it to the position.

![Shader Graph Demo](images/physics_vehicles.png)

This visual effect brings flat plane geometry to life, creating interactive environments with minimal performance overhead.
