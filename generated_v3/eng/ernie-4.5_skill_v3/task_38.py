from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo
from ase.units import kB

# Create bulk Cu and attach EMT calculator
atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
atoms.calc = EMT()

# Optimize geometry first
opt = BFGS(atoms)
opt.run(fmax=0.01)

# Calculate vibrational frequencies
vib = Vibrations(atoms, name='cu_vib')
vib.run()
vib.summary()

# Get vibrational energies in eV
vib_energies = vib.get_energies()  # in eV

# Calculate Helmholtz free energy at 300K
thermo = HarmonicThermo(vib_energies=vib_energies)
F = thermo.get_helmholtz_energy(temperature=300, verbose=False)

print(f"Helmholtz free energy at 300K: {F:.4f} eV")
