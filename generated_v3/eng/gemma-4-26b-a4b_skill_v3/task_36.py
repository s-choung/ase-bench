import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase import units

# 1. Setup Silver FCC bulk
atoms = bulk('Ag', 'fcc', a=4.08)
atoms.calc = EMT()

# 2. Generate energy-volume data
volumes = []
energies = []
cell = atoms.get_cell()

for scale in np.linspace(0.95, 1.05, 7):
    test_atoms = atoms.copy()
    test_atoms.set_cell(cell * scale, scale_atoms=True)
    test_atoms.calc = EMT()
    volumes.append(test_atoms.get_volume())
    energies.append(test_atoms.get_potential_energy())

# 3. Fit Equation of State (Birch-Murnaghan)
eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()

# 4. Extract equilibrium lattice constant (a = (V/sqrt(2))^(1/3) for FCC)
a0 = (v0 / np.sqrt(2))**(1/3)

# 5. Convert Bulk Modulus to GPa
# B in ASE is in eV/Angstrom^3. 1 eV/A^3 = 160.21766 GPa
B_GPa = B * 160.21766

print(f"Equilibrium lattice constant: {a0:.4f} Å")
print(f"Bulk modulus: {B_GPa:.4f} GPa")
