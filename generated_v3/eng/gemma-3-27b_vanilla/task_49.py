from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.lattice.eos import EquationOfState
import numpy as np

def calculate_equilibrium_lattice_constant(atoms):
    energies = []
    lattice_constants = np.linspace(3.5, 4.0, 7)
    for a in lattice_constants:
        atoms.set_cell([a, a, a], scale_axes=True)
        calc = EMT()
        atoms.calc = calc
        energy = atoms.get_potential_energy()
        energies.append(energy)
    eos = EquationOfState(lattice_constants, energies)
    return eos.a0

def relax_slab():
    bulk_cu = fcc111('Cu', size=(1, 1, 1), vacuum=10.0)
    a0 = calculate_equilibrium_lattice_constant(bulk_cu.copy())
    slab = fcc111('Cu', size=(3, 3, 4), vacuum=10.0, cell=(a0, a0, a0))
    
    calc = EMT()
    slab.calc = calc

    for layer in range(2):
        slab[layer * 3:(layer + 1) * 3].set_positions(slab[layer * 3:(layer + 1) * 3].get_positions(), apply_offset=True)
        slab[layer * 3:(layer + 1) * 3].set_fixed(True)

    dyn = BFGS(slab, trajectory='cu_slab.traj')
    dyn.run()
    
    energy = slab.get_potential_energy()
    print(f"Final energy: {energy}")
    
    layer_z_coords = []
    for i in range(4):
        z_coords = slab[i*3:(i+1)*3].get_z()
        layer_z_coords.append(np.mean(z_coords))
    
    for i, z in enumerate(layer_z_coords):
      print(f"Layer {i+1} average z: {z}")

if __name__ == '__main__':
    relax_slab()
