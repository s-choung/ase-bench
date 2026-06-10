from ase.md.verlet import VelocityVerlet
from ase.md.nvt import NVTIntegrator
from ase.equil import EquilibriumData
from ase.calculators import EMT
from ase.constraints import FixAtom
from ase.units import angstrom, fs, kcal
import numpy as np

calc = EMT(ucell=(3, 0, 0), Gamma=True)
atoms = calc.build_supercell(Ag, shift=(0, 0, 0), size=(2, 2, 2))
atoms.set_constraint(FixAtom(0))

integrator = NVTIntegrator(timestep=5.0 * fs)
md = VelocityVerlet(atoms, integrator)

temp = []
for i in range(200):
    md.mdstep()
    if i % 50 == 0:
        temp.append(atoms.get_temperature())

print(temp)
