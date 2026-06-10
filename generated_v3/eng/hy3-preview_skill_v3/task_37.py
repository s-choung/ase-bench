from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo
import numpy as np

# Create N2 molecule
atoms = Atoms('N2', positions=[[0, 0, 0], [0, 0, 1.1]])
atoms.calc = EMT()

# Optimize geometry
opt = BFGS(atoms)
opt.run(fmax=0.01)

# Calculate vibrations
vib = Vibrations(atoms, name='vib')
vib.run()

# Get vibrational energies (excluding translations/rotations)
vib_energies = vib.get_energies()
# For N2 (linear, 3N-5 = 1 vibration), take only vibrational modes
# Typically first 5 modes are trans/rot for linear molecule
vib_energies = vib_energies[5:] if len(vib_energies) > 5 else vib_energies

# Calculate Gibbs free energy
thermo = IdealGasThermo(
    vib_energies=vib_energies,
    atoms=atoms,
    geometry='linear',
    symmetrynumber=2,
    spin=0
)

G = thermo.get_gibbs_energy(temperature=298.15, pressure=101325)
print(f"Gibbs free energy: {G:.6f} eV")
