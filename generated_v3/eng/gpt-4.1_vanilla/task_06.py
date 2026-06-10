from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase import units
from ase.io.trajectory import Trajectory

atoms = bulk('Cu', 'fcc', a=3.615).repeat((2,2,2))
atoms.calc = EMT()

from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, TempProfile

MaxwellBoltzmannDistribution(atoms, 300*units.kB)

def get_status(atoms):
    ekin = atoms.get_kinetic_energy()
    epot = atoms.get_potential_energy()
    etot = ekin + epot
    temp = ekin / (1.5 * units.kB * len(atoms))
    return temp, ekin, etot

t0, ek0, et0 = get_status(atoms)
print(f'Initial T = {t0:.1f} K, E_kin = {ek0:.3f} eV, E_tot = {et0:.3f} eV')

dyn = Langevin(atoms, 5*units.fs, temperature_K=300, friction=0.02)
for i in range(100):
    dyn.run(1)

t1, ek1, et1 = get_status(atoms)
print(f'Final   T = {t1:.1f} K, E_kin = {ek1:.3f} eV, E_tot = {et1:.3f} eV')
