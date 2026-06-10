from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo

# Build and optimize bulk Cu
atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()
BFGS(atoms).run(fmax=0.01)

# Vibrational analysis
vib = Vibrations(atoms, name='vib-cu')
vib.run()
vib_energies = vib.get_energies()  # eV array
vib.summary()

# Compute Helmholtz free energy at 300 K
thermo = HarmonicThermo(vib_energies=vib_energies, atoms=atoms)
helmholtz_vib = thermo.get_free_energy(temperature=300.0)

e_pot = atoms.get_potential_energy()
print(f"\nPotential energy:          {e_pot:.6f} eV")
print(f"Vibrational free energy:   {helmholtz_vib:.6f} eV")
print(f"Total Helmholtz F (300 K): {e_pot + helmholtz_vib:.6f} eV")

vib.clean()
