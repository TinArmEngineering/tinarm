import pint

q = pint.UnitRegistry()

operating_point = {
    "current_density": ((9.53**2 + 11.31**2) ** 0.5 * q.A) * 43 / (153.0 * q.mm**2),
    "current_angle": 115 * q.degrees,
    "simulated_speed": 3600 * q.rpm,
}
