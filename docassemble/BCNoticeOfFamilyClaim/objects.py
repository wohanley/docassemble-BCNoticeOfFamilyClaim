from docassemble.base.util import DAObject

class CourtRegistry(DAObject):
    def summary(self):
        return f"#### {word('Name')}\n\n{self.name}\n\n#### {word('Address')}\n\n{self.address}"
