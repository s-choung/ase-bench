from ase import Atoms
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

# Create FCC Cu primitive cell
a0_guess = 3.6  # initial guess in Angstrom
cu = Atoms('Cu', positions=[[0, 0, 0]], cell=[a0_guess, a0_guess, a0_guess], pbc=True)
cu.set_calculator(EMT())

# Generate volumes around the guess
volumes = []
energies = []
for x in np.linspace(0.95, 1.05, 7):
    cu.set_cell([a0_guess*x, a0_guess*x, a0_guess*x], scale_atoms=True)
    volumes.append(cu.get_volume())
    energies.append(cu.get_potential_energy())

# Fit EOS
eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()

# Print results
print(f"Equilibrium volume: {v0:.4f} A^3")
print(f"Bulk modulus: {B:.4f} eV/A^3")
