import ase
from ase.lattice.cubic import FaceCenteredCubic
from ase.md.langevin import Langevin
from ase.calculators.emt import EMT

atoms = FaceCenteredCubic('Cu', a=3.615, size=(2,2,2))
atoms.set_calculator(EMT())

integrator = Langevin(atoms, temperature=300, friction=0.01, dt=5.0)

for step in range(200):
    temp = 300 + (600 - 300) * step / 200
    integrator.temperature = temp
    integrator.run(1)
    if step % 50 == 0:
        print(f"Step {step}, Temp: {temp} K")
