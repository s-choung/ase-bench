from ase import Atoms
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
from ase.optimize import BFGS

# Create H2O molecule
h2o = Atoms('H2O', positions=[
    [0, 0, 0],  # O
    [0, 0.957, 0.867],  # H
    [0, -0.957, 0.867]  # H
])

# Set calculator and optimize geometry
h2o.calc = EMT()
BFGS(h2o).run(fmax=0.01)

# Calculate vibrations
vib = Vibrations(h2o, name='h2o_vib')
vib.run()

# Get frequencies (cm⁻¹) and energies (eV)
frequencies = vib.get_frequencies()
energies = vib.get_energies()

# Print results
for i, (freq, energy) in enumerate(zip(frequencies, energies)):
    print(f'Mode {i+1}: {freq:.2f} cm⁻¹, {energy:.4f} eV')

vib.clean()
