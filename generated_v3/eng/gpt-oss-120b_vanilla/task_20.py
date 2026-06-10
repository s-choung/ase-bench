#!/usr/bin/env python3
from ase.build import nanotube
from ase.calculators.emt import EMT

# (6,6) armchair nanotube, 4 repeat units along the tube axis
cnt = nanotube(6, 6, length=4, periodic=True)

# optional: assign a simple calculator (EMT) – not used for the output here
cnt.set_calculator(EMT())

print("Number of atoms :", len(cnt))
print("Cell vectors (Å):")
for vec in cnt.get_cell():
    print("  ", "  ".join(f"{x:8.3f}" for x in vec))
