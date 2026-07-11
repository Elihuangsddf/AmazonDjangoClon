# ¡Hola! Bienvenido a mi Clon de Amazon

¡Hola a todos! Este es mi proyecto de Clon de Amazon, una tienda virtual funcional en la que he estado trabajando para poner a prueba y mejorar mis habilidades de desarrollo web usando **Python** y **Django**. 

La idea de este proyecto nació de querer replicar cómo funciona un gigante del e-commerce por detrás, desde navegar por el catálogo hasta agregar cosas al carrito. 

---

## ¿Qué puede hacer esta app?

Traté de meterle varias de las cosas esenciales que esperas ver en una tienda en línea real:
- **Catálogo por áreas:** Dividí la tienda en varias categorías (Electrónica, Hogar, Moda, Móviles, etc.) para que la navegación tenga sentido.
- **Carrito de compras:** Funciona de manera súper fluida. Puedes agregar productos, quitar los que ya no quieres, o sumar más unidades, y el total se actualiza.
- **Área de contacto:** Si hay dudas, los usuarios pueden enviar mensajes a servicio al cliente y quedan guardados.
- **Panel de control:** Como es Django, aproveché su panel de administración para poder gestionar el inventario, subir fotos nuevas de los productos y leer los mensajes de los clientes sin dolor de cabeza.

Ah, por cierto, **¡el código está súper limpio!** Hace poco le di una repasada para quitar todos los comentarios de sobra y dejar todas las variables y funciones en formato `camelCase` puro.

---

##  Con qué está construido (Stack)

Nada súper raro, usé el stack clásico pero confiable:
- **El corazón del sistema (Backend):** Python 3 con Django (versión 5+).
- **Base de datos:** Usualmente lo corro con PostgreSQL (usando `psycopg2`), aunque con SQLite3 también funciona perfecto si solo lo quieres probar rápido.
- **El diseño (Frontend):** HTML5, CSS3 y JavaScript puro. Nada de frameworks pesados.

---

## Cómo probarlo en tu compu

Si quieres descargar el proyecto y jugar un rato con él, es súper fácil. Aquí te dejo los pasos:

1. **Descarga el código**
   ```bash
   git clone https://github.com/Elihuangsddf/AmazonDjangoClon.git
   cd AmazonDjangoClon
   ```

2. **Crea un entorno virtual** (siempre recomendado para no hacer un desastre con tus paquetes locales)
   - Si estás en Windows:
     ```bash
     python -m venv env
     env\Scripts\activate
     ```
   - Si usas Mac/Linux:
     ```bash
     python3 -m venv env
     source env/bin/activate
     ```

3. **Instala lo necesario**
   ```bash
   pip install django psycopg2 pillow
   ```
   *(Ojo: Si no tienes configurado Postgres, tal vez quieras comentar esa parte en `settings.py` y dejar que Django use SQLite por defecto para evitar errores al instalar `psycopg2`).*

4. **Prepara la base de datos**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Correr servidor**
   ```bash
   python manage.py runserver
   ```
   Y listo, entra a `http://127.0.0.1:8000/` en tu navegador para ver la tienda. Para entrar al panel de administración, la ruta es `/admin/`.

---

## Contacto

Si tienes alguna pregunta, feedback o propuesta, ¡no dudes en escribirme!

- **Correo:** elihuangper@gmail.com
- **LinkedIn:** [Elihú Neftalí Ángeles Pérez](https://www.linkedin.com/in/elihú-neftalí-ángeles-pérez-866942377)
