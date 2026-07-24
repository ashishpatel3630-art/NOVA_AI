"""
Custom Button Component
"""


from PySide6.QtWidgets import QPushButton



class AuraButton(QPushButton):


    def __init__(
        self,
        text:str
    ):

        super().__init__(text)


        self.setMinimumHeight(40)