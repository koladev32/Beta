from apps.core.renderers import AppsJSONRenderer

class EventJSONRenderer(AppsJSONRenderer):
    object_label = 'event'
    object_label_plural='events'

class CommentJSONRenderer(AppsJSONRenderer):
    object_label='comment'
    object_label_plural = 'comments'