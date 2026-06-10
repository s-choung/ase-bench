#!/usr/bin/env python
# ASE script: NPT MD on an Al FCC 2x2x2 supercell (500 K, 10 GPa ≈ 0.517615 eV/Å^3)
# 100 MD steps using NPTBerendsen

from ase import Atoms, units
from ase.calculators.emt import EMT
from ase MD.calculators import _LJ, Thermostat
from ase.md.langevin import Langevin
from ase.md.npt import NPTBerendsen

# --- build initial structure ---
# bulk FCC Al lattice constant: 4.05 Å
a = 4.05 * units.Ang
n = 2
atoms = Atoms('Al', positions=[
    [(i * a / 2, j * a / 2, k * a / 2) for i in (0, n) for j in (0, n) for k in (0, n)]
], cell=(n * a, n * a, n * a), pbc=True)

# --- calculator and temperature ---
atoms.set_calculator(EMT())
T_target = 500 * units.K

# --- NPT Berendsen thermostat/barostat ---
pressure_target = -10 * units.GPa   # negative for compression
npt = NPTBerendsen(timestep=1.0 * units.fs,
                  temperature=T_target,
                  pressure=pressure_target)

# --- attach thermostat (Langevin) for T control ---
thermo = Thermostat(atoms, npt, timestep=1.0 * units.fs,
                   gamma=1.0 / units.ps,  # low friction for weak T coupling
                   friction=0.01,
                   nstcomm=1)

# print initial cell volume (eV)
V_initial = atoms.get_volume() / units.eV
print(f'Initial Volume = {V_initial:.4f} eV/Å^3')

# --- run 100 steps ---
nsteps = 100
for i in range(nsteps):
    thermo.run(steps=1)

# print final cell volume (eV)
V_final = atoms.get_volume() / units.eV
print(f'Final Volume = {V_final:.4f} eV/Å^3')
