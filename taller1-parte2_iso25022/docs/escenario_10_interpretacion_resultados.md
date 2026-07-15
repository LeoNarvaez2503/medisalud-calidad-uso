# Escenario 10: Interpretación de Resultados y Causa Raíz

Este documento presenta el análisis crítico de los resultados obtenidos en el programa de medición de Calidad en Uso de **MediSalud HIS**, aplicando la técnica de **Análisis de Causa Raíz (5 Por Qué)** para diagnosticar y justificar los incumplimientos detectados.

---

## 1. Análisis Crítico de Métricas Incumplidas

De las 6 métricas evaluadas, tres no alcanzaron el rango de calidad deseado por la organización:

### A. Cumplimiento de Latencia HCE (RNF-01) — *Calculado: 67.87% (Umbral: $\ge$ 90%)*
* **Interpretación:** Aunque el tiempo promedio global es de 7.43 segundos (aparentemente cumpliendo con la meta de 8s), el **32.13% de los registros de evolución clínica superan los 8 segundos**, acumulándose especialmente en el intervalo de 10 a 17 segundos. Esto significa que 1 de cada 3 pacientes experimenta tiempos de consulta excesivamente largos debido a que su médico espera a que la pantalla del HIS responda.

#### Análisis de Causa Raíz (5 Por Qué):
1. **¿Por qué los médicos perciben que la HCE es lenta y el 32.13% supera los 8 segundos?** Porque el guardado de la nota de evolución tarda en responder en el frontend.
2. **¿Por qué tarda tanto en guardarse la nota clínica?** Porque las llamadas al microservicio de backend HCE `/api/historias/guardar` experimentan latencias superiores a 5 segundos bajo concurrencia.
3. **¿Por qué el microservicio de HCE experimenta altas latencias bajo concurrencia?** Porque se bloquea temporalmente al intentar persistir los datos y registrar recetas en la base de datos PostgreSQL.
4. **¿Por qué se bloquea la base de datos PostgreSQL?** Porque el microservicio realiza consultas de verificación de inventario de farmacia e interacciones medicamentosas de manera síncrona y bloqueante dentro de la transacción de guardado de la HCE.
5. **¿Por qué se hacen de manera síncrona?** Debido a un diseño acoplado heredado en la arquitectura de microservicios, donde no se implementó un bus de eventos asíncronos para la comunicación entre el microservicio de HCE y el de Farmacia.

---

### B. Índice de Satisfacción (CSAT Normalizado) — *Calculado: 72.27% (Umbral: $\ge$ 80%)*
* **Interpretación:** El CSAT promedio de 3.61 sobre 5 (0.7227 normalizado) demuestra insatisfacción latente. Al desglosar por perfiles, los médicos y pacientes (los usuarios con interacción directa con la HCE y el Portal) arrojan los puntajes más bajos, mientras que los administradores muestran niveles intermedios.

#### Análisis de Causa Raíz (5 Por Qué):
1. **¿Por qué los médicos y pacientes se sienten insatisfechos con el sistema?** Porque experimentan frustración e interrupciones constantes durante sus tareas diarias.
2. **¿Por qué experimentan interrupciones?** Porque el portal de citas a menudo expira la sesión de los pacientes y los médicos deben reintentar el guardado de notas clínicas varias veces.
3. **¿Por qué expiran las sesiones en el portal y falla el guardado?** Porque el sistema presenta micro-caídas y bloqueos transaccionales en horas pico.
4. **¿Por qué el sistema colapsa en horas de alta demanda?** Porque los recursos del clúster de servidores on-premise no tienen auto-escalamiento dinámico y la base de datos central carece de un pool de conexiones optimizado.
5. **¿Por qué no hay auto-escalamiento ni optimización de base de datos?** Porque la infraestructura está desplegada en servidores físicos estáticos y no se han implementado prácticas modernas de DevOps ni de observabilidad continua para dimensionar dinámicamente la capacidad.

---

### C. Tasa de Errores de Facturación (RNF-03) — *Calculado: 3.01% (Umbral: $\le$ 1%)*
* **Interpretación:** La tasa de 3.01% representa 256 facturas con cobros duplicados o deducibles de seguro mal aplicados en un volumen mensual simulado de 8,500 transacciones. Esto supera el triple del límite del 1% tolerado en el RNF-03, exponiendo a la red a multas del regulador de salud, reclamos de aseguradoras y pérdida reputacional.

#### Análisis de Causa Raíz (5 Por Qué):
1. **¿Por qué los pacientes y el área financiera registran cobros duplicados e inconsistencias?** Porque la pasarela de pagos realiza débitos automáticos sin confirmar adecuadamente el estado transaccional de la factura.
2. **¿Por qué la pasarela procesa el cobro sin confirmar la factura?** Porque el módulo de facturación del HIS experimenta caídas durante los cierres de caja y los cajeros presionan repetidamente el botón de cobro ("Double Submit").
3. **¿Por qué el módulo de facturación colapsa durante los cierres de caja?** Porque el microservicio de facturación realiza sincronizaciones síncronas bloqueantes con la base de datos SQL Server heredada (módulo financiero antiguo).
4. **¿Por qué la base de datos SQL Server antigua se bloquea?** Porque está saturada con reportes pesados de auditoría de finanzas ejecutándose simultáneamente con las transacciones de caja de la tarde.
5. **¿Por qué se ejecutan juntas en el mismo servidor de base de datos?** Porque no se ha implementado un patrón de replicación de lectura para reportes (Read Replica), forzando a las transacciones de caja y los reportes analíticos a compartir el mismo hilo de ejecución de la base de datos de producción.

---

## 2. Acciones Correctivas de Impacto Inmediato

Con base en el análisis de causa raíz, se recomiendan tres acciones correctivas prioritarias en el roadmap técnico de 90 días:

1. **Migración a bus de eventos asíncronos:** Desacoplar la HCE del inventario de farmacia implementando RabbitMQ para que el guardado de notas clínicas sea no-bloqueante (reduciendo la latencia de guardado de 10s a menos de 2s).
2. **Implementación de Réplica de Lectura en SQL Server:** Configurar una base de datos secundaria para reportes analíticos del área contable, liberando de carga transaccional al servidor principal de facturación de ventanillas.
3. **Prevención de Double Submit en Interfaz:** Implementar validación en el frontend (React/Flutter) que deshabilite el botón de pago inmediatamente después del primer click, reduciendo a cero los cobros duplicados incidentales.
