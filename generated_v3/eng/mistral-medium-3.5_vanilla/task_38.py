from ase import Atoms
from ase.calculators.emt import EMT
from ase.thermochemistry import HarmonicThermo
from ase.phonons import Phonons

cu = Atoms('Cu', pbc=True)
cu.calc = EMT()
phonons = Phonons(cu, EMT(), supercell=(4, 4, 4))
phonons.run()
vib_energies = phonons.get_frequencies().flatten()
thermo = HarmonicThermo(vib_energies, potentialenergy=cu.get_potential_energy())
print(thermo.get_helmholtz_energy(300))
