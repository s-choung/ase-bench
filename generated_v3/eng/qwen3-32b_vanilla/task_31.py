from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.berendsen import NPTBerendsen

atoms = bulk('Al', 'fcc', a=4.0) * (2, 2, 2)
atoms.set_calculator(EMT())
print(f"Initial volume: {atoms.get_volume():.2f} Å³")

pressure_ev_per_ang3 = 10.0 / 160.21766208  # Convert 10 GPa to eV/Å³
dyn = NPTBerendsen(atoms, 0.5, 500, pressure_ev_per_ang3, taut=100, taup=1000)
dyn.run(100)

print(f"Final volume: {atoms.get_volume():.2f} Å³")
