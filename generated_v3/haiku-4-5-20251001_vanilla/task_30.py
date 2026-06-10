from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.io import write
from ase import units

atoms = bulk('Cu', 'fcc', a=3.61, cubic=True)
atoms = atoms.repeat((3, 3, 3))

atoms.calc = EMT()

initial_volume = atoms.get_volume()
initial_pressure = atoms.get_stress()[0] / units.GPa

md = NPTBerendsen(atoms, timestep=5*units.fs, temperature_K=300, externalstress=1e5,
                  taut=100*units.fs, taup=1000*units.fs)

for i in range(200):
    md.run(1)

final_volume = atoms.get_volume()
final_pressure = atoms.get_stress()[0] / units.GPa

print(f"Initial volume: {initial_volume:.4f} Å³")
print(f"Final volume: {final_volume:.4f} Å³")
print(f"Initial pressure: {initial_pressure:.4f} GPa")
print(f"Final pressure: {final_pressure:.4f} GPa")

write('npt_final.traj', atoms)
