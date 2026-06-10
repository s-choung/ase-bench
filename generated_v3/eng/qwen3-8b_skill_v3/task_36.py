import numpy as np
from ase import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

atoms = bulk('Ag', 'fcc')
cell = atoms.get_cell()
volumes = []
energies = []

for x in np.linspace(0.95, 1.05, 7):
    a = atoms.copy()
    a.set_cell(cell * x, scale_atoms=True)
    a.calc = EMT()
    volumes.append(a.get_volume())
    energies.append(a.get_potential_energy())

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()

a_eq = v0 ** (1/3)
B_GPa = B * 2.307285e3

print(f"Equilibrium lattice constant: {a_eq:.4f} Å")
print(f"Bulk modulus: {B_GPa:.2f} GPa")
