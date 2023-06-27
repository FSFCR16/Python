class Agenda():


    def __init__(self):

        self.miagenda={}

    def agregarPersonas(self,nombre,telefono):

        self.miagenda[nombre]=telefono

    def __len__(self):
        return len(self.miagenda)

agendaPersonal=Agenda()

agendaPersonal.agregarPersonas("juan", "1312312")
agendaPersonal.agregarPersonas("david", "3213123")
agendaPersonal.agregarPersonas("luis", "312323")

print(len(agendaPersonal))