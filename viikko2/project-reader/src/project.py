class Project:
    def __init__(self, name, description, license, author, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license = license
        self.author = author
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, dependencies):
        return "\n- " + "\n- ".join(dependencies) if len(dependencies) > 0 else "-"

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license}"
            f"\n"
            f"\nAuthors: {self._stringify_dependencies(self.author)}"
            f"\n"
            f"\nDependencies: {self._stringify_dependencies(self.dependencies)}"
            f"\n"
            f"\nDevelopment dependencies: {self._stringify_dependencies(self.dev_dependencies)}"
        )