import pandas

original_data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
fur_colour_series = original_data['Primary Fur Color']
greys = len(original_data[fur_colour_series == 'Gray'])
reds = len(original_data[fur_colour_series == 'Cinnamon'])
blacks = len(original_data[fur_colour_series == 'Black'])

final_dict = {
    'Fur Color': ['grey', 'red', 'black'],
    'Count': [greys, reds, blacks]
}

final_data = pandas.DataFrame(final_dict)
final_data.to_csv('squirrel_count.csv')
print(final_data)
