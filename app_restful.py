from flask import Flask,request
from flask_restful import Resource, Api
from habilidades import Habilidades, Lista_Habilidades
import json

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
        {
            
                    'id':0,
                    'nome':'Rafael',
                    'habilidades':['Python','Flask']
         },
        {
            
                    'id':1,
                    'nome':'Galleani',
                    'habilidades':['Python','Django']
         }
    ]


class Desenvolvedor(Resource):
    def get(self, id):
           try:
               response = desenvolvedores[id]
           except  IndexError:
               mensagem = 'Desenvolvedor de ID {} não existe'.format(id)
               response = {'Status':'Erro','Mensagem':mensagem}
           except  Exception:
               mensagem = 'Erro desconhecidor. Procure o Adiministrador da Api'
               response = {'Status':'Erro','Mensagem':mensagem}
           return response
            
        
    def put(self, id):
           dados = json.loads(request.data)
           desenvolvedores[id] = dados
           return  dados
        
    def delete(self, id):
           try:
               desenvolvedores.pop(id)
               response = {'Statuy':'sucessor','Mensagem':'Registrador excluidor'}
           except IndexError:
               mensagem = 'Desenvolvedor de ID {} não existe'.format(id)
               response ={'Statuy':'Error','Mensagem':mensagem}
           return response
    
class listaDesenvolvedor(Resource):
    def get(self):
        return desenvolvedores

    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] =posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]
    
api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(listaDesenvolvedor, '/dev/')
api.add_resource(Habilidades, '/habilidades/<int:id>/')
api.add_resource(Lista_Habilidades,  '/habilidades/')

if __name__=='__main__':
    app.run(debug=True)
