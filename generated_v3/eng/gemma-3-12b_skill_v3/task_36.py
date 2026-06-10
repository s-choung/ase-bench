from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

atoms = bulk('Ag', 'fcc', a=4.08)  # Approximate Ag FCC lattice constant
atoms.calc = EMT()

volumes, energies = [], []
a0 = atoms.get_cell_lengths()[0]
for x in np.linspace(0.95, 1.05, 7):
    a = a0 * x
    atoms.set_cell([a], scale_atoms=True)
    volumes.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()

print(f"Equilibrium volume: {v0:.3f} Bohr^3")
print(f"Equilibrium bulk modulus: {B:.2f} GPa")
