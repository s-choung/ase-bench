from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS

# Initial water geometry (Angstroms)
mol = Atoms('H2O',
            positions=[[0.0, 0.0, 0.0],
                       [0.757, 0.586, 0.0],
                       [-0.757, 0.586, 0.0]])

mol.calc = EMT()
e_before = mol.get_potential_energy()
print('Energy before optimization :', e_before)

opt = BFGS(mol)
opt.run(fmax=0.05)

e_after = mol.get_potential_energy()
print('Energy after optimization  :', e_after)
