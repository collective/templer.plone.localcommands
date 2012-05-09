"""
Local command templates for the archetype templer templates
"""
import os
from templer.core.vars import var
from templer.localcommands import TemplerLocalTemplate

from Cheetah.Template import Template as cheetah_template


class ArchetypeSubTemplate(TemplerLocalTemplate):
    use_cheetah = True
    parent_templates = ['archetype']


class ContentType(ArchetypeSubTemplate):
    """
    A Content Type skeleton
    """

    _template_dir = 'templates/archetype/contenttype'
    summary = "A content type skeleton"

    vars = [
        var('contenttype_name', 'Content type name ',
            default='Example Type'),
        var('contenttype_description', 'Content type description ',
            default='Description of the Example Type'),
        var('folderish', 'True/False: Content type is Folderish ',
            default=False),
        var('global_allow', 'True/False: Globally addable ',
            default=True),
        var('allow_discussion', 'True/False: Allow discussion ',
            default=False),
        ]

    def pre(self, command, output_dir, vars):
        vars['contenttype_classname'] =\
            vars['contenttype_name'].replace(" ", "")
        vars['schema_name'] =\
            vars['contenttype_classname'] + "Schema"
        vars['content_class_filename'] =\
            vars['contenttype_classname'].lower()
        vars['types_xml_filename'] =\
            vars['contenttype_name'].replace(" ", "_")
        vars['interface_name'] =\
            "I" + vars['contenttype_name'].replace(" ", "")
        vars['add_permission_name'] =\
            vars['package_dotted_name'] + ': Add ' + vars['contenttype_name']
