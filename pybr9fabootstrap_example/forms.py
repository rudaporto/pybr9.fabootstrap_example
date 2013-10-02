from formalchemy import forms
from formalchemy import tables
from pyramid.renderers import get_renderer
from fa.bootstrap.views import ModelView as Base
from fa.bootstrap import fanstatic_resources


class FieldSet(forms.FieldSet):
    pass


class Grid(tables.Grid):
    pass


class ModelView(Base):

    def render(self, **kwargs):
        result = super(ModelView, self).render(**kwargs)
        result['main_template'] = get_renderer('pybr9fabootstrap_example:templates/main_template.pt').implementation()
        result['main'] = get_renderer('fa.bootstrap:templates/admin/master.pt').implementation()
        return result

    def update_resources(self):
        """A hook to add some fanstatic resources"""
        fanstatic_resources.bootstrap.need()
