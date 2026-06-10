from ase import Atoms
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
from ase.io import read

# Create H2O molecule
h2o = Atoms('H2O')
h2o.center(vacuum=6.0)

# Set the EMT calculator
h2o.calc = EMT()

# Relax the structure to get the equilibrium geometry
from ase.optimize import BFGS
relax = BFGS(h2o)
relax.run(fmax=0.05)
print('Optimization completed.')

# Perform vibrational analysis
vib = Vibrations(h2o)
vib.run()

# Print the vibrational frequencies (cm^-1) and energies (eV)
for i in range(vib.nfound * vib.ncvib):
    freq = vib.get_frequencies()[i] * 100.0  # Convert from THz to cm^-1
    energy = vib.get_energies()[i]           # Energy in eV
    print(f"Mode {i+1}: Frequency = {freq:.2f} cm⁻¹, Energy = {energy:.6f} eV")
