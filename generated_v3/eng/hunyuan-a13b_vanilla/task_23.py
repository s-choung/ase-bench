from ase import Atom, Atoms
from ase.io import write
from ase.calculators import EMT

# create Pt(111) slab
d = 2.0  # lattice constant
Pt = Atoms('Pt', positions=[(0, 0, 0), (0, 0.5, 0.5), (0.5, 0, 0.5), (0.5, 0.5, 0)], cell=(d, d, d))
Pt = Pt.stack((Pt, Pt, Pt))

# define adsorption sites
OH = Atoms('O', positions=[(0, 0, -0.1)], cell=Pt.cell)
ontop = OH.translate((0, 0, 1))
桥 = OH.translate((d/2, d/2, -0.1))
fcc = OH.translate((d/4, d/4, d/4))

# build structures
structs = {
    'ontop': Atoms('Pt', positions=Pt.get_positions()) + ontop,
    '桥': Atoms('Pt', positions=Pt.get_positions()) + 桥,
    'fcc': Atoms('Pt', positions=Pt.get_positions()) + fcc
}

# attach EMT calculator and compute energies
energies = {}
for site in structs:
    structs[site].calc = EMT()
    energies[site] = structs[site].calc.kernel()

# compare and print results
min_energy_site = min(energies, key=energies.get)
print(f"The {min_energy_site} site has the lowest energy: {energies[min_energy_site]:.4f} eV")
