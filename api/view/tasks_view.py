from flask_restful import Resource
from api import api, db
from ..models import tarefa_model
from ..schemas import tarefa_schema
from flask import request, make_response, jsonify
from ..entities import tarefa
from ..services import tarefas_service


class TarefaList(Resource):

    def get(self):
        tarefas = tarefa_model.Tarefa.query.all()
        ts = tarefa_schema.TarefaSchema(many=True)
        return make_response(ts.jsonify(tarefas), 200)

    def post(self):
        ts = tarefa_schema.TarefaSchema()
        validate = ts.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            titulo = request.json["titulo"]
            descricao = request.json["descricao"]
            data_expiracao = request.json["data_expiracao"]
            tarefa_bd = tarefa_model.Tarefa(titulo=titulo, descricao=descricao,
                                            data_expiracao=data_expiracao)
            db.session.add(tarefa_bd)
            db.session.commit()
            # nova_tarefa = tarefa.Tarefa(titulo=titulo, descricao=descricao, data_expiracao=data_expiracao)
            # result = tarefas_service.cadastrar_tarefa(nova_tarefa)

            return make_response(ts.jsonify(tarefa_bd), 201)


class TarefaDetail(Resource):

    def get(self, id):
        tarefa = tarefa_model.Tarefa.query.filter_by(id=id).first()
        if tarefa is None:
            return make_response(jsonify("Tarefa não encontrada"), 404)
        ts = tarefa_schema.TarefaSchema()
        return make_response(ts.jsonify(tarefa), 200)

    def put(self, id):
        pass


api.add_resource(TarefaList, '/tarefas')
api.add_resource(TarefaDetail, '/tarefas/<int:id>')
