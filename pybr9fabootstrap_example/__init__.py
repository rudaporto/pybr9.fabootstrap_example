from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from pybr9fabootstrap_example.models import appmaker
from pybr9fabootstrap_example import models, forms

def main(global_config, **settings):
    """ This function returns a WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    appmaker(engine)
    config = Configurator(settings=settings)
    config.add_static_view('static', 'pybr9fabootstrap_example:static', cache_max_age=3600)
    config.add_view('pybr9fabootstrap_example.views.view_home',
                    name="",
                    renderer="templates/home.pt")

    config.include('pyramid_formalchemy')
    # Adding the jquery libraries
    config.include('fa.bootstrap')
    # Adding the package specific routes
    config.include('pybr9fabootstrap_example.routes')

    config.formalchemy_admin("/admin",
                             models=models,
                             forms=forms,
                             session_factory=models.DBSession,
                             view="pybr9fabootstrap_example.forms.ModelView")

    return config.make_wsgi_app()
