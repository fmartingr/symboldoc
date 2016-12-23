# -*- coding: utf-8 -*-
import os
import ast
import unittest

import symboldoc


PATH = os.getcwd()
if 'tests' not in PATH:
    PATH += '/tests/'


class ASTTest(unittest.TestCase):
    @property
    def module_for_tests(self):
        return os.path.join(PATH, 'moduletest.py')

    def get_ast_tree(self):
        return symboldoc.get_ast_tree(self.module_for_tests)

    def test_get_ast_tree_ok(self):
        tree = self.get_ast_tree()
        self.assertIsInstance(tree, ast.Module)

    def test_iter_tree_return_all_objects(self):
        tree = self.get_ast_tree()
        items = list(symboldoc.iter_tree(tree))
        # 6: Module, Method, Return, Class, Method, Return
        self.assertEqual(len(items), 6)

    def test_find_symbol_in_tree_ok(self):
        tree = self.get_ast_tree()
        node = symboldoc.find_symbol_in_tree(tree, 'my_function')
        self.assertIsInstance(node, ast.FunctionDef)

    def test_find_symbol_in_tree_ko(self):
        tree = self.get_ast_tree()
        node = symboldoc.find_symbol_in_tree(tree, 'not_my_function')
        self.assertIsNone(node)
