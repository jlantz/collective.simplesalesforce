from zope.component import getUtility
from zope.interface import Interface
from five import grok
from simple_salesforce import Salesforce
from plone.registry.interfaces import IRegistry
from collective.simplesalesforce.controlpanel import ISalesforceSettings


def get_settings():
    registry = getUtility(IRegistry)
    return registry.forInterface(ISalesforceSettings, False)

class ISalesforceUtility(Interface):
    """ A global utility providing methods to access the Salesforce REST API """

    def get_connection():
        """ returns a simple salesforce connection instance """

class SalesforceUtility(object):
    grok.implements(ISalesforceUtility)

    def get_connection(self):
        settings = get_settings()
        sf = Salesforce(
            username=settings.username,
            password=settings.password,
            security_token=settings.security_token,
            sandbox=settings.sandbox
        )
        return sf

grok.global_utility(SalesforceUtility, provides=ISalesforceUtility)
