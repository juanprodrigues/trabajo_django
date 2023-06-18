from .models import Trabajador
# Necesario para poder ver el is_trabajador como un valor en los templates, como me interesa que se pueda determinar en las vistas
#  no se podia ya que base.html no estaba recibiendo algun contexto para poder determinar esta accion

# Forma de utilizar en el Templates---> 
# 
#   {% if trabajador_exists %}
#     <li class="nav-item">
#       <a class="nav-link" href="{% url 'alta_trabajador' %}">Modificar Usuario</a>
#     </li>
#   {% else %}
#       <li class="nav-item">
#         <div style="background-color: rgb(4, 0, 255);">
#           <a class="nav-link" href="{% url 'alta_trabajador' %}" style="color: white;">Brindar servicios</a>
#         </div>
#       </li>
#   {% endif %}

def trabajador_context(request):
    trabajador_exists = Trabajador.objects.filter(username=request.user.username).exists()
    return {
        'trabajador_exists': trabajador_exists
    }
