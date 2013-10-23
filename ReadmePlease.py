import sublime, sublime_plugin
import os
import re

class ReadmePleaseCommand(sublime_plugin.WindowCommand):

  def description(self):
    'Quick access to packages README'

  def run(self):

    variations = ["README.*", "readme.*", "Readme.*", "ReadMe.*"]

    self.helps = set()

    for spelling in variations:
        readmes = sublime.find_resources(spelling)

        for readme in readmes:
            package = (readme.split('/'))

            if len(package) > 3:
                continue
            package_name = package[-2]
            readme_name = package[-1]
            self.helps.add((package_name, readme_name, readme))

    self.helps = list(self.helps)
    self.helps.sort()
    self.window.show_quick_panel(list(map(lambda x: [x[0], x[1]], self.helps)), self.onSelect)

  def onSelect(self, i):
    if (i != -1):
        help = self.helps[i]

        help_view = sublime.active_window().run_command("open_file", { "file": "${packages}/%s/%s" % (help[0],help[1])})
