from ase import Atoms
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
import numpy as np

# Create water molecule
water = Atoms('H2O',
              positions=[[0.757, 0.586, 0.0],
                         [-0.757, 0.586, 0.0],
                         [0.0, -0.044, 0.0]],
              calculator=EMT())

# Optimize geometry
water.get_forces()  # Run single point to initialize calculator
water.set_calculator(EMT())
from ase.optimize import BFGS
opt = BFGS(water)
opt.run(fmax=0.01)

# Calculate vibrations
vib = Vibrations(water, name='h2o_vib')
vib.run()

# Print frequencies in cm^-1 and energies in eV
print("Vibrational modes of H2O:")
print("Mode  Frequency (cm^-1)  Energy (eV)")
print("-" * 40)
for i, (freq, energy) in enumerate(zip(vib.get_frequencies(), 
                                        vib.get_energies())):
    if np.abs(freq) > 1e-3:  # Skip imaginary frequencies close to zero
        print(f"{i+1:4d}  {freq:14.2f}  {energy:12.6f}")

vib.clean()
