import numpy as np
from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo

# Setup N2 molecule
atoms = molecule('N2')
atoms.calc = EMT()

# Geometry optimization (essential before vibrations)
opt = BFGS(atoms)
opt.run(fmax=0.01)

# Vibrational analysis
vib = Vibrations(atoms, name='n2_vib')
vib.run()
vib_energies = vib.get_energies()  # returns energies in eV
vib.clean()

# Thermochemistry calculation
# IdealGasThermo expects vibrational energies in Joules (J)
# ASE's vib_energies are in eV, convert using units.eV
from ase import units
thermo = IdealGasThermo(
    vib_energies=vib_energies * units.eV,
    atoms=atoms,
    geometry='linear',
    symmetrynumber=2,
    spin=0
)

# Calculate Gibbs free energy at 298.15K and 101325 Pa (1 atm)
G = thermo.get_gibbs_energy(temperature=298.15, pressure=101325)

print(f"Gibbs Free Energy at 298.15K, 1 atm: {G:.4f} eV")
