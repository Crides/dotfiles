# Autogenerated config.py
# Documentation:
#   qute://help/configuring.html
#   qute://help/settings.html

# Uncomment this to still load settings configured via autoconfig.yml
# config.load_autoconfig()

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'file://*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'chrome://*/*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'qute://*/*')

config.load_autoconfig()

# Text color of the completion widget. May be a single color to use for
# all columns or a list of three colors, one for each column.
# Type: List of QtColor, or QtColor
c.colors.completion.fg = '#d5c4a1'

# Background color of the completion widget for odd rows.
# Type: QssColor
c.colors.completion.odd.bg = '#665c54'

# Background color of the completion widget for even rows.
# Type: QssColor
c.colors.completion.even.bg = '#282828'

# Foreground color of completion widget category headers.
# Type: QtColor
c.colors.completion.category.fg = '#fabd2f'

# Background color of the completion widget category headers.
# Type: QssColor
c.colors.completion.category.bg = '#282828'

# Top border color of the completion widget category headers.
# Type: QssColor
c.colors.completion.category.border.top = '#282828'

# Bottom border color of the completion widget category headers.
# Type: QssColor
c.colors.completion.category.border.bottom = '#282828'

# Foreground color of the selected completion item.
# Type: QtColor
c.colors.completion.item.selected.fg = '#3c3836'

# Background color of the selected completion item.
# Type: QssColor
c.colors.completion.item.selected.bg = '#fabd2f'

# Top border color of the selected completion item.
# Type: QssColor
c.colors.completion.item.selected.border.top = '#fabd2f'

# Bottom border color of the selected completion item.
# Type: QssColor
c.colors.completion.item.selected.border.bottom = '#fabd2f'

# Foreground color of the matched text in the selected completion item.
# Type: QtColor
c.colors.completion.item.selected.match.fg = '#fb4934'

# Foreground color of the matched text in the completion.
# Type: QtColor
c.colors.completion.match.fg = '#b8bb26'

# Color of the scrollbar handle in the completion view.
# Type: QssColor
c.colors.completion.scrollbar.fg = '#d5c4a1'

# Color of the scrollbar in the completion view.
# Type: QssColor
c.colors.completion.scrollbar.bg = '#282828'

# Background color for the download bar.
# Type: QssColor
c.colors.downloads.bar.bg = '#282828'

# Color gradient start for download text.
# Type: QtColor
c.colors.downloads.start.fg = '#282828'

# Color gradient start for download backgrounds.
# Type: QtColor
c.colors.downloads.start.bg = '#83a598'

# Color gradient end for download text.
# Type: QtColor
c.colors.downloads.stop.fg = '#282828'

# Color gradient stop for download backgrounds.
# Type: QtColor
c.colors.downloads.stop.bg = '#8ec07c'

# Foreground color for downloads with errors.
# Type: QtColor
c.colors.downloads.error.fg = '#fb4934'

# Font color for hints.
# Type: QssColor
c.colors.hints.fg = '#282828'

# Background color for hints. Note that you can use a `rgba(...)` value
# for transparency.
# Type: QssColor
c.colors.hints.bg = '#fabd2f'

# Font color for the matched part of hints.
# Type: QtColor
c.colors.hints.match.fg = '#d5c4a1'

# Text color for the keyhint widget.
# Type: QssColor
c.colors.keyhint.fg = '#d5c4a1'

# Highlight color for keys to complete the current keychain.
# Type: QssColor
c.colors.keyhint.suffix.fg = '#d5c4a1'

# Background color of the keyhint widget.
# Type: QssColor
c.colors.keyhint.bg = '#282828'

# Foreground color of an error message.
# Type: QssColor
c.colors.messages.error.fg = '#282828'

# Background color of an error message.
# Type: QssColor
c.colors.messages.error.bg = '#fb4934'

# Border color of an error message.
# Type: QssColor
c.colors.messages.error.border = '#fb4934'

# Foreground color of a warning message.
# Type: QssColor
c.colors.messages.warning.fg = '#282828'

# Background color of a warning message.
# Type: QssColor
c.colors.messages.warning.bg = '#d3869b'

# Border color of a warning message.
# Type: QssColor
c.colors.messages.warning.border = '#d3869b'

# Foreground color of an info message.
# Type: QssColor
c.colors.messages.info.fg = '#d5c4a1'

# Background color of an info message.
# Type: QssColor
c.colors.messages.info.bg = '#282828'

# Border color of an info message.
# Type: QssColor
c.colors.messages.info.border = '#282828'

# Foreground color for prompts.
# Type: QssColor
c.colors.prompts.fg = '#d5c4a1'

# Border used around UI elements in prompts.
# Type: String
c.colors.prompts.border = '#282828'

# Background color for prompts.
# Type: QssColor
c.colors.prompts.bg = '#282828'

# Background color for the selected item in filename prompts.
# Type: QssColor
c.colors.prompts.selected.bg = '#fabd2f'

# Foreground color of the statusbar.
# Type: QssColor
c.colors.statusbar.normal.fg = '#b8bb26'

# Background color of the statusbar.
# Type: QssColor
c.colors.statusbar.normal.bg = '#282828'

# Foreground color of the statusbar in insert mode.
# Type: QssColor
c.colors.statusbar.insert.fg = '#282828'

# Background color of the statusbar in insert mode.
# Type: QssColor
c.colors.statusbar.insert.bg = '#83a598'

# Foreground color of the statusbar in passthrough mode.
# Type: QssColor
c.colors.statusbar.passthrough.fg = '#282828'

# Background color of the statusbar in passthrough mode.
# Type: QssColor
c.colors.statusbar.passthrough.bg = '#8ec07c'

# Foreground color of the statusbar in private browsing mode.
# Type: QssColor
c.colors.statusbar.private.fg = '#282828'

# Background color of the statusbar in private browsing mode.
# Type: QssColor
c.colors.statusbar.private.bg = '#665c54'

# Foreground color of the statusbar in command mode.
# Type: QssColor
c.colors.statusbar.command.fg = '#d5c4a1'

# Background color of the statusbar in command mode.
# Type: QssColor
c.colors.statusbar.command.bg = '#282828'

# Foreground color of the statusbar in private browsing + command mode.
# Type: QssColor
c.colors.statusbar.command.private.fg = '#d5c4a1'

# Background color of the statusbar in private browsing + command mode.
# Type: QssColor
c.colors.statusbar.command.private.bg = '#282828'

# Foreground color of the statusbar in caret mode.
# Type: QssColor
c.colors.statusbar.caret.fg = '#282828'

# Background color of the statusbar in caret mode.
# Type: QssColor
c.colors.statusbar.caret.bg = '#d3869b'

# Foreground color of the statusbar in caret mode with a selection.
# Type: QssColor
c.colors.statusbar.caret.selection.fg = '#282828'

# Background color of the statusbar in caret mode with a selection.
# Type: QssColor
c.colors.statusbar.caret.selection.bg = '#83a598'

# Background color of the progress bar.
# Type: QssColor
c.colors.statusbar.progress.bg = '#83a598'

# Default foreground color of the URL in the statusbar.
# Type: QssColor
c.colors.statusbar.url.fg = '#d5c4a1'

# Foreground color of the URL in the statusbar on error.
# Type: QssColor
c.colors.statusbar.url.error.fg = '#fb4934'

# Foreground color of the URL in the statusbar for hovered links.
# Type: QssColor
c.colors.statusbar.url.hover.fg = '#d5c4a1'

# Foreground color of the URL in the statusbar on successful load
# (http).
# Type: QssColor
c.colors.statusbar.url.success.http.fg = '#8ec07c'

# Foreground color of the URL in the statusbar on successful load
# (https).
# Type: QssColor
c.colors.statusbar.url.success.https.fg = '#b8bb26'

# Foreground color of the URL in the statusbar when there's a warning.
# Type: QssColor
c.colors.statusbar.url.warn.fg = '#d3869b'

# Background color of the tab bar.
# Type: QssColor
c.colors.tabs.bar.bg = '#282828'

# Color gradient start for the tab indicator.
# Type: QtColor
c.colors.tabs.indicator.start = '#83a598'

# Color gradient end for the tab indicator.
# Type: QtColor
c.colors.tabs.indicator.stop = '#8ec07c'

# Color for the tab indicator on errors.
# Type: QtColor
c.colors.tabs.indicator.error = '#fb4934'

# Foreground color of unselected odd tabs.
# Type: QtColor
c.colors.tabs.odd.fg = '#d5c4a1'

# Background color of unselected odd tabs.
# Type: QtColor
c.colors.tabs.odd.bg = '#665c54'

# Foreground color of unselected even tabs.
# Type: QtColor
c.colors.tabs.even.fg = '#d5c4a1'

# Background color of unselected even tabs.
# Type: QtColor
c.colors.tabs.even.bg = '#282828'

# Foreground color of selected odd tabs.
# Type: QtColor
c.colors.tabs.selected.odd.fg = '#282828'

# Background color of selected odd tabs.
# Type: QtColor
c.colors.tabs.selected.odd.bg = '#d5c4a1'

# Foreground color of selected even tabs.
# Type: QtColor
c.colors.tabs.selected.even.fg = '#282828'

# Background color of selected even tabs.
# Type: QtColor
c.colors.tabs.selected.even.bg = '#d5c4a1'

# Foreground color of pinned unselected odd tabs.
# Type: QtColor
c.colors.tabs.pinned.odd.fg = '#fbf1c7'

# Background color of pinned unselected odd tabs.
# Type: QtColor
c.colors.tabs.pinned.odd.bg = '#b8bb26'

# Foreground color of pinned unselected even tabs.
# Type: QtColor
c.colors.tabs.pinned.even.fg = '#fbf1c7'

# Background color of pinned unselected even tabs.
# Type: QtColor
c.colors.tabs.pinned.even.bg = '#8ec07c'

# Foreground color of pinned selected odd tabs.
# Type: QtColor
c.colors.tabs.pinned.selected.odd.fg = '#d3869b'

# Background color of pinned selected odd tabs.
# Type: QtColor
c.colors.tabs.pinned.selected.odd.bg = '#d5c4a1'

# Foreground color of pinned selected even tabs.
# Type: QtColor
c.colors.tabs.pinned.selected.even.fg = '#282828'

# Background color of pinned selected even tabs.
# Type: QtColor
c.colors.tabs.pinned.selected.even.bg = '#d5c4a1'
# base16-qutebrowser (https://github.com/theova/base16-qutebrowser)
# Base16 qutebrowser template by theova
# Gruvbox dark, medium scheme by Dawid Kurek (dawikur@gmail.com), morhetz (https://github.com/morhetz/gruvbox)

base00 = "#282828"
base01 = "#3c3836"
base02 = "#504945"
base03 = "#665c54"
base04 = "#bdae93"
base05 = "#d5c4a1"
base06 = "#ebdbb2"
base07 = "#fbf1c7"
base08 = "#fb4934"
base09 = "#fe8019"
base0A = "#fabd2f"
base0B = "#b8bb26"
base0C = "#8ec07c"
base0D = "#83a598"
base0E = "#d3869b"
base0F = "#d65d0e"

# set qutebrowser colors

# Text color of the completion widget. May be a single color to use for
# all columns or a list of three colors, one for each column.
c.colors.completion.fg = base05

# Background color of the completion widget for odd rows.
c.colors.completion.odd.bg = base03

# Background color of the completion widget for even rows.
c.colors.completion.even.bg = base00

# Foreground color of completion widget category headers.
c.colors.completion.category.fg = base0A

# Background color of the completion widget category headers.
c.colors.completion.category.bg = base00

# Top border color of the completion widget category headers.
c.colors.completion.category.border.top = base00

# Bottom border color of the completion widget category headers.
c.colors.completion.category.border.bottom = base00

# Foreground color of the selected completion item.
c.colors.completion.item.selected.fg = base01

# Background color of the selected completion item.
c.colors.completion.item.selected.bg = base0A

# Top border color of the selected completion item.
c.colors.completion.item.selected.border.top = base0A

# Bottom border color of the selected completion item.
c.colors.completion.item.selected.border.bottom = base0A

# Foreground color of the matched text in the selected completion item.
c.colors.completion.item.selected.match.fg = base08

# Foreground color of the matched text in the completion.
c.colors.completion.match.fg = base0B

# Color of the scrollbar handle in the completion view.
c.colors.completion.scrollbar.fg = base05

# Color of the scrollbar in the completion view.
c.colors.completion.scrollbar.bg = base00

# Background color for the download bar.
c.colors.downloads.bar.bg = base00

# Color gradient start for download text.
c.colors.downloads.start.fg = base00

# Color gradient start for download backgrounds.
c.colors.downloads.start.bg = base0D

# Color gradient end for download text.
c.colors.downloads.stop.fg = base00

# Color gradient stop for download backgrounds.
c.colors.downloads.stop.bg = base0C

# Foreground color for downloads with errors.
c.colors.downloads.error.fg = base08

# Font color for hints.
c.colors.hints.fg = base00

# Background color for hints. Note that you can use a `rgba(...)` value
# for transparency.
c.colors.hints.bg = base0A

# Font color for the matched part of hints.
c.colors.hints.match.fg = base05

# Text color for the keyhint widget.
c.colors.keyhint.fg = base05

# Highlight color for keys to complete the current keychain.
c.colors.keyhint.suffix.fg = base05

# Background color of the keyhint widget.
c.colors.keyhint.bg = base00

# Foreground color of an error message.
c.colors.messages.error.fg = base00

# Background color of an error message.
c.colors.messages.error.bg = base08

# Border color of an error message.
c.colors.messages.error.border = base08

# Foreground color of a warning message.
c.colors.messages.warning.fg = base00

# Background color of a warning message.
c.colors.messages.warning.bg = base0E

# Border color of a warning message.
c.colors.messages.warning.border = base0E

# Foreground color of an info message.
c.colors.messages.info.fg = base05

# Background color of an info message.
c.colors.messages.info.bg = base00

# Border color of an info message.
c.colors.messages.info.border = base00

# Foreground color for prompts.
c.colors.prompts.fg = base05

# Border used around UI elements in prompts.
c.colors.prompts.border = base00

# Background color for prompts.
c.colors.prompts.bg = base00

# Background color for the selected item in filename prompts.
c.colors.prompts.selected.bg = base0A

# Foreground color of the statusbar.
c.colors.statusbar.normal.fg = base0B

# Background color of the statusbar.
c.colors.statusbar.normal.bg = base00

# Foreground color of the statusbar in insert mode.
c.colors.statusbar.insert.fg = base00

# Background color of the statusbar in insert mode.
c.colors.statusbar.insert.bg = base0D

# Foreground color of the statusbar in passthrough mode.
c.colors.statusbar.passthrough.fg = base00

# Background color of the statusbar in passthrough mode.
c.colors.statusbar.passthrough.bg = base0C

# Foreground color of the statusbar in private browsing mode.
c.colors.statusbar.private.fg = base00

# Background color of the statusbar in private browsing mode.
c.colors.statusbar.private.bg = base03

# Foreground color of the statusbar in command mode.
c.colors.statusbar.command.fg = base05

# Background color of the statusbar in command mode.
c.colors.statusbar.command.bg = base00

# Foreground color of the statusbar in private browsing + command mode.
c.colors.statusbar.command.private.fg = base05

# Background color of the statusbar in private browsing + command mode.
c.colors.statusbar.command.private.bg = base00

# Foreground color of the statusbar in caret mode.
c.colors.statusbar.caret.fg = base00

# Background color of the statusbar in caret mode.
c.colors.statusbar.caret.bg = base0E

# Foreground color of the statusbar in caret mode with a selection.
c.colors.statusbar.caret.selection.fg = base00

# Background color of the statusbar in caret mode with a selection.
c.colors.statusbar.caret.selection.bg = base0D

# Background color of the progress bar.
c.colors.statusbar.progress.bg = base0D

# Default foreground color of the URL in the statusbar.
c.colors.statusbar.url.fg = base05

# Foreground color of the URL in the statusbar on error.
c.colors.statusbar.url.error.fg = base08

# Foreground color of the URL in the statusbar for hovered links.
c.colors.statusbar.url.hover.fg = base05

# Foreground color of the URL in the statusbar on successful load
# (http).
c.colors.statusbar.url.success.http.fg = base0C

# Foreground color of the URL in the statusbar on successful load
# (https).
c.colors.statusbar.url.success.https.fg = base0B

# Foreground color of the URL in the statusbar when there's a warning.
c.colors.statusbar.url.warn.fg = base0E

# Background color of the tab bar.
c.colors.tabs.bar.bg = base00

# Color gradient start for the tab indicator.
c.colors.tabs.indicator.start = base0D

# Color gradient end for the tab indicator.
c.colors.tabs.indicator.stop = base0C

# Color for the tab indicator on errors.
c.colors.tabs.indicator.error = base08

# Foreground color of unselected odd tabs.
c.colors.tabs.odd.fg = base05

# Background color of unselected odd tabs.
c.colors.tabs.odd.bg = base03

# Foreground color of unselected even tabs.
c.colors.tabs.even.fg = base05

# Background color of unselected even tabs.
c.colors.tabs.even.bg = base00

# Background color of pinned unselected even tabs.
c.colors.tabs.pinned.even.bg = base0C

# Foreground color of pinned unselected even tabs.
c.colors.tabs.pinned.even.fg = base07

# Background color of pinned unselected odd tabs.
c.colors.tabs.pinned.odd.bg = base0B

# Foreground color of pinned unselected odd tabs.
c.colors.tabs.pinned.odd.fg = base07

# Background color of pinned selected even tabs.
c.colors.tabs.pinned.selected.even.bg = base05

# Foreground color of pinned selected even tabs.
c.colors.tabs.pinned.selected.even.fg = base00

# Background color of pinned selected odd tabs.
c.colors.tabs.pinned.selected.odd.bg = base05

# Foreground color of pinned selected odd tabs.
c.colors.tabs.pinned.selected.odd.fg = base0E

# Foreground color of selected odd tabs.
c.colors.tabs.selected.odd.fg = base00

# Background color of selected odd tabs.
c.colors.tabs.selected.odd.bg = base05

# Foreground color of selected even tabs.
c.colors.tabs.selected.even.fg = base00

# Background color of selected even tabs.
c.colors.tabs.selected.even.bg = base05

# Background color for webpages if unset (or empty to use the theme's
# color).
# c.colors.webpage.bg = base00
