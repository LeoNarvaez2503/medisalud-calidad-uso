# Escenario 3: Comprensión del Modelo SQuaRE

Este documento detalla el análisis teórico y la aplicación práctica del marco normativo de la familia **ISO/IEC 25000 (SQuaRE)**, enfocándose en la diferenciación de los niveles de calidad y la organización jerárquica de la norma.

---

## 1. Niveles de Calidad: Interna, Externa y en Uso

Bajo la familia de normas ISO/IEC 25000, la calidad del software no se mide en un único plano, sino que se divide en tres niveles complementarios que reflejan distintas etapas del ciclo de vida del producto:

```
[ Calidad Interna ]  =======>  [ Calidad Externa ]  =======>  [ Calidad en Uso ]
(Estática: Código)             (Dinámica: Pruebas)            (Operación: Producción)
```

### A. Calidad Interna (Vista Estática)
*   **Definición:** Evalúa las propiedades del software que no dependen de su ejecución. Se enfoca en el código fuente, la arquitectura, los esquemas de bases de datos y la documentación técnica.
*   **Cómo se mide:** Se evalúa de manera automatizada mediante herramientas de análisis estático (ej. SonarQube, linters, escáneres de seguridad). Mide indicadores como complejidad ciclomática, duplicación de código, adherencia a estándares de codificación (limpieza) y porcentaje de cobertura de pruebas unitarias.
*   **Enfoque:** Desarrolladores y arquitectos de software.

### B. Calidad Externa (Vista Dinámica en Pruebas)
*   **Definición:** Evalúa el comportamiento del software cuando se ejecuta, pero dentro de un entorno de pruebas controlado y simulado (QA / Staging).
*   **Cómo se mide:** Se realiza ejecutando el sistema para validar que cumpla los requisitos funcionales y no funcionales. Mide métricas como tiempos de respuesta bajo carga simulada, comportamiento de la API frente a fallos inyectados, tasas de éxito en pruebas automatizadas de interfaz (ej. Selenium, Cypress) y escaneos de vulnerabilidades activas en ejecución.
*   **Enfoque:** Ingenieros de pruebas (QA), testers y analistas de sistemas.

### C. Calidad en Uso (Vista Operativa Real)
*   **Definición:** Mide el grado en que el software ayuda a usuarios reales a alcanzar sus metas reales en el entorno de producción real, bajo las condiciones cotidianas del negocio.
*   **Cómo se mide:** Se evalúa recolectando datos directamente de la operación diaria (producción). Utiliza registros de incidentes (como quejas de lentitud o errores de cobro), encuestas de satisfacción del cliente (SUS), tasa de abandono de tareas en producción, número de errores cometidos por los usuarios en vivo y pérdidas financieras asociadas a fallos.
*   **Enfoque:** Clientes finales, usuarios de negocio, directores de operaciones y auditores de calidad.

---

## 2. Tabla 3.2: Ejemplos de Calidad en el Módulo de Receta Médica (MediSalud HIS)

Para comprender cómo interactúan estos tres niveles en el sistema **MediSalud HIS**, se presenta un ejemplo práctico centrado en la funcionalidad de **Registro de Receta Electrónica**:

| Nivel de Calidad | Ejemplo de Medición Específico en MediSalud HIS | Herramienta / Método de Medición |
| :--- | :--- | :--- |
| **Calidad Interna** | Validar que el código del método `guardarRecetaElectronica()` en el backend de HCE tenga una complejidad ciclomática menor a 10 y que cuente con al menos un 80% de cobertura de pruebas unitarias para asegurar su mantenibilidad. | Análisis estático de código con **SonarQube** e informes de cobertura de **Pytest**. |
| **Calidad Externa** | Ejecutar una prueba de carga simulada con 150 usuarios concurrentes (médicos ficticios) en el ambiente de Staging para verificar que el endpoint `/api/recetas/guardar` responda en menos de 2 segundos sin generar fallos 500. | Simulación de carga usando **JMeter** o **Locust** en un entorno de pruebas controlado. |
| **Calidad en Uso** | Contabilizar cuántas veces en el mes los médicos reales en producción reportaron que la receta electrónica se guardó con una dosis incorrecta (lo cual infringe el RNF de seguridad clínica y expone al paciente a riesgos de salud). | Monitoreo del archivo de quejas e incidentes en producción (`incidentes_2025.csv`). |

---

## 3. Mapa Conceptual de la Familia SQuaRE (ISO/IEC 25000)

El siguiente mapa conceptual organiza jerárquicamente las normas clave que componen el estándar SQuaRE, detallando la función específica de cada una dentro del proceso de control de calidad:

```mermaid
flowchart TD
    subgraph SQuaRE ["Familia ISO/IEC 25000: SQuaRE (System and Software Quality Requirements and Evaluation)"]
        direction TB
        
        G25000["ISO/IEC 25000: Guía General y Planificación<br><i>(Define la terminología común, objetivos del marco y directrices para planificación)</i>"]
        
        subgraph Divisiones ["Módulos de Trabajo Clave"]
            direction LR
            
            M25010["ISO/IEC 25010: Modelos de Calidad<br><b>¿Qué medir?</b><br><i>(Define las características que componen la Calidad del Producto y la Calidad en Uso)</i>"]
            
            M25020["ISO/IEC 2502X: División de Medición<br><b>¿Cómo medir?</b><br><i>(Fórmulas matemáticas y métricas. Ej: <b>ISO/IEC 25022</b> para Calidad en Uso)</i>"]
            
            M25040["ISO/IEC 25040: División de Evaluación<br><b>¿Cómo evaluar?</b><br><i>(Metodología, fases y requisitos para ejecutar un proceso de evaluación formal)</i>"]
        end
        
        G25000 --> M25010
        G25000 --> M25020
        G25000 --> M25040
        
        M25010 -.-> |"Define las características<br>analizadas por"| M25020
        M25020 -.-> |"Proporciona las métricas<br>matemáticas usadas en"| M25040
    end
    
    style SQuaRE fill:#fdfdfd,stroke:#333,stroke-width:2px;
    style G25000 fill:#e1f5fe,stroke:#0288d1,stroke-width:2px;
    style M25010 fill:#fff3e0,stroke:#f57c00,stroke-width:2px;
    style M25020 fill:#e8f5e9,stroke:#388e3c,stroke-width:2px;
    style M25040 fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px;
```

### Relación y Roles de las Normas:
1.  **ISO/IEC 25000 (Guía General):** Es el mapa de ruta. Establece el marco común y define el vocabulario para que todos los involucrados (desarrolladores, evaluadores, clientes) hablen el mismo lenguaje de calidad.
2.  **ISO/IEC 25010 (Modelos de Calidad / ¿Qué medir?):** Estructura conceptualmente la calidad. Para la *Calidad del Producto*, define 8 características (como mantenibilidad, seguridad o compatibilidad). Para la *Calidad en Uso*, define las 5 características analizadas en este taller (Efectividad, Eficiencia, Satisfacción, Libertad de Riesgo y Cobertura de Contexto).
3.  **ISO/IEC 25022 (Medición de Calidad en Uso / ¿Cómo medir?):** Traduce el modelo teórico de la 25010 en números. Proporciona las métricas y fórmulas específicas (por ejemplo, la fórmula para la tasa de error en transacciones o el tiempo promedio de tarea) para evaluar empíricamente la calidad en uso en producción.
4.  **ISO/IEC 25040 (Proceso de Evaluación):** Establece el "paso a paso" metodológico para llevar a cabo la evaluación de calidad de principio a fin, definiendo responsabilidades y entregables en las fases de requisitos, diseño, ejecución y reporte.
