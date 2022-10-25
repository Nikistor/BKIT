class FigureColor:
    """
    Класс «Цвет фигуры»
    """
    def __init__(self):
        self._color = None

    @property
    def colorproperty(self):
        """
        Get-аксессор
        Get – аксессор, который используется для чтения значения из внутреннего поля класса
        """
        return self._color

    @colorproperty.setter
    def colorproperty(self, value):
        """
        Set-аксессор
        Set – аксессор, используемый для записи значения во внутреннее поле класса.
        """
        self._color = value