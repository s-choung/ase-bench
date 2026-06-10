from ase.build import bulk
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS
from ase.eos import EquationOfState
import numpy as np
import os

def eos_fit(metal, a_initial):
    # Create initial structure
    atoms = bulk(metal, 'fcc', a=a_initial)
    atoms.set_calculator(EMT())

    # Apply constraints to fix the atoms' positions for cell optimization
    atoms.set_constraint(FixAtoms())

    # Prepare volume-energies arrays
    volumes = []
    energies = []

    # Scale the alat and compute energies
    for i in range(7):
        scale = 0.95 + 0.1 * i
        atoms.set_cell(atoms.get_cell() * scale, scale_atoms=True)
        atoms.get_potential_energy()
        volumes.append(atoms.get_volume())
        energies.append(atoms.get_potential_energy())

    # Fit to an equation of state
    eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
    v0, e0, B = eos.fit()
    a_eq = np.cbrt(v0) / len(atoms)**(1/3)  # Equilibrium lattice parameter

    return a_eq, B

# Define initial guesses for the lattice constant
a_initials = {
    'Cu': 3.63,
    'Ag': 4.09,
    'Au': 4.08
}

results = []

# Loop over metals and calculate EOS fitting
for metal, a_initial in a_initials.items():
    a_eq, B = eos_fit(metal, a_initial)
    results.append((metal, a_eq, B))
    print(f'{metal}: a_eq = {a_eq:.4f} Å, B = {B:.2f} GPa')

# Print results in table format
print("\nComparison Table:")
print(f"{'Metal':<5} | {'Eq. Lattice Const. (Å)':<30} | {'Bulk Modulus (GPa)':<20}")
print("-" * 75)
for metal, a_eq, B in results:
    print(f"{metal:<5} | {a_eq:<30.4f} | {B:<20.2f}")
