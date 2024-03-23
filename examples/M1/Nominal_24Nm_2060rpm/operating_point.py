import pint

q = pint.UnitRegistry()

operating_point = {
    "q_axis_current_density": 6.27768442 * q.A * q.mm**-2,
    "d_axis_current_density": 0 * q.A * q.mm**-2,
    "current_angle": 255 * q.degrees,
    "simulated_speed": 2060 * q.rpm,
}
