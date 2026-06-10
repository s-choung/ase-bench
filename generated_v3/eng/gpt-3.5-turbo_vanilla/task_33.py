from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import QuasiNewton
from ase.vibrations import Vibrations

# Create a CH4 molecule
ch4 = Atoms('CH4', positions=[[0.000, 0.000, 0.000],
                               [0.634, 0.634, 0.634],
                               [-0.634, -0.634, 0.634],
                               [0.634, -0.634, -0.634],
                               [-0.634, 0.634, -0.634]])

# Set EMT calculator and optimize structure
ch4.set_calculator(EMT())
relax = QuasiNewton(ch4)
relax.run()

# Perform vibration calculation
vib = Vibrations(ch4)
vib.run()

# Filter and print only real frequencies
for freq in vib.get_thermodynamic_properties().frequencies:
    if freq.imag == 0:
        print(freq)
