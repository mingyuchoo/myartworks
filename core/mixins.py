from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin

try:
    import json
except ImportError:
    from django.utils import simplejson as json
import django.utils.six
from django.core import serializers
from django.core.exceptions import ImproperlyConfigured
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse, HttpResponseBadRequest


class PostWriterMixin(object):
    """
    PostWriterMixin
    """
    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        pk = self.kwargs.get("pk", None)
        queryset = queryset.get(pk=pk)
        try:
            obj = queryset.get()
        except ObjectDoesNotExist:
            raise PermissionDenied
        return obj


class WriterOnlyMixin(LoginRequiredMixin):
    """
    WriterOnlyMixin
    """
    obj = None

    def check_writer(self, request):
        self.obj = self.get_object()
        return request.user == self.obj.writer

    def get(self, request, *args, **kwargs):
        if not self.check_writer(request):
            raise PermissionDenied
        return super(WriterOnlyMixin, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if not self.check_writer(request):
            raise PermissionDenied
        return super(WriterOnlyMixin, self).post(request, *args, **kwargs)



class WriterOnlyMixin(LoginRequiredMixin):
    """
    WriterOnlyMixin
    """
    obj = None

    def check_writer(self, request):
        self.obj = self.get_object()
        return request.user == self.obj.writer

    def get(self, request, *args, **kwargs):
        if not self.check_writer(request):
            raise PermissionDenied
        return super(WriterOnlyMixin, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if not self.check_writer(request):
            raise PermissionDenied
        return super(WriterOnlyMixin, self).post(request, *args, **kwargs)


class ProjectManagerOnlyMixin(LoginRequiredMixin):
    """
    ProjectManagerOnlyMixin
    """
    obj = None

    def check_project_manager(self, request):
        self.obj = self.get_object()
        return request.user == self.obj.project.manager

    def get(self, request, *args, **kwargs):
        if not self.check_project_manager(request):
            raise PermissionDenied
        return super(ProjectManagerOnlyMixin, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if not self.check_project_manager(request):
            raise PermissionDenied
        return super(ProjectManagerOnlyMixin, self).post(request, *args, **kwargs)


class TeamLeaderOnlyMixin(LoginRequiredMixin):
    """
    TeamLeaderOnlyMixin
    """
    obj = None

    def check_project_manager(self, request):
        self.obj = self.get_object()
        return request.user == self.obj.team.leader

    def get(self, request, *args, **kwargs):
        if not self.check_project_manager(request):
            raise PermissionDenied
        return super(TeamLeaderOnlyMixin, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if not self.check_project_manager(request):
            raise PermissionDenied
        return super(TeamLeaderOnlyMixin, self).post(request, *args, **kwargs)



class JSONResponseMixin(object):
    """
    A mixin that allows you to easily serialize simple data such as a dict or
    Django modules.
    """
    content_type = None
    json_dumps_kwargs = None
    json_encoder_class = DjangoJSONEncoder

    def get_context_type(self):
        if (self.content_type is not None and
                not isinstance(self.content_type,
                               (six.string_types, six.text_type))):
            raise ImproperlyConfigured(
                '{0} is missing a content type. Define {0}.content_type, '
                'or override {0}.get_content_type().'.format(
                    self.__class__.__name__))
        return self.content_type or "application/json"

    def get_json_dumps_kwargs(self):
        if self.json_dumps_kwargs is None:
            self.json_dumps_kwargs = {}
        self.json_dumps_kwargs.setdefault('ensure_ascii', False)
        return self.json_dumps_kwargs

    def render_json_response(self, context_dict, status=200):
        """
        Limited serialization for shipping plain data. Do not use for models
        or other complex or custom objects.
        """
        json_context = json.dumps(
            serializers.serialize('json', context_dict),
            cls=self.json_encoder_class,
            **self.get_json_dumps_kwargs()).encode('utf-8')

        return HttpResponse(json_context,
                            content_type=self.get_context_type(),
                            status=status)

    def render_json_object_response(self, objects, **kwargs):
        """
        Serializers objects using Django's builtin JSON serializer. Additional
        kwargs can be used the same way for django.core.serializers.serialize.
        """
        json_data = serializers.serialize("json", objects, **kwargs)
        return HttpResponse(json_data, content_type=self.get_context_type())


class AjaxResponseMixin(object):
    """
    Mixin allows you to define a alternative methods for ajax requests, Similar
    to the normal get, post, and put methods, you can use get_ajax, post_ajax,
    and put_ajax.
    """
    request = None
    args = None
    kwargs = None

    def dispatch(self, request, *args, **kwargs):
        request_method = request.method.lower()

        if request.is_ajax() and request_method in self.http_method_names:
            handler = getattr(self, "{0}_ajax".format(request_method),
                              self.http_method_not_allowed)
            self.request = request
            self.args = args
            self.kwargs = kwargs
            return handler(request, *args, **kwargs)

        return super(AjaxResponseMixin, self).dispatch(request, *args, **kwargs)

    def get_ajax(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)

    def post_ajax(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def put_ajax(self, request, *args, **kwargs):
        return self.put(request, *args, **kwargs)

    def delete_ajax(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)


class JsonRequestResponseMixin(JSONResponseMixin):
    """
    Extends JSONResponseMixin. Attempts to parse request at JSON. If request
    is properly formatted, the json is saved to self.request_json as a Python
    object. request_json will be None for im-parsible requests.
    Set the attribute request_json to True to return a 400 "Bad Request" error
    for requests that don't contain JSON.

    Note: To allow public access to your view, you'll need to use the csrf_except
    decorator or CsrfExemptMixin.

    Example Usage:

    class SomeView(CsrfExemptMixin, JsonRequestResponseMixin):
        def post(self, request, *args, **kwargs):
            do_stuff_with_contents_of_request_json()
                return self.render_json_response(
                    {'message': 'Thanks!'})
    """
    request = None
    args = None
    kwargs = None
    request_json = None
    require_json = False
    error_response_dict = {"errors": ["Improperly formatted request"]}

    def render_bad_request_response(self, error_dict=None):
        if error_dict is None:
            error_dict = self.error_response_dict
        json_context = json.dumps(
            error_dict,
            cls=self.json_encoder_class,
            **self.get_json_dumps_kwargs()
        ).encode('utf-8')
        return HttpResponseBadRequest(
            json_context, context_type=self.get_context_type())

    def get_request_json(self):
        try:
            return json.loads(self.request.body.decode('utf-8'))
        except ValueError:
            return None

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        self.args = args
        self.kwargs = kwargs
        self.request_json = self.get_request_json()
        if self.require_json and self.request_json is None:
            return self.render_bad_request_response()
        return super(JsonRequestResponseMixin, self).dispatch(
            request, *args, **kwargs)


class JSONRequestResponseMixin(JsonRequestResponseMixin):
    pass
