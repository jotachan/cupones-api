from app.api import app 

def test_precio_endpoint():
    app.config['TESTING'] = True
    client = app.test_client()

    response = client.post('/precio', json={
        "precio": 10000,
        "cupon": "OFERTA10",
        "impuesto": 0.19
    })

    assert response.status_code == 200
    json_data = response.get_json()
    assert "precio_final" in json_data

    esperado = round(10000 * 0.90 * 1.19, 2)
    assert json_data["precio_final"] == esperado

def test_precio_sin_cupon():
    app.config['TESTING'] = True
    client = app.test_client()

    response = client.post('/precio', json={
        "precio": 5000
    })

    assert response.status_code == 200
    json_data = response.get_json()
    assert "precio_final" in json_data

    esperado = round(5000 * 1.19, 2)
    assert json_data["precio_final"] == esperado
