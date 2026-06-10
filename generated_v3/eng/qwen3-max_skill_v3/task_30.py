from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

atoms = bulk('Cu', 'fcc', a=3.6) * (3, 3, 3)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

init_volume = atoms.get_volume()
print(f"Initial volume: {init_volume:.2f} Å³")
print(f"Initial pressure: {atoms.get_pressure():.2f} bar")

md = NPTBerendsen(atoms, timestep=5*units.fs, temperature_K=300, 
                  pressure_au=1*units.bar, taut=100*units.fs, taup=1000*units.fs)
md.run(200)

final_volume = atoms.get_volume()
print(f"Final volume: {final_volume:.2f} Å³")
print(f"Final pressure: {atoms.get_pressure():.2f} bar")
