from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase import units
import numpy as np

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
atoms.calc = EMT()
cell0 = atoms.get_cell()

volumes, energies = [], []
for s in np.linspace(0.95, 1.05, 9):
    atoms.set_cell(cell0 * s, scale_atoms=True)
    volumes.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())

eos = EquationOfState(volumes, energies)
v0, e0, B = eos.fit(show=False)

a0 = v0 ** (1 / 3)
print(f'a0 = {a0:.3f} Å')
print(f'V0 = {v0:.3f} Å³')
print(f'B  = {B / units.GPa:.1f} GPa')
