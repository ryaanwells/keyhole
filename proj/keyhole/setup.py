from models import Resources

def register(res):
    name = res.__class__.__name__
    print name
    print res.Meta.keyhole
    Resources.objects.get_or_create(name=name)

