from ase import Atoms
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

# Setup FCC Cu structure
a_guess = 3.6  # Initial lattice constant (Å)
atoms = Atoms('Cu', positions=[[0, 0, 0]], cell=[a_guess, a_guess, a_guess],
              pbc=True)

# Volume-energy points
volumes, energies = [], []
strains = np.linspace(0.95, 1.05, 7)  # Range of strains

for s in strains:
    scaled = atoms.copy()
    scaled.set_cell(atoms.cell * s, scale_atoms=True)
    scaled.calc = EMT()
    volumes.append(scaled.get_volume())
    energies.append(scaled.get_potential_energy())

# EOS fitting (Birch-Murnaghan)
eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()  # B in eV/Å³
B_GPa = B * 160.21766208  # Convert to GPa

print(f'Equilibrium volume: {v0:.3f} Å³')
print(f'Bulk modulus: {B_GPa:.1f} GPa')
