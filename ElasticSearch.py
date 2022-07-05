import elasticsearch
print (elasticsearch.VERSION)

from elasticsearch import Elasticsearch
elastic_client = Elasticsearch(hosts=["https://eitanmedical.es.westeurope.azure.elastic-cloud.com"])


