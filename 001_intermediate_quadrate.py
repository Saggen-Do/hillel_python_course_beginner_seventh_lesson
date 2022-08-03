quadrate_lengh = float(input('Enter side length: '))


def quadrate(quadrate_lengh):
    perimeter_quadrate = quadrate_lengh * 4
    diagonal_quadrate = round((((quadrate_lengh ** 2) * 2) ** 0.5), 2)
    area_quadrate = quadrate_lengh * quadrate_lengh
    return ((('perimeter_quadrate', perimeter_quadrate), ('diagonal_quadrate', diagonal_quadrate),
                      ('area_quadrate', area_quadrate)))


print(quadrate(quadrate_lengh))
