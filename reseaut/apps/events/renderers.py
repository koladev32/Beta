from apps.core.renderers import AppsJSONRenderer

class EventJSONRenderer(AppsJSONRenderer):
    object_label = 'event'
    object_label_plural='events'