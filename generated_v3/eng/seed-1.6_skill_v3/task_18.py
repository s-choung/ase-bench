from ase.build import molecule

ch4 = molecule('CH4')
print('Atomic coordinates:\n', ch4.get_positions())
c_h_bonds = [ch4.get_distance(0, i) for i in range(1, 5)]
print('C-H bond lengths:', c_h_bonds)
print('Chemical formula:', ch4.get_chemical_formula())
