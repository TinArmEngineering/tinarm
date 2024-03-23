import pint

q = pint.UnitRegistry()

operating_point = {
    "d_axis_current_density": (-9.53 * q.A * 43) / (153.0 * q.mm**2),
    "q_axis_current_density": (11.31 * q.A * 43) / (153.0 * q.mm**2),
    "current_angle": (115 - 80) * q.degrees,
    "simulated_speed": 3600 * q.rpm,
}
