from zeep import Client

client = Client('http://soapclient.com/cxml/soapresponder.wsdl')
result = client.service.Method1('oi',        'tchau')

print(result) 