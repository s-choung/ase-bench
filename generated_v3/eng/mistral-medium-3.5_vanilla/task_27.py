from ase import Atoms
from ase.md import VelocityScaler, NVT
from ase.calculators.emt import EMT
from ase.lattice.cubic import FaceCenteredCubic
from ase.units import fs

atoms = FaceCenteredCubic('Ag', size=(2, 2, 2))
atoms.calc = EMT()
atoms.set_momenta(lattice_temperature=300 *ase.units.kB)

dyn = NVT(atoms, timestep=5*fs, temperature=500, taut=100*fs)
dyn.attach(VelocityScaler(500, taut=100*fs), interval=1)

def print_temp():
    print(f'Temperature: {atoms.get_temperature():.2f} K')

dyn.attach(print_temp, interval=50)
dyn.run(200)
