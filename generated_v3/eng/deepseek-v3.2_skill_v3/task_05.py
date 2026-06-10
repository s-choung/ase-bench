import numpy as np
from ase import Atoms
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

atoms = Atoms('Cu4', positions=[[0, 0, 0], [0.5, 0.5, 0],
                                [0.5, 0, 0.5], [0, 0.5, 0.5]],
              cell=[[1, 0,256, [0, 1, 0], [0, 0, 1]], pbc=True)

scales = np.linspace(0.95, 1.05, 9)
volumes, energies = [], []

for s in scales:
    a = atoms.copy()
    a.set_cell(atoms.cell * s, scale_atoms=True)
    a.calc = EMT()
    volumes.append(a.get_volume())
    energies.append(a.get_potential_energy())

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()
eos.plot('eos.png')

alat = (4*v0)**(1/3)
print(f'Lattice constant: {alat:.4f} Å')
print(f'Equilibrium volume: {v0:.4f} Å³')
print(f'Bulk modulus: {B/1e9:.2f} GPa')
