class Project:
    def __init__(self, name, description, dependencies, dev_dependencies, license, authors):
        self.name = name
        self.description = description
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies
        self.license = license
        self.authors = authors

    def _stringify_dependencies(self, dependencies):
        return "\n- ".join(dependencies)

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license or '-'}\n"
            f"\nAuthors: \n- {self._stringify_dependencies(self.authors)}"
            f"\nDependencies: \n- {self._stringify_dependencies(self.dependencies)}"
            f"\nDevelopment dependencies: \n- {self._stringify_dependencies(self.dev_dependencies)}"
        )