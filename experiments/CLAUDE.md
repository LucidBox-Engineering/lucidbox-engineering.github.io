# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a minimalist PCB (Printed Circuit Board) visualization built as a single-file HTML/Canvas application. It simulates animated circuit traces connecting components with particles flowing along orthogonal paths.

## Architecture

### Single File Structure
The entire project is contained in `index.html` with three main sections:
- **Styles**: Minimal CSS for full-screen dark canvas
- **Canvas Setup**: Responsive canvas with resize handling
- **Animation System**: Class-based architecture for components, traces, and particles

### Core Classes

**Component** - Represents PCB chips
- Renders as dark rectangles with subtle core detail
- Provides methods to get perimeter points for trace connections
- Currently hardcoded to 2 components (left and right)

**Trace** - Represents PCB circuit paths
- `generatePath()`: Creates strictly orthogonal (Manhattan) routing between points
- All segments must be horizontal OR vertical (no diagonals)
- Uses multiple waypoints to create realistic 90-degree turns
- Supports parallel trace spacing via offset parameter
- Two types: inter-component traces and off-screen traces

**Particle** - Represents data flowing through traces
- Animates along trace paths with glow effect
- Progress-based positioning (0.0 to 1.0)
- Multiple particles per trace for visual density

### Path Routing Algorithm

The `generatePath()` method creates orthogonal traces with multiple direction changes:
- Determines primary routing direction (horizontal-first vs vertical-first)
- Extends straight from start point before first turn
- Creates intermediate waypoints for multiple 90-degree turns
- Applies offsets perpendicular to routing direction for parallel traces
- Ends with straight approach to destination

### Rendering Order
1. Clear canvas
2. Draw traces (faint cyan lines)
3. Update and draw particles (glowing cyan dots)
4. Draw components (dark rectangles) - drawn last so particles appear behind

## Development

### Running Locally
Simply open `index.html` in a web browser. No build system or dependencies required.

### Key Configuration
All visual parameters are in the `config` object:
- `componentCount`: Number of chips (currently hardcoded to 2)
- `tracesPerConnection`: Parallel traces between components
- `traceColor`, `traceWidth`: Visual styling for circuit paths
- `particleColor`, `particleSize`, `particleSpeedBase`: Particle appearance and speed
- `glow`: Shadow blur radius for particle glow effect

### Modifying Trace Routing
When changing the path generation algorithm, ensure all line segments maintain orthogonality:
- Each path point must differ from the previous point in ONLY X or ONLY Y (not both)
- Use separate horizontal and vertical movements
- Apply offsets only perpendicular to the current movement direction
