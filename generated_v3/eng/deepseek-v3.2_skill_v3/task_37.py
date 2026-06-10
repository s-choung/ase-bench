from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo
import numpy as np

# Create and optimize N2 molecule
atoms = molecule('N2')
atoms.calc = EMT()
opt = BFGS(atoms)
opt.run(fmax=0.01)

# Calculate vibrational frequencies
vib = Vibrations(atoms, name='vib_n2')
vib.run()
vib_energies = vib.get_energies()
vib.clean()

# Compute Gibbs free energy
thermo = IdealGasThermo(vib_energies=vib_energies,
                        atoms=atoms,
                        geometry='linear',
                        symmetrynumber=2,
                        spin=0)
G = thermo.get_gibbs_energy(temperature=298.15, pressure=101325)

print(f"Gibbs free energy at 298.15 K, 1 atm: {G:.6f} eV")
