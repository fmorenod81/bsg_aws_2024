from datetime import datetime
import boto3

dynamodb = boto3.resource('dynamodb')

now = datetime.now()
print("Antes   De Solicitud Creacion : ", now.time() )
table= dynamodb.create_table(
    TableName="Notes",
                KeySchema=[
                    {"AttributeName": "year", "KeyType": "HASH"},
                    {"AttributeName": "title", "KeyType": "RANGE"},
                ],
                AttributeDefinitions=[
                    {"AttributeName": "year", "AttributeType": "N"},
                    {"AttributeName": "title", "AttributeType": "S"},
                ],
                BillingMode='PAY_PER_REQUEST'
)
now = datetime.now()
print("Despues De Solicitud Creacion : ", now.time() )
table.meta.client.get_waiter('table_exists').wait(TableName='Notes')
now = datetime.now()
print("Despues De Espera Creacion : ", now.time() )
print(table.item_count)
