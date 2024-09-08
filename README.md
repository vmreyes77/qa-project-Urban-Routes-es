# Proyecto Urban Routes 

### Víctor Manuel Reyes Vargas, Cohort 9, Sprint 8

Es este proyecto hemos evaluado todos los pasos para pedir un taxi con la tarifa "Comfort".

Específicamente hemos probado lo siguiente:

* El llenado de las direcciones
* El botón para pedir un taxi funcione como esperado
* La selección y detalles de la tarifa Comfort
* La agregación de todos los campos obligatorios (Teléfono, Método de pago)
* Las funciones para agregar un comentario para el conductor
* Agregar amenidades para el viaje (Mantas, pañuelos, Helados)
* Y que el pedido termine el proceso correctamente una vez hecha la reserva

Para realizar las pruebas primero hay que ingresar a la página de Urban Routes adquiriendo una URL del servidor, luego
se llenan los campos "Desde" y "Hasta" con direcciones válidas (Ej. "East 2nd Street, 601" y "1300 1st St"). Y hacemos
click en el botón "Pedir un taxi".

Seleccionamos la tarifa "Comfort" y procedemos a llenar los campos necesarios para hacer el pedido:

1. Al hacer click en el campo "Número de teléfono", procedemos a ingresar un número telefónico (Ej. +1 123 123 12 12) 
en el campo designado y hacemos click en el botón siguiente. En la ventana emergente se nos pide ingresar un código SMS,
para esto tenemos la función ***retrieve_phone_code()***, que al ejecutarla nos ofrese este código.


2. Luego tenemos que seleccionar un método de pago. Al hacer click en este se nos ofrece la opción de ingresar una
tarjeta de crédito. Hacemos click en "agregar tarjeta" y necesitaremos ingresar el número (Ej. "1234 5678 9100") y el
código de seguridad de la misma (Ej. "111").
Luego tenemos que deselcionar el campo del código de la tarjeta para presionar "Agregar".


3. En el campo opcional "mensaje para el conductor..." podemo dejar un mensaje para que el conductor designado lo tenga
en cuenta. En esta prueba le hemos dejado uno.


4. Dentro de los "Requisitos del pedido" hemos agregado un "Manta y pañuelo", y hemos agregado 2 unidades de "helado".


5. Por último hacemos click en el botón de reserva donde se nos lleva automáticamente a la ventana de "resumen del pedido",
donde podemos ver todos los detalles del pedido.

En esta ventana se nos muestra un tiempo de espera de 25 segundos, el cual al terminar nos muestra nuestro conductor designado
para el viaje.

Luego de esto el proceso se da por terminado.

Las pruebas fueron realizadas utilizando PyCharm de manera local, una vez hecho el trabajo se cargó el código en GitHub
y el respositorio fue enviado a revisión.

Las pruebas fueron realizadas en **Windows 11** con el navegador **Google Chrome** y una resolución de **1920x1080**.
