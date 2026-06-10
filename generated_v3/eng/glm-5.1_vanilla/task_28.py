from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase import units

atoms = bulk('Cu', 'fcc') * (2, 2, 2)
atoms.calc = EMT()

T0, T1, N = 300, 600, 200
dyn = Langevin(atoms, 5 * units.fs, temperature_K=T0, friction=0.01)

def ramp():
    dyn.set_temperature(temperature_K=T0 + (T1 - T0) * dyn.nsteps / N)

def print_temp():
    T = atoms.get_kinetic_energy() / (1.5 * len(atoms) * units.kB)
    print(f"Step {dyn.nsteps}: T = {T:.2f} K")

dyn.attach(ramp)
dyn.attach(print_temp, interval=50)
dyn.run(N)
