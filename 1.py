#!/usr/bin/python
# -*- coding: utf-8 -*-
# consume_wsdl_soap_ws_pss.py
import logging.config
from pysimplesoap.client import SoapClient

logging.config.dictConfig({
    'version': 1,
    'formatters': {
        'verbose': {
            'format': '%(name)s: %(message)s'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'pysimplesoap.helpers': {
            'level': 'DEBUG',
            'propagate': True,
            'handlers': ['console'],
        },
    }
})

WSDL_URL = 'http://www.webservicex.net/stockquote.asmx?WSDL'
client = SoapClient(wsdl=WSDL_URL, ns="web", trace=True)
client['AuthHeaderElement'] = {'username': 'someone', 'password': 'nottelling'}

#Discover operations
list_of_services = [service for service in client.services]
print(list_of_services)

#Discover params
method = client.services['StockQuote']

response = client.GetQuote(symbol='GOOG')
print('GetQuote: {}'.format(response['GetQuoteResult']))