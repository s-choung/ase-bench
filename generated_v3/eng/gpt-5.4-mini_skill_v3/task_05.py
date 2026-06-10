import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
cell0 = atoms.get_cell().copy()

volumes, energies = [], []
for s in np.linspace(0.94, 1.06, 9):
    a = atoms.copy()
    a.set_cell(cell0 * s, scale_atoms=True)
    a.calc = EMT()
    volumes.append(a.get_volume())
    energies.append(a.get_potential_energy())

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()

print(f"Equilibrium volume: {v0:.6f} Å^3")
print(f"Bulk modulus: {B:.6f} eV/Å^3")
