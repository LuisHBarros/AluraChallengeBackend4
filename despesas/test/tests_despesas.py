from rest_framework.test import APITestCase
from despesas.models import Despesa
from rest_framework import status
from django.urls import reverse


class CursosTestCase(APITestCase):
    
    def setUp(self):
        self.list_url = reverse('Despesas-list')
        self.curso_1 = Despesa.objects.create(
            descricao ='Compra Palio', valor=20000.00, categoria='t', data='2022/09/25'
        )
        self.curso_2 = Despesa.objects.create(
            descricao ='Venda PS4', valor=2500.00, categoria='o', data='2022/09/25'
        )
        self.curso_3 = Despesa.objects.create(
            descricao ='Aluguel', valor=1250.00, categoria='m', data='2022/09/25'
        )       
    def test_get(self):
        """Teste que verifica a listagem de cursos por meio da requisição GET em 'Cursos'."""
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        
    def test_post(self):
        """Teste que verifica a publicação de cursos por meio da requisição POST em 'Cursos'."""
        data = {
            'descricao':'Mercado',
            'valor':400.00,
            'categoria':'a',
            'data':'2022/09/05'
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]["id"], 1)
        self.assertEqual(response.data[0]["descricao"], "Mercado")
        self.assertEqual(response.data[0]["valor"], 400.00)
        self.assertEqual(response.data[0]["categoria"], 'a')
        self.assertEqual(response.data[0]["data"], '2022/09/05')
        
    def test_delete(self):
        """Teste que verifica a exclusão da requisição DELETE em 'Cursos'."""
        response = self.client.delete('/despesas/1/')
        self.assertEquals(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        
    def test_put(self):
        """Teste que verifica a atualização de dados por meio da requisição PUT em 'Cursos'."""
        data = {
            'codigo_curso':'CTT3',
            'descricao':'Curso test atualização',
            'nivel':'I'
        }
        response = self.client.put('/cursos/1', data=data)
        self.assertEquals(response.status_code, status.HTTP_301_MOVED_PERMANENTLY)
        # data = {
        #     'codigo_curso':'CTT3',
        #     'descricao':'Curso test4',
        #     'nivel':'A'
        # }
        # response = self.client.put('/cursos/1/', data=data)
        # self.assertEquals(response.status_code, status.HTTP_200_OK)