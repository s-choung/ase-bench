from ase import Atoms, units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

atoms = bulk('Al', 'fcc', a=4.05) * (2, 2, 2)
atoms.calc = EMT()

print(f"Initial cell volume: {atoms.get_volume():.4f} Ang^3")

pressure_gpa = 10.0
pressure_ev_ang3 = pressure_gpa * units.GPa

MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

md = NPTBerendsen(atoms, timestep=5*units.fs, temperature_K=500, 
                  externalstress=pressure_ev_ang3, taut=75*units.fs, taup=75*units.fs)
md.run(100)

print(f"Final cell volume: {atoms.get_volume():.4f} Ang^3")
