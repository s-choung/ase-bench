from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo

atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()
opt = BFGS(atoms)
opt.run(fmax=0.02)

vib = Vibrations(atoms, name='Cu_vibrations')
vib.run()
frequencies = vib.get_frequencies()

thermo = HarmonicThermo(atoms, frequencies)
helmholtz_free_energy = thermo.get_helmholtz_energy(temperature=300)

print(f"Helmholtz free energy at 300K: {helmholtz_free_energy:.3f} eV")
