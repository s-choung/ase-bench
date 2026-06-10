from ase.build import bulk
from ase.md.verlet import VelocityVerlet
from ase import units
from ase.calculators.emt import EMT

atoms = bulk('Pd', 'fcc', cubic=True).repeat(2)
atoms.calc = EMT()
atoms.set_momenta(atoms.get_momenta() * 0.0)  # Zero initial momenta
MaxwellBoltzmannDistribution(atoms, temperature_K=500)

dyn = VelocityVerlet(atoms, timestep=2 * units.fs)
e_start = atoms.get_total_energy()

def printenergy(a=atoms):
    epot = a.get_potential_energy()
    ekin = a.get_kinetic_energy()
    print(f'Epot = {epot:.3f} eV  Ekin = {ekin:.3f} eV  Etot = {epot + ekin:.3f} eV')

dyn.attach(printenergy, interval=50)
dyn.run(200)

e_end = atoms.get_total_energy()
print(f'Energy difference: {e_end - e_start:.6f} eV')
