 #echo "#".join(['', ' -*- extra stuff goes here -*-'])#

def upgrade_to_${normalized_destination}(context):
    print "Upgrading to ${destination}"

    # Here you'll have to put your migration step code. For example run a
    # specific generic setup profile for each .xml that needs to be updated
    # context.runImportStepFromProfile(default_profile, 'controlpanel')
    # Or simply put your code here as you normally do in setuphandlers.py
    # steps

