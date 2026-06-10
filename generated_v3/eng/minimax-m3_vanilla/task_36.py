from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

a0 = 4.09  # Ag reference lattice constant (Å)
calc = EMT()
scaling = np.linspace(0.95, 1.05, 7)

volumes, energies = [], []
for s in scaling:
    atoms = bulk('Ag', 'fcc', a=a0 * s)
    atoms.calc = calc
    energies.append(atoms.get_potential_energy())
    volumes.append(atoms.get_volume())

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B0 = eos.fit()

# Convert bulk modulus from eV/Å³ to GPa (1 eV/Å³ = 160.2176634 GPa)
B0_GPa = B0 * 160.2176634
a_eq = (4 * v0) ** (1/3)  # FCC has 4 atoms per cell

print(f"Equilibrium lattice constant: {a_eq:.4f} Å")
print(f"Bulk modulus: {B0_GPa:.2f} GPa")
