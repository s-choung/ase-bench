from ase import Atoms
from ase.calculators.emt import EMT
from ase.thermochemistry import IdealGasThermo
from ase.optimize import BFGS
import numpy as np

# Create N2 molecule
n2 = Atoms('N2', positions=[[0, 0, 0], [1.1, 0, 0]])
n2.cell = [10, 10, 10]
n2.center()

# Set up calculator and optimize geometry
n2.calc = EMT()
dyn = BFGS(n2)
dyn.run(fmax=0.01)

# Compute vibrational frequencies
from ase.vibrations import Vibrations
vib = Vibrations(n2)
vib.run()
freqs = vib.get_frequencies()

# Remove translational and rotational modes (6 zero/near-zero modes)
freqs = freqs[freqs > 10]  # Keep only vibrational modes (cm^-1)

# Calculate Gibbs free energy at 298.15 K and 1 atm
thermo = IdealGasThermo(
    energies=[n2.get_potential_energy()],
    vibrations=vib,
    geometry='linear',
    symmetrynumber=2,
    temperature=298.15,
    pressure=101325  # 1 atm in Pa
)

gibbs = thermo.get_gibbs_energy()
print(f"Gibbs free energy: {gibbs:.3f} eV")
