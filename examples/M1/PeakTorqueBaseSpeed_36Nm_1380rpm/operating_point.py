import pint

q = pint.UnitRegistry()

operating_point = {
    "q_axis_current_density": (36.96 * q.A * 43) / (153.0 * q.mm**2),
    "d_axis_current_density": (0 * q.A * 43) / (153.0 * q.mm**2),
    "current_angle": -286 * q.degrees,
    "simulated_speed": 1380 * q.rpm,
}
