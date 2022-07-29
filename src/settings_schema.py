settings_schema = {
    "groups": [
        {
            "name": "accent_colors",
            "title": _("Accent Colors"),
            "description": _("These colors are used across many different widgets, such as buttons, labels, and entries, to indicate that a widget is important, interactive, or currently active."),
            "variables": [
                {
                    "name": "accent_color",
                    "title": _("Standalone Color"),
                    "explanation": _("The standalone colors are similar to the background ones, but provide better contrast when used as foreground color on top of a neutral background - for example, colorful text in a window."),
                    "adw_gtk3_support": "yes"
                },
                {
                    "name": "accent_bg_color",
                    "title": _("Background Color"),
                    "adw_gtk3_support": "yes"
                },
                {
                    "name": "accent_fg_color",
                    "title": _("Foreground Color"),
                    "adw_gtk3_support": "yes"
                }
            ]
        },
        {
            "name": "destructive_colors",
            "title": _("Destructive Colors"),
            "description": _("These colors are used for buttons to indicate a dangerous action, such as deleting a file."),
            "variables": [
                {
                    "name": "destructive_color",
                    "title": _("Standalone Color"),
                    "explanation": _("The standalone colors are similar to the background ones, but provide better contrast when used as foreground color on top of a neutral background - for example, colorful text in a window."),
                    "adw_gtk3_support": "yes"
                },
                {
                    "name": "destructive_bg_color",
                    "title": _("Background Color"),
                    "adw_gtk3_support": "yes"
                },
                {
                    "name": "destructive_fg_color",
                    "title": _("Foreground Color"),
                    "adw_gtk3_support": "partial"
                }
            ]
        },
        {
            "name": "success_colors",
            "title": _("Success Colors"),
            "description": _("These colors are used across many different widgets, such as buttons, labels, entries, and level bars, to indicate a success or a high level."),
            "variables": [
                {
                    "name": "success_color",
                    "title": _("Standalone Color"),
                    "explanation": _("The standalone colors are similar to the background ones, but provide better contrast when used as foreground color on top of a neutral background - for example, colorful text in a window."),
                    "adw_gtk3_support": "yes"
                },
                {
                    "name": "success_bg_color",
                    "title": _("Background Color"),
                    "adw_gtk3_support": "yes"
                },
                {
                    "name": "success_fg_color",
                    "title": _("Foreground Color"),
                    "adw_gtk3_support": "partial"
                }
            ]
        },
        {
            "name": "warning_colors",
            "title": _("Warning Colors"),
            "description": _("These colors are used across many different widgets, such as buttons, labels, entries, and level bars, to indicate a warning or a low level."),
            "variables": [
                {
                    "name": "warning_color",
                    "title": _("Standalone Color"),
                    "explanation": _("The standalone colors are similar to the background ones, but provide better contrast when used as foreground color on top of a neutral background - for example, colorful text in a window."),
                    "adw_gtk3_support": "yes"
                },
                {
                    "name": "warning_bg_color",
                    "title": _("Background Color"),
                    "adw_gtk3_support": "yes"
                },
                {
                    "name": "warning_fg_color",
                    "title": _("Foreground Color"),
                    "adw_gtk3_support": "partial"
                }
            ]
        },
        {
            "name": "error_colors",
            "title": _("Error Colors"),
            "description": _("These colors are used across many different widgets, such as buttons, labels, and entries, to indicate a failure."),
            "variables": [
                {
                    "name": "error_color",
                    "title": _("Standalone Color"),
                    "explanation": _("The standalone colors are similar to the background ones, but provide better contrast when used as foreground color on top of a neutral background - for example, colorful text in a window."),
                    "adw_gtk3_support": "yes"
                },
                {
                    "name": "error_bg_color",
                    "title": _("Background Color"),
                    "adw_gtk3_support": "yes"
                },
                {
                    "name": "error_fg_color",
                    "title": _("Foreground Color"),
                    "adw_gtk3_support": "partial"
                }
            ]
        },
        {
            "name": "window_colors",
            "title": _("Window Colors"),
            "description": _("These colors are used primarily for windows."),
            "variables": [
                {
                    "name": "window_bg_color",
                    "title": _("Background Color"),
                    "adw_gtk3_support": "yes"
                },
                {
                    "name": "window_fg_color",
                    "title": _("Foreground Color"),
                    "adw_gtk3_support": "yes"
                }
            ]
        },
        {
            "name": "view_colors",
            "title": _("View Colors"),
            "description": _("These colors are used in a variety of widgets, such as text views and entries."),
            "variables": [
                {
                    "name": "view_bg_color",
                    "title": _("Background Color"),
                    "adw_gtk3_support": "yes"
                },
                {
                    "name": "view_fg_color",
                    "title": _("Foreground Color"),
                    "adw_gtk3_support": "yes"
                }
            ]
        },
        {
            "name": "headerbar_colors",
            "title": _("Header Bar Colors"),
            "description": _("These colors are used for header bars, as well as widgets that are meant to be visually attached to it, such as search bars or tab bars."),
            "variables": [
                {
                    "name": "headerbar_bg_color",
                    "title": _("Background Color"),
                    "adw_gtk3_support": "yes"
                },
                {
                    "name": "headerbar_fg_color",
                    "title": _("Foreground Color"),
                    "adw_gtk3_support": "yes"
                },
                {
                    "name": "headerbar_border_color",
                    "title": _("Border Color"),
                    "explanation": _("The border color has the same default value as a foreground color, but doesn't change along with it. This can be useful if a light window has a dark header bar with light text; in this case it may be desirable to keep the border dark. This variable is only used for vertical borders - for example, separators between the two header bars in a split header bar layout."),
                    "adw_gtk3_support": "no"
                },
                {
                    "name": "headerbar_backdrop_color",
                    "title": _("Backdrop Color"),
                    "explanation": _("The backdrop color is used instead of the background color when the window is not focused. By default it's an alias of the window's background color and changes together with it. When changing this variable, make sure to set it to a value matching your header bar background color."),
                    "adw_gtk3_support": "yes"
                },
                {
                    "name": "headerbar_shade_color",
                    "title": _("Shade Color"),
                    "explanation": _("The shade color is used to provide a dark border for header bars and similar widgets that separates them from the main window."),
                    "adw_gtk3_support": "no"
                }
            ]
        },
        {
            "name": "card_colors",
            "title": _("Card Colors"),
            "description": _("These colors are used for cards and boxed lists."),
            "variables": [
                {
                    "name": "card_bg_color",
                    "title": _("Background Color"),
                    "adw_gtk3_support": "yes"
                },
                {
                    "name": "card_fg_color",
                    "title": _("Foreground Color"),
                    "adw_gtk3_support": "yes"
                },
                {
                    "name": "card_shade_color",
                    "title": _("Shade Color"),
                    "explanation": _("The shade color is used for shadows that are used by cards to separate themselves from the window background, as well as for row dividers in the cards."),
                    "adw_gtk3_support": "no"
                }
            ]
        },
        {
            "name": "dialog_colors",
            "title": _("Dialog Colors"),
            "description": _("These colors are used for message dialogs."),
            "variables": [
                {
                    "name": "dialog_bg_color",
                    "title": _("Background Color"),
                    "adw_gtk3_support": "no"
                },
                {
                    "name": "dialog_fg_color",
                    "title": _("Foreground Color"),
                    "adw_gtk3_support": "no"
                }
            ]
        },
        {
            "name": "popover_colors",
            "title": _("Popover Colors"),
            "description": _("These colors are used for popovers."),
            "variables": [
                {
                    "name": "popover_bg_color",
                    "title": _("Background Color"),
                    "adw_gtk3_support": "yes"
                },
                {
                    "name": "popover_fg_color",
                    "title": _("Foreground Color"),
                    "adw_gtk3_support": "yes"
                }
            ]
        },
        {
            "name": "misc_colors",
            "title": _("Miscalleneous Colors"),
            "description": _("Colors that don't fit in any particular group."),
            "variables": [
                {
                    "name": "shade_color",
                    "title": _("Shade Color"),
                    "explanation": _("The shade color is used by inline tab bars, as well as the transitions in leaflets and flaps, and info bar borders."),
                    "adw_gtk3_support": "no"
                },
                {
                    "name": "scrollbar_outline_color",
                    "title": _("Scrollbar Outline Color"),
                    "explanation": _("The scrollbar outline color is used by scrollbars to ensure that overlay scrollbars are visible regardless of the content color."),
                    "adw_gtk3_support": "no"
                }
            ]
        }
    ],
    "palette": [
        {
            "prefix": "blue_",
            "title": _("Blue"),
            "n_shades": 5
        },
        {
            "prefix": "green_",
            "title": _("Green"),
            "n_shades": 5
        },
        {
            "prefix": "yellow_",
            "title": _("Yellow"),
            "n_shades": 5
        },
        {
            "prefix": "orange_",
            "title": _("Orange"),
            "n_shades": 5
        },
        {
            "prefix": "red_",
            "title": _("Red"),
            "n_shades": 5
        },
        {
            "prefix": "purple_",
            "title": _("Purple"),
            "n_shades": 5
        },
        {
            "prefix": "brown_",
            "title": _("Brown"),
            "n_shades": 5
        },
        {
            "prefix": "light_",
            "title": _("Light"),
            "n_shades": 5
        },
        {
            "prefix": "dark_",
            "title": _("Dark"),
            "n_shades": 5
        }
    ],
    "custom_css_app_types": [
        "gtk4",
        "gtk3"
    ]
}