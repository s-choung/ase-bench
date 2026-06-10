import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

a0 = 3.6
atoms0 = bulk('Cu', 'fcc', a=a0)

volumes = []
energies = []

for s in np.linspace(0.94, 1.06, 9):
    atoms = atoms0.copy()
    atoms.set_cell(atoms0.get_cell() * s, scale_atoms=True)
    atoms.calc = EMT()
    volumes.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()

a_eq = (4.0 * v0) ** (1.0 / 3.0)
B_GPa = B / 160.21766208

print(f'Equilibrium lattice constant a = {a_eq:.6f} Å')
print(f'Equilibrium volume V0 = {v0:.6f} Å^3/atom')
print(f'Bulk modulus B = {B:.6f} eV/Å^3')
print(f'Bulk modulus B = {B_GPa:.3f} GPa')
