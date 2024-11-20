from drf_spectacular.openapi import AutoSchema

class MySchema(AutoSchema):
    def get_tags(self, path, method):
        return ['my-tag']