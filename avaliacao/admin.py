from django.contrib import admin

from .models import avaliacao

admin.site.register(avaliacao)

from .models import ficha_de_saude
admin.site.register(ficha_de_saude)

from .models import treino
admin.site.register(treino)

from .models import objetivos
admin.site.register(objetivos)

from .models import medicamento
admin.site.register(medicamento)

from .models import nutricao
admin.site.register(nutricao)

from .models import personal
admin.site.register(personal)
