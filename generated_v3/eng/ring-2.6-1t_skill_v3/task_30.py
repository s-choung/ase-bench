from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

# build 3x3x3 Cu FCC supercell
atoms = bulk('Cu', 'fcc', a=3.6).repeat((3, 3, 3))
atoms.calc = EMT()

# initialise velocities
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

# initial properties
V0 = atoms.get_volume()
P0 = -atoms.get_stress().trace() / 3   # hydrostatic pressure (eV/Å³)

# NPT Berendsen integrator
dyn = NPTBerendsen(
    atoms,
    timestep=5 * units.fs,
    temperature_K=300,
    pressure=1.0 * units.bar,
    taut=100 * units.fs,
    taup=1000 * units.fs,
)
dyn.run(200)

# final properties
V1 = atoms.get_volume()
P1 = -atoms.get_stress().trace() / 3

print(f"Initial volume = {V0:.2f} Å³   pressure = {P0:.4f} eV/Å³")
print(f"Final   volume = {V1:.2f} Å³   pressure = {P1:.4f} eV/Å³")
