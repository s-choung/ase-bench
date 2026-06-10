from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo
import numpy as np

# Create N2 molecule and set calculator
atoms = Atoms('N2', positions=[[0, 0, 0], [1.1, 0, 0]])
atoms.calc = EMT()

# Optimize geometry
BFGS(atoms).run(fmax=0.01)

# Calculate vibrations
vib = Vibrations(atoms, name='vib')
vib.run()
freqs = vib.get_frequencies()
vib.clean()

# Calculate Gibbs free energy using ideal gas thermodynamics
thermo = IdealGasThermo(vib_energies=vib.get_energies(),
                        atoms=atoms,
                        geometry='linear',
                        symmetrynumber=2,
                        spin=0)
G = thermo.get_gibbs_energy(temperature=298.15, pressure=101325)

print(f"Gibbs free energy at 298.15 K and 1 atm: {G:.6f} eV")
