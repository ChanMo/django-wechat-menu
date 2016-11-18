from django.test import TestCase
from .models import Menu as MenuModel
from .api import Menu as MenuApi

class Menu(TestCase):
    def setUp(self):
        main1 = MenuModel.objects.create(name="main1")
        MenuModel.objects.create(name="chil1",parent=main1,type='view',value='hh')
        MenuModel.objects.create(name="chil2",parent=main1,type='click',value='hh')
        main2 = MenuModel.objects.create(name="main2")

    def test_menu_list(self):
        wx = MenuApi()
        data = wx.get_menu()
        print(data)
