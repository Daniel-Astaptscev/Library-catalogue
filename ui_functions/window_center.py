def center(self):
    """
    Перемещает любое окно приложения в центр экрана.

    Args:
        self: текущее окно приложения.
    """
    self.update_idletasks()
    width = self.winfo_width()
    frm_width = self.winfo_rootx() - self.winfo_x()
    win_width = width + 2 * frm_width
    height = self.winfo_height()
    titlebar_height = self.winfo_rooty() - self.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = self.winfo_screenwidth() // 2 - win_width // 2
    y = self.winfo_screenheight() // 2 - win_height // 2
    self.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    self.deiconify()
