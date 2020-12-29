from django.test import TestCase
from rest_framework.test import APIRequestFactory

# Create your tests here.

factory = APIRequestFactory()

request = factory.post('/cliente/', {'nome':'fulano'}, format='json', content_type='application/json')
request = factory.post('/cliente/', {'idade':''}, format='json', content_type='application/json')
request = factory.post('/cliente/', {'nome':'fulano'}, format='json', content_type='application/json')

request = factory.put('/cliente/1/', {'idade': '45'}, format='json', content_type='application/json')

request = factory.get('/cliente/', format='json', content_type='application/json')
request = factory.get('/medico/', format='json', content_type='application/json')
request = factory.get('/clinica/', format='json', content_type='application/json')



class GetAllClientesTest(TestCase):
    

    def setUp(self):
        Cliente.objects.create(
            nome='Casper', idade=30, endereco='rua dos bobos', cpf=99999999999)
        Cliente.objects.create(
            nome='Muffin', idade=15, endereco='rua dos bobos', cpf=99999999999)
        Cliente.objects.create(
            nome='Rambo', idade=24, endereco='Rua dos bobos', cpf=99999999999)
        Cliente.objects.create(
            nome='Ricky', idade=64, endereco='Rua dos bobos', cpf=99999999999)

    def test_get_all_puppies(self):
        # get API response
        response = client.get(reverse('get_post_cliente'))
        # get data from db
        clientes = Cliente.objects.all()
        serializer = ClienteSerializer(clientes, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


        self.assertEqual(response.data, serializer.data)
        AssertionError: {} != [OrderedDict([('nome', 'Casper'), ('idade',[687 chars])])]


@api_view(['GET', 'POST'])
def get_post_clientes(request):
    # get all puppies
    if request.method == 'GET':
        puppies = Cliente.objects.all()
        serializer = ClienteSerializer(clientes, many=True)
        return Response(serializer.data)
    # insert a new record for a puppy
    elif request.method == 'POST':
        return Response({})

        Ran 2 tests in 0.072s

        OK


class CreateNewClienteTest(TestCase):
    def setUp(self):
        self.valid_payload = {
            'nome': 'Muffin',
            'idade': 4,
            'endereco': 'rua de baixo ',
            'cpf': 99999999999
        }
        self.invalid_payload = {
            'nome': '',
            'idade': 40,
            'endereco': 'vila do chaves',
            'cpf': 99999999999
        }

    def test_create_valid_cliente(self):
        response = client.post(
            reverse('get_post_clientes'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_cliente(self):
        response = client.post(
            reverse('get_post_clientes'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        AssertionError: 200 != 400

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        AssertionError: 200 != 201