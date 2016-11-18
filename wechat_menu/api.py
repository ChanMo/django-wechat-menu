import json
from wechat.api import Base
from .models import Menu as MenuModel

class Menu(Base):
    """ Wechat Menu Api """
    def sync_menu(self):
        menu = self.get_menu()
        url = self.get_url(
            'menu/create',
            {'access_token': self.get_token()}
        )
        result = self.get_data(url, menu)
        return result


    def get_menu(self):
        top = MenuModel.objects.root_nodes()
        button = {'button':[]}
        for i, item in enumerate(top):
            children = item.get_children()
            if children:
                sub_button = []
                for i, chil_item in enumerate(children):
                    sub_button.append(self.get_child_menu(chil_item))
                button['button'].append({
                    'name': item.name,
                    'sub_button': sub_button
                })
            else:
                button['button'].append(self.get_child_menu(item))

        button = json.dumps(button, ensure_ascii=False)
        #button = button.encode('utf8')
        return button


    def get_child_menu(self, menu):
        if menu.type == 'view':
            button = {
                'name': menu.name,
                'type': menu.type,
                'url': menu.value,
            }
        elif menu.type == 'click':
            button = {
                'name': menu.name,
                'type': menu.type,
                'key': menu.value,
            }
        else:
            button = {
                'name': menu.name,
            }
        return button
