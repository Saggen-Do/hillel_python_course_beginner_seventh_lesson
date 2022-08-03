add_month =['january', 'march', 'may', 'july', 'september', 'november']
even_month = ['february', 'april', 'june', 'august', 'october', 'december']
def new_year(add_month, even_month):
    whole_year = list(zip(add_month, even_month))
    new_year = []
    for i in whole_year:
        for it in i:
            new_year.append(it)
    return new_year

print(new_year(add_month, even_month))