from curso.models import Proyecto
from curso.models import Desafio
from curso.models import Estudiante
from curso.models import Grupo

proyecto = Proyecto(descripcion="Usar herramientas tecnologicas para la resolucion de problemas", cliente="Felipe Fica", fecha="30-04-2019") 

proyecto.save()

grupo1 = Grupo(nombre="Grupo 1", proyecto="TICs") 

grupo1.save()

estudiante1 = Estudiante(nombre="Jorge Alis", descripcion="jalis@gmail.com", numeroTelefonico= 99475678, grupo=grupo1) 

estudiante1.save()

estudiante2 = Estudiante(nombre="Felipe Avello", descripcion="favello@gmail.com", numeroTelefonico= 994959583, grupo=grupo1) 

estudiante2.save()

estudiante3 = Estudiante(nombre="Daniel Fica", descripcion="dfica@gmail.com", numeroTelefonico= 927654390, grupo="Grupo 1") 

estudiante3.save()

estudiante4 = Estudiante(nombre="Alvaro Salas", descripcion="asalas@gmail.com", numeroTelefonico= 923409856, grupo="Grupo 1") 

estudiante4.save()

desafio1 = Desafio(titulo="Desafio 1", descripcion="Hacer una pagina web, en la que se use bootstrap", fecha="2019-04-26") 

desafio1.save()

desafio2 = Desafio(titulo="Desafio 2", descripcion="Subir un repositorio a git", fecha="2019-04-26") 

desafio2.save()

