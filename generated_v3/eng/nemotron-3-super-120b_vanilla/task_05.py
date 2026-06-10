from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

volumes = []
energies = []
for a in np.linspace(3.4, 4.0, 13):          # scan lattice constants around Cu
    atoms = bulk('Cu', 'fcc', a=a)
    atoms.calc = EMT()
    energies.append(atoms.get_potential_energy())
    volumes.append(atoms.get_volume())

eos = EquationOfState(volumes, energies)
v0, e0, B = eos.fit()
print(f'Equilibrium volume: {v0:.3f} Å^3')
print(f'Bulk modulus: {B:.3f} eV/Å^3')
print(f'Bulk modulus: {B*160.2:.1f} GPa')
