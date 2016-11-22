
from model.group import Group



def test_add_group(app):

    old_groups=app.group.get_group_list()

    group = Group(name="knlnölnlmlml", header="GUBJHB", footer="lknlknkln")

    app.group.create(group)

    new_groups = app.group.get_group_list()

    assert len(old_groups)+1 == app.group.count()       #count() - хэш функция

    old_groups.append(group)  # к новой группе присваивается самый большой идентификатор

    assert sorted(old_groups, key = Group.id_or_max) == sorted(new_groups, key = Group.id_or_max)


'''def test_add_empty_group(app):

    old_groups = app.group.get_group_list()

    group = Group(name="", header="", footer="")

    app.group.create(group)

    new_groups = app.group.get_group_list()

    assert len(old_groups) + 1 == len(new_groups)

    old_groups.append(group)

    assert sorted(old_groups, key = Group.id_or_max) == sorted(new_groups, key = Group.id_or_max)

'''



