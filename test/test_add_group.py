
from model.group import Group
#import pytest
#from data.groups import constant as testdata
import pytest


#@pytest.mark.parametrize("group", testdata, ids = [repr(x) for x in testdata] )  # ids- список с текстовым представлением данных (преобразование в строки )
#The builtin pytest.mark.parametrize decorator enables parametrization of arguments for a test function.

def test_add_group(app, db, json_groups, check_ui):             # параметр передается тестовым фреймворком

    group = json_groups

    with pytest.allure.step("Given a group list"):

        old_groups=db.get_group_list()

    with pytest.allure.step("When I add a group %s to the list" % group):

        app.group.create(group)

    #assert len(old_groups)+1 == app.group.count()                                                 #count() - хэш функция

    with pytest.allure.step('Then the new group list is equal to the old list with the added group'):

        new_groups = db.get_group_list()

        old_groups.append(group)

        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

    #if check_ui :

       # assert sorted(new_groups, key= Group.id_or_max) == sorted(app.group.get_group_list(),key= Group.id_or_max)


'''def test_add_empty_group(app):

    old_groups = app.group.get_group_list()

    group = Group(name="", header="", footer="")

    app.group.create(group)

    new_groups = app.group.get_group_list()

    assert len(old_groups) + 1 == len(new_groups)

    old_groups.append(group)

    assert sorted(old_groups, key = Group.id_or_max) == sorted(new_groups, key = Group.id_or_max)

'''



