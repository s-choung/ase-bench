from ase import Atoms
from ase.lattice.cubic import FaceCenteredCubic
from ase.md.verlet import VelocityVerlet
from ase.calculators.emt import EMT
from ase import units

atoms = FaceCenteredCubic(size=(2, 2, 2), symbol="Pd", pbc=True)
atoms.calc = EMT()
atoms.set_momenta([0, 0, 0])  # Zero initial momenta
atoms.set_temperatures([500 * units.kB])  # Set temperature

dyn = VelocityVerlet(atoms, timestep=2 * units.fs)
energy_initial = atoms.get_total_energy()

dyn.run(200)

energy_final = atoms.get_total_energy()
print(f"Energy difference: {energy_final - energy_initial} eV")
