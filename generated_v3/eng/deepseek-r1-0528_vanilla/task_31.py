from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution

atoms = bulk('Al', 'fcc', a=4.05).repeat((2, 2, 2))
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=500)

initial_volume = atoms.get_volume()
print(f"Initial volume: {initial_volume:.2f} Ang^3")

dyn = NPTBerendsen(atoms, timestep=5.0 * units.fs, 
                   temperature_K=500, pressure_au=10 * units.GPa,
                   taut=100 * units.fs, taup=1000 * units.fs)

dyn.run(100)

final_volume = atoms.get_volume()
print(f"Final volume: {final_volume:.2f} Ang^3")
