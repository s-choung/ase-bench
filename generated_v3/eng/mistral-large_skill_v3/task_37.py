from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo
import numpy as np

# Optimize N2
atoms = molecule('N2')
atoms.calc = EMT()
BFGS(atoms).run(fmax=0.01)

# Calculate vibrations
vib = Vibrations(atoms, name='n2_vib')
vib.run()
freqs = vib.get_frequencies()
vib_energies = vib.get_energies()
vib.clean()

# Thermochemistry
thermo = IdealGasThermo(vib_energies=vib_energies,
                        potentialenergy=atoms.get_potential_energy(),
                        atoms=atoms,
                        geometry='linear',
                        symmetrynumber=2,
                        spin=0)
G = thermo.get_gibbs_energy(temperature=298.15, pressure=101325)
print(f"Gibbs free energy at 298.15K and 1 atm: {G:.6f} eV")
