from ase import Atoms
from ase.calculators.emd import EMT
from ase.calculators.lj import Lj
from ase.constraints import FixAtoms
from ase.build import fcc111_surface, hcp_site
from ase.neb import NEB
from ase.io import write
import numpy as np

calc = EMT(kpts=(2, 2, 1))
calc.pseudopotential = 'Cu_PBE'
atoms = fcc111_surface(c=3.63, height=2.0, symmetry='p', size=(4, 4, 4))
atoms.set_calculator(calc)
atoms.get_projection()
atoms.center(vacuum=5.0)

hcp_site_coord = np.array([[0, 0, 0], [1/3, 2/3, 0], [2/3, 1/3, 0]])
hcp_site_atoms = []
for coord in hcp_site_coord:
    hcp_site_atoms.append(Atoms({ 'Cu': coord }, cell=atoms.cell, vacuum=0))
hcp_site_atoms = np.array(hcp_site_atoms)

projected_hcp_atoms = atoms.copy()
for atom in hcp_site_atoms:
    projected_hcp_atoms += atom

projected_hcp_atoms.set_calculator(calc)
projected_hcp_atoms.center(vacuum=5.0)

constraints = FixAtoms(indices=[range(atoms.get_number_of_atoms())])
neb = NEB(atoms, energy_cut=10.0, max_energy=100.0, neighbors=20, constraints=constraints)
neb.add_structure(projected_hcp_atoms)

neb.calculate()

energy_barrier = neb.energy(atoms) - neb.energy(projected_hcp_atoms)
print(f"Energy Barrier: {energy_barrier}")

write('cu_diffusion.traj', atoms)
