class By(object):
    def __init__(self, tag_name=None, container=None, **kwargs):
        self.tag_name = tag_name
        self.container = container
        self._attrs = kwargs

    @property
    def attrs(self):
        if 'class_' in self._attrs.keys():
            self._attrs.update({'class': self._attrs.get('class_')})
            self._attrs.pop('class_')
        return self._attrs
