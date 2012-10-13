class SetupVarious:

    def __call__(self, context):

        # Ordinarily, GenericSetup handlers check for the existence of XML files.
        # Here, we are not parsing an XML file, but we use this text file as a 
        # flag to check that we actually meant for this import step to be run.
        # The file is found in profiles/default.

        if context.readDataFile('${namespace_package}.${package}') is None:
            return

        # Add additional setup code here
        site = context.getSite()

        # do something...


def setupVarious(context):
    """ setup various step. Handles for steps not handled by a gs profile """
    handler = SetupVarious()
    handler(context)

