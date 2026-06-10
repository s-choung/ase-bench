from ase.build import bulk
from ase.md import NPTBerendsen
from ase import units
from ase.calculators.emt import EMT

cu = bulk('Cu', 'fcc', cubic=True).repeat(3)
cu.calc = EMT()

dyn = NPTBerendsen(cu, timestep=5*units.fs, temperature_K=300,
                   externalstress=1*units.bar, taut=100*units.fs,
                   taup=1000*units.fs)

print(f"Initial volume: {cu.get_volume():.2f} Å³, Pressure: {cu.get_stress()/units.bar:.2f} bar")

def print_status():
    print(f"Step {dyn.get_number_of_steps()}: Volume = {cu.get_volume():.2f} Å³, Pressure = {cu.get_stress()[0]/units.bar:.2f} bar")

dyn.attach(print_status, interval=200)
dyn.run(200)

print(f"Final volume: {cu.get_volume():.2f} Å³, Pressure: {cu.get_stress()/units.bar:.2f} bar")
