from ase.build import bulk
from ase.calculators.emt import EMT
from ase.phonons import Phonons
from ase.thermochemistry import HarmonicThermo
import numpy as np

cu = bulk('Cu', 'fcc', a=3.61, cubic=True)
cu.calc = EMT()

phonons = Phonons(cu, EMT(), supercell=(7, 7, 7), delta=0.05)
phonons.run()

phonons.read(acoustic=True)
phonon_energies = phonons.get_frequencies(qpoint=[0, 0, 0])
phonon_energies_ev = phonon_energies / 8065.54

print("Phonon frequencies at Gamma point (eV):")
for i, freq in enumerate(phonon_energies_ev):
    if freq > 1e-5:
        print(f"  Mode {i}: {freq:.6f} eV")

vib_energies = phonon_energies_ev[phonon_energies_ev > 1e-5]

thermo = HarmonicThermo(vib_energies=vib_energies, electronicenergy=cu.get_potential_energy())
helmholtz_free_energy = thermo.get_helmholtz_energy(temperature=300)

print(f"\nHelmholtz Free Energy at 300K: {helmholtz_free_energy:.6f} eV")
