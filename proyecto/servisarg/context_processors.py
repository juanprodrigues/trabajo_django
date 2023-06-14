from .models import Trabajador
# Necesario para poder ver el is_trabajador como un valor en los templates, como me interasa que se pueda determinar en las vistas
#  no se podia ya que base no estaba recibiendo algun contexto
def trabajador_context(request):
    is_trabajador = False
    trabajador_exists = Trabajador.objects.filter(username=request.user.username).exists()

    if request.user.is_authenticated:
        # is_trabajador = Trabajador.objects.filter(username=request.user.username).exists()
        # is_trabajador = Trabajador.objects.filter(username=request.user.username).exists()
        is_trabajador=True
    return {
        'is_trabajador': is_trabajador,
        'trabajador_exists': trabajador_exists

    }
