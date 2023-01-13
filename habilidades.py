from flask import Flask,request
from flask_restful import Resource
import json
lista_habilidades = [
                     {
                      'id':0,
                      'habilidade':'python'},
                     {
                         'id':1,
                         'habilidade':'java'},
                     {
                         'id':2,
                         'habilidade':'Flask'
                         },
                     {
                         'id':3,
                         'habilidade':'PHP'
                      }
]

class Habilidades(Resource):
    
    def get(self, id):
        try:
            return lista_habilidades[id]
        except IndexError:
            return {'Status':'Error','Mensagem':'Habilidade não existem'}
        except IndexError:
            return {'Status':'Error','Mensagem':'Error Desconhecidorw'}
        
    def put(self, id):
         try:
             dados = json.loads(request.data)
         except IndexError:
             mensagem = 'Habilidade já existem'.format(lista_habilidades[id])
             return {'Status':'Error','Mensagem':mensagem}
         except Exception:
             mensagem = 'Error Desconhecido'
             return {'Status':'Error','Mensagem':mensagem}
         if  lista_habilidades[id]  != dados:
              lista_habilidades[id] = dados
              return lista_habilidades[id]
    def delete(self, id):
        try:
           lista_habilidades.pop(id)
           return {'Status':'Sucesso Deleta'}
        except IndexError:
             mensagem = 'Habilidade já existem'
             return {'Status':'Error','Mensagem':mensagem}
        except Exception:
             mensagem = 'Error Desconhecido'
             return {'Status':'Error','Mensagem':mensagem}
        
         
         
class Lista_Habilidades(Resource):
        def get(self):
            return lista_habilidades
        
        def post(self):
           dados =   json.loads(request.data)
           posicao = len(lista_habilidades)
           dados['id'] = posicao 
           lista_habilidades.append(dados)
           return lista_habilidades[posicao]
