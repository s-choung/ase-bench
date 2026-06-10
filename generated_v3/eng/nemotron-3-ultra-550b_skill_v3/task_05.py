import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

cell0 = atoms.get_cell()
volumes, energies = [], []
for scale in np.linspace(0.95, 1.05, 9):
    a = atoms.copy()
    a.set_cell(cell0 * scale, scale_atoms=True)
    volumes.append(a.get_volume())
    energies.append(a.get_potential_energy())

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()

print(f"Equilibrium volume: {v0:.3f} Å³")
print(f"Bulk modulus: {B:.2f} eV/Å³")
