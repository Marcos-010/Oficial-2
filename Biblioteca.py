class Livro:  #Biblioteca

    def __init__(self, Nomedolivro, autor, editora, ano_publicacao, ano_aquisicao, lido, data ):
        self.Nomedolivro = Nomedolivro
        self.autor = autor
        self.editora = editora
        self.ano_publicacao = ano_publicacao
        self.ano_aquisicao = ano_aquisicao
        self.lido = lido
        self.data = data

    def __repr__(self):
        return repr((self.Nomedolivro))

    def buscapeloautor(self, autor):
        for i in Biblioteca:
            if autor == i.autor:
                print(i)
                # return

    def buscapelotitulo(self, Nomedolivro):
        for i in Biblioteca:
           if Nomedolivro == i.Nomedolivro:
               print(i)

    def Ler_livro(self,data):
       self.lido = 'Sim'
       self.data = data

    def info(self):

        print()
        print('Nome do livro da Biblioteca...................: ' + self.Nomedolivro)
        print('O autor(a) principal do Livro.................: ' + self.autor)
        print('A editora(o) do Livro.........................: ' + self.editora)
        print('Ano de publicação do Livro....................: ' + str(self.ano_publicacao))
        print('Ano de aquisição do Livro.....................: ' + str(self.ano_aquisicao))
        print('Livro lido....................................: ' + self.lido)
        print('data..........................................: ' + str(self.data))

LI = Livro('O Pequeno Príncipe', 'Antoine de Saint-Exupéry', 'Éditions Gallimard', 1943, 2018, 'Não', 000)
LII = Livro('A Culpa É das Estrelas', 'John Green', 'Intrínseca', 2012, 2020, 'Não', 000)
LIII = Livro('O príncipe cruel', 'Holly Black', 'Galera Record', 2018, 2021, 'Não', 000)
LIV = Livro('A rainha do nada', 'Holly Black', 'Galera Record', 2019, 2021, 'Não', 000)
LV = Livro('Corte de espinhos e rosas', 'Sarah J Naas', 'Galera Record', 2018, 2021,'Não',000)

Biblioteca = [LI, LII, LIII, LIV, LV]

print()
print(sorted(Biblioteca, key=lambda Livro: Livro.Nomedolivro))

print('Buscando titulo')
Biblioteca[0].buscapelotitulo('A Culpa É das Estrelas')
print('Buscando titulo')
Biblioteca[0].buscapelotitulo('Corte de espinhos e rosas')

print('Buscando autor')
Biblioteca[0].buscapeloautor('John Green')
print('Buscando autor')
Biblioteca[0].buscapeloautor('Sarah J Naas')

LI.info()
LII.info()
LIII.info()
LIV.info()
LV.info()

LII.Ler_livro(2020)
LIV.Ler_livro(2019)
LV.Ler_livro(2021)
LII.info()
LIV.info()
LV.info()

Biblioteca[0].buscapelotitulo('A Culpa É das Estrelas')
Biblioteca[0].buscapelotitulo('Corte de espinhos e rosas')
Biblioteca[0].buscapeloautor('John Green')
Biblioteca[0].buscapeloautor('Sarah J Naas')
