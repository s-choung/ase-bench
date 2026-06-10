from ase.build import bulk
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

atoms = bulk('Pd', 'fcc', a=3.89).repeat((2, 2, 2))
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

dyn = VelocityVerlet(atoms, timestep=2 * units.fs)
e_init = atoms.get_total_energy()

def print_energy():
    e = atoms.get_total_energy()
    print(f'Time: {dyn.get_time()/units.fs:.1f} fs, E_total: {e:.6f} eV')

dyn.attach(print_energy, interval=50)
dyn.run(200)

e_final = atoms.get_total_energy()
print(f'Energy difference: {e_final - e_init:.6f} eV')
