"""
Local templates that are generally useful for every plone related project.
"""
from templer.core.vars import var
from templer.localcommands import TemplerLocalTemplate

class PloneSubTemplate(TemplerLocalTemplate):
    use_cheetah = True
    parent_templates = ['plone_basic', 'archetype']


class View(PloneSubTemplate):
    """
    A browser view skeleton
    """
    _template_dir = 'templates/plone/view'
    summary = "A browser view skeleton"

    vars = [
      var('view_name', 'Browser view name',  default="Example"), ]

    def pre(self, command, output_dir, vars):
        """
        you can use package_namespace, package_namespace2, package
        and package_dotted_name of the parent package here. you get them
        for free in the vars argument
        """
        vars['view_filename'] = vars['view_name'].lower().replace(' ', '')
        vars['view_classname'] = vars['view_name'].replace(' ', '')


class UpgradeSteps(PloneSubTemplate):
    """
    An upgrade steps skeleton

    TODO: make this local command available just if exists a generic profile.
    Don't know if it is necessary

    Some validators for source and destination are needed?
    
    """
    _template_dir = 'templates/plone/upgradesteps'
    summary = "An upgrade steps skeleton"

    vars = [
      var('source', 'Source',  default="*"),
      var('destination', 'Destination',  default=""),
      ]

    def pre(self, command, output_dir, vars):
        """
        you can use package_namespace, package_namespace2, package
        and package_dotted_name of the parent package here. you get them
        for free in the vars argument
        """
        vars['normalized_destination'] = vars['destination'].replace('.', '_')


class BrowserLayer(PloneSubTemplate):
    """
    A browserlayer skeleton
    """
    _template_dir = 'templates/plone/browserlayer'
    summary = "A Plone browserlayer"

    vars = [
        var('interface_name',
            'Interface name for the browserlayer',
            default="IMyPackageBrowserLayer"),
        var('layer_name',
            "Browser layer name",
            default='MyPackage'), ]

    def check_vars(self, vars, cmd):
        """
        Overloading check_vars to print welcome message and provide sensitive default values
        """

        print "A BrowserLayer is generally used in packages to be installed in a Plone Site."
        print "If you didn't choose Register Profile option when creating this package"
        print "you will need to add a <genericsetup:registerProfile /> directive in"
        print "the main configure.zcml.\n"
        package_dotted_name = [vars['namespace_package']]
        if 'namespace_package2' in vars:
            package_dotted_name.append(vars['namespace_package2'])
        package_dotted_name.append(vars['package'])

        layer_name = ''.join([x.capitalize() for x in package_dotted_name])
        self.vars[1].default = layer_name
        self.vars[0].default = 'I%sLayer' % (layer_name)

        return super(BrowserLayer, self).check_vars(vars, cmd)


    def pre(self, command, output_dir, vars):
        """
        you can use package_namespace, package_namespace2, package
        and package_dotted_name of the parent package here. you get them
        for free in the vars argument
        """
        vars['interface_filename'] = vars['layer_name'].lower() + 'layer'


class Portlet(PloneSubTemplate):
    """
    A Plone portlet skeleton
    """
    _template_dir = 'templates/plone/portlet'
    summary = "A Plone Portlet"

    vars = [
      var('portlet_name', 'Portlet name (human readable)',
          default="Example portlet"),
      var('portlet_type_name', 'Portlet type name (should not contain spaces)',
          default="ExamplePortlet"),
      var('description', 'Portlet description', default=""),
           ]

    def pre(self, command, output_dir, vars):
        """
        you can use package_namespace, package_namespace2, package
        and package_dotted_name of the parent package here. you get them
        for free in the vars argument
        """
        vars['portlet_filename'] = vars['portlet_type_name'].lower()

        vars['dotted_name'] = "%s.portlets" % vars['package_dotted_name']

