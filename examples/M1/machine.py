import pint
q = pint.UnitRegistry()

stator_parameters = {
    "slot_liner_thikness": 300 * q.um,
    "stator_bore": 8.20 * q.cm,
    "tooth_tip_depth": 1.0 * q.mm,
    "slot_opening": 1.5 * q.mm,
    "tooth_width": 9.8 * q.mm,
    "stator_outer_diameter": 0.136 * q.m,
    "back_iron_thickness": 5.5 * q.mm,
    "stator_internal_radius": 500 * q.um,
    "number_slots": 12 * q.count,
    "tooth_tip_angle": 70 * q.degrees
    }

air_gap_length = 1 * q.mm

rotor_parameters = {
    "rotor_od": stator_parameters["stator_bore"] - 2 * air_gap_length,
    "rotor_bore": 40 * q.mm,
    "banding_thickness": 0.5 * q.mm,
    "number_poles": 10 * q.count,
    "magnet_thickness": 4.5 * q.millimeter,
    "magnet_pole_arc": 150 * q.degrees,
    "magnet_inset": 0.25 * q.millimeter
    }

winding_parameters = {
    "symmetry": 2 * q.count,
    "number_phases": 3 * q.count,
    "number_layers": 2 * q.count,
    "coil_span": 1 * q.count,
    "turns_per_coil": 43 * q.count,
    "empty_slots": 0 * q.count,
    "fill_factor": 42 * q.percent
    }
