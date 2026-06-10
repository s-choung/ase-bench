#!/usr/bin/env python3

from ase import Atoms
from asse import NudgedElasticBand
from numpy import array

# -----------------------------------------------------------
# lattice parameters for Cu FCC
a_cu = 3.614  # lattice constant (angstroms)

# bulk surface atoms (Cu(111))
bulk = Atoms('Cu32',
             positions=array([[-0.5*a_cu, -a_cu, 0.] for _ in range(16)] +  # lower half
                            [[0.5*a_cu, -a_cu, 0.] for _ in range(16)] +  # upper half
                            [[-0.5*a_cu, +a_cu, 0.] for _ in range(16)] +  # lower
                            [[0.5*a_cu, +a_cu, 0.] for _ in range(16)],     # upper
             cell=[[a_cu, 0., 0.], [0., a_c_cu, 0.], [0., 0., 2*a_cu]],
             pbc=[1,1,0])

# adsorbates: positions of an fcc/hollow and an hcp/hollow site
h1 = bulk.position + array([0., 0., 3.0])   # fcc hollow on the slab
h2 = bulk.position + array([0., 0., -3.0])  # hcp hollow on the slab

# -----------------------------------------------------------
# initial and final configurations
config0 = bulk.copy()
config0 += Atoms('Cu',
                positions=[h1],
                cell=bulk.cell,
                pbc=[1,1,0])

configN = bulk.copy()
configN += Atoms('Cu',
                positions=[h2],
                cell=bulk.cell,
                pbc=[1,1,0])

# -----------------------------------------------------------
# calculators
# EMT can now be loaded as a module calculator (see ASE docs)
try:
    from auto_calculator import EMT
    calc0 = EMT()
    calcN = EMT()
except ImportError:
    calc0 = EMT(potential='Cu')
    calcN = EMT(potential='Cu')

nb = NudgedElasticBand([config0, configN], k=2.0, scaler=0.5)

# use the same calculator for all images
for i, config in enumerate(nb.images):
    config.calc = calc0  # EMT calculator (Cu)
nb.calc = calc0

# relaxed interpolation (IDPP)
nb.run(fmax=0.05)

# -----------------------------------------------------------
# results
print('Maximum NEB energy (eV):', nb.get_all_algebraic_maximum() * 1.602176565e-19)
print('Corresponding image index:', nb.get_all_algebraic_maximum_index())
# initial image energy
e0 = nb.images[0].get_potential_energy() * 1.602176565e-19
# barrier in eV
barrier_ev = ((nb.get_all_algebraic_maximum() - e0) / 1.602176565e-19)
print('Barrier (eV):', barrier_ev)

# -----------------------------------------------------------
