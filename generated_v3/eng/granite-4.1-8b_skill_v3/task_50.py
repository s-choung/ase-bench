from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.io import write
from ase.thermochemistry import EquationOfState
import numpy as np

metals = {'Cu': 3.52, 'Ag': 4.09, 'Au': 4.08}  # Approximate experimental lattice constants (Å)

for metal, lattice_const in metals.items():
    # Create FCC bulk structure
    atoms = bulk(metal, 'fcc', a=lattice_const, cubic=True)

    # Set EMT calculator
    atoms.calc = EMT()

    # Optimize the structure to get a good initial geometry
    optimizer = BFGS(atoms)
    optimizer.run(fmax=0.05)  # Optimize until forces are small

    # Prepare volumes and energies for EOS fitting
    volumes = []
    energies = []
    steps = 9
    for i in range(steps):
        cell_factor = 1.0 + (i - (steps - 1) / 2) / (steps / 2)
        a_temp = lattice_const * cell_factor
        atoms_copy = atoms.copy()
        atoms_copy.set_cell(atoms_copy.cell * a_temp, scale_atoms=True)
        atoms_copy.calc = EMT()
        energies.append(atoms_copy.get_potential_energy())
        volumes.append(atoms_copy.get_volume())

    # Fit Equation of State
    eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
    v0, e0, B = eos.fit()

    print(f"Metal: {metal}")
    print(f"Equilibrium lattice constant (a0) = {v0 ** (1/3):.3f} Å")
    print(f"Bulk modulus (B) = {B / 10:.2f} GPa")
    print("-" * 40)

# Comparison table format printed above
