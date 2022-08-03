month = (input('Enter month: '))


def season(month):
    # year = {'winter': ['december', 'january', 'february'],
    #         'spring': ['march', 'april', 'may'],
    #         'summer': ['june', 'july', 'august'],
    #         'autumn': ['september', 'october', 'november']}
    year = {'winter': ['12', '1', '2'],
            'spring': ['3', '4', '5'],
            'summer': ['6', '7', '8'],
            'autumn': ['9', '10', '11']}
    return {key for key, val in year.items() if any(month in s for s in val)}


print(season(month))
