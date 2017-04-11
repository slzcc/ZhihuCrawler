from elasticsearch import Elasticsearch
item = 1
def ElasticSet(data,ElasticServer,item=None):
    es = Elasticsearch([ElasticServer])

    # es.index(index="zhihu-index", doc_type='tweet', id=item, body=data)

    es.index(index="zhihu-index", doc_type='tweet', body=data)

    es.indices.refresh(index="zhihu-index")