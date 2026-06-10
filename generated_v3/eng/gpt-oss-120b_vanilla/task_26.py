#!/usr/bin/env python3
# ASE bulk optimization of Ni (FCC) with EMT and PreconLBFGS

from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import PreconLBFGS

# Create a Ni FCC crystal (2x2x2 supercell for a modest size)
atoms = bulk('Ni', 'fcc', a=3.52).repeat((2, 2, 2))

# Attach the EMT calculator
atoms.calc = EMT()

# Optimizer with automatic preconditioner
opt = PreconLBFGS(atoms, precon='auto')

# Run geometry optimization (force convergence 0.01 eV/Å)
opt.run(fmax=0.01)

# Output results
print(f"Number of optimizer steps: {opt.get_number_of_steps()}")
print(f"Final total energy (eV): {atoms.get_potential_energy():.6f}")
print("Final cell vectors (Å):")
for vec in atoms.get_cell():
    print("  " + " ".join(f"{c: .6f}" for c in vec))
