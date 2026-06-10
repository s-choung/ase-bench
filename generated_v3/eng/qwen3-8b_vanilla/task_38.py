from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
from ase.thermodynamics import HarmonicThermo

atoms = bulk('Cu', 'fcc', a=3.615, cubic=True)
atoms.calc = EMT()
vib = Vibrations(atoms)
vib.run()
freq_thz = vib.get_frequencies()
freq_cm = freq_thz * 3335.64
thermo = HarmonicThermo(atoms, frequencies=freq_cm)
free_energy = thermo.get_helmholtz_energy(temperature=300)
print(free_energy)
