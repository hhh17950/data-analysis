import json
from pygal_maps_world.i18n import COUNTRIES
import pygal
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS


def get_country_code(country_name):
    for code, name in sorted(COUNTRIES.items()):
        if name == country_name:
            return code
        # 筛选出get_country_code不能帅选出的国别码
        elif country_name == 'Yemen, Rep.':
            return 'ye'
        elif country_name == 'Libya':
            return 'ly'
        elif country_name == 'Vietnam':
            return 'vn'
        elif country_name == 'Venezuela, RB':
            return 've'
        elif country_name == 'Tanzania':
            return 'tz'
        elif country_name == 'Egypt, Arab Rep.':
            return 'eg'
        elif country_name == 'Bolivia':
            return 'bo'
        elif country_name == 'Congo, Dem. Rep.':
            return 'cd'
        elif country_name == 'Iran, Islamic Rep.':
            return 'ir'
        elif country_name == 'Korea, Dem. Rep.':
            return 'kp'
        elif country_name == 'Korea, Rep.':
            return 'kr'
        elif country_name == 'Lao PDR':
            return 'la'
        elif country_name == 'Hong Kong SAR, China':
            return 'hh'
        elif country_name == 'Macao SAR, China':
            return 'mo'
        elif country_name == 'Moldova':
            return 'md'
    return None


filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)
    cc_population = {}
    for pop_dict in pop_data:
        if pop_dict['Year'] == '2010':
            country_name = pop_dict['Country Name']
            population = int(float(pop_dict['Value']))
            code = get_country_code(country_name)
            if code:
                cc_population[code] = population
    cc_pop_1, cc_pop_2, cc_pop_3, cc_pop_4 = {}, {}, {}, {}
    for cc, pop in cc_population.items():
        if pop < 10000000:
            cc_pop_1[cc] = pop
        elif pop < 100000000:
            cc_pop_2[cc] = pop
        elif pop < 1000000000:
            cc_pop_3[cc] = pop
        else:
            cc_pop_4[cc] = pop
    wm_style = RS('#336699', base_style=LCS)
    wm = pygal.maps.world.World(style=wm_style)
    wm.title = "2010年世界人口数据图"
    wm.add('0-10m', cc_pop_1)
    wm.add('10m-100m', cc_pop_2)
    wm.add('100m-1bn', cc_pop_3)
    wm.add('>1bn', cc_pop_4)
    wm.render_to_file('world_population.svg')
