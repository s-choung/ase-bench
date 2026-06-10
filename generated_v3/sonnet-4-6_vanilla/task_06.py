from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.units import fs, kB
from ase import units
import numpy as np

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True).repeat(2)
atoms.calc = EMT()

from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
MaxwellBoltzmannDistribution(atoms, temperature_K=300)

def get_temp(atoms):
    ekin = atoms.get_kinetic_energy()
    return ekin / (1.5 * kB * len(atoms))

def get_info(atoms, label):
    ekin = atoms.get_kinetic_energy()
    epot = atoms.get_potential_energy()
    temp = get_temp(atoms)
    print(f"[{label}] T={temp:.1f} K | E_kin={ekin:.4f} eV | E_pot={epot:.4f} eV | E_tot={ekin+epot:.4f} eV")

get_info(atoms, "Initial")

dyn = Langevin(atoms, timestep=5*fs, temperature_K=300, friction=0.01/fs)
dyn.run(100)

get_info(atoms, "Final ")
