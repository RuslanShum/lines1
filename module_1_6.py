my_dict={'Sergey':2000,'Pavel':2003,'Igor':1999}
print(my_dict)
print('Existing value:',my_dict.get('Sergey'))
print('Not existing value:',my_dict.get('Yuri',))
my_dict.update({'Svetlana':1995,
               'Liza':2010})
del my_dict['Sergey']
print(my_dict)
my_set={1,1,1,1,'яблоко',42.314}
print(my_set)
print(my_set.add(13))
print('Modified set:',my_set.add((5,6,1.6)))
print(my_set)