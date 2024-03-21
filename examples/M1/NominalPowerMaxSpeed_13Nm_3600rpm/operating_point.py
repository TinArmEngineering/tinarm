import pint

q = pint.UnitRegistry()

operating_point = {
    "current_density": 6.23 * q.A * q.mm**-2,
    "current_angle": 255 * q.degrees,
    "simulated_speed": 3600 * q.rpm,
}
