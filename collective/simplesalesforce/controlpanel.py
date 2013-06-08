from z3c.form import interfaces

from zope import schema
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.interface import Interface

from plone.app.registry.browser import controlpanel

class ISalesforceSettings(Interface):
    """ Global settings for collective.simplesalesforce stored in the registry """
    username = schema.TextLine(
        title=u"Salesforce Username",
        description=u"The username of the Salesforce user to authenticate using"
    )
    password = schema.TextLine(
        title=u"Password",
        description=u"Enter the password for the Salesforce user"
    )
    security_token = schema.TextLine(
        title=u"Security Token",
        description=u"Enter the security token for the Salesforce user"
    )
    sandbox = schema.Bool(
        title=u"Sandbox?",
        description=u"If connecting to a Sandbox instance, check this box.  Otherwise, production instance is assumed"
    )


class SalesforceSettingsEditForm(controlpanel.RegistryEditForm):
    schema = ISalesforceSettings
    label = u"Salesforce Settings"
    description = u"Configuration for collective.salesforce providing integration with Salesforce.com"

#    def updateFields(self):
#        super(SalesforceSettingsEditForm, self).updateFields()

#    def updateWidgets(self):
#        super(SalesforceSettingsEditForm, self).updateWidgets()

class SalesforceSettingsControlPanel(controlpanel.ControlPanelFormWrapper):
    form = SalesforceSettingsEditForm
