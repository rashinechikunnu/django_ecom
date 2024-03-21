from django import template

register=template.Library()

@register.filter(name='brando')

def brandz(list_data,brand_size):
    brands =[]
    i = 0
    for  data in list_data:
        brands.append(data)
        i = i+1
        if i == brand_size:
            yield brands
            i =0
            brands =[]
    if brands :
            yield brands