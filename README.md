# Procedural City Block Generator

This project is a work-in-progress exploration of procedural scene generation using Blender and Python (bpy).

The goal is to gradually build a simple synthetic data generation pipeline inspired by workflows used in computer vision and simulation environments.


## Concept Direction

The final goal of this project is to evolve into a procedural city block generator that can:

- Generate structured urban layouts
- Place buildings using rules (not pure randomness)
- Simulate roads, spacing, and zones
- Support dataset generation for AI / computer vision tasks


## Current Features

- Iterates over all mesh objects in the scene
- Applies random transformations to objects
- Prints transformation logs for debugging
- Basic understanding of Blender Python API (`bpy`)


## Example Behavior

Each script execution currently:

- Moves mesh objects to random positions
- Rotates objects randomly (optional)
- Logs object transformations

This serves as a baseline for future structured city generation.

##  Technologies

- Blender 3.x+
- Python 3.x
- Blender Python API (`bpy`)
- Python random module

---

## Project Vision

This project will evolve into a structured procedural generation system including:

- Road layout generation
- Building placement rules
- Asset-based generation system (buildings, cars, trees)
- Config-driven scene generation (JSON)
- Export of dataset annotations for AI training

## Next Steps

- Introduce structured city grid system
- Replace pure randomness with rule-based placement
- Add multiple asset types (building variations)
- Implement scene configuration via JSON
- Begin dataset export pipeline (COCO-style metadata)