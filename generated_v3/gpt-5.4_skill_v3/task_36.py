import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase import units

a0 = 4.09
atoms0 = bulk('Ag', 'fcc', a=a0, cubic=True)
cell0 = atoms0.get_cell()

scales = np.linspace(0.95, 1.05, 7)
volumes = []
energies = []

for s in scales:
    atoms = atoms0.copy()
    atoms.set_cell(cell0 * s, scale_atoms=True)
    atoms.calc = EMT()
    volumes.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()

a_eq = v0 ** (1 / 3)
B_GPa = B / units.kJ * 1.0e24

print(f"Equilibrium lattice constant (Angstrom): {a_eq:.6f}")
print(f"Bulk modulus (GPa): {B_GPa:.6f}")
