    // Crear una instancia del WebSocket
    const socket = new WebSocket('ws://localhost:8080/chat/');  // Reemplaza la URL con la ruta correcta de tu WebSocket

    // Evento de conexión del WebSocket
    socket.onopen = function() {
        console.log('Conectado al WebSocket');
    };

    // Evento de recepción de mensajes del WebSocket
    socket.onmessage = function(event) {
        const mensaje = JSON.parse(event.data).mensaje;
        recibirMensaje(mensaje);
    };

    // Función para enviar un mensaje al WebSocket
    function enviarMensaje(mensaje) {
        const mensajeJSON = JSON.stringify({ 'mensaje': mensaje });
        socket.send(mensajeJSON);
    }

    // Evento de envío del formulario de mensaje
    messageForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const mensaje = messageInput.value;

        // Enviar el mensaje al WebSocket
        enviarMensaje(mensaje);

        // Limpiar el campo de entrada
        messageInput.value = '';
    });

    // Función para mostrar los mensajes en el frontend
    function mostrarMensaje(mensaje) {
        const mensajeElemento = document.createElement('p');
        mensajeElemento.textContent = mensaje;
        messagesDiv.appendChild(mensajeElemento);
    }

    // Función para recibir mensajes del WebSocket y mostrarlos en el frontend
    function recibirMensaje(mensaje) {
        mostrarMensaje(mensaje);
    }