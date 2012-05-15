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
