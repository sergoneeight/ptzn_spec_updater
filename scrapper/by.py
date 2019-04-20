class By(object):
    def __init__(self, tag_name=None, class_=None, id=None, container=None):
        self.tag_name = tag_name
        self.container = container
        self.__class = class_
        self.__id = id

    @property
    def attrs(self):
        locable = {}
        if self.__class:
            locable.update({'class': self.__class})
        elif self.__id:
            locable.update({'id': self.__id})

        return locable
