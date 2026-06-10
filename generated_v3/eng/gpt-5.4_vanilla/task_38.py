from ase.build import bulk
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.phonons import Phonons
from ase.thermochemistry import HarmonicThermo

a = bulk('Cu', 'fcc', a=3.61).repeat((2, 2, 2))
a.calc = EMT()

ph = Phonons(a, EMT(), supercell=(2, 2, 2), delta=0.01)
ph.run()
ph.read(acoustic=True)

omega_kn = ph.band_structure([[0, 0, 0]])[0]
energies = [w for w in omega_kn if w > 1e-6]

thermo = HarmonicThermo(vib_energies=energies, potentialenergy=a.get_potential_energy())
F = thermo.get_helmholtz_energy(temperature=300.0)

print(f"Helmholtz free energy at 300 K: {F:.6f} eV")
