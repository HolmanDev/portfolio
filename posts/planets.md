---
title: "PRODUCING PLANETS IN C#"
date: "2026-05-18"
summary: "Optimizing Level of Detail (LOD) planet meshes with octrees in Unity..."
thumbnail: "images/lod_planets.png"
---
# Producing Planets in C#

Generating realistic planetary bodies in real-time requires smart data structures and procedural generation techniques. This post covers the design of an **Octree-based Level of Detail (LOD)** system implemented in Unity.

## Core Architecture

To render massive planets without exhausting GPU memory, we divide the planet's sphere into 6 quadtree faces (forming a cube map), and project them onto a sphere. As the camera gets closer:
1. We subdivide the quadtree nodes.
2. We request new noise heights for vertices.
3. We generate high-res mesh chunks on background worker threads.

Here is a simplified C# snippet demonstrating subdivision checking:

```csharp
public void UpdateNode(Vector3 cameraPosition) {
    float distance = Vector3.Distance(cameraPosition, center);
    if (distance < subdivideDistance && depth < maxDepth) {
        Subdivide();
    } else if (distance > collapseDistance && isSubdivided) {
        Collapse();
    }
}
```

## Visualizing Heightfields

We use a layered 3D Perlin and simplex noise pipeline to generate realistic continents, mountains, and ocean trenches.

![LOD Planet Generation Example](images/lod_planets.png)

This mesh calculation is offloaded to jobs using the C# Job System, compiling down to highly optimized native code with Burst Compiler.
