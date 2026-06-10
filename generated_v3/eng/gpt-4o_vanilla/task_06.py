from ase import Atoms
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.units import fs, kB

# Create 2x2x2 Cu FCC supercell
atoms = Atoms('Cu', positions=[(0, 0, 0)])
atoms.set_cell((3.6, 3.6, 3.6), scale_atoms=True)
atoms = atoms*(2, 2, 2)

# Setup calculator
atoms.calc = EMT()

# Langevin dynamics at 300K
dyn = Langevin(atoms, timestep=5*fs, temperature=300*kB, friction=0.02)

def print_status(a, t):
    epot = a.get_potential_energy()
    temp = t.get_temperature()
    print(f'T{t.nsteps} Temp={temp:.2f}K Epot={epot:.2f}eV')

print_status(atoms, dyn)
dyn.run(100)
print_status(atoms, dyn)
