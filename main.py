from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDIconButton
from kivymd.uix.boxlayout import MDBoxLayout
import kivymd.uix.toolbar
from kivymd.uix.list import IRightBody, TwoLineAvatarIconListItem

from utils import phone_saver


class MainWindow(MDBoxLayout):
    pass


class DeleteButton(IRightBody, MDIconButton):
    pass


class SearchResultItem(TwoLineAvatarIconListItem):
    pass

def save_contact(self, name, phones):
    if phone_saver(name, phones):
        pass


class PhoneBookApp(MDApp):
    def name_search_result_list(self, query):
        print(query + " name")

    def phone_search_result_list(self, query):
        print(query + " phone")

    def build(self):
        return MainWindow()

    def save_contact(name, phones):
        if phone_saver(name, phones):
            pass


if __name__ == "__main__":
    PhoneBookApp().run()
