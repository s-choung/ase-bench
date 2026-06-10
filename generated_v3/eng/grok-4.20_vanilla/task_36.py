from ase.build import bulk
from ase.calculators.emt import EMT
import numpy as np
from ase.eos import EquationOfState

# Setup Ag FCC bulk
a0 = 4.09
atoms = bulk('Ag', 'fcc', a=a0)
atoms.calc = EMT()

# Lattice constants: +/-5% over 7 points
scales = np.linspace(0.95, 1.05, 7)
volumes = []
energies = []

for s in scales:
    atoms.set_cell(atoms.cell * s, scale_atoms=True)
    e = atoms.get_potential_energy()
    v = atoms.get_volume()
    volumes.append(v)
    energies.append(e)

# Fit EOS
eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B, Bp = eos.fit()

# Equilibrium lattice constant
a_eq = (v0 * 4)**(1/3)

# Bulk modulus in GPa (EMT energies in eV, volumes in Ang^3)
B_gpa = B * 160.217662

print(f"Equilibrium lattice constant: {a_eq:.4f} Å")
print(f"Bulk modulus: {B_gpa:.1f} GPa")
