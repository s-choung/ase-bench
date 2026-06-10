from ase import Atoms
from ase.build import bulk
from ase.md.nptberendsen import NPTBerendsen
from ase.constraints import FixSymmetry
from ase import units

# Build and supercell
atoms = bulk('Al', 'fcc', a=4.05)
atoms *= (2, 2, 2)
atoms.calc = EMT()
atoms.set_constraint(FixSymmetry)

# NPT Berendsen
T = 500.0  # K
P_ext = 10.0 * units.GPa  # 10 GPa in ASE pressure units
tau_p = 100.0 * units.fs   # pressure relaxation time

print('Initial volume:', atoms.get_volume())

md = NPTBerendsen(atoms, timestep=1.0 * units.fs,
                  temperature=T, pressure=P_ext,
                  tau_t=100.0 * units.fs, tau_p=tau_p)
md.run(100)

print('Final volume:', atoms.get_volume())
