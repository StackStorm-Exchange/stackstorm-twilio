from twilio.rest import Client

from st2common.runners.base_action import Action


class TwilioSendSMSAction(Action):
    def __init__(self, config):
        super(TwilioSendSMSAction, self).__init__(config=config)
        self.client = Client(self.config['account_sid'], self.config['auth_token'])

    def run(self, from_number, to_number, body):
        try:
            self.client.messages.create(body=body, from_=from_number, to=to_number)
        except Exception as e:
            error_msg = ('Failed sending sms to: %s, exception: %s\n' %
                         (to_number, str(e)))
            self.logger.error(error_msg)
            raise Exception(error_msg)

        self.logger.info('Successfully sent sms to: %s\n' % to_number)
