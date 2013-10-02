from pybr9fabootstrap_example import models, forms

def includeme(config):

    try:
        # Example for pyramid_routesalchemy and akhet
        from pybr9fabootstrap_example.models import MyModel
        config.formalchemy_model("/my_model", package='pybr9fabootstrap_example',
                                 model='pybr9fabootstrap_example.models.MyModel',
                                 session_factory=models.DBSession,
                                 view='pybr9fabootstrap_example.forms.ModelView')
    except ImportError:
        pass
