#!/usr/bin/env python3
import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter

def lattice_constant(atoms):
    a, b, c, _, _, _ = atoms.get_cell_lengths_and_angles()
    return a  # cubic cell -> a = b = c

# FCC Cu bulk, rough lattice constant
atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

print("=== Before optimization ===")
print(f"Lattice constant (Å): {lattice_constant(atoms):.4f}")
print(f"Cell volume (Å³):  {atoms.get_volume():.4f}")
print(f"Energy (eV):       {atoms.get_potential_energy():.6f}")

# simultaneous cell + atomic positions optimization
opt = BFGS(FrechetCellFilter(atoms))
opt.run(fmax=0.01)

print("\n=== After optimization ===")
print(f"Lattice constant (Å): {lattice_constant(atoms):.4f}")
print(f"Cell volume (Å³):  {atoms.get_volume():.4f}")
print(f"Energy (eV):       {atoms.get_potential_energy():.6f}")
