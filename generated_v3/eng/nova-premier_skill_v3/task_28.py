from ase import Atoms, units
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution

atoms = Atoms('Cu64', positions=bulk('Cu', 'fcc', a=3.6).repeat((2,2,2)).positions)
atoms.calc = EMT()

def temp_ramp(step):
    return 300 + 3*(step//50) * 100/max_step

max_step = 200
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
dyn = Langevin(atoms, timestep=5*units.fs, temperature_K=temp_ramp)

for i in range(max_step):
    dyn.run(steps=1)
    if i % 50 == 0:
        print(f"Step {i:3d}: T={atoms.get_temperature():.1f} K")
