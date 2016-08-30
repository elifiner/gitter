#!/usr/bin/env python

import imp
import unittest

gitter = imp.load_source('gitter', 'gitter')
GIT = gitter.GITBIN + " "

class TestingGitRunner(gitter.GitRunner):
    def set_menu_result(self, selected):
        self._selected = selected

    def run(self):
        # disable printing help notice
        return self._run()

    def _show_menu(self, options, multiselect, precolored=False):
        # override to inject menu responses
        return self._selected

    def _system(self, command):
        # capture external calls to git
        self._last_command = command

class GitterTests(unittest.TestCase):
    def test_help(self):
        gt = TestingGitRunner(["--help"])
        gt.run()
        self.assertEquals(GIT + "--help", gt._last_command)

if __name__ == '__main__':
    unittest.main()
