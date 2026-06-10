from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo
import numpy as np

# Build and optimise N2
atoms = molecule('N2')
atoms.calc = EMT()
BFGS(atoms).run(fmax=0.01)

# Vibrational analysis
vib = Vibrations(atoms, name='n2_vib')
vib.run()
freqs_cm = vib.get_frequencies()          # cm⁻¹
vib_energies_eV = vib.get_energies()    # eV
vib.clean()

# Thermochemistry
thermo = IdealGasThermo(vib_energies=vib_energies_eV,
                        atoms=atoms,
                        geometry='linear',
                        symmetrynumber=2,
                        spin=0)
G_eV = thermo.get_gibbs_energy(temperature=298.15, pressure=101325)

# Output
print('Vibrational frequencies (cm⁻¹):')
print(np.round(freqs_cm, 2))
print(f'\nGibbs free energy at 298.15 K and 1 atm: {G_eV:.6f} eV')
