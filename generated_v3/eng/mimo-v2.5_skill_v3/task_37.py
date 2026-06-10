import numpy as np
from ase import Atoms
from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo
from ase import units

# Create N2 molecule and set calculator
n2 = molecule('N2')
n2.calc = EMT()

# Optimize geometry
opt = BFGS(n2, trajectory=None, logfile=None)
opt.run(fmax=0.01)

# Calculate vibrational frequencies
vib = Vibrations(n2, name='n2_vib')
vib.run()
vib_energies = vib.get_energies()  # Energies in eV
vib.clean()

# Ideal gas thermodynamics
thermo = IdealGasThermo(
    vib_energies=vib_energies,
    atoms=n2,
    geometry='linear',
    symmetrynumber=2,
    spin=0
)

# Gibbs free energy at 298.15 K and 1 atm (101325 Pa)
gibbs_energy = thermo.get_gibbs_energy(
    temperature=298.15,
    pressure=101325
)

print(f"N2 vibrational frequencies (cm⁻¹): {vib_energies / (0.0001239842 / units.kB):.2f}")
print(f"Gibbs free energy at 298.15K, 1 atm: {gibbs_energy:.6f} eV")
