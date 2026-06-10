from ase import Atoms, units
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.lattice.cubic import FaceCenteredCubic

cu = FaceCenteredCubic('Cu', size=(2, 2, 2))
calc = EMT()
cu.calc = calc
dyn = Langevin(cu, 5 * units.fs, temperature_K=300, friction=0.02)

def update_temp(step):
    if step % 50 == 0:
        print(f'Step: {step}, Temp: {cu.get_temperature():.2f}K')
    dyn.set_temperature(300 + (step//50)*75)

dyn.attach(update_temp, interval=1)
dyn.run(200)
