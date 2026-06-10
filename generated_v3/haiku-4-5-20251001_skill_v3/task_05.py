import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

volumes = []
energies = []

for x in np.linspace(0.95, 1.05, 7):
    a = atoms.copy()
    a.set_cell(a.get_cell() * x, scale_atoms=True)
    a.calc = EMT()
    volumes.append(a.get_volume())
    energies.append(a.get_potential_energy())

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()

a0 = (4 * v0) ** (1/3)

print(f"Equilibrium lattice constant: {a0:.4f} Å")
print(f"Equilibrium volume: {v0:.4f} Ų")
print(f"Bulk modulus: {B:.4f} eV/Ų = {B*160.21766208:.2f} GPa")
