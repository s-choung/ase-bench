import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

a0 = 4.09
scale = np.linspace(0.95, 1.05, 7)

volumes = []
energies = []

for s in scale:
    a = a0 * s
    atoms = bulk('Ag', 'fcc', a=a)
    atoms.calc = EMT()
    energies.append(atoms.get_potential_energy())
    volumes.append(atoms.get_volume())

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()

a_eq = (4 * v0) ** (1 / 3)
B_GPa = B / 0.006241509074460763

print(f'Equilibrium lattice constant: {a_eq:.6f} Å')
print(f'Bulk modulus: {B_GPa:.3f} GPa')
