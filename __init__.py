from os.path import dirname, join

from ratp_skill.index import ratp
from onyx.skills.core import OnyxSkill
from onyx.util.log import getLogger

__author__ = ''

LOGGER = getLogger(__name__)

class RATPSkill(OnyxSkill):
    def __init__(self):
        super(RATPSkill, self).__init__(name="RATPSkill")

    def get_blueprint(self):
        return ratp

    def initialize(self):
        LOGGER.info("RATP Skill initialize")

    def stop(self):
        pass

def create_skill():
    return RATPSkill()
