import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

volumes, energies = [], []
cell_orig = atoms.get_cell()

for x in np.linspace(0.9, 1.1, 7):
    a = atoms.copy()
    a.set_cell(cell_orig * x, scale_atoms=True)
    volumes.append(a.get_volume())
    energies.append(a.get_potential_energy())

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()

print(f"Equilibrium Volume: {v0:.4f} A^3")
print(f"Bulk Modulus: {B:.4f} eV/A^3")
