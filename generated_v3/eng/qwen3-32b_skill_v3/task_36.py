import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

initial = bulk('Ag', 'fcc', a=4.086)
scale_factors = np.linspace(0.95, 1.05, 7)
volumes = []
energies = []

for x in scale_factors:
    atoms = initial.copy()
    atoms.set_cell(initial.get_cell() * x, scale_atoms=True)
    atoms.calc = EMT()
    energies.append(atoms.get_potential_energy())
    volumes.append(atoms.get_volume())

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()
a0 = v0 ** (1/3)
B_GPa = B * 160.217662  # Convert eV/Å³ to GPa

print(f"Equilibrium lattice constant: {a0:.3f} Å")
print(f"Bulk modulus: {B_GPa:.2f} GPa")
