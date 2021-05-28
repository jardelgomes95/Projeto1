from django.contrib import admin

from .models import matricula

admin.site.register(matricula)

from .models import financeiro
admin.site.register(financeiro)

from .models import outros_servico
admin.site.register(outros_servico)

from .models import pilates
admin.site.register(pilates)

from .models import fitdance
admin.site.register(fitdance)

from .models import funcional
admin.site.register(funcional)

from .models import kangoodance
admin.site.register(kangoodance)

from .models import muaythai
admin.site.register(muaythai)

from .models import frequencia
admin.site.register(frequencia)
