from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

atoms = bulk('Ag', 'fcc', a=4.09, cubic=True)
cell = atoms.get_cell()
volumes, energies = [], []

for scale in np.linspace(0.95, 1.05, 7):
    scaled_atoms = atoms.copy()
    scaled_atoms.set_cell(cell * scale, scale_atoms=True)
    scaled_atoms.calc = EMT()
    volumes.append(scaled_atoms.get_volume())
    energies.append(scaled_atoms.get_potential_energy())

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()
a0 = v0 ** (1/3)
B_gpa = B * 160.2177

print(f"Equilibrium lattice constant: {a0:.4f} Å")
print(f"Bulk modulus: {B_gpa:.2f} GPa")
