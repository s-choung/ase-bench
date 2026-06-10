from ase import Atoms
from ase.lattice.cubic import FaceCenteredCubic
from ase.md import Langevin
from ase.calculators.emt import EMT
from ase.units import fs

atoms = FaceCenteredCubic('Cu', size=(2, 2, 2))
atoms.calc = EMT()
dyn = Langevin(atoms, timestep=5*fs, temperature=300, friction=0.002)
print(f'Initial T: {atoms.get_temperature():.2f}K, E: {atoms.get_potential_energy():.4f}eV')
dyn.run(100)
print(f'Final T: {atoms.get_temperature():.2f}K, E: {atoms.get_potential_energy():.4f}eV')
