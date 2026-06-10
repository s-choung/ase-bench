from ase.build import fcc111
from ase.calculators.emt import EMT

slab = fcc111('Pt', size=(4, 4, 3), vacuum=10.0)
positions = slab.get_positions()
z = positions[:, 2]
max_z = max(z)
surface_indices = [i for i in range(len(z)) if abs(z[i] - max_z) < 1e-3]

def add_oxygen(slab, pos, height):
    o_pos = [pos[0], pos[1], max_z + height]
    new_slab = slab.copy()
    new_slab.append(ASE.Atom('O', o_pos))
    new_slab.set_calculator(EMT())
    return new_slab

ontop = add_oxygen(slab, positions[surface_indices[0]], 1.5)
e_ontop = ontop.get_potential_energy()

bridge = add_oxygen(slab, [(positions[surface_indices[0]][0] + positions[surface_indices[1]][0])/2, 
                           (positions[surface_indices[0]][1] + positions[surface_indices[1]][1])/2, 
                           max_z + 1.5], 1.5)
e_bridge = bridge.get_potential_energy()

hollow = add_oxygen(slab, [(positions[surface_indices[0]][0] + positions[surface_indices[1]][0] + positions[surface_indices[2]][0])/3,
                           (positions[surface_indices[0]][1] + positions[surface_indices[1]][1] + positions[surface_indices[2]][1])/3,
                           max_z + 1.5], 1.5)
e_hollow = hollow.get_potential_energy()

energies = {'ontop': e_ontop, 'bridge': e_bridge, 'hollow': e_hollow}
min_site = min(energies, key=energies.get)
print(f"Lowest energy site: {min_site} with energy {energies[min_site]:.3f} eV")
