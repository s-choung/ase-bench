import ase
from ase.lattice.cubic import FaceCenteredCubic
from ase.calculators.emt import EMT
from ase.md import NPTBerendsen

atoms = FaceCenteredCubic('Al', a=4.049, size=(2,2,2))
atoms.set_calculator(EMT())

pressure = 10 * 6.2415e-3  # Convert GPa to eV/Ang^3

dynamics = NPTBerendsen(atoms, temperature_K=500, pressure=pressure, time_step=1.0, nsteps=100)

print("Initial volume:", atoms.get_volume())
dynamics.run()
print("Final volume:", atoms.get_volume())
