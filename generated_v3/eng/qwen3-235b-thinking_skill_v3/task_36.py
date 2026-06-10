import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

atoms = bulk('Ag', 'fcc')
cell = atoms.get_cell()
factors = np.linspace(0.95, 1.05, 7)
volumes = []
energies = []

for f in factors:
    a = atoms.copy()
    a.set_cell(cell * f, scale_atoms=True)
    a.calc = EMT()
    volumes.append(a.get_volume())
    energies.append(a.get_potential_energy())

eos = EquationOfState(volumes, energies)
v0, e0, B = eos.fit()
a0 = v0 ** (1.0 / 3.0)
B_GPa = B * 160.21766208

print(f"Equilibrium lattice constant: {a0:.3f} Å")
print(f"Bulk modulus: {B_GPa:.1f} GPa")
