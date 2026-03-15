from rest_framework.exceptions import NotFound

def get_object(model,pk):
    try:
        return model.objects.get(pk=pk)
    except model.DoesNotExist:
        raise NotFound(f"{model.__name__} with {pk} not found")