import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.utils.eos import EquationOfState

# Experimental FCC Ag lattice constant (Å)
a0 = 4.085
# Generate 7 lattice constant points +/-5% around a0
lattice_constants = np.linspace(0.95 * a0, 1.05 * a0, 7)

volumes = []
energies = []
for a in lattice_constants:
    atoms = bulk('Ag', 'fcc', a=a)
    atoms.calc = EMT()
    energies.append(atoms.get_potential_energy())
    volumes.append(atoms.get_volume())

# Fit Birch-Murnaghan EOS
eos = EquationOfState(volumes, energies)
v0, B0, _ = eos.fit()

# Convert units: equilibrium lattice constant (Å), bulk modulus (GPa)
a_eq = v0 ** (1/3)
B0_gpa = B0 * 160.2176634  # 1 eV/Å³ = 160.218 GPa

# Output results
print(f"Equilibrium lattice constant: {a_eq:.3f} Å")
print(f"Bulk modulus: {B0_gpa:.1f} GPa")
