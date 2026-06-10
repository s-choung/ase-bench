from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md import NPTBerendsen

atoms = bulk('Cu', 'fcc', a=3.6) * (3, 3, 3)
atoms.set_calculator(EMT())

V0 = atoms.get_volume()
s0 = atoms.get_stress()
p0 = -(s0[0] + s0[1] + s0[2]) / 3

print(f'Initial volume: {V0:.2f} Å³')
print(f'Initial pressure: {p0:.4f} eV/Å³')

dyn = NPTBerendsen(atoms, temperature_K=300, taut=100 * units.fs,
                   external_pressure=1.0e5, taup=1000 * units.fs,
                   timestep=5 * units.fs)
dyn.run(200)

Vf = atoms.get_volume()
sf = atoms.get_stress()
pf = -(sf[0] + sf[1] + sf[2]) / 3

print(f'Final volume: {Vf:.2f} Å³')
print(f'Final pressure: {pf:.4f} eV/Å³')
