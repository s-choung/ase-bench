from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
atoms *= (2, 2, 2)
atoms.set_calculator(EMT())

dyn = Langevin(atoms, timestep=5e-15, temperature=300)

for step in range(200):
    dyn.step()
    if step % 50 == 0:
        print(f"Step {step}: T={atoms.get_temperature():.2f} K")
