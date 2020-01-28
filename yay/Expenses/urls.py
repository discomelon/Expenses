from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^Farhan$', display_Farhan, name="display_Farhan"),
    url(r'^Nadia$', display_Nadia, name="display_Nadia"),
    url(r'^FarhanFamilySuperFund$', display_FarhanFamilySuperFund, name="display_FarhanFamilySuperFund"),
    url(r'^Ongie$', display_Ongie, name="display_Ongie"),
    url(r'^OrangeTrust$', display_OrangeTrust, name="display_OrangeTrust"),

    url(r'^add_Farhan$', add_Farhan, name="add_Farhan"),
    url(r'^add_Nadia$', add_Nadia, name="add_Nadia"),
    url(r'^add_FarhanFamilySuperFund$', add_FarhanFamilySuperFund, name="add_FarhanFamilySuperFund"),
    url(r'^add_Ongie$', add_Ongie, name="add_Ongie"),
    url(r'^add_OrangeTrust$', add_OrangeTrust, name="add_OrangeTrust"),

    url(r'^Farhan/edit_item/(?P<pk>\d+)$', edit_Farhan, name="edit_Farhan"),
    url(r'^Nadia/edit_item/(?P<pk>\d+)$', edit_Nadia, name="edit_Nadia"),
    url(r'^FarhanFamilySuperFund/edit_item/(?P<pk>\d+)$', edit_FarhanFamilySuperFund, name="edit_FarhanFamilySuperFund"),
    url(r'^Ongie/edit_item/(?P<pk>\d+)$', edit_Ongie, name="edit_Ongie"),
    url(r'^OrangeTrust/edit_item/(?P<pk>\d+)$', edit_OrangeTrust, name="edit_OrangeTrust"),

    url(r'^Farhan/delete/(?P<pk>\d+)$', delete_Farhan, name="delete_Farhan"),
    url(r'^Nadia/delete/(?P<pk>\d+)$', delete_Nadia, name="delete_Nadia"),
    url(r'^FarhanFamilySuperFund/delete/(?P<pk>\d+)$', delete_FarhanFamilySuperFund, name="delete_FarhanFamilySuperFund"),
    url(r'^Ongie/delete/(?P<pk>\d+)$', delete_Ongie, name="delete_Ongie"),
    url(r'^OrangeTrust/delete/(?P<pk>\d+)$', delete_OrangeTrust, name="delete_OrangeTrust"),

]