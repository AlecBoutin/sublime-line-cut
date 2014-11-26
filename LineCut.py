import sublime, sublime_plugin

class LineCutCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		selectedRegions = self.view.sel()
		regionsToDelete = map(lambda r: self.view.full_line(r), selectedRegions)
		copyStr = ''.join(map(lambda r: self.view.substr(r), regionsToDelete))
		for region in regionsToDelete:
			self.view.erase(edit, region)
		sublime.set_clipboard(copyStr)