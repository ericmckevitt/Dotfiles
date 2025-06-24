# oh wait wrong file location
config.load_autoconfig()

# :config-edit will open the config in kitty nvim session
c.editor.command = ["kitty", "-e", "nvim", "{}"]

c.url.searchengines = {
    'DEFAULT': 'https://www.google.com/search?q={}',
    'yt': 'https://www.youtube.com/results?search_query={}',
    'gh': 'https://github.com/search?q={}',
}
c.url.start_pages = ["https://www.google.com/"]
c.url.default_page = "https://www.google.com/"
c.fonts.default_size = "14pt"
c.tabs.position = "top"
c.tabs.show = "multiple"
c.editor.command = ["nvim", "{}"]

# Bindings
config.bind('M', 'hint links spawn mpv {hint-url}')
config.bind('xb', 'config-cycle statusbar.show always never')
