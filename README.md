collective.simplesalesforce
===========================
This package provides an integration wrapper for the simple-salesforce library for accessing the Salesforce.com REST API.  It also provides a control panel where the authentication info can be set and a utility (ISalesforceUtility) to fetch an active connection to Salesforce.

Example (after plugging in authentication info to Plone control panel):

>>> from zope.component import getUtility
>>> from collective.simplesalesforce.utils import ISalesforceUtility
>>> sf = getUtility(ISalesforceUtility).get_connection()
>>> sf.query("select id from contact where email = 'someperson@mailinator.com'")

For more info on the API of simple-salesforce, check the URL below.  
https://github.com/neworganizing/simple-salesforce


Replacing Beatbox
=================
This package was created to replace beatbox where appropriate.  The process of migrating from beatbox to simple-salesforce for query, create, and update actions proved to be rather easy for collective.salesforce.fundraising

For an example of porting, check the commit:
https://github.com/innocenceproject/collective.salesforce.fundraising/commit/b36a918ecf8a0bca614c03df9017bbd9a167c894
