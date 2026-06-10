from ase import Atoms
from ase.lattice.cubic import FaceCenteredCubic
from ase.calculators.emt import EMT
from ase.units import kJ, Angstrom, Bohr
from ase.eos import EquationOfState
import numpy as np

# Create FCC Cu unit cell with lattice constant ~3.6 Angstrom
a0 = 3.6
atoms = FaceCenteredCubic('Cu', latticeconstant=a0)

# Set EMT calculator
atoms.calc = EMT()

# Generate volumes by scaling the unit cell
volumes = []
energies = []
scale_range = np.linspace(0.92, 1.08, 7)

for scale in scale_range:
    atoms_new = atoms.copy()
    atoms_new.set_cell(atoms_new.cell * scale, scale_atoms=True)
    volumes.append(atoms_new.get_volume())
    energies.append(atoms_new.get_potential_energy())

# Fit EOS using Murnaghan model
eos = EquationOfState(volumes, energies, fittype='murnaghan')
v0, e0, B = eos.fit()
B *= kJ / Angstrom**3  # Convert to GPa

# Output results
print(f"Equilibrium volume: {v0:.3f} Å³")
print(f"Bulk modulus: {B:.2f} GPa")
