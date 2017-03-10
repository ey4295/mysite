#! /usr/bin/python3.4
# -*- coding: utf-8 -*-
"""
Twilio is an SMS gateway service,
which means  it’s a service that allows
 you to send text messages from your programs
"""
from twilio.rest import TwilioRestClient

account_sid='ACcd65f6468777e1ba55920c1d0f853c66'
auth_token='f97db0d0d6a6010702cc95708ed8be3c'
twi_client=TwilioRestClient(account_sid,auth_token)
my_twilio_number='(201)297-4038'
xuqh_cell='+8615094347232'
maomao_cell='+8615852189072'

def send_text(message,to_cell):
    """
        This functin helps send messages to xuqh and maomao
        :param message: content
        :param to_cell: receiver,like-"+86xxxxxxxxxxxx"
        :return: void
    """
    twi_client.messages.create(body=message,
                               from_=my_twilio_number, to=to_cell)
