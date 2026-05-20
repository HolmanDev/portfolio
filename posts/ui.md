---
title: "RETRO OS WEB DESIGN"
date: "2026-04-15"
summary: "How to style classic DOS/Win16-like interfaces using modern CSS grid..."
thumbnail: "images/player_controller.png"
---
# Retro OS Web Design

Bringing nostalgic styles from the 80s and 90s to the web is a fun exercise in CSS control. This post discusses the styling tokens and design principles used to construct `PORTFOLIO.EXE`.

## Design Rules

1. **Monospace Typography**: Always use pixelated/monospaced fonts like *Press Start 2P* or standard Courier.
2. **Beveled Borders**: Emulate old windows by using heavy borders with varying colors to represent lighting (e.g. gold, yellow, and dark lines).
3. **Strict Grid Layouts**: Retro interfaces relied on strict grids and window regions rather than flowing flexboxes. Using CSS grid helps maintain this rigidity.

```css
.frame {
  display: grid;
  grid-template-rows: auto 1fr auto;
  border: 6px solid var(--gold);
}
```

## Creating Retro Elements

Using custom linear gradients, we can emulate CRT monitor scanlines:

```css
body::after {
  content: '';
  position: fixed;
  inset: 0;
  background: repeating-linear-gradient(
    0deg, transparent, transparent 2px,
    rgba(0,0,0,0.05) 2px, rgba(0,0,0,0.05) 4px
  );
  pointer-events: none;
}
```

This simple overlay gives the webpage a CRT glow that completes the retro desktop visual experience!
