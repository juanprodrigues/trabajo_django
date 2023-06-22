from django.apps import AppConfig

class ServisargConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "servisarg"
    def ready(self):
        insert_data()



from django.db import connection
# def insert_data():
#     with connection.cursor() as cursor:
#         cursor.execute("SELECT COUNT(*) FROM servisarg_oficio;")
#         count = cursor.fetchone()[0]
#         print(count)
#         if count == 0:
#             sql_statements = [
#                 "INSERT INTO servisarg_oficio (nombre) VALUES ('Cosinero');",
#                 "INSERT INTO servisarg_oficio (nombre) VALUES ('Electricista');",
#                 "INSERT INTO servisarg_oficio (nombre) VALUES ('Plomero');",
#                 "INSERT INTO servisarg_oficio (nombre) VALUES ('Pintor');",
#                 "INSERT INTO servisarg_oficio (nombre) VALUES ('Jardinero');",
#                 "INSERT INTO servisarg_oficio (nombre) VALUES ('Limpieza de hogar');",
#                 "INSERT INTO servisarg_oficio (nombre) VALUES ('Instalador de aire acondicionado');",
#                 "INSERT INTO servisarg_oficio (nombre) VALUES ('Reparación de electrodomésticos');",
#                 "INSERT INTO servisarg_oficio (nombre) VALUES ('Fontanero');",
#                 "INSERT INTO servisarg_oficio (nombre) VALUES ('Mudanzas');",
#                 "INSERT INTO servisarg_oficio (nombre) VALUES ('Gasista');",
#                 "INSERT INTO servisarg_oficio (nombre) VALUES ('Cuidador de mascotas');",
#                 "INSERT INTO servisarg_oficio (nombre) VALUES ('Decorador de interiores');",
#                 "INSERT INTO servisarg_oficio (nombre) VALUES ('Reparación de computadoras');",
#                 "INSERT INTO servisarg_oficio (nombre) VALUES ('Organizador profesional');",
#                 "INSERT INTO servisarg_oficio (nombre) VALUES ('Diseñador gráfico');"
#             ]

#             with connection.cursor() as cursor:
#                 for sql_statement in sql_statements:
#                     cursor.execute(sql_statement)
#                     print("Insertando:", sql_statement)

#             print("Datos insertados correctamente.")
        
#     with connection.cursor() as cursor:
#         cursor.execute("SELECT COUNT(*) FROM servisarg_consultareclamosugerencia;")
#         count = cursor.fetchone()[0]
#         if count == 0:
#                 print("Insertanto datos en la base de datos")
#                 sql_statements = [
#                     "INSERT INTO servisarg_consultareclamosugerencia (nombre, apellido, email, fecha_consulta, tipo, mensaje,leido , fecha_creacion) VALUES ('Juan', 'Pérez', 'juan@example.com', '2023-06-21', 'Consulta', '¿Cuál es el método de pago para un servicio?', False, 'NOW()');",
#                     "INSERT INTO servisarg_consultareclamosugerencia (nombre, apellido, email, fecha_consulta, tipo, mensaje,leido , fecha_creacion) VALUES ('María', 'Gómez', 'maria@example.com', '2023-06-21', 'Reclamo', 'Necesito ayuda con la devolución de un producto.', False, 'NOW()');",
#                     "INSERT INTO servisarg_consultareclamosugerencia (nombre, apellido, email, fecha_consulta, tipo, mensaje, leido, fecha_creacion) VALUES ('Pedro', 'López', 'pedro@example.com', '2023-06-21', 'Sugerencia', 'Me gustaría que agreguen más opciones de pago.', False, 'NOW()');",
#                     "INSERT INTO servisarg_consultareclamosugerencia (nombre, apellido, email, fecha_consulta, tipo, mensaje,leido , fecha_creacion) VALUES ('Ana', 'Rodríguez', 'ana@example.com', '2023-06-21', 'Consulta', '¿Cuál es el horario de atención al cliente?', False, 'NOW()');",
#                     "INSERT INTO servisarg_consultareclamosugerencia (nombre, apellido, email, fecha_consulta, tipo, mensaje, leido, fecha_creacion) VALUES ('Carlos', 'González', 'carlos@example.com', '2023-06-21', 'Reclamo', 'No recibí el producto que compré.', False, 'NOW()');",
#                     "INSERT INTO servisarg_consultareclamosugerencia (nombre, apellido, email, fecha_consulta, tipo, mensaje, leido, fecha_creacion) VALUES ('Laura', 'López', 'laura@example.com', '2023-06-21', 'Sugerencia', 'Sería genial si añadieran más colores disponibles.', False, 'NOW()');",
#                     "INSERT INTO servisarg_consultareclamosugerencia (nombre, apellido, email, fecha_consulta, tipo, mensaje,leido , fecha_creacion) VALUES ('Roberto', 'Torres', 'roberto@example.com', '2023-06-21', 'Consulta', '¿Cuál es la política de devoluciones?', False, 'NOW()');",
#                     "INSERT INTO servisarg_consultareclamosugerencia (nombre, apellido, email, fecha_consulta, tipo, mensaje, leido, fecha_creacion) VALUES ('Marcela', 'Hernández', 'marcela@example.com', '2023-06-21', 'Reclamo', 'El producto llegó dañado.', False, 'NOW()');",
#                     "INSERT INTO servisarg_consultareclamosugerencia (nombre, apellido, email, fecha_consulta, tipo, mensaje,leido , fecha_creacion) VALUES ('Fernando', 'Gutiérrez', 'fernando@example.com', '2023-06-21', 'Sugerencia', 'Podrían mejorar la velocidad de envío.', False, 'NOW()');",
#                     "INSERT INTO servisarg_consultareclamosugerencia (nombre, apellido, email, fecha_consulta, tipo, mensaje,leido , fecha_creacion) VALUES ('Luisa', 'Martínez', 'luisa@example.com', '2023-06-21', 'Consulta', '¿Qué métodos de pago aceptan?', False, 'NOW()');",
#                     "INSERT INTO servisarg_consultareclamosugerencia (nombre, apellido, email, fecha_consulta, tipo, mensaje,leido , fecha_creacion) VALUES ('Pedro', 'Gómez', 'pedro@example.com', '2023-06-21', 'Reclamo', 'No estoy satisfecho con la calidad del producto.', False, 'NOW()');",
#                     "INSERT INTO servisarg_consultareclamosugerencia (nombre, apellido, email, fecha_consulta, tipo, mensaje,leido , fecha_creacion) VALUES ('Laura', 'Fernández', 'laura@example.com', '2023-06-21', 'Sugerencia', 'Sería genial si tuvieran una opción de envío express.', False, 'NOW()');",
#                     "INSERT INTO servisarg_consultareclamosugerencia (nombre, apellido, email, fecha_consulta, tipo, mensaje,leido , fecha_creacion) VALUES ('Javier', 'Torres', 'javier@example.com', '2023-06-21', 'Consulta', '¿Cuál es el plazo de entrega?', False, 'NOW()');",
#                     "INSERT INTO servisarg_consultareclamosugerencia (nombre, apellido, email, fecha_consulta, tipo, mensaje,leido , fecha_creacion) VALUES ('Carolina', 'Hernández', 'carolina@example.com', '2023-06-21', 'Reclamo', 'El producto no coincide con la descripción.', False, 'NOW()');",
#                     "INSERT INTO servisarg_consultareclamosugerencia (nombre, apellido, email, fecha_consulta, tipo, mensaje,leido , fecha_creacion) VALUES ('Diego', 'Gutiérrez', 'diego@example.com', '2023-06-21', 'Sugerencia', 'Agregar más tallas disponibles.', False, 'NOW()');",
#                     "INSERT INTO servisarg_consultareclamosugerencia (nombre, apellido, email, fecha_consulta, tipo, mensaje,leido , fecha_creacion) VALUES ('Camila', 'Martínez', 'camila@example.com', '2023-06-21', 'Consulta', '¿Cuál es el proceso de devolución?', False, 'NOW()');",
#                     "INSERT INTO servisarg_consultareclamosugerencia (nombre, apellido, email, fecha_consulta, tipo, mensaje,leido , fecha_creacion) VALUES ('Santiago', 'Gómez', 'santiago@example.com', '2023-06-21', 'Reclamo', 'No recibí el número de seguimiento del envío.', False, 'NOW()');",
#                     "INSERT INTO servisarg_consultareclamosugerencia (nombre, apellido, email, fecha_consulta, tipo, mensaje,leido , fecha_creacion) VALUES ('Valentina', 'Fernández', 'valentina@example.com', '2023-06-21', 'Sugerencia', 'Incluir más fotografías del producto en el sitio web.', False, 'NOW()');",
#                     "INSERT INTO servisarg_consultareclamosugerencia (nombre, apellido, email, fecha_consulta, tipo, mensaje,leido , fecha_creacion) VALUES ('Jorge', 'Torres', 'jorge@example.com', '2023-06-21', 'Consulta', '¿Cuál es el tiempo estimado de entrega?', False, 'NOW()');",
#                     "INSERT INTO servisarg_consultareclamosugerencia (nombre, apellido, email, fecha_consulta, tipo, mensaje,leido , fecha_creacion) VALUES ('Lucía', 'Hernández', 'lucia@example.com', '2023-06-21', 'Reclamo', 'El producto llegó con defectos de fabricación.', False, 'NOW()');",
#                     "INSERT INTO servisarg_consultareclamosugerencia (nombre, apellido, email, fecha_consulta, tipo, mensaje, leido, fecha_creacion) VALUES ('Mateo', 'Gutiérrez', 'mateo@example.com', '2023-06-21', 'Sugerencia', 'Agregar más opciones de color para el producto.', False, 'NOW()');",
#                     "INSERT INTO servisarg_consultareclamosugerencia (nombre, apellido, email, fecha_consulta, tipo, mensaje,leido , fecha_creacion) VALUES ('María', 'Martínez', 'maria@example.com', '2023-06-21', 'Consulta', '¿Qué métodos de envío utilizan?', False, 'NOW()');",
#                     "INSERT INTO servisarg_consultareclamosugerencia (nombre, apellido, email, fecha_consulta, tipo, mensaje, leido, fecha_creacion) VALUES ('Juan', 'Gómez', 'juan@example.com', '2023-06-21', 'Reclamo', 'El producto no se ajusta a las medidas indicadas.', False, 'NOW()');",
#                     "INSERT INTO servisarg_consultareclamosugerencia (nombre, apellido, email, fecha_consulta, tipo, mensaje,leido , fecha_creacion) VALUES ('Laura', 'Fernández', 'laura@example.com', '2023-06-21', 'Sugerencia', 'Ofrecer más promociones y descuentos.', False, 'NOW()');",
#                     "INSERT INTO servisarg_consultareclamosugerencia (nombre, apellido, email, fecha_consulta, tipo, mensaje,leido , fecha_creacion) VALUES ('Pedro', 'Torres', 'pedro@example.com', '2023-06-21', 'Consulta', '¿Cómo puedo realizar un seguimiento de mi pedido?', False, 'NOW()');",
#                     "INSERT INTO servisarg_consultareclamosugerencia (nombre, apellido, email, fecha_consulta, tipo, mensaje, leido, fecha_creacion) VALUES ('Carolina', 'Hernández', 'carolina@example.com', '2023-06-21', 'Reclamo', 'El producto que recibí es diferente al que ordené.', False, 'NOW()');",
#                     "INSERT INTO servisarg_consultareclamosugerencia (nombre, apellido, email, fecha_consulta, tipo, mensaje, leido, fecha_creacion) VALUES ('Diego', 'Gutiérrez', 'diego@example.com', '2023-06-21', 'Sugerencia', 'Ofrecer más opciones de pago, como PayPal.', False, 'NOW()');",
#                 ]

#                 with connection.cursor() as cursor:
#                     for sql_statement in sql_statements:
#                         cursor.execute(sql_statement)
#                         print("Insertanto: ",sql_statement)

def insert_data():
    with connection.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM servisarg_oficio;")
        count = cursor.fetchone()[0]
        print(count)
        if count == 0:
            sql_statements = [
                "INSERT INTO servisarg_oficio (nombre) VALUES ('Cosinero')",
                "INSERT INTO servisarg_oficio (nombre) VALUES ('Electricista')",
                "INSERT INTO servisarg_oficio (nombre) VALUES ('Plomero')",
                "INSERT INTO servisarg_oficio (nombre) VALUES ('Pintor')",
                "INSERT INTO servisarg_oficio (nombre) VALUES ('Jardinero')",
                "INSERT INTO servisarg_oficio (nombre) VALUES ('Limpieza de hogar')",
                "INSERT INTO servisarg_oficio (nombre) VALUES ('Instalador de aire acondicionado')",
                "INSERT INTO servisarg_oficio (nombre) VALUES ('Reparación de electrodomésticos')",
                "INSERT INTO servisarg_oficio (nombre) VALUES ('Fontanero')",
                "INSERT INTO servisarg_oficio (nombre) VALUES ('Mudanzas')",
                "INSERT INTO servisarg_oficio (nombre) VALUES ('Gasista')",
                "INSERT INTO servisarg_oficio (nombre) VALUES ('Cuidador de mascotas')",
                "INSERT INTO servisarg_oficio (nombre) VALUES ('Decorador de interiores')",
                "INSERT INTO servisarg_oficio (nombre) VALUES ('Reparación de computadoras')",
                "INSERT INTO servisarg_oficio (nombre) VALUES ('Organizador profesional')",
                "INSERT INTO servisarg_oficio (nombre) VALUES ('Diseñador gráfico')"
            ]

            for sql_statement in sql_statements:
                cursor.execute(sql_statement)
                print("Insertando:", sql_statement)

            print("Datos insertados correctamente.")

    with connection.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM servisarg_consultareclamosugerencia;")
        count = cursor.fetchone()[0]
        if count == 0:
            print("Insertando datos en la base de datos")
            sql_statements = [
                "INSERT INTO servisarg_consultareclamosugerencia (nombre, apellido, email, fecha_consulta, tipo, mensaje, leido, fecha_creacion) VALUES ('Juan', 'Pérez', 'juan@example.com', '2023-06-21', 'Consulta', '¿Cuál es el método de pago para un servicio?', False, NOW())",
                "INSERT INTO servisarg_consultareclamosugerencia (nombre, apellido, email, fecha_consulta, tipo, mensaje, leido, fecha_creacion) VALUES ('María', 'Gómez', 'maria@example.com', '2023-06-21', 'Reclamo', 'Necesito ayuda con la devolución de un producto.', False, NOW())",
                "INSERT INTO servisarg_consultareclamosugerencia (nombre, apellido, email, fecha_consulta, tipo, mensaje, leido, fecha_creacion) VALUES ('Pedro', 'López', 'pedro@example.com', '2023-06-21', 'Sugerencia', 'Me gustaría que agreguen más opciones de pago.', False, NOW())",
                "INSERT INTO servisarg_consultareclamosugerencia (nombre, apellido, email, fecha_consulta, tipo, mensaje, leido, fecha_creacion) VALUES ('Ana', 'Rodríguez', 'ana@example.com', '2023-06-21', 'Consulta', '¿Cuál es el horario de atención al cliente?', False, NOW())",
                "INSERT INTO servisarg_consultareclamosugerencia (nombre, apellido, email, fecha_consulta, tipo, mensaje, leido, fecha_creacion) VALUES ('Carlos', 'González', 'carlos@example.com', '2023-06-21', 'Reclamo', 'No recibí el producto que compré.', False, NOW())",
                "INSERT INTO servisarg_consultareclamosugerencia (nombre, apellido, email, fecha_consulta, tipo, mensaje, leido, fecha_creacion) VALUES ('Laura', 'López', 'laura@example.com', '2023-06-21', 'Sugerencia', 'Sería genial si añadieran más colores disponibles.', False, NOW())",
                "INSERT INTO servisarg_consultareclamosugerencia (nombre, apellido, email, fecha_consulta, tipo, mensaje, leido, fecha_creacion) VALUES ('Roberto', 'Torres', 'roberto@example.com', '2023-06-21', 'Consulta', '¿Cuál es la política de devoluciones?', False, NOW())",
                "INSERT INTO servisarg_consultareclamosugerencia (nombre, apellido, email, fecha_consulta, tipo, mensaje, leido, fecha_creacion) VALUES ('Marcela', 'Hernández', 'marcela@example.com', '2023-06-21', 'Reclamo', 'El producto llegó dañado.', False, NOW())",
                "INSERT INTO servisarg_consultareclamosugerencia (nombre, apellido, email, fecha_consulta, tipo, mensaje, leido, fecha_creacion) VALUES ('Fernando', 'Gutiérrez', 'fernando@example.com', '2023-06-21', 'Sugerencia', 'Podrían mejorar la velocidad de envío.', False, NOW())",
                "INSERT INTO servisarg_consultareclamosugerencia (nombre, apellido, email, fecha_consulta, tipo, mensaje, leido, fecha_creacion) VALUES ('Luisa', 'Martínez', 'luisa@example.com', '2023-06-21', 'Consulta', '¿Qué métodos de pago aceptan?', False, NOW())",
                "INSERT INTO servisarg_consultareclamosugerencia (nombre, apellido, email, fecha_consulta, tipo, mensaje, leido, fecha_creacion) VALUES ('Pedro', 'Gómez', 'pedro@example.com', '2023-06-21', 'Reclamo', 'No estoy satisfecho con la calidad del producto.', False, NOW())",
                "INSERT INTO servisarg_consultareclamosugerencia (nombre, apellido, email, fecha_consulta, tipo, mensaje, leido, fecha_creacion) VALUES ('Laura', 'Fernández', 'laura@example.com', '2023-06-21', 'Sugerencia', 'Sería genial si tuvieran una opción de envío express.', False, NOW())",
                "INSERT INTO servisarg_consultareclamosugerencia (nombre, apellido, email, fecha_consulta, tipo, mensaje, leido, fecha_creacion) VALUES ('Javier', 'Torres', 'javier@example.com', '2023-06-21', 'Consulta', '¿Cuál es el plazo de entrega?', False, NOW())",
                "INSERT INTO servisarg_consultareclamosugerencia (nombre, apellido, email, fecha_consulta, tipo, mensaje, leido, fecha_creacion) VALUES ('Carolina', 'Hernández', 'carolina@example.com', '2023-06-21', 'Reclamo', 'El producto no coincide con la descripción.', False, NOW())",
                "INSERT INTO servisarg_consultareclamosugerencia (nombre, apellido, email, fecha_consulta, tipo, mensaje, leido, fecha_creacion) VALUES ('Diego', 'Gutiérrez', 'diego@example.com', '2023-06-21', 'Sugerencia', 'Agregar más tallas disponibles.', False, NOW())",
                "INSERT INTO servisarg_consultareclamosugerencia (nombre, apellido, email, fecha_consulta, tipo, mensaje, leido, fecha_creacion) VALUES ('Camila', 'Martínez', 'camila@example.com', '2023-06-21', 'Consulta', '¿Cuál es el proceso de devolución?', False, NOW())",
                "INSERT INTO servisarg_consultareclamosugerencia (nombre, apellido, email, fecha_consulta, tipo, mensaje, leido, fecha_creacion) VALUES ('Santiago', 'Gómez', 'santiago@example.com', '2023-06-21', 'Reclamo', 'No recibí el número de seguimiento del envío.', False, NOW())",
                "INSERT INTO servisarg_consultareclamosugerencia (nombre, apellido, email, fecha_consulta, tipo, mensaje, leido, fecha_creacion) VALUES ('Valentina', 'Fernández', 'valentina@example.com', '2023-06-21', 'Sugerencia', 'Incluir más fotografías del producto en el sitio web.', False, NOW())",
                "INSERT INTO servisarg_consultareclamosugerencia (nombre, apellido, email, fecha_consulta, tipo, mensaje, leido, fecha_creacion) VALUES ('Jorge', 'Torres', 'jorge@example.com', '2023-06-21', 'Consulta', '¿Cuál es el tiempo estimado de entrega?', False, NOW())",
                "INSERT INTO servisarg_consultareclamosugerencia (nombre, apellido, email, fecha_consulta, tipo, mensaje, leido, fecha_creacion) VALUES ('Lucía', 'Hernández', 'lucia@example.com', '2023-06-21', 'Reclamo', 'El producto llegó con defectos de fabricación.', False, NOW())",
                "INSERT INTO servisarg_consultareclamosugerencia (nombre, apellido, email, fecha_consulta, tipo, mensaje, leido, fecha_creacion) VALUES ('Mateo', 'Gutiérrez', 'mateo@example.com', '2023-06-21', 'Sugerencia', 'Agregar más opciones de color para el producto.', False, NOW())",
                "INSERT INTO servisarg_consultareclamosugerencia (nombre, apellido, email, fecha_consulta, tipo, mensaje, leido, fecha_creacion) VALUES ('María', 'Martínez', 'maria@example.com', '2023-06-21', 'Consulta', '¿Qué métodos de envío utilizan?', False, NOW())",
                "INSERT INTO servisarg_consultareclamosugerencia (nombre, apellido, email, fecha_consulta, tipo, mensaje, leido, fecha_creacion) VALUES ('Juan', 'Gómez', 'juan@example.com', '2023-06-21', 'Reclamo', 'El producto no se ajusta a las medidas indicadas.', False, NOW())",
                "INSERT INTO servisarg_consultareclamosugerencia (nombre, apellido, email, fecha_consulta, tipo, mensaje, leido, fecha_creacion) VALUES ('Laura', 'Fernández', 'laura@example.com', '2023-06-21', 'Sugerencia', 'Ofrecer más promociones y descuentos.', False, NOW())",
                "INSERT INTO servisarg_consultareclamosugerencia (nombre, apellido, email, fecha_consulta, tipo, mensaje, leido, fecha_creacion) VALUES ('Pedro', 'Torres', 'pedro@example.com', '2023-06-21', 'Consulta', '¿Cómo puedo realizar un seguimiento de mi pedido?', False, NOW())",
                "INSERT INTO servisarg_consultareclamosugerencia (nombre, apellido, email, fecha_consulta, tipo, mensaje, leido, fecha_creacion) VALUES ('Carolina', 'Hernández', 'carolina@example.com', '2023-06-21', 'Reclamo', 'El producto que recibí es diferente al que ordené.', False, NOW())",
                "INSERT INTO servisarg_consultareclamosugerencia (nombre, apellido, email, fecha_consulta, tipo, mensaje, leido, fecha_creacion) VALUES ('Diego', 'Gutiérrez', 'diego@example.com', '2023-06-21', 'Sugerencia', 'Ofrecer más opciones de pago, como PayPal.', False, NOW())"
            ]
            for sql_statement in sql_statements:
                cursor.execute(sql_statement)
                print("Insertando:", sql_statement)

            print("Datos insertados correctamente.")