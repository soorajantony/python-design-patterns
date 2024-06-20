"""
Single Responsibility Model
Each class has its own responsibility
PersistanceManager is a seperate class since it might be used by different classes and any change can be done at one place
Antipattern : a single class has everything, creating a massive object
"""
class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.entries.append(f"{self.count}: {text}")
        self.count += 1

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return "\n".join(self.entries)

    # break SRP
    def save(self, filename):
        pass

    def load(self, filename):
        pass

    def load_from_web(self, uri):
        pass


class PersistenceManager:
    def save_to_file(journal, filename):
        file = open(filename, "w")
        file.write(str(journal))
        file.close()


j = Journal()
j.add_entry("I cried today.")
j.add_entry("I ate a bug.")
print(f"Journal entries:\n{j}\n")

#p = PersistenceManager()
#file = r'c:\temp\journal.txt'
#p.save_to_file(j, file)

# verify!
#with open(file) as fh:
#    print(fh.read())
