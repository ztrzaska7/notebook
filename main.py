class Notebook:
    def __init__(self):
        self.notes=[]
    def add_note(self,text):
        self.notes.append(text)
    def delete_notes(self,indeks):
        if indeks >=0 and indeks< len(self.notes):
            del self.notes[indeks]

    def show_notes(self):
        if len(self.notes)==0:
            print("There are no notes")
        else:
            for indeks, note in enumerate(self.notes):
                print(f"The note{indeks+1}: {note}")

    def save_note(self,file_name):
        try:
            with open(file_name, 'w') as file:
                for note in self.notes:
                    file.write(note + '\n')
            print(f"Notes are saved in the file {file_name}")
        except IOError:
            print("Error")

    def load_from_the_file(self,file_name):
        try:
            with open(file_name, 'r') as file:
                self.notes=[line.rstrip('\n') for line in file]
            print(f"The notes are loaded from the file {file_name}")
        except IOError:
            print('Error ocurred loading the notes')

notebook=Notebook()
notebook.add_note("First note")
notebook.add_note("Second")
notebook.show_notes()
notebook.save_note('notatki.txt')
notebook.delete_notes(0)
notebook.show_notes()