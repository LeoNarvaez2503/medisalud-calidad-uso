# Plan de Mejora Continua: MediSalud HIS

## Ciclo PDCA

| Fase | Acciones | Responsable | Evidencia |
| :--- | :--- | :--- | :--- |
| Planificar | Definir umbrales por RNF, tareas prioritarias y fuentes de datos oficiales. | Gerencia de Calidad, TI, Direccion Medica | Catalogo de metricas y matriz de priorizacion. |
| Hacer | Ejecutar pipeline semanal, generar logs HCE, encuesta CSAT e indicadores JSON. | TI y Calidad | `dashboards/indicadores.json`, salidas de scripts. |
| Verificar | Comparar resultados contra umbrales: HCE <= 8s, facturacion <= 1%, CSAT >= 0.80. | Calidad, Auditoria, Direccion Medica | Informe ejecutivo mensual. |
| Actuar | Corregir cuellos de botella, ajustar procesos, mejorar UX y reforzar integraciones criticas. | TI, Producto, Operaciones | Backlog de mejoras y seguimiento de incidentes. |

## Roadmap de 90 Dias

| Periodo | Objetivo | Actividades | Indicador esperado |
| :--- | :--- | :--- | :--- |
| Dias 1-30 | Estabilizar medicion | Validar datasets, automatizar ejecucion y acordar umbrales oficiales. | 100% de metricas principales calculadas semanalmente. |
| Dias 31-60 | Reducir friccion en HCE | Analizar horarios pico, optimizar endpoints y revisar UX de registro clinico. | Aumento del porcentaje de notas en <= 8 segundos. |
| Dias 61-90 | Controlar riesgo financiero y clinico | Auditar errores de facturacion, alertas de alergias/interacciones y receta electronica. | Reduccion de incidentes de Libertad de Riesgo. |

## Gobernanza

- Gerencia de Calidad lidera la interpretacion de indicadores.
- TI administra scripts, datos, automatizacion y observabilidad.
- Direccion Medica valida riesgos clinicos y prioriza correcciones que afectan seguridad del paciente.
- Facturacion y Auditoria Financiera validan RNF-03 y conciliaciones.

## Criterio de Exito

El programa se considera efectivo si MediSalud puede demostrar trimestralmente, con datos reproducibles, que las tareas criticas mejoran en efectividad, eficiencia, satisfaccion, libertad de riesgo y cobertura de contexto.
