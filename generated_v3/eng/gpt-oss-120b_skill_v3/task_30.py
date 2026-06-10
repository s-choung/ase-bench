from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

# Cu FCC 3×3×3 supercell
atoms = bulk('Cu', 'fcc', a=3.6) * (3, 3, 3)
atoms.calc = EMT()

# initial velocities (300 K) and remove COM drift
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

# initial state
print(f"Initial volume  : {atoms.get_volume():.2f} Å³")
print(f"Initial pressure: {atoms.get_pressure() * units.bar:.2f} bar")

# NPT Berendsen MD
dyn = NPTBerendsen(atoms,
                   timestep=5 * units.fs,
                   temperature_K=300,
                   taut=100 * units.fs,
                   pressure=1 * units.bar,
                   taup=1000 * units.fs,
                   compressible=True)

dyn.run(200)   # 200 steps

# final state
print(f"Final volume  : {atoms.get_volume():.2f} Å³")
print(f"Final pressure: {atoms.get_pressure() * units.bar:.2f} bar")
