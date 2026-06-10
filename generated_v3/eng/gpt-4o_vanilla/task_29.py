from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase import units
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution

atoms = bulk('Pd', 'fcc', a=3.9) * (2, 2, 2)
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, 500 * units.kB)

dyn = VelocityVerlet(atoms, 2 * units.fs)

init_energy = atoms.get_total_energy()

def print_energy(a=atoms):
    epot = a.get_potential_energy()
    ekin = a.get_kinetic_energy()
    print(f'Total Energy: {epot + ekin:.5f} eV')

dyn.attach(print_energy, interval=200)
dyn.run(200)

end_energy = atoms.get_total_energy()
print(f'Initial Energy: {init_energy:.5f} eV')
print(f'Final Energy:   {end_energy:.5f} eV')
print(f'Energy Change:  {end_energy - init_energy:.5f} eV')
