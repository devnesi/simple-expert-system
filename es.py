from experta import *
import inquirer

sintomas = ['febre','irritação na pele','dor de cabeça', 'nariz pingando', 'conjuntivite','tosse','dor corporal','arrepios','dor de garganta','espirrando','glândulas inchadas']
perguntas = [
  inquirer.Text('nome', message="Informe o nome do paciente"),
  inquirer.Checkbox('sintomas',
                    message="Informe os sintomas",
                    choices=sintomas,
                   ),
]

answers = inquirer.prompt(perguntas)

class Doenca(Fact):
    pass

class RobotDoenca(KnowledgeEngine):
    def printX(self, nome, doenca, tratamento):
        print(nome + ' tem ' + doenca)
        print(tratamento)
    
    @Rule(Doenca(sintomas=['tosse','espirrando','nariz pingando']))
    def sarampo(self):
        self.printX(answers['nome'], 'sarampo', 'O tratamento do sarampo consiste em aliviar os sintomas através de repouso, hidratação e medicamentos como Paracetamol, durante cerca de 10 dias, que é o tempo de duração da doença.')
    
    @Rule(Doenca(sintomas=['dor de cabeça','espirrando','dor de garganta','nariz pingando','arrepios']))
    def resfriado(self):
        self.printX(answers['nome'], 'resfriado', 'O tratamento é apenas sintomático.')

    @Rule(Doenca(sintomas=['febre','dor de cabeça','dor corporal','conjuntivite','arrepios','dor de garganta','nariz pingando','tosse']))
    def gripe(self):
        self.printX(answers['nome'], 'gripe', 'O tratamento consiste em repouso na cama e a ingestão de muitos líquidos')
    
    @Rule(Doenca(sintomas=['febre','glândulas inchadas']))
    def caxumba(self):
        self.printX(answers['nome'], 'caxumba', 'O tratamento é apenas sintomático.')
    
    @Rule(Doenca(sintomas=['febre','arrepios','dor corporal','irritação na pele']))
    def catapora(self):
        self.printX(answers['nome'], 'catapora', 'O tratamento é consiste em medicamentos antialérgicos')

engine = RobotDoenca()
engine.reset()
engine.declare(Doenca(sintomas=answers['sintomas']))
engine.run()
