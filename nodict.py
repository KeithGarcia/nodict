#!/usr/bin/env python3
"""
Implementation of the NoDict assignment
"""

__author__ = 'Keith Garcia, Co-Author Ben McKenzie'


class Node:
    def __init__(self, key, value=None):
        """Init Node"""
        self.hash = None
        self.key = key
        self.value = value
        self.hash = hash(self.key)

    def __repr__(self):
        """Key/Value contents"""
        return f'{self.__class__.__name__}({self.key}, {self.value})'

    def __eq__(self, other):
        """Equals"""
        return self.key == other.key


class NoDict:
    def __init__(self, num_buckets=10):
        """Init NoDict"""
        self.buckets = [[] for i in range(num_buckets)]

    def __repr__(self):
        """Return a string representing the NoDict contents"""
        return '\n'.join([f'{self.__class__.__name__}.{i}:{bucket}' for i, bucket in enumerate(self.buckets)])

    def add(self, key, value):
        """Put key/value into NoDict"""
        added_node = Node(key, value)
        index = added_node.hash % len(self.buckets)
        for node in self.buckets[index]:
            if node == added_node:
                self.buckets[index].remove(node)
        self.buckets[index].append(added_node)

    def get(self, key):
        """key lookup/return node value"""
        got_node = Node(key)
        index = got_node.hash % len(self.buckets)
        for node in self.buckets[index]:
            if node == got_node:
                return node.value
        raise KeyError(f'{key} not found')

    def __getitem__(self, key):
        """Square bracket reading"""
        return self.get(key)

    def __setitem__(self, key, value):
        """Square bracket assignment"""
        self.add(key, value)
