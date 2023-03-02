import sublime
import sublime_plugin
import os
import shutil
import threading
import re


to_snake_case_pattern = re.compile(r'(?!^)(?<!_)([A-Z])')

def to_snake_case(txt):
	return to_snake_case_pattern.sub(r'_\1', txt).lower()

class SnakeCaseSelectionCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sel = self.view.sel()
		regions_by_line = self.view.split_by_newlines(sel[0])
		word_match_pattern = re.compile(r'^\s*(\w+)') # extracts the first word
		replacements = {}

		for region in regions_by_line:
			txt = self.view.substr(region)
			matches = word_match_pattern.findall(txt)
			if len(matches) == 0:
				continue

			txt = txt.replace(matches[0], to_snake_case(matches[0]))
			replacements[matches[0]] = to_snake_case(matches[0])

		full_region_txt = self.view.substr(sel[0])
		for orig_word in replacements:
			full_region_txt = full_region_txt.replace(orig_word, replacements[orig_word])
		self.view.replace(edit, self.view.full_line(sel[0]), full_region_txt)


class ToUpperSelectionCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sel = self.view.sel()
		for selection in sel:
			regions_by_line = self.view.split_by_newlines(selection)

			for region in regions_by_line:
				txt = self.view.substr(region)
				self.view.replace(edit, region, txt.upper())


class ToLowerSelectionCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sel = self.view.sel()
		for selection in sel:
			regions_by_line = self.view.split_by_newlines(selection)

			for region in regions_by_line:
				txt = self.view.substr(region)
				self.view.replace(edit, region, txt.lower())

