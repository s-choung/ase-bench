import numpy as np
from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.phonons import Phonons

atoms = bulk("Cu", "fcc", a=3.615)

ph = Phonons(atoms, EMT(), supercell=(4, 4, 4), delta=0.01, name="cu_fcc_emt_phonon")
ph.clean()
ph.run()
ph.read(acoustic=True)

omega_eV = ph.band_structure(np.array([[0.0, 0.0, 0.0]]), verbose=False)[0]
freq_cm1 = omega_eV / units.invcm

print(freq_cm1)

ph.clean()
