---
title: "CONTAINERIZING STACKS"
date: "2026-03-30"
summary: "Setting up multi-stage alpine builds for rust and node microservices..."
thumbnail: "images/lod_planets.png"
---
# Containerizing stacks

To deploy retro software or modern microservices reliably, we use Docker. This log discusses optimizing size using multi-stage builds.

## Multi-Stage Concept

Instead of shipping compiler toolchains inside the final runner image, we separate the build stage from the execution stage. This keeps production images incredibly small and secure.

Here is a standard example for a Rust microservice:

```dockerfile
# Stage 1: Build binary
FROM rust:1.80-alpine AS builder
RUN apk add --no-cache musl-dev
WORKDIR /app
COPY . .
RUN cargo build --release

# Stage 2: Minimal runner
FROM alpine:3.18
WORKDIR /app
COPY --from=builder /app/target/release/microservice .
CMD ["./microservice"]
```

Using this approach, the final runtime container is reduced from over `1.5 GB` down to just `15 MB`!
