"""
@author Weiwei Cao  2020-05-03
This is a class of Button.
"""


class Button:
    def __init__(self, btn_pos: tuple, btn_size: tuple, txt_pos: tuple, txt: str):
        """
        Initialize a Button object with below attributes
        :param btn_pos: a pair of coordinate, (x, y)
        :param btn_size: a pair of size, (width, height)
        :param txt_pos: a pair of coordinate, (x, y)
        :param txt: a string that will displayed on button
        """
        self.button_pos = btn_pos
        self.button_width = btn_size[0]
        self.button_height = btn_size[1]
        self.button_text_pos = txt_pos
        self.button_txt = txt

    def get_position(self) -> tuple:
        """
        get button start coordinate
        :return: a tuple contains start coordinate (x, y)
        """
        return self.button_pos

    def get_size(self) -> tuple:
        """
        get the size of button
        :return: a tuple contains width and height of the button (width, height)
        """
        return self.button_width, self.button_height

    def get_text(self) -> tuple:
        """
        get the text information on the button
        :return: a tuple contains (text, [x, y])
        """
        return self.button_txt, self.button_text_pos

    def is_hover(self, mouse_pos: tuple) -> bool:
        """
        To check  whether the mouse is hover on the button
        :param mouse_pos: an status of mouse object
        :return: True if the mouse is hover on the button else return False
        """
        if self.button_pos[0] <= mouse_pos[0] <= (self.button_pos[0] + self.button_width) \
                and self.button_pos[1] <= mouse_pos[1] <= (self.button_pos[1] + self.button_height):
            return True
        else:
            return False

    def is_click(self, click_status: tuple) -> bool:
        """
        To check whether the button is clicked by the mouse
        :param click_status: status of mouse object
        :param mouse_pos: status of mouse click
        :return: True if the mouse is clicked on the button else return False
        """
        if click_status[0] == 1 or click_status[1] == 1 or click_status[2] == 1:
            return True
        else:
            return False
