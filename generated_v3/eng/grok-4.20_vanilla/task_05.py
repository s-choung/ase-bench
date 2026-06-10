from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

volumes = []
energies = []
for x in np.linspace(0.95, 1.05, 9):
    atoms.set_cell(atoms.cell * x, scale_atoms=True)
    e = atoms.get_potential_energy()
    v = atoms.get_volume()
    volumes.append(v)
    energies.append(e)

eos = EquationOfState(volumes, energies, 'birchmurnaghan')
v0, e0, B = eos.fit()

a0 = (v0 * 4)**(1/3)
print(f'Equilibrium volume: {v0:.5f} Å³')
print(f'Bulk modulus: {B:.2f} GPa')
print(f'Equilibrium lattice constant: {a0:.5f} Å')
