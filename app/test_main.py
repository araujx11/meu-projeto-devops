import pytest
from app.main import app

@pytest.fixture
def cliente():
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c

def test_rota_raiz_retorna_ok(cliente):
    resposta = cliente.get("/")
    assert resposta.status_code == 200

def test_rota_raiz_contem_status(cliente):
    resposta = cliente.get("/")
    dados = resposta.get_json()
    assert dados["status"] == "ok"

def test_health_check(cliente):
    resposta = cliente.get("/saude")
    assert resposta.status_code == 200

def test_soma_correta(cliente):
    resposta = cliente.get("/soma/3/4")
    dados = resposta.get_json()
    assert dados["resultado"] == 7

def test_soma_com_zero(cliente):
    resposta = cliente.get("/soma/10/0")
    dados = resposta.get_json()
    assert dados["resultado"] == 10