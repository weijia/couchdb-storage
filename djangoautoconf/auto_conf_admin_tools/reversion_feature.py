from djangoautoconf.auto_conf_admin_tools.admin_feature_base import AdminFeatureBase
from django.conf import settings

__author__ = 'weijia'


class ReversionFeature(AdminFeatureBase):
    def __init__(self):
        super(ReversionFeature, self).__init__()
        self.related_search_fields = {}

    def process_parent_class_list(self, parent_list, class_inst):
        if "reversion" in settings.INSTALLED_APPS:
            from reversion import VersionAdmin
            parent_list.append(VersionAdmin)
