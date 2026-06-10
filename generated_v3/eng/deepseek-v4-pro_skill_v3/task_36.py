import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase import units

# Initial FCC Ag with approximate lattice constant
a0 = 4.09
atoms = bulk('Ag', 'fcc', a=a0, cubic=True)
atoms.calc = EMT()

# Generate 7 points in +/-5% range
scales = np.linspace(0.95, 1.05, 7)
volumes = []
energies = []

for s in scales:
    a = atoms.copy()
    a.set_cell(atoms.get_cell() * s, scale_atoms=True)
    a.calc = EMT()
    volumes.append(a.get_volume())
    energies.append(a.get_potential_energy())

# Fit Birch-Murnaghan EOS
eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()

# Convert bulk modulus from eV/A^3 to GPa
B_GPa = B * units.GPa  # units.GPa = 160.21766208 (eV/A^3 -> GPa)

# Equilibrium lattice constant from V0
a_eq = (4 * v0) ** (1/3)  # FCC: V = a^3/4

print(f"Equilibrium lattice constant: {a_eq:.4f} A")
print(f"Bulk modulus: {B_GPa:.2f} GPa")
