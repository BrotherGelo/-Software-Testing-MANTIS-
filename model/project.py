from sys import maxsize


class Project:

    def __init__(self, id=None, name=None, description=None, status=None):
        self.id = id
        self.name = name
        self.description = description
        self.status = status


    def __repr__(self):
        return "%s:%s:%s:%s" % (self.id, self.name, self.description, self.status)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and\
               (self.name is None or other.name is None or self.name == other.name) and \
               (self.description is None or other.description is None or self.description == other.description) and \
               (self.status is None or other.status is None or self.status == other.status)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize