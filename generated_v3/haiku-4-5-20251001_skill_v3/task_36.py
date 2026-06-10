import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase import units

atoms = bulk('Ag', 'fcc', a=4.09)
a0 = atoms.get_cell()[0, 0]

volumes = []
energies = []

for x in np.linspace(0.95, 1.05, 7):
    a = atoms.copy()
    a.set_cell([[a0 * x, 0, 0], [0, a0 * x, 0], [0, 0, a0 * x]], scale_atoms=True)
    a.calc = EMT()
    volumes.append(a.get_volume())
    energies.append(a.get_potential_energy())

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()

a_eq = (v0 * 4) ** (1/3)
B_GPa = B / units.GPa

print(f"Equilibrium lattice constant: {a_eq:.4f} Å")
print(f"Bulk modulus: {B_GPa:.2f} GPa")
