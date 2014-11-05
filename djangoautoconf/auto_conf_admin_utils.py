import inspect
from django.conf import settings

if "guardian" in settings.INSTALLED_APPS:
    from guardian.admin import GuardedModelAdmin as SingleModelAdmin
else:
    from django.contrib.admin import ModelAdmin as SingleModelAdmin


from django.contrib.admin import ModelAdmin
from django.contrib import admin
#The following not work with guardian?
#import xadmin as admin


def register_normal_admin(admin_class, class_inst):
    # admin.site.register(class_inst)
    try:
        from normal_admin.admin import user_admin_site
        user_admin_site.register(class_inst, admin_class)
    except:
        pass
        #register(class_inst)


def get_valid_admin_class(admin_class, class_inst):
    if admin_class is None:
        admin_class = type(class_inst.__name__ + "Admin", (SingleModelAdmin, ), {})
    return admin_class


def register_admin(admin_class, class_inst):
    try:
        admin.site.register(class_inst, admin_class)
    except:
        pass


def register_to_sys(class_inst, admin_class=None):
    admin_class = get_valid_admin_class(admin_class, class_inst)
    register_admin(admin_class, class_inst)
    register_normal_admin(admin_class, class_inst)


def get_valid_admin_class_with_list(admin_list, class_inst):
    final_parents = admin_list.append(ModelAdmin)
    admin_class = type(class_inst.__name__ + "Admin", set(final_parents), {})
    return admin_class


def register_to_sys_with_admin_list(class_inst, admin_list=[]):
    admin_class = get_valid_admin_class_with_list(admin_list, class_inst)
    register_admin(admin_class, class_inst)
    register_normal_admin(admin_class, class_inst)


def register_all(class_list, admin_class_list=[]):
    for i in class_list:
        register_to_sys_with_admin_list(i, admin_class_list)


def register_all_in_module(module_instance, exclude_name=[], admin_class_list=[]):
    class_list = []
    for name, obj in inspect.getmembers(module_instance):
        if inspect.isclass(obj):
            if obj.__name__ in exclude_name:
                continue
            class_list.append(obj)
    register_all(class_list, admin_class_list)