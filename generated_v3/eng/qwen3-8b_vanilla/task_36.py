from ase import Atoms, units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.tools import birchmurnaghan

a0 = 4.08
a_values = [a0 * (0.95 + i * 0.1 / 6) for i in range(7)]
energies = []
volumes = []

for a in a_values:
    atoms = bulk('Ag', 'fcc', a=a, orthorhombic=False)
    atoms.calc = EMT()
    e = atoms.get_potential_energy()
    energies.append(e)
    volumes.append(a**3)

bm = birchmurnaghan.BirchMurnaghan(volumes, energies)
a_eq = bm.v0 ** (1/3)
B_eq = bm.B0 * 160.2176634

print(f"Equilibrium lattice constant: {a_eq:.4f} Å")
print(f"Bulk modulus: {B_eq:.2f} GPa")
