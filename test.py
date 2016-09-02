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
        self.assertEqual(GIT + "--help", gt._last_command)

class GitterTestCheckout(unittest.TestCase):
    def test_checkout_local_branch(self):
        gt = TestingGitRunner(["checkout"])
        gt._selected = [gitter.LocalBranch('develop')]
        gt.run()
        self.assertEqual(GIT + "checkout develop", gt._last_command)

    def test_remote_branch(self):
        gt = TestingGitRunner(["checkout"])
        gt._selected = [gitter.RemoteBranch('bugfix')]
        gt.run()
        self.assertEqual(GIT + "checkout -b bugfix bugfix", gt._last_command)

    def test_modified(self):
        gt = TestingGitRunner(["checkout"])
        gt._selected = [gitter.ModifiedFile('somefile.py')]
        gt.run()
        self.assertEqual(GIT + "checkout somefile.py", gt._last_command)

    def test_deleted(self):
        gt = TestingGitRunner(["checkout"])
        gt._selected = [gitter.DeletedFile('deleted.py')]
        gt.run()
        self.assertEqual(GIT + "checkout deleted.py", gt._last_command)

    def test_multiple(self):
        gt = TestingGitRunner(["checkout"])
        gt._selected = [gitter.ModifiedFile('somefile.py'), gitter.DeletedFile('deleted.py')]
        gt.run()
        self.assertEqual(GIT + "checkout somefile.py deleted.py", gt._last_command)

if __name__ == '__main__':
    unittest.main()
