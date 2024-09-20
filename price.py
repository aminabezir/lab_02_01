import color
import details

def calculate_painting_cost(color_num, part):
    base_cost = 12000

    color_coefficient = color.coefficient_by_colour(color_num)
    part_coefficient = details.coefficient_by_part(part)

    total_cost = base_cost*color_coefficient*part_coefficient
    return total_cost