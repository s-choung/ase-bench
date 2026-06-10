from ase.build import bulk
from ase.calculators.emt import EMT
from ase.units import GPa, eV, Ang, fs
from ase.md.npt import NPTBerendsen

# Build Al FCC 2x2x2 supercell
al = bulk('Al', a=4.05, crystalstructure='fcc')
atoms = al * (2, 2, 2)
atoms.calc = EMT()

# Convert 10 GPa to eV/Å³
pressure = 10 * GPa / (eV / Ang**3)

print("Initial cell volume (Å³):", atoms.get_cell().volume)

# NPT Berendsen MD: 500 K, 10 GPa, 100 steps, Δt = 1 fs
dyn = NPTBerendsen(atoms, 500, pressure, 1 * fs,
                    ttime=100 * fs, ptime=500 * fs)
dyn.run(100)

print("Final cell volume (Å³):", atoms.get_cell().volume)
