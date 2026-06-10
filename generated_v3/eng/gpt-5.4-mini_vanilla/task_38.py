from ase.build import bulk
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo

atoms = bulk('Cu', 'fcc', a=3.615)
atoms.calc = EMT()

vib = Vibrations(atoms, name='cu_bulk_vib')
vib.run()
frequencies = vib.get_frequencies()

energies = frequencies[frequencies > 1e-8]
thermo = HarmonicThermo(vib_energies=energies, potentialenergy=atoms.get_potential_energy())
F = thermo.get_helmholtz_energy(temperature=300.0)

print("F(300 K) = {:.6f} eV".format(F))

vib.clean()
