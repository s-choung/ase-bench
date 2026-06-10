# render_autoframe_v2.py  (blender-atom-render Mode 1 + PBC box, atom-framed)
# Usage: blender --background --python render_autoframe_v2.py -- input.xyz output.png [perspective|top]
#
# Key behaviour:
#  - FRAMES ON THE ATOMS (not the vacuum-padded cell) so slabs / nanotubes /
#    small molecules fill the frame instead of being shrunk by big vacuum.
#  - draws the periodic unit cell as an emissive wireframe box ONLY when the cell
#    is compact (box ~ atoms, i.e. bulk/supercell). For vacuum slabs / molecules
#    in a big box, the empty box would dominate, so it is skipped.
import bpy, sys, mathutils, math, re

argv = sys.argv[sys.argv.index("--") + 1:]
xyz_path = argv[0]
output_path = argv[1]
angle = argv[2] if len(argv) > 2 else "perspective"


def read_lattice(path):
    """-> (a,b,c, centroid) from extxyz, or None if non-periodic / parse fail.
    centroid is the atom-position mean (io_mesh_atomic recenters on it)."""
    try:
        with open(path) as f:
            n = int(f.readline())
            comment = f.readline()
            pos = [mathutils.Vector([float(x) for x in f.readline().split()[1:4]])
                   for _ in range(n)]
        m = re.search(r'[Ll]attice="([^"]+)"', comment)
        if not m:
            return None
        v = [float(x) for x in m.group(1).split()]
        if len(v) != 9:
            return None
        a, b, c = mathutils.Vector(v[0:3]), mathutils.Vector(v[3:6]), mathutils.Vector(v[6:9])
        if min(a.length, b.length, c.length) < 1e-6:
            return None
        centroid = sum(pos, mathutils.Vector((0, 0, 0))) / max(len(pos), 1)
        return a, b, c, centroid
    except Exception:
        return None


for obj in list(bpy.data.objects):
    bpy.data.objects.remove(obj, do_unlink=True)
bpy.ops.outliner.orphans_purge(do_recursive=True)

bpy.ops.preferences.addon_enable(module="io_mesh_atomic")
bpy.ops.import_mesh.xyz(filepath=xyz_path, ball="1", mesh_azimuth=128, mesh_zenith=128,
                        scale_ballradius=1.0, scale_distances=1.0)

mesh_objs = [o for o in bpy.context.scene.objects if o.type == 'MESH']
if not mesh_objs:
    sys.exit(1)

# ---- ATOM bounds (framing is based on these, NOT the cell) ----
amin = mathutils.Vector((1e9, 1e9, 1e9))
amax = mathutils.Vector((-1e9, -1e9, -1e9))
for obj in mesh_objs:
    for corner in obj.bound_box:
        wp = obj.matrix_world @ mathutils.Vector(corner)
        for ax in range(3):
            amin[ax] = min(amin[ax], wp[ax]); amax[ax] = max(amax[ax], wp[ax])
acenter = (amin + amax) / 2
asize = amax - amin
atom_span = max(asize.x, asize.y, asize.z, 1.0)

# ---- cell box: ALWAYS drawn (incl. slabs), aligned to the recentered atoms ----
lat = read_lattice(xyz_path)
if lat:
    a, b, c, centroid = lat
    origin = -centroid
    idx = lambda i, j, k: i * 4 + j * 2 + k
    corners = [origin + i*a + j*b + k*c
               for i in (0, 1) for j in (0, 1) for k in (0, 1)]
    faces = [
        (idx(0,0,0), idx(0,0,1), idx(0,1,1), idx(0,1,0)),
        (idx(1,0,0), idx(1,0,1), idx(1,1,1), idx(1,1,0)),
        (idx(0,0,0), idx(0,0,1), idx(1,0,1), idx(1,0,0)),
        (idx(0,1,0), idx(0,1,1), idx(1,1,1), idx(1,1,0)),
        (idx(0,0,0), idx(0,1,0), idx(1,1,0), idx(1,0,0)),
        (idx(0,0,1), idx(0,1,1), idx(1,1,1), idx(1,0,1)),
    ]
    mesh = bpy.data.meshes.new("CellBox")
    mesh.from_pydata([tuple(v) for v in corners], [], faces)
    mesh.update()
    box = bpy.data.objects.new("CellBox", mesh)
    bpy.context.collection.objects.link(box)
    diag = max((a + b + c).length, 1.0)
    wf = box.modifiers.new("wf", "WIREFRAME")
    wf.thickness = max(0.08, diag * 0.009)
    wf.use_replace = True
    mat = bpy.data.materials.new("CellMat")
    mat.use_nodes = True
    nt = mat.node_tree
    for nd in list(nt.nodes):
        nt.nodes.remove(nd)
    out = nt.nodes.new("ShaderNodeOutputMaterial")
    emi = nt.nodes.new("ShaderNodeEmission")
    emi.inputs["Color"].default_value = (0.30, 0.62, 0.95, 1.0)
    emi.inputs["Strength"].default_value = 1.6
    nt.links.new(emi.outputs["Emission"], out.inputs["Surface"])
    box.data.materials.append(mat)
    # include the full box in the frame so it isn't clipped
    for v in corners:
        for ax in range(3):
            amin[ax] = min(amin[ax], v[ax]); amax[ax] = max(amax[ax], v[ax])

center = (amin + amax) / 2
max_dim = max(amax.x - amin.x, amax.y - amin.y, amax.z - amin.z, 1.0)

cam_data = bpy.data.cameras.new("AutoCam")
cam_data.type = 'ORTHO'
cam_data.ortho_scale = max_dim * 1.7          # farther / more margin, full cell box visible

cam_obj = bpy.data.objects.new("AutoCam", cam_data)
bpy.context.collection.objects.link(cam_obj)
cam_dist = max_dim * 3.2
if angle == "top":
    cam_obj.location = center + mathutils.Vector((cam_dist*0.15, -cam_dist*0.15, cam_dist*0.95))
else:
    cam_obj.location = center + mathutils.Vector((cam_dist*0.55, -cam_dist*0.55, cam_dist*0.5))
cam_obj.rotation_euler = (center - cam_obj.location).to_track_quat('-Z', 'Y').to_euler()
bpy.context.scene.camera = cam_obj

for name, energy, loc, rot in [
    ("Key", 3.5, (cam_dist, -cam_dist, cam_dist*1.5), (30, 0, -45)),
    ("Fill", 1.2, (-cam_dist, cam_dist*0.5, cam_dist*0.3), (60, 0, 135)),
    ("Rim", 1.5, (-cam_dist*0.3, cam_dist*0.8, cam_dist*0.6), (45, 0, 180)),
]:
    light = bpy.data.lights.new(name, type='SUN')
    light.energy = energy
    o = bpy.data.objects.new(name, light)
    bpy.context.collection.objects.link(o)
    o.location = center + mathutils.Vector(loc)
    o.rotation_euler = tuple(math.radians(x) for x in rot)

bpy.context.scene.render.resolution_x = 900
bpy.context.scene.render.resolution_y = 900
bpy.context.scene.render.film_transparent = True
bpy.context.scene.render.image_settings.file_format = 'PNG'
bpy.context.scene.render.image_settings.color_mode = 'RGBA'
bpy.context.scene.render.filepath = output_path
bpy.ops.render.render(write_still=True)
