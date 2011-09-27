from models import Igualito
import appengine_admin

class IgualitoAdmin(appengine_admin.ModelAdmin):
    model = Igualito
    listFields = ('nombre',)
    editFields = ('nombre', 'imagen1', 'imagen2')
    readonlyFields = ('fecha',)

appengine_admin.register(IgualitoAdmin)