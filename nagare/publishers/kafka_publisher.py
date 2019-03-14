# --
# Copyright (c) 2008-2019 Net-ng.
# All rights reserved.
#
# This software is licensed under the BSD License, as described in
# the file LICENSE.txt, which you should have received as part of
# this distribution.
# --

"""The Kafka publisher"""

from nagare.server import publisher


class Publisher(publisher.Publisher):
    """The Kafka publisher"""

    def __init__(self, name, dist, kafka_consumer_service, **config):
        super(Publisher, self).__init__(name, dist, **config)
        self.consumer = kafka_consumer_service

    def generate_banner(self):
        banner = super(Publisher, self).generate_banner()

        topics = ['`{}`'.format(topic) for topic in sorted(self.consumer.subscription())]
        return banner + ' on topics {}'.format(', '.join(topics))

    def _serve(self, app, **conf):
        super(Publisher, self)._serve(app)

        try:
            for msg in self.consumer:
                self.start_handle_request(app, msg=msg)
        except KeyboardInterrupt:
            self.consumer.close()

        return 0
