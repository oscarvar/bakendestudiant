from Repositorios.RepositorioEstudiante import RepositorioEstudiante
from Modelos.Estudiante import Estudiante
class ControladorEstudiante():
    def __init__(self):
        print("Creando Controlador de EStuidante")
        self.repositorioEstudiante = RepositorioEstudiante()
    def index(self):
        print("Listando Estudiantes")
        return self.repositorioEstudiante.findAll()
    def create(self,infoEstudiante):
        print("Creando un Estudiante")
        nuevoEstudiante=Estudiante(infoEstudiante)
        return self.repositorioEstudiante.save(nuevoEstudiante)
    def show(self,id):
        print("Mostrando un Estudiante")
        elEstudiante=Estudiante(self.repositorioEstudiante.findById(id))
        return elEstudiante.__dict__
    def update(self,id,infoEstudiante):
        print("Actualizando un Estudiante")
        estudianteActual=Estudiante(self.repositorioEstudiante.findById(id))
        estudianteActual.cedula=infoEstudiante["cedula"]
        estudianteActual.nombre = infoEstudiante["nombre"]
        estudianteActual.apellido = infoEstudiante["apellido"]
        return self.repositorioEstudiante.save(estudianteActual)
    def delete(self,id):
        print("Eliminando un Estudiante")
        return self.repositorioEstudiante.delete(id)