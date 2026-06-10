from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md import NPTBerendsen
from ase import units

al = bulk('Al', 'fcc', a=4.05, cubic=True) * (2, 2, 2)
al.calc = EMT()

pressure_gpa = 10.0
pressure_ev_ang3 = pressure_gpa * units.GPa / (units.eV / units.Ang**3)

dyn = NPTBerendsen(al, timestep=1.0*units.fs, temperature_K=500,
                   externalstress=pressure_ev_ang3, ttime=25*units.fs, pfactor=1000*units.fs**2*units.GPa)
print(f"Initial volume: {al.get_volume():.2f} Å³")

dyn.run(100)

print(f"Final volume: {al.get_volume():.2f} Å³")
