# DSBM_P8-SemaforoESP32
Este repositorio es para la continuación de la práctica 7 de Diseño de Sistemas Basados en Microprocesador de la ESI (UCLM). Se desea añadir al proyecto del semáforo la funcionalidad de ordenes via wifi con un microcontrolador ESP32 y el uso de UARTs.

## Versiones
### Versión 0.5
 - Esqueleto del código generado con STM32CUBEMX.
 - main copiado de la práctica anterior.

### Versión 0.8
 - Esqueleto del código completo.

### Versión 1.0
 - Primera parte completa.
 - La placa STM recibe bien.
 - Falta gestionar el funcionamiento del semáforo con las ordenes del esp32.

### Versión 2.0
 - El programa funciona con botón y con ordenes por separado.
 - Falta integrar ambas funcionalidades en una sola.

### Versión 2.5
 - Funcionalidad del ESP32 completada.
   - Si el programa está realizando la secuencia del botón no atenderá las ordenes del ESP32.
   - Si el programa está atendiendo ordenes del ESP32, no aceptará la interrupción del botón.

### Versión 3.0
 - Documentación añadida.