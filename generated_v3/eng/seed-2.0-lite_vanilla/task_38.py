from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo
from ase.units import h, c, eV

# Create 2x2x2 supercell of fcc Cu bulk
atoms = bulk('Cu', 'fcc', a=3.615, cubic=True) * (2, 2, 2)
atoms.calc = EMT()

# Relax atomic positions to equilibrium
opt = BFGS(atoms)
opt.run(fmax=0.01)

# Calculate vibrational frequencies
vib = Vibrations(atoms)
vib.run()
freqs_cm = vib.get_frequencies()
vib.clean()  # Remove temporary calculation files

# Convert wavenumbers (cm⁻¹) to energies (eV)
freqs_ev = h * c * freqs_cm * 100 / eV

# Compute vibrational Helmholtz free energy at 300K
thermo = HarmonicThermo(freqs_ev)
helmholtz_free_energy = thermo.get_helmholtz_energy(temperature=300)

print(f"Helmholtz free energy at 300K: {helmholtz_free_energy:.4f} eV")
