from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

atoms = bulk('Ag', 'fcc', a=4.09)
cell = atoms.get_cell()
atoms.calc = EMT()

volumes, energies = [], []
for x in np.linspace(0.95, 1.05, 7):
    a = atoms.copy()
    a.set_cell(cell * x, scale_atoms=True)
    volumes.append(a.get_volume())
    energies.append(a.get_potential_energy())

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()
a0 = v0 ** (1.0 / 3.0)

B_GPa = B * 160.21766208

print(f"Equilibrium lattice constant: {a0:.4f} Ang")
print(f"Bulk modulus: {B_GPa:.2f} GPa")
