# Reto Final Integrador: Telemedicina 2.0 (MediSalud Ecuador)

El Reto Final Integrador evalúa la capacidad de transferir todo el conocimiento conceptual y técnico adquirido a un nuevo módulo crítico en expansión: **Telemedicina 2.0**, bajo el marco normativo de **ISO/IEC 25022**.

---

## 1. Ficha Usuario-Tarea-Contexto (Telemedicina 2.0)

Se elaboró la ficha técnica que define los parámetros de interacción del nuevo módulo:

| Parámetro | Definición del Entorno de Telemedicina 2.0 |
|:---|:---|
| **Proceso de Negocio** | Teleconsulta médica e indicaciones virtuales. |
| **Usuario Primario** | Paciente (38,000+ usuarios) y Médico Tratante (640 médicos). |
| **Tarea Representativa** | Completar una videollamada de teleconsulta de inicio a fin (mínimo 15 minutos), incluyendo la recepción de indicaciones remotas y receta digital. |
| **Contexto de Uso** | Paciente conectado mediante red celular comercial (3G/4G) desde dispositivos móviles (App Flutter en Android/iOS) o red doméstica WiFi, y el médico desde el portal web en su consultorio o domicilio. |
| **Atributos de Calidad** | **Efectividad:** tasa de finalización sin cortes.<br>**Eficiencia:** duración de consulta.<br>**Satisfacción:** CSAT del paciente.<br>**Libertad de Riesgo:** privacidad de datos del paciente.<br>**Cobertura de Contexto:** consistencia de la llamada entre tipos de red (WiFi vs 3G/4G). |

---

## 2. Catálogo de Métricas de Telemedicina 2.0

Se definieron e implementaron las siguientes 5 métricas en el módulo `scripts/metricas_telemedicina.py`:

1. **Tasa de Éxito de Teleconsulta (Efectividad):**
   * *Fórmula:* $X = \frac{\text{Teleconsultas finalizadas correctamente}}{\text{Teleconsultas intentadas}}$
   * *Rango deseado:* $X \ge 0.95$ (95% de éxito).
2. **Duración Promedio de Teleconsulta (Eficiencia):**
   * *Fórmula:* $X = \text{Promedio de duración en minutos de las consultas completadas}$
   * *Rango deseado:* $X \le 30.0\text{ min}$ (para optimizar la agenda médica).
3. **CSAT Normalizado del Paciente (Satisfacción):**
   * *Fórmula:* $X = \frac{\text{Calificación CSAT promedio (1-5)}}{5}$
   * *Rango deseado:* $X \ge 0.80$ (Equivalente a $\ge 4.0/5.0$).
4. **Tasa de Incidentes de Privacidad (Libertad de Riesgo):**
   * *Fórmula:* $X = \frac{\text{Sesiones con exposición incidental de datos de otros pacientes}}{\text{Total de sesiones intentadas}}$
   * *Rango deseado:* $X \le 0.005$ (Menos del 0.5% de riesgo de privacidad).
5. **Consistencia de Éxito por Conexión (Cobertura de Contexto):**
   * *Fórmula:* $X = \frac{\text{Tasa de éxito de videollamada en la peor conexión (3G)}}{\text{Tasa de éxito de videollamada en la mejor conexión (Fibra/WiFi)}}$
   * *Rango deseado:* $X \ge 0.85$ (Variación de calidad por red menor al 15%).

---

## 3. Resultados y Evidencia Empírica de Telemedicina 2.0

Se ejecutó el pipeline de telemedicina (`generar_datos_telemedicina.py` y `metricas_telemedicina.py`) sobre un total de **1,240 sesiones simuladas** de 10 días de consulta, obteniendo los siguientes resultados reales:

| Métrica ISO/IEC 25022 | Valor Calculado | Umbral de Calidad | Estado | Hallazgo |
|:---|:---:|:---:|:---:|:---|
| **Tasa de éxito de teleconsulta** (Efectividad) | **88.31%** | $\ge 95\%$ | 🔴 **NO CUMPLE** | 145 videollamadas se cortaron o cancelaron antes del cierre. |
| **Duración promedio** (Eficiencia) | **22.1 min** | $\le 30\text{ min}$ | ✅ **CUMPLE** | Duración alineada con los protocolos médicos y de agenda. |
| **CSAT normalizado** (Satisfacción) | **75.27%** | $\ge 80\%$ | 🔴 **NO CUMPLE** | Calificación CSAT de 3.76/5.0, afectada por frustración de caídas. |
| **Tasa de incidentes de privacidad** (Riesgo) | **0.65%** | $\le 0.5\%$ | 🔴 **NO CUMPLE** | 8 sesiones expusieron brevemente datos de otros pacientes. |
| **Consistencia por tipo de red** (Cobertura) | **79.54%** | $\ge 85\%$ | 🔴 **NO CUMPLE** | Rendimiento muy bajo en 3G (tasa de éxito del 78% vs 98% en WiFi). |

---

## 4. Diagnóstico Técnico y Plan de Acción (Telemedicina)

### A. Diagnóstico de Causa Raíz
* **Caídas de llamadas en redes móviles (3G/4G):** El protocolo de streaming de video del módulo móvil intenta transmitir a resolución 1080p sin compresión dinámica de bitrate. En redes 3G o 4G congestionadas, la latencia de paquetes supera los 800ms, provocando la terminación abrupta del socket de conexión por timeout.
* **Incidentes de Privacidad:** Al fallar y reintentar la reconexión de la videollamada, el microservicio reutiliza el token de autenticación del paciente de forma inconsistente, asociando ocasionalmente la interfaz de video al ID del paciente de la sesión previa en la cola del servidor.

### B. Plan de Acción de 60 Días
1. **Compresión dinámica y WebRTC:** Implementar ajuste dinámico de bitrate en la App móvil (Flutter) para bajar automáticamente la resolución a 360p en conexiones 3G/4G lentas, manteniendo el audio fluido y evitando timeouts (Meta: elevar tasa de éxito al 95%).
2. **Ciclo de vida único para tokens:** Invalidar de forma atómica y del lado del servidor el ID de sesión anterior ante cualquier reconexión fallida, forzando una nueva autenticación mediante OAuth2 y eliminando los fallos de privacidad.
3. **Monitoreo de red móvil:** Habilitar métricas de red local en los logs de la App para cruzar velocidad de carga de paquetes con satisfacción CSAT, permitiendo diagnosticar cuellos de banda específicos de operadoras locales en Ecuador.
