from pathlib import Path
import json, math, shutil
import cadquery as cq
import trimesh
import numpy as np
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
H_FULL = 65.0
H_COUPON = 32.5
AF = 33.0
HEX_WALL = 2.5
REAR = 2.5
HOLE_D = 8.2
MATE_PLATE_SHIFT = (55.95930178319408, -37.59950266752112, 0.0)

# Frozen R2 chevron loop in coupon coordinates; R1 is reconstructed by filling this
# exact opening and then cutting the original Ø8.2 through-hole.
CHEVRON = [
    (101.99217987060547, 134.22000122070312),
    (92.31217956542969, 139.80874633789062),
    (82.63217926025390, 134.22000122070312),
    (92.31217956542969, 150.98625183105469),
]
R1_HOLE_CENTER = (91.81217956542970, 143.51420593261710)

R1_COUPON_OUTER = [(96.887177,154.465256),(92.312180,162.389374),(87.612183,154.248749),(87.322891,154.417145),(87.288864,154.462799),(87.264946,154.546890),(87.266594,154.863571),(87.382271,155.817062),(87.376305,156.015930),(87.334633,156.132034),(86.539688,156.596161),(86.422104,156.580780),(86.104286,156.448715),(86.050797,156.441650),(86.038910,156.440079),(85.997116,156.451370),(82.297119,150.042786),(82.327797,150.012238),(82.353004,149.951309),(82.397537,149.610031),(82.443008,149.500504),(82.840851,149.273376),(83.242424,149.044128),(83.363808,149.066086),(83.539024,149.160370),(84.306938,149.737289),(84.580353,149.897049),(84.595772,149.900925),(84.665138,149.918381),(84.721703,149.911743),(85.012177,149.745407),(81.737183,144.072952),(81.926315,143.971252),(81.993500,143.974640),(82.092575,144.010681),(82.358765,144.178009),(83.075661,144.719299),(83.248863,144.815948),(83.382812,144.844604),(84.472649,144.224304),(84.524529,144.110825),(84.570976,143.761978),(84.625450,143.675583),(80.675453,136.833969),(80.573387,136.837952),(80.248047,136.703751),(80.123825,136.691940),(79.041718,137.325623),(78.999557,137.455948),(78.996666,137.654266),(79.106979,138.545761),(79.118797,138.859955),(79.100471,138.963776),(79.069817,139.023651),(78.887184,139.136597),(73.312180,129.480408),(73.312180,106.314613),(92.312180,95.344955),(111.312180,106.314613),(111.312180,129.480408),(105.612175,139.353104),(105.902657,139.519440),(105.959213,139.526077),(106.044006,139.504745),(106.317421,139.344986),(107.085335,138.768051),(107.260544,138.673782),(107.381927,138.651825),(107.686287,138.825577),(108.181343,139.108200),(108.226822,139.217712),(108.271355,139.558990),(108.291977,139.608841),(108.296562,139.619934),(108.327240,139.650482),(104.627243,146.059067),(104.593048,146.049820),(104.585449,146.047775),(104.573563,146.049332),(104.520073,146.056412),(104.202248,146.188477),(104.180870,146.191269),(104.084671,146.203857),(103.289726,145.739731),(103.248047,145.623627),(103.242088,145.424744),(103.357765,144.471252),(103.359413,144.154587),(103.335495,144.070496),(103.301468,144.024841),(103.012177,143.856445),(99.737175,149.528900),(99.554543,149.415955),(99.523888,149.356079),(99.505562,149.252258),(99.517372,148.938065),(99.627693,148.046570),(99.624794,147.848236),(99.582634,147.717926),(98.500526,147.084229),(98.376305,147.096054),(98.050972,147.230255),(97.948906,147.226273),(93.998909,154.067871),(94.053383,154.154282),(94.099823,154.503128),(94.151703,154.616608),(95.241547,155.236908),(95.375488,155.208252),(95.548698,155.111603),(96.265594,154.570312),(96.531784,154.402985),(96.630859,154.366943),(96.698044,154.363556)]
R1_COUPON_HEX = [(75.812180,107.757988),(75.812180,126.810539),(92.312180,136.336823),(108.812180,126.810539),(108.812180,107.757988),(92.312180,98.231705)]

# Frozen side-mate cross-section extracted from the physically approved coupon.
# It is an extrusion, so preserving this 2D profile preserves the print geometry.
SIDE_MATE = [
(87.627693176,155.947586060),(87.624794006,156.145904541),(87.582633972,156.276229858),
(86.500526428,156.909912109),(86.376304626,156.898101807),(86.050979614,156.763900757),
(85.948913574,156.767868042),(81.998916626,149.926284790),(82.053382874,149.839859009),
(82.099822998,149.491012573),(82.151702881,149.377532959),(83.241546631,148.757247925),
(83.375488281,148.785888672),(83.548698425,148.882553101),(84.265594482,149.423828125),
(84.531784058,149.591156006),(84.630867004,149.627212524),(84.658348083,149.628593445),
(84.691936493,149.630279541),(84.698043823,149.630584717),(84.887176514,149.528900146),
(81.612182617,143.856430054),(81.902656555,143.690109253),(81.948936462,143.684677124),
(81.959220886,143.683456421),(82.044006348,143.704788208),(82.317420959,143.864562988),
(83.085334778,144.441482544),(83.260551453,144.535766602),(83.381935120,144.557723999),
(84.181343079,144.101333618),(84.226821899,143.991821289),(84.271354675,143.650543213),
(84.296569824,143.589614868),(84.321662903,143.564620972),(84.327247620,143.559066772),
(80.627243042,137.150466919),(80.593048096,137.159713745),(80.585449219,137.161773682),
(80.531959534,137.154708862),(80.520072937,137.153137207),(80.202255249,137.021057129),
(80.084671021,137.005691528),(79.289726257,137.469802856),(79.248054504,137.585906982),
(79.242088318,137.784790039),(79.357765198,138.738281250),(79.359413147,139.054946899),
(79.335494995,139.139038086),(79.307655334,139.176406860),(79.301467896,139.184707642),
(79.012184143,139.353103638),(75.312179565,132.944519043),(65.352890015,138.694519043),
(80.352890015,164.675277710),(90.312179565,158.925277710),(87.737174988,154.465240479),
(87.554542542,154.578186035),(87.523887634,154.638076782),(87.505561829,154.741897583),
(87.517372131,155.056076050),
]

def ensure_dirs():
    for v in ('R1-HOLE','R2-CHEVRON'):
        for d in ('STL','drawings','validation','TEST-COUPON/STL','TEST-COUPON/STEP','TEST-COUPON/drawings','TEST-COUPON/validation'):
            (ROOT/v/d).mkdir(parents=True, exist_ok=True)

def export_stl(shape, path):
    path.parent.mkdir(parents=True, exist_ok=True)
    cq.exporters.export(shape, str(path), tolerance=0.01, angularTolerance=0.1)

def export_step(shape, path):
    path.parent.mkdir(parents=True, exist_ok=True)
    cq.exporters.export(shape, str(path))

def compound(*objs):
    vals=[]
    for o in objs:
        if isinstance(o, cq.Workplane): vals.extend(o.vals())
        elif isinstance(o, cq.Shape): vals.append(o)
        else: vals.append(o)
    return cq.Compound.makeCompound(vals)

def build_side_mate():
    return cq.Workplane('XY').polyline(SIDE_MATE).close().extrude(H_COUPON)

def build_r1_coupon():
    outer=cq.Workplane('XY').polyline(R1_COUPON_OUTER).close().extrude(H_COUPON)
    hex_cut=(cq.Workplane('XY').workplane(offset=REAR).polyline(R1_COUPON_HEX).close().extrude(H_COUPON-REAR+1))
    cx,cy=R1_HOLE_CENTER
    hole=(cq.Workplane('XY').center(cx,cy).circle(HOLE_D/2).extrude(H_COUPON+2).translate((0,0,-1)))
    return outer.cut(hex_cut).cut(hole).clean()

def section_loops(stl_path, z):
    m=trimesh.load_mesh(stl_path, force='mesh')
    sec=m.section(plane_origin=[0,0,z], plane_normal=[0,0,1])
    if sec is None: return [],m
    return [np.asarray(loop)[:,:2] for loop in sec.discrete],m

def draw_section(stl_path, out_png, z, title, xlim=None, ylim=None):
    loops,m=section_loops(stl_path,z)
    fig,ax=plt.subplots(figsize=(8,8))
    for xy in loops: ax.plot(xy[:,0],xy[:,1],linewidth=1.8)
    ax.set_aspect('equal'); ax.grid(True,alpha=.25); ax.set_xlabel('mm'); ax.set_ylabel('mm'); ax.set_title(title)
    if xlim: ax.set_xlim(*xlim)
    if ylim: ax.set_ylim(*ylim)
    fig.savefig(out_png,dpi=180,bbox_inches='tight'); plt.close(fig)
    return m

def write_validation(stl_path, out_json, extra):
    m=trimesh.load_mesh(stl_path, force='mesh')
    data={
      'file':stl_path.name,
      'watertight':bool(m.is_watertight),
      'bounds_mm':m.bounds.tolist(),
      'extents_mm':m.extents.tolist(),
      'volume_mm3':float(m.volume),
      'surface_area_mm2':float(m.area),
      **extra,
    }
    out_json.write_text(json.dumps(data,indent=2),encoding='utf-8')

def main():
    ensure_dirs()
    r1_step=ROOT/'R1-HOLE/STEP-Onshape/V17T3_LITE_FINAL_R1_HOLE_Onshape.step'
    r2_step=ROOT/'R2-CHEVRON/STEP-Onshape/V17T3_LITE_FINAL_R2_CHEVRON_Onshape.step'
    r1_full=cq.importers.importStep(str(r1_step))
    r2_full=cq.importers.importStep(str(r2_step))

    r1_stl=ROOT/'R1-HOLE/STL/V17T3_LITE_FINAL_R1_HOLE.stl'
    r2_stl=ROOT/'R2-CHEVRON/STL/V17T3_LITE_FINAL_R2_CHEVRON.stl'
    export_stl(r1_full,r1_stl); export_stl(r2_full,r2_stl)
    shutil.copyfile(r1_stl,ROOT/'R1-HOLE/STL/V17T3_LITE_FINAL_R1_HOLE_print_plate.stl')
    shutil.copyfile(r2_stl,ROOT/'R2-CHEVRON/STL/V17T3_LITE_FINAL_R2_CHEVRON_print_plate.stl')

    r2_coupon_src=ROOT/'R2-CHEVRON/TEST-COUPON/STEP/V17T3_LITE_FINAL_R2_TEST_CHEVRON.step'
    r2_coupon=cq.importers.importStep(str(r2_coupon_src))
    r1_coupon=build_r1_coupon()
    mate=build_side_mate()

    export_step(r1_coupon,ROOT/'R1-HOLE/TEST-COUPON/STEP/V17T3_LITE_FINAL_R1_TEST_HOLE.step')
    export_step(mate,ROOT/'R1-HOLE/TEST-COUPON/STEP/V17T3_TEST_SIDE_MATE.step')
    export_step(mate,ROOT/'R2-CHEVRON/TEST-COUPON/STEP/V17T3_TEST_SIDE_MATE.step')

    r1c_stl=ROOT/'R1-HOLE/TEST-COUPON/STL/V17T3_LITE_FINAL_R1_TEST_HOLE.stl'
    r2c_stl=ROOT/'R2-CHEVRON/TEST-COUPON/STL/V17T3_LITE_FINAL_R2_TEST_CHEVRON.stl'
    mate1=ROOT/'R1-HOLE/TEST-COUPON/STL/V17T3_TEST_SIDE_MATE.stl'
    mate2=ROOT/'R2-CHEVRON/TEST-COUPON/STL/V17T3_TEST_SIDE_MATE.stl'
    export_stl(r1_coupon,r1c_stl); export_stl(r2_coupon,r2c_stl); export_stl(mate,mate1); shutil.copyfile(mate1,mate2)

    for variant,coupon in [('R1-HOLE',r1_coupon),('R2-CHEVRON',r2_coupon)]:
        assy=compound(coupon,mate)
        plate=compound(coupon,mate.translate(MATE_PLATE_SHIFT))
        export_stl(assy,ROOT/f'{variant}/TEST-COUPON/STL/assembled_check.stl')
        export_step(assy,ROOT/f'{variant}/TEST-COUPON/STEP/assembled_check.step')
        export_stl(plate,ROOT/f'{variant}/TEST-COUPON/STL/print_plate.stl')
        export_step(plate,ROOT/f'{variant}/TEST-COUPON/STEP/print_plate.step')

    draw_section(r1_stl,ROOT/'R1-HOLE/drawings/section.png',H_FULL/2,'R1-HOLE — mid-height section')
    draw_section(r2_stl,ROOT/'R2-CHEVRON/drawings/section.png',H_FULL/2,'R2-CHEVRON — mid-height section')
    draw_section(r1_stl,ROOT/'R1-HOLE/drawings/connector_detail.png',H_FULL/2,'R1-HOLE — corrected upper connector detail',xlim=(58,126),ylim=(118,166))
    for variant,stl in [('R1-HOLE',r1c_stl),('R2-CHEVRON',r2c_stl)]:
        draw_section(stl,ROOT/f'{variant}/TEST-COUPON/drawings/section.png',H_COUPON/2,f'{variant} — test coupon section')
        draw_section(ROOT/f'{variant}/TEST-COUPON/STL/assembled_check.stl',ROOT/f'{variant}/TEST-COUPON/drawings/assembled_section.png',H_COUPON/2,f'{variant} — assembled coupon check')

    common={'af_mm':AF,'hex_wall_mm':HEX_WALL,'rear_wall_mm':REAR,'height_mm':H_FULL,
            'connector':{'male_neck_mm':5.2,'male_head_mm':8.2,'male_depth_mm':2.5,
                         'female_mouth_mm':5.7,'female_inner_mm':8.7,'female_depth_mm':2.7,
                         'side_clearance_per_side_mm':0.25,'depth_clearance_mm':0.20}}
    write_validation(r1_stl,ROOT/'R1-HOLE/validation/model.json',{**common,'corner_feature':'3 x Ø8.2 mm through-hole'})
    write_validation(r2_stl,ROOT/'R2-CHEVRON/validation/model.json',{**common,'corner_feature':'3 x through-chevron'})
    write_validation(r1c_stl,ROOT/'R1-HOLE/TEST-COUPON/validation/coupon.json',{'height_mm':H_COUPON,'af_mm':AF,'corner_feature':'Ø8.2 through-hole'})
    write_validation(r2c_stl,ROOT/'R2-CHEVRON/TEST-COUPON/validation/coupon.json',{'height_mm':H_COUPON,'af_mm':AF,'corner_feature':'through-chevron'})

if __name__=='__main__': main()
