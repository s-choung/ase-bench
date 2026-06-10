from ase import Atoms, units
from ase.build import bulk, make_supercell
from ase.md.nptberendsen import NPTBerendsen
from ase.calculators.emt import EMT

# Initialize Al FCC structure
al = bulk('Al', 'fcc', a=4.05)
atoms = make_supercell(al, [[2,0,0],[0,2,0],[0,0,2]])
atoms.calc = EMT()

# Convert pressure to eV/Ang^3
pressure = 10 * 1e9 * (units.Pascal * units.m**3 / units.GPa * units.J / units.eV)

# NPT MD setup
dyn = NPTBerendsen(atoms, T=500*units.kB, pressure=pressure, ttime=100*units.fs, taut=50*units.fs)
print("Initial volume: {:.3f}".format(atoms.get_volume()))
dyn.run(100)
print("Final volume: {:.3f}".format(atoms.get_volume()))
