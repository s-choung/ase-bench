import ase
from ase.build import bulk, make_supercell
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase.units import fs

atoms = bulk('Cu', 'fcc', a=3.6)
atoms = make_supercell(atoms, (2, 2, 2))
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

integrator = Langevin(atoms, timestep=5*fs, temperature_K=300, friction=0.01/fs)

for step in range(200):
    integrator.run(1)
    if step % 50 == 0:
        temp = 300 + (600 - 300) * (step / 200)
        integrator.temperature_K = temp
        print(f"Step {step}, Temperature: {temp} K")
