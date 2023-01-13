from flask import Flask, jsonify, request, json

app = Flask(__name__)

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

# devolve um desenvolvedor pelo ID, tambem altera e deleta um desenvolvedor
@app.route('/dev/<int:id>/', methods=['GET','PUT','DELETE'])
def  desenvolvedor(id):
       if request.method == 'GET':
           try:
                 response = desenvolvedores[id]
                 return  jsonify(response)
           except IndexError:
               mensagem = 'Desenvolvedor de ID {} não existe'.format(id)
               response = {'Status':'Erro','Mensagem':mensagem}
           except Exception:
               mensagem = 'Erro desconhecido. Procure o adiminstrador da API'
               renponse = {'Status':'Erro', 'Mensagem':mensagem}
           return  jsonify(response)
        
       elif request.method ==  'PUT':
            dados = json.loads(request.data)
            desenvolvedores[id] = dados
            return jsonify(dados)
        
       elif request.method == 'DELETE':
            desenvolvedores.pop(id)
            return jsonify({'Status':'sucessor','mensagem':'Reegistro excluido'})
# lista todos os desenvolvedores e premite registrar um novo desenvolvedor
@app.route('/dev/', methods=['GET', 'POST'])
def  list_dev():
        if  request.method == 'POST':
             dados = json.loads(request.data)
             posicao = len(desenvolvedores)
             dados['id'] = posicao
             desenvolvedores.append(dados)
             return jsonify(desenvolvedores[posicao])
        elif request.method == 'GET':
               return jsonify(desenvolvedores)


if   __name__ =="__main__":
      app.run(debug=True)
