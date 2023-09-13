

define config.name = _("Funeral")


define gui.show_name = False


define config.version = "1.0"


define gui.about = _p("""
""")


define build.name = "Funeral"


define config.has_sound = True
define config.has_music = True
define config.has_voice = True



# define config.main_menu_music = "main-menu-theme.ogg"


define config.enter_transition = dissolve
define config.exit_transition = dissolve


define config.intra_transition = dissolve


define config.after_load_transition = dissolve


define config.end_game_transition = dissolve



define config.window = "auto"


define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)



default preferences.text_cps = 0


default preferences.afm_time = 15


define config.save_directory = "Funeral-1688422695"


define config.window_icon = "gui/window_icon.png"


init python:

   

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)


    build.documentation('*.html')
    build.documentation('*.txt')


