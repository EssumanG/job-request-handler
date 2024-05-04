import os, json
import pika

from dotenv import load_dotenv

load_dotenv()

class CloudAMQPProducer:
    """ The interface between this project CloudAMQP"""


    EXCHANGE = "job_notifier_exchange"
    EXCHANGE_TYPE= "direct"
    QUEUE_NAME ="job_notifier_queue"
    ROUTING_KEY = "jobs_search"

    def __init__(self) -> None:
        """ Sets up a coneection and a channel when this class is instantiated """
        url = os.environ["CLOUDAMQP_URL"]
        self._params = pika.URLParameters(url)

        self.__connection = pika.BlockingConnection(self._params)

    def __create_channel(self) -> pika.BlockingConnection:
        if not self.__connection or self.__connection.is_closed:
            self.__connection = pika.BlockingConnection(self._params)
        channel = self.__connection.channel()
        return channel
    
    async def __create_exchanges_queues(self) -> None:
        """ Declares a qqueue and an exchange using the channel created """
        channel = self.__create_channel()

        channel.exchange_declare(
            exchange=self.EXCHANGE,
            exchange_type=self.EXCHANGE_TYPE
        )

        channel.queue_declare(queue=self.QUEUE_NAME)

        channel.queue_bind(
            self.QUEUE_NAME,
            self.EXCHANGE,
            self.ROUTING_KEY
        )
    
    async def publish_message(self, messge_body) -> None:
        """ Publish a message to CloudAMQP """

        await self.__create_exchanges_queues()


        channel = self.__create_channel()

        channel.basic_publish(
            exchange=self.EXCHANGE,
            routing_key=self.ROUTING_KEY,
            body=json.dumps(messge_body)

        )

        print ("[x] Message sent to consumer")

        self.__connection.close()

cloudamqp: CloudAMQPProducer = CloudAMQPProducer()