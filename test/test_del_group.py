from model.group import Group
import random

def test_delete_some_group(app,db, check_ui):

    if len(db.get_group_list())== 0: # falls keine Gruppe gibt´s

        app.group.create(Group(name="test")) # erstellen wir eine Gruppe

    old_groups = db.get_group_list()

    group = random.choice(old_groups)

   # index = randrange(len(old_groups)) # сортировка в бд и в ui происходит по разному, поэтому переходим на id

    app.group.delete_group_by_id(group.id)

    new_groups = db.get_group_list()

    assert len(old_groups) - 1 == len(new_groups)

    old_groups.remove(group)

    #old_groups[index:index+1] = []

    assert old_groups == new_groups

    if check_ui:

        assert sorted(new_groups, key= Group.id_or_max) == sorted(app.group.get_group_list(),key= Group.id_or_max)


