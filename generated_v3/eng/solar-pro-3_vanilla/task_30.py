import ase
from ase.build import bulk
from ase.calculators.lj import LennardJones
from ase.calculators.emt import EMT
from ase.md import VelocityVerlet
from ase.md.npt import NPTBerendsen

# units
fs = ase.units.fs

# build Cu FCC supercell (3x3x3)
cu = bulk('Cu', 'fcc', a='3.614*u.AA')
atoms = cu * 3 * 3 * 3
atoms.center()

# calculator - EMT
atoms.set_calculator(EMT())

# velocity scaling to target temperature
atoms.rattle(1, seed=42, degrees=2)
atoms.info['T'] = 300.0
TemperatureVerlet(atoms, 5*fs, atoms.info['T'], tgroup=1)

# NPT simulation
npt = NPTBerendsen(
    atoms,
    timestep=5*fs,
    taut=100*fs,
    taup=1000*fs,
    temperature=300*units.K,
    pressure=1*units.bar,
    couplings=['cell'],
    logfile=None
)

# initial volume and pressure
V0 = atoms.get_volume()
P0 = atoms.get_pressure()

# run 200 steps
npt.run(steps=200)

# final volume and pressure
Vf = atoms.get_volume()
Pf = atoms.get_pressure()

print(f"Initial volume: {V0} {units.Ang**3}")
print(f"Final volume:   {Vf} {units.Ang**3}")
print(f"Initial pressure: {P0} {units.bar}")
print(f"Final pressure:   {Pf} {units.bar}")
