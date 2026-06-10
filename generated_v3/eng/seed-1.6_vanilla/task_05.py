from ase import Atoms
from ase.calculators.emt import EMT
from ase.eos import EOS
import numpy as np

# Generate FCC Cu structures with varying lattice constants
a_vals = np.linspace(3.4, 3.8, 5)
volumes, energies = [], []
for a in a_vals:
    atoms = Atoms('Cu4', cell=[a, a, a], pbc=True,
                  scaled_positions=[(0,0,0), (0,0.5,0.5), (0.5,0,0.5), (0.5,0.5,0)])
    atoms.calc = EMT()
    volumes.append(a**3)
    energies.append(atoms.get_potential_energy())

# EOS fitting (Birch-Murnaghan model)
eos = EOS('birchmurnaghan')
v0, _, b0, _ = eos.fit(volumes, energies)

# Print results
print(f'Equilibrium volume: {v0:.4f} Å³')
print(f'Bulk modulus: {b0:.4f} eV/Å³')
