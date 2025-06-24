from ranger.gui.colorscheme import ColorScheme
from ranger.gui.color import *

class CatppuccinMocha(ColorScheme):
    progress_bar_color = 208  # peach or similar

    def use(self, context):
        fg, bg, attr = default_colors

        if context.reset:
            return default_colors

        if context.in_browser:
            if context.selected:
                # This highlights the current file/folder under cursor
                attr |= reverse
            if context.directory:
                fg = 110  # teal
            if context.marked:
                fg = 208  # peach
                attr |= bold

        if context.in_titlebar:
            attr |= bold
            fg = 140  # mauve

        if context.in_statusbar:
            fg = 245
            bg = 60

        return fg, bg, attr

