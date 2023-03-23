"""
Testing
==============

FileSystem = {
    1: [type="Directory", name="Root", children=[2, 5]},
    2: {type="Directory", name="Test Directory", children=[3, 4]},
    3: {type="File", name = "File1", size=100},
    4: {type="File", name = "File2", size=200},
    5: {type="File", name = "File3", size=300},
}

"""

class FileSystem:
    def __init__(self):
        return

import sys
import math

class Entity:
    def __init__(self, entity_type, name, size, children):
        self.id = id
        self.entity_type = entity_type
        self.name = name
        self.size = size
        self.children = children

    def get_size(self, fileSystem: FileSystem, entityId):
        """Get size of entity passed to function."""
        entity_size = 0

        for i in fileSystem:
            if i.type == 'directory':
                #
            elif i.type == 'file':
                file_size += i.size

        return entity_size

    def get_sizes(self, file_system: FileSystem, entity_id: list):
        """Get sizes of entities passed to function."""
        # User Recursion
        total_size_count = 0
        for i in file_system:
            if i.id is in entity_id:
                if i.type == 'Directory' and i.has_children():
                    for j in i.children:
                        total_size_countj.get_size()


def solution(x):
    """
    Function
    """

    return x


if __name__ == '__main__':
    input = ' '.join(sys.argv[1:])

    result = solution(input)

    print(result)
