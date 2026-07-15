# Escenario 5: Mapeo de Características de Calidad y Priorización

Para optimizar los recursos del programa de Aseguramiento de la Calidad del Software de **MediSalud Ecuador**, se construyó la matriz de mapeo y priorización. El objetivo es identificar qué tareas críticas serán sometidas a medición bajo la norma ISO/IEC 25022.

---

## Criterios de Priorización
La priorización se realiza cruzando dos dimensiones esenciales:
* **Impacto en el Negocio (Clínico y Financiero):**
  * **Alto:** Fallos ponen en riesgo la vida de pacientes, la privacidad de datos de salud o generan pérdidas directas de ingresos.
  * **Medio:** Fallos causan ineficiencias operativas o retrasos en soporte administrativo.
  * **Bajo:** Fallos estéticos o molestias menores que no interrumpen los procesos de negocio.
* **Frecuencia de Uso:**
  * **Alta:** La tarea se ejecuta cientos de veces al día (por ejemplo, registros clínicos o agendamiento).
  * **Media:** La tarea se ejecuta de forma periódica en turnos específicos o cierres.
  * **Baja:** La tarea se ejecuta semanal o mensualmente.

---

## Matriz de Mapeo Tarea–Característica–Prioridad

| Tarea de Usuario | Impacto Negocio | Frecuencia de Uso | Características ISO/IEC 25022 Relacionadas | Prioridad | Medir en Fase 1 |
|:---|:---:|:---:|:---|:---:|:---:|
| **Registrar nota de evolución clínica** | Alto | Alta | Eficiencia, Efectividad, Satisfacción, Libertad de Riesgo (Clínico) | **1** | Sí |
| **Agendar cita en el portal del paciente** | Alto | Alta | Efectividad, Eficiencia, Satisfacción, Cobertura de Contexto (Web/Móvil) | **1** | Sí |
| **Facturar consulta con seguro médico** | Alto | Media | Libertad de Riesgo (Económico), Efectividad, Eficiencia | **2** | Sí |
| **Completar sesión de teleconsulta** | Alto | Media | Efectividad, Cobertura de Contexto (Redes), Satisfacción | **2** | Sí |
| **Dispensar medicamento en farmacia** | Alto | Media | Libertad de Riesgo (Salud), Efectividad | **2** | Sí |
| **Consultar historial de resultados de laboratorio** | Medio | Alta | Efectividad, Satisfacción | **3** | No |
| **Generar reporte gerencial mensual** | Medio | Baja | Eficiencia, Efectividad | **3** | No |
| **Actualizar datos personales desde la App** | Bajo | Media | Cobertura de Contexto, Satisfacción | **4** | No |

---

## Alcance del Programa de Medición

* **Prioridad 1 (Crítico inmediato):** Se medirá el **Registro de notas de evolución (HCE)** debido a la lentitud en horas pico y las quejas de médicos, y el **Portal de citas** por el alto abandono de reservas.
* **Prioridad 2 (Riesgo y Telemedicina):** Se medirá el módulo de **Facturación** para controlar el error del coaseguro (evitando doble cobro) y la **Teleconsulta** para supervisar la tasa de caídas de llamadas bajo cobertura 3G/4G.
* **Prioridad 3 y 4 (Mejora futura):** Postergadas para el segundo semestre para evitar sobrecargar a los equipos técnicos y mantener el foco en la estabilización de los RNF prioritarios.
