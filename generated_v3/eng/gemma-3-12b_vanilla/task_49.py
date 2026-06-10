from ase.build import fcc
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.eos import EquationOfState
import numpy as np

def main():
    lcb = 3.61
    eos = EquationOfState(fcc('Cu', size=4, latticeconstant=lcb))
    vos = eos.set(symbol='Cu', r0=lcb, eos_type='morse')
    a = vos.fit()[0]

    slab = fcc('Cu', size=(2, 2, 4), latticeconstant=a)
    fix = [atom.index for atom in slab if atom.position[2] < a / 2]
    for atom in slab:
        if atom.index in fix:
            atom.frozen = True

    calc = EMT()
    slab.calc = calc

    dyn = BFGS(slab, trajectory='cu_slab.traj')
    dyn.run(fmax=0.02)

    energy = slab.get_potential_energy()

    z_coords = [atom.position[2] for atom in slab]
    layer_avg_z = [np.mean(z_coords[i*2:(i+1)*2]) for i in range(4)]

    print(f"Final energy: {energy}")
    print("Layer average z-coordinates:")
    for i, z in enumerate(layer_avg_z):
        print(f"Layer {i+1}: {z}")

if __name__ == '__main__':
    main()
