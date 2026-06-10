import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

atoms = bulk('Ag', 'fcc', a=4.09)
cell = atoms.get_cell()
volumes, energies = [], []

for x in np.linspace(0.95, 1.05, 7):
    a = atoms.copy()
    a.set_cell(cell * x, scale_atoms=True)
    a.calc = EMT()
    volumes.append(a.get_volume())
    energies.append(a.get_potential_energy())

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()
lattice_constant = (v0 / atoms.get_volume()) ** (1 / 3) * atoms.get_cell()[0, 0]
bulk_modulus_GPa = B / 1.60218e-2

print(f'Equilibrium lattice constant: {lattice_constant:.2f} Å')
print(f'Bulk modulus: {bulk_modulus_GPa:.2f} GPa')
