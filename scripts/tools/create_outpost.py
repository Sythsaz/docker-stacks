from authentik.outposts.models import Outpost, OutpostType
from authentik.providers.proxy.models import ProxyProvider
import uuid

provider = ProxyProvider.objects.first()
outpost = Outpost.objects.filter(name='External Proxy').first()
if not outpost:
    outpost = Outpost.objects.create(name='External Proxy', type=OutpostType.PROXY)
    
outpost.providers.add(provider)
outpost.save()
print('TOKEN:', outpost.token.key)
