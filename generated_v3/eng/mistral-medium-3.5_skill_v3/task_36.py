from ase import bulk
from ase.calculators.emt import EMT
from ase(eos) import EquationOfState
import numpy as np

a0 = 4.09
atoms = bulk('Ag', 'fcc', a=a0)
volumes, energies = [], []
for x in np.linspace(0.95, 1.05, 7):
    a = atoms.copy()
    a.set_cell(a0 * x * np.eye(3), scale_atoms=True)
    a.calc = EMT()
    volumes.append(a.get_volume())
    energies.append(a.get_potential_energy())
eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()
print(f"{a0 * (v0/atoms.get_volume())**0.33:.3f} Å, {B/10:.1f} GPa")
