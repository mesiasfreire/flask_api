from flask import request
from flask_restful import Resource
from api import api
from ..schemas import tarefa_schema
from flask import request, make_response, jsonify
from ..entities import tarefa
from ..services import tarefas_service


class TaskList(Resource):

    def get(self):
        return "Holl Mundo"

    def post(self):
        ts = tarefa_schema.TarefaSchema()
        validate = ts.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            titulo = request.json["titulo"]
            descricao = request.json["descricao"]
            data_expiracao = request.json["data_expiracao"]

            nova_tarefa = tarefa.Tarefa(titulo=titulo, descricao=descricao, data_expiracao=data_expiracao)

            result = tarefas_service.cadastrar_tarafa(nova_tarefa)

            return make_response(ts.jsonify(result, 201))

api.add_resource(TaskList, '/tarefas')
