ASEGURAMIENTO DE LA CALIDAD DEL SOFTWARE
Taller Calidad de Uso
Medición de la Calidad en Uso mediante ISO/IEC 25022
Caso de estudio: Sistema de Historia Clínica Electrónica
Red Hospitalaria MediSalud Ecuador
Marco de referencia: ISO/IEC 25000 (SQuaRE)
Norma central: ISO/IEC 25022 — Measurement of Quality in Use
Nivel: Séptimo Semestre — Ingeniería de Software
Modalidad: Taller práctico basado en caso de estudio empresarial
Ing. Diego Leonardo Gamboa Saﬂa Mgtr.
Versión 1.0
Ficha Técnica del Material
Asignatura
Aseguramiento de la Calidad del Software
Unidad temática
Evaluación de la Calidad del Producto de Software — Modelo SQuaRE
Norma aplicada
ISO/IEC 25022:2016 — Measurement of Quality in Use
Modalidad
Presencial / En Línea
Prerrequisitos
Ingeniería de software
Caso de estudio
Sistema de Historia Clínica Electrónica (HCE) de una red hospitalaria
nacional
Índice general
Presentación General del Taller
8
Caso de Estudio: Red Hospitalaria MediSalud Ecuador
10
1. Introducción al Caso Empresarial
15
1.1. Parte 1 — Fundamento Teórico . . . . . . . . . . . . . . . . . . . . . . . . . . . .
15
1.1.1.
El rol del Ingeniero de Calidad en un contexto empresarial real . . . . . .
15
1.1.2.
De la percepción a la evidencia . . . . . . . . . . . . . . . . . . . . . . . .
15
1.1.3.
Presentación del equipo de trabajo . . . . . . . . . . . . . . . . . . . . . .
15
1.2. Parte 2 — Actividad Práctica . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
16
1.2.1.
Paso 1: Creación del repositorio de trabajo
. . . . . . . . . . . . . . . . .
16
1.2.2.
Paso 2: Instalación del entorno Python . . . . . . . . . . . . . . . . . . . .
16
1.2.3.
Paso 3: Análisis dirigido del caso . . . . . . . . . . . . . . . . . . . . . . .
17
2. Comprensión de ISO/IEC 25022
18
2.1. Parte 1 — Fundamento Teórico . . . . . . . . . . . . . . . . . . . . . . . . . . . .
18
2.1.1.
¿Qué es ISO/IEC 25022?
. . . . . . . . . . . . . . . . . . . . . . . . . . .
18
2.1.2.
Las cinco características de Calidad en Uso . . . . . . . . . . . . . . . . .
18
2.1.3.
Aplicación conceptual al caso MediSalud . . . . . . . . . . . . . . . . . . .
19
2.1.4.
Estructura general de una métrica en ISO/IEC 25022
. . . . . . . . . . .
19
2.2. Parte 2 — Actividad Práctica . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
20
3. Comprensión del Modelo SQuaRE
22
3.1. Parte 1 — Fundamento Teórico . . . . . . . . . . . . . . . . . . . . . . . . . . . .
22
3.1.1.
¿Qué es SQuaRE? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
22
3.1.2.
Relación entre ISO/IEC 25010 y 25022 . . . . . . . . . . . . . . . . . . . .
22
3.2. Parte 2 — Actividad Práctica . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
23
4. Identicación de Atributos de Calidad en Uso
25
4.1. Parte 1 — Fundamento Teórico . . . . . . . . . . . . . . . . . . . . . . . . . . . .
25
4.1.1.
El modelo Usuario–Tarea–Contexto
. . . . . . . . . . . . . . . . . . . . .
25
4.1.2.
Atributos de calidad en uso . . . . . . . . . . . . . . . . . . . . . . . . . .
25
4.2. Parte 2 — Actividad Práctica . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
25
5. Mapeo de Características de Calidad
28
5.1. Parte 1 — Fundamento Teórico . . . . . . . . . . . . . . . . . . . . . . . . . . . .
28
5.1.1.
¿Por qué priorizar? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
28
5.1.2.
Matriz de priorización . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
28
5.2. Parte 2 — Actividad Práctica . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
28
3
4
Taller ISO/IEC 25022 — Calidad en Uso
6. Diseño de Métricas
31
6.1. Parte 1 — Fundamento Teórico . . . . . . . . . . . . . . . . . . . . . . . . . . . .
31
6.1.1.
Anatomía de una métrica ISO/IEC 25022 . . . . . . . . . . . . . . . . . .
31
6.1.2.
Catálogo de métricas ISO/IEC 25022 aplicadas a MediSalud
. . . . . . .
32
6.2. Parte 2 — Actividad Práctica . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
32
7. Obtención de Datos
35
7.1. Parte 1 — Fundamento Teórico . . . . . . . . . . . . . . . . . . . . . . . . . . . .
35
7.1.1.
Fuentes típicas de datos para Calidad en Uso . . . . . . . . . . . . . . . .
35
7.1.2.
Calidad del dato antes que calidad del indicador
. . . . . . . . . . . . . .
35
7.2. Parte 2 — Actividad Práctica . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
35
8. Automatización de la Medición
39
8.1. Parte 1 — Fundamento Teórico . . . . . . . . . . . . . . . . . . . . . . . . . . . .
39
8.1.1.
¿Por qué automatizar? . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
39
8.1.2.
Arquitectura del pipeline de medición
. . . . . . . . . . . . . . . . . . . .
39
8.2. Parte 2 — Actividad Práctica . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
39
9. Construcción de Indicadores
45
9.1. Parte 1 — Fundamento Teórico . . . . . . . . . . . . . . . . . . . . . . . . . . . .
45
9.1.1.
De la métrica al indicador . . . . . . . . . . . . . . . . . . . . . . . . . . .
45
9.1.2.
Principios de buena visualización de indicadores de calidad
. . . . . . . .
45
9.2. Parte 2 — Actividad Práctica . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
45
10.Interpretación de Resultados
49
10.1. Parte 1 — Fundamento Teórico . . . . . . . . . . . . . . . . . . . . . . . . . . . .
49
10.1.1. Errores comunes de interpretación
. . . . . . . . . . . . . . . . . . . . . .
49
10.1.2. Técnica de análisis de causa raíz (5 Por Qué) . . . . . . . . . . . . . . . .
49
10.2. Parte 2 — Actividad Práctica . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
49
11.Presentación Ejecutiva para Directivos
52
11.1. Parte 1 — Fundamento Teórico . . . . . . . . . . . . . . . . . . . . . . . . . . . .
52
11.1.1. Comunicar calidad de software a audiencias no técnicas
. . . . . . . . . .
52
11.1.2. Estructura recomendada de un informe ejecutivo . . . . . . . . . . . . . .
52
11.2. Parte 2 — Actividad Práctica . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
52
12.Plan de Mejora Continua
55
12.1. Parte 1 — Fundamento Teórico . . . . . . . . . . . . . . . . . . . . . . . . . . . .
55
12.1.1. El ciclo PDCA aplicado a la Calidad en Uso . . . . . . . . . . . . . . . . .
55
12.1.2. Gobernanza del programa . . . . . . . . . . . . . . . . . . . . . . . . . . .
55
12.2. Parte 2 — Actividad Práctica . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
55
Reto Final Integrador
58
Solución Propuesta del Reto Final
60
ÍNDICE GENERAL
5
Rúbrica de Evaluación
62
Glosario
65
Anexos
66
Índice de ﬁguras
1.
Arquitectura simpliﬁcada de MediSalud HIS . . . . . . . . . . . . . . . . . . . . .
12
3.1. Ubicación de ISO/IEC 25022 dentro de la familia SQuaRE
. . . . . . . . . . . .
23
8.1. Pipeline de automatización de la medición de Calidad en Uso . . . . . . . . . . .
39
6
Índice de tablas
1.
Mapa general de escenarios del taller . . . . . . . . . . . . . . . . . . . . . . . . .
9
2.
Perﬁles de usuario de MediSalud HIS . . . . . . . . . . . . . . . . . . . . . . . . .
11
3.
Requerimientos no funcionales priorizados . . . . . . . . . . . . . . . . . . . . . .
13
1.1. Matriz de análisis inicial del caso MediSalud . . . . . . . . . . . . . . . . . . . . .
17
2.1. Características de Calidad en Uso según ISO/IEC 25022 . . . . . . . . . . . . . .
19
2.2. Plantilla de clasiﬁcación de incidentes según ISO/IEC 25022 . . . . . . . . . . . .
20
3.1. Divisiones de la familia ISO/IEC 25000 (SQuaRE) . . . . . . . . . . . . . . . . .
22
3.2. Los tres niveles de calidad aplicados a MediSalud HIS
. . . . . . . . . . . . . . .
24
4.1. Plantilla Usuario–Tarea–Contexto
. . . . . . . . . . . . . . . . . . . . . . . . . .
26
5.1. Matriz de mapeo tarea–característica–prioridad (fragmento) . . . . . . . . . . . .
29
6.1. Catálogo de métricas de Calidad en Uso — MediSalud HIS
. . . . . . . . . . . .
32
7.1. Fuentes de datos según característica ISO/IEC 25022 . . . . . . . . . . . . . . . .
35
12.1. Cronograma propuesto del programa de medición continua . . . . . . . . . . . . .
56
12.2. Matriz de responsables del programa de medición . . . . . . . . . . . . . . . . . .
56
12.3. Solución: ﬁcha Usuario–Tarea–Contexto de Telemedicina 2.0 . . . . . . . . . . . .
60
12.4. Solución: catálogo de métricas de Telemedicina 2.0 . . . . . . . . . . . . . . . . .
60
12.5. Rúbrica de evaluación del Reto Final Integrador
. . . . . . . . . . . . . . . . . .
63
12.6. Comandos frecuentes utilizados a lo largo del taller . . . . . . . . . . . . . . . . .
66
7
Presentación General del Taller
Objetivo General
Desarrollar en los estudiantes la capacidad de aplicar la norma ISO/IEC 25022 para
medir la Calidad en Uso de un sistema software empresarial real, combinando fundamento teórico
riguroso con práctica intensiva sobre herramientas modernas de medición, automatización y
visualización de indicadores de calidad.
Filosofía del Taller
Este material no es un compendio teórico. Cada uno de los doce escenarios que lo compo-
nen combina una base conceptual sólida con actividades de laboratorio completamente guiadas,
ejecutadas sobre un caso de estudio empresarial único y coherente: la red hospitalaria Medi-
Salud Ecuador y su sistema de Hospital Information System (HIS). El estudiante recorrerá el
ciclo completo de este proyecto real de evaluación de calidad en uso: desde la comprensión de la
norma hasta la entrega de un informe ejecutivo y un plan de mejora continua.
. Nota
Todas las herramientas utilizadas en este taller forman parte de una edición Community,
Free o Trial suﬁciente para ﬁnes académicos. No se requiere presupuesto institucional o
personal para su ejecución completa.
Estructura de cada Escenario
Cada escenario sigue la misma arquitectura pedagógica:
1. Parte 1 — Fundamento Teórico: deﬁniciones, marco normativo, fórmulas y ejemplos
aplicados al caso MediSalud.
2. Parte 2 — Actividad Práctica: laboratorio guiado con ﬁcha técnica, instalación, con-
ﬁguración, ejecución, capturas sugeridas y solución de errores.
3. Resultados obtenidos e interpretación.
4. Análisis crítico.
5. Preguntas de discusión.
6. Conclusiones parciales.
8
Presentación General
9
Mapa de Escenarios
Tabla 1: Mapa general de escenarios del taller
#
Escenario
Duración
1
Introducción al caso empresarial MediSalud
2h
2
Comprensión de ISO/IEC 25022
3h
3
Comprensión del modelo SQuaRE (ISO/IEC 25000)
2h
4
Identiﬁcación de atributos de Calidad en Uso
3h
5
Mapeo de características de calidad
2h
6
Diseño de métricas
3h
7
Obtención de datos (logs, BD, encuestas)
3h
8
Automatización de la medición con Python
4h
9
Construcción de indicadores (KPI)
3h
10
Interpretación de resultados
3h
11
Presentación ejecutiva para directivos
3h
12
Plan de mejora continua
2h
Reto Final Integrador
4h
Caso de Estudio: Red Hospitalaria Me-
diSalud Ecuador
Descripción de la Empresa
MediSalud Ecuador es una red privada de salud constituida en 2009, con cobertura en
cinco ciudades del país (Quito, Guayaquil, Cuenca, Ambato y Manta). La red opera actualmente:
4 hospitales generales de tercer nivel.
12 centros de atención ambulatoria.
1 laboratorio clínico centralizado con sucursales.
1 central de imagenología y diagnóstico por imágenes.
Un servicio de telemedicina en expansión desde 2022.
La organización atiende aproximadamente 38.000 pacientes activos por mes y emplea a
más de 2.100 colaboradores, entre personal médico, administrativo y de TI.
Estructura Organizacional
Dirección General — deﬁne objetivos estratégicos de la red.
Dirección Médica — supervisa protocolos clínicos y calidad asistencial.
Gerencia de Tecnología (TI) — responsable del sistema HIS, infraestructura y ciber-
seguridad.
Gerencia de Calidad y Aseguramiento — responsable de certiﬁcaciones (ISO 9001,
acreditación hospitalaria) y ahora del programa de Calidad en Uso del Software.
Departamento de Admisión y Facturación.
Departamento de Enfermería y Hospitalización.
Departamento de Farmacia.
Call Center y Agendamiento de Citas.
10
Caso de Estudio
11
El Sistema: MediSalud HIS
El núcleo tecnológico de la operación es MediSalud HIS, un sistema de información hos-
pitalaria que integra:
Módulo de Historia Clínica Electrónica (HCE) (historia clínica electrónica).
Módulo de admisión, agendamiento y facturación.
Módulo de farmacia e inventario de insumos médicos.
Portal del paciente (web y app móvil) para citas y resultados.
Módulo de telemedicina (videoconsulta e indicaciones remotas).
Módulo de reportes gerenciales y business intelligence.
Usuarios del Sistema
Tabla 2: Perﬁles de usuario de MediSalud HIS
Perl
Uso principal
Usuarios activos
Médico tratante
Registro de HCE, órdenes, recetas
640
Enfermería
Signos vitales, administración de medicamentos
910
Personal de admisión
Agendamiento, facturación
210
Farmacia
Dispensación, inventario
85
Paciente (portal/app)
Citas, resultados, telemedicina
38.000+
Gerencia / Calidad
Reportes, indicadores
45
Arquitectura del Sistema
MediSalud HIS sigue una arquitectura de microservicios desplegada en contenedores, con las
siguientes capas:
Frontend web: React, desplegado como SPA.
Aplicación móvil: Android/iOS (Flutter).
Backend: microservicios en Spring Boot y FastAPI, expuestos vía API REST.
Base de datos transaccional: PostgreSQL (HCE, facturación) y SQL Server (módulo
ﬁnanciero heredado).
Mensajería: colas asíncronas para integración entre laboratorio, imagenología y HCE.
Infraestructura: contenedores Docker orquestados en un clúster on-premise, con planes
de migración a la nube pública.
Observabilidad: logs centralizados y métricas de infraestructura (aún incipientes, sin
estandarizar).
12
Taller ISO/IEC 25022 — Calidad en Uso
Portal Web
(React)
App Móvil
(Flutter)
API Gateway
Microservicio
HCE
Microservicio
Facturación
Microservicio
Farmacia
PostgreSQL / SQL Server
Figura 1: Arquitectura simpliﬁcada de MediSalud HIS
Tecnologías Utilizadas
React, Flutter, Spring Boot, FastAPI, PostgreSQL, SQL Server, Docker, Nginx, RabbitMQ,
Git/GitHub, Jenkins (en migración a GitHub Actions).
Procesos Críticos del Negocio
1. Agendamiento y admisión de pacientes.
2. Atención médica y registro de historia clínica.
3. Prescripción y dispensación de medicamentos.
4. Facturación y gestión de seguros/reaseguros.
5. Telemedicina y seguimiento remoto.
6. Generación de reportes gerenciales para toma de decisiones.
Problemática Actual
Durante el último año, la Gerencia de Calidad ha recibido señales de alerta consistentes:
Quejas recurrentes de médicos por lentitud del módulo de HCE en horas pico (10:00–
12:00).
Incremento del tiempo de espera para agendar citas vía portal del paciente.
Errores de doble facturación reportados por el área ﬁnanciera.
Abandono de sesiones en la app móvil antes de completar el registro de síntomas en
telemedicina.
Caso de Estudio
13
Ausencia de métricas objetivas: las decisiones se toman actualmente por percepción, no
por datos.
El área de TI aﬁrma que «el sistema funciona correctamente» basándose únicamente en
la disponibilidad de los servidores (uptime), sin considerar la experiencia real del usuario
ﬁnal.
Riesgos Identiﬁcados
Riesgo clínico: demoras en el registro de HCE pueden retrasar decisiones médicas críticas.
Riesgo ﬁnanciero: errores de facturación afectan el ﬂujo de caja y la relación con asegura-
doras.
Riesgo reputacional: fricciones en el portal del paciente afectan la retención de usuarios
frente a competidores.
Riesgo regulatorio: la normativa ecuatoriana de protección de datos en salud exige traza-
bilidad y disponibilidad de la información clínica.
Objetivos del Negocio
1. Reducir en un 30 % el tiempo de registro de HCE en consulta externa en un plazo de 6
meses.
2. Disminuir los errores de facturación duplicada a menos del 1 % de las transacciones.
3. Aumentar la tasa de ﬁnalización de teleconsultas al 95 %.
4. Establecer un programa permanente de medición de Calidad en Uso basado en
ISO/IEC 25022, con reportes trimestrales a Dirección General.
Requerimientos No Funcionales Relevantes para el Taller
Tabla 3: Requerimientos no funcionales priorizados
Código
Requerimiento
RNF-01
El registro de una nota de evolución clínica no debe tardar más de 8 segundos en el
90 % de los casos.
RNF-02
El portal de citas debe permitir agendar una cita en máximo 3 pasos, sin errores de
disponibilidad.
RNF-03
La tasa de errores de facturación no debe superar el 1 % de las transacciones men-
suales.
RNF-04
El sistema debe permitir auditar el uso por rol, sede y horario.
RNF-05
Las teleconsultas deben completarse sin caídas de conexión en más del 95 % de los
casos.
14
Taller ISO/IEC 25022 — Calidad en Uso
. Nota
Este caso de estudio será utilizado de forma transversal en los doce escenarios del taller.
Todos los archivos de datos (CSV, logs, JSON) referenciados en las prácticas simulan –de
forma anonimizada y ﬁcticia– el comportamiento real de MediSalud HIS.
ESCENARIO 1
Introducción al Caso Empresarial
‰ Objetivo del Escenario
Familiarizarse con el caso de estudio de la organización MediSalud Ecuador, su sistema
HIS, su problemática de calidad y el rol que jugará el equipo de Aseguramiento de la
Calidad del Software a lo largo del taller, estableciendo el contrato pedagógico y el entorno
de trabajo compartido.
1.1
Parte 1 — Fundamento Teórico
1.1.1
El rol del Ingeniero de Calidad en un contexto empresarial real
En la industria, el aseguramiento de la calidad no se limita a probar que el software «no
falla»; consiste en demostrar, con evidencia medible, que el sistema permite a los usuarios
reales alcanzar sus objetivos de forma efectiva, eﬁciente y satisfactoria, dentro de un contexto
de uso determinado. Esta idea es precisamente el núcleo de la Calidad en Uso (Quality in Use),
el concepto central que se desarrollará durante todo el taller.
1.1.2
De la percepción a la evidencia
Como se describió en el caso de estudio (capítulo introductorio), MediSalud Ecuador toma
decisiones de TI basándose en percepciones («el sistema funciona bien porque los servidores están
arriba»). El objetivo de este taller es transformar esa cultura hacia una cultura de decisiones
basada en métricas, siguiendo el ciclo:
Observar el uso real →Medir con métricas normalizadas →Construir indicadores →
Interpretar →Actuar
1.1.3
Presentación del equipo de trabajo
Durante el taller, grupo de 4–5 estudiantes asumirá el rol de un consultor externo de
Calidad de Software contratado por la Gerencia de Calidad de MediSalud para implementar,
de principio a ﬁn, un programa de medición basado en ISO/IEC 25022.
15
16
Taller ISO/IEC 25022 — Calidad en Uso
1.2
Parte 2 — Actividad Práctica
Ficha de Laboratorio
Objetivo:
Conﬁgurar el entorno de trabajo compartido del taller
y realizar el primer reconocimiento del caso
Tiempo estimado:
± 1 hora
Nivel de dicultad:
Básico
Herramientas requeridas:
Cuenta de GitHub, Visual Studio Code, Python 3.11+,
Git
Archivos / datos necesarios:
Repositorio medisalud-calidad-uso (se crea en este
laboratorio), documento de caso de estudio (capítulo
previo)
1.2.1
Paso 1: Creación del repositorio de trabajo
1. Ingresar a https://github.com y crear una cuenta institucional (si no se dispone de una).
2. Crear un nuevo repositorio llamado medisalud-calidad-uso, público o privado según la
política del curso.
3. Clonar el repositorio en el equipo local:
1
git clone https://github.com/<usuario>/medisalud-calidad-uso.git
2
cd medisalud-calidad-uso
3
mkdir -p data scripts dashboards docs reportes
Listing 1.1: Clonado del repositorio de trabajo
1.2.2
Paso 2: Instalación del entorno Python
1
python3 --version # Verificar Python 3.11 o superior
2
python3 -m venv venv
3
source venv/bin/activate # En Windows: venv\Scripts\activate
4
pip install --upgrade pip
5
pip install pandas numpy matplotlib plotly jupyter openpyxl
Listing 1.2: Creación de entorno virtual para todo el taller
8 Advertencia / Error Frecuente
Error frecuente: python3: command not found en Windows.
Solución: en Windows utilizar python en lugar de python3, y veriﬁcar que la casilla «Add
Python to PATH» haya sido marcada durante la instalación del intérprete descargado
desde https://python.org.
CAPÍTULO 1. INTRODUCCIÓN AL CASO EMPRESARIAL
17
1.2.3
Paso 3: Análisis dirigido del caso
En grupos de 4–5 estudiantes, completar la siguiente matriz en el archivo docs/analisis_inicial.md:
Tabla 1.1: Matriz de análisis inicial del caso MediSalud
Pregunta guía
Respuesta del grupo
¿Cuáles son los 3 procesos más críticos del negocio?
¿Qué usuarios se ven más afectados por la problemática actual?
¿Qué evidencia tiene hoy MediSalud sobre la calidad de su software?
¿Qué evidencia le falta?
3 Resultado Esperado
Al ﬁnalizar este escenario, cada grupo dispone de: (1) un repositorio Git funcional con
la estructura de carpetas del taller, (2) un entorno Python operativo, y (3) un docu-
mento inicial de análisis del caso que evidencia comprensión crítica de la problemática
empresarial.
Resolución de Problemas
Error de permisos en Git (Permission denied (publickey)): conﬁgurar una llave
SSH con ssh-keygen -t ed25519 y agregarla en GitHub →Settings →SSH Keys.
Conictos de versión de Python: usar pyenv para gestionar múltiples versiones si el
sistema operativo trae una versión antigua preinstalada.
Preguntas de Discusión
1. ¿Por qué la disponibilidad de servidores (uptime) no es suﬁciente para aﬁrmar que un
sistema tiene buena calidad en uso?
2. ¿Qué diferencia existe entre la calidad interna, la calidad externa y la calidad en uso de
un producto software?
3. En el caso de MediSalud, ¿qué stakeholder se beneﬁciaría más de un programa de medición
de calidad en uso: el paciente, el médico o la gerencia? Justiﬁque.
Conclusiones Parciales
Este primer escenario estableció el marco de trabajo y evidenció que las decisiones de TI
en MediSalud carecen de sustento medible. Los escenarios siguientes dotarán al estudiante del
marco normativo (ISO/IEC 25000 y 25022) necesario para cerrar esa brecha.
n Recomendaciones
Aproveche este escenario para indagar experiencias previas de los estudiantes con siste-
mas lentos o poco usables (bancos, universidades, salud) y conectar esas vivencias con el
concepto de Calidad en Uso antes de formalizarlo en el Escenario 2.
ESCENARIO 2
Comprensión de ISO/IEC 25022
‰ Objetivo del Escenario
Comprender en profundidad la norma ISO/IEC 25022 (Measurement of Quality in Use),
sus cinco características, sus fórmulas de medición y su rol dentro de la familia SQuaRE,
aplicándolas conceptualmente al caso MediSalud HIS.
2.1
Parte 1 — Fundamento Teórico
2.1.1
¿Qué es ISO/IEC 25022?
ISO/IEC 25022 es la norma internacional, perteneciente a la familia Software product Quality
Requirements and Evaluation (SQuaRE) (ISO/IEC 25000), que deﬁne un modelo de medición
de la Calidad en Uso de un producto software. A diferencia de ISO/IEC 25010 (que deﬁne el
modelo de calidad, es decir, qué características debe tener un producto), la norma 25022 deﬁne
cómo medir dichas características desde la perspectiva de quien efectivamente utiliza el sistema
en un contexto real de uso.
. Nota
La Calidad en Uso no se mide sobre el código fuente ni sobre el producto en abstracto: se
mide observando a usuarios reales realizando tareas reales en un contexto de uso
especíco.
2.1.2
Las cinco características de Calidad en Uso
ISO/IEC 25022 organiza la Calidad en Uso en cinco características:
18
CAPÍTULO 2. COMPRENSIÓN DE ISO/IEC 25022
19
Tabla 2.1: Características de Calidad en Uso según ISO/IEC 25022
Característica
Denición
Efectividad (Eectiveness)
Precisión y grado de completitud con que
los usuarios alcanzan sus objetivos especí-
ﬁcos.
Eciencia (Eciency)
Recursos utilizados (tiempo, esfuerzo, per-
sonas) en relación con la efectividad alcan-
zada.
Satisfacción (Satisfaction)
Grado en que las necesidades del usuario
son cubiertas, generando percepciones y
respuestas positivas de utilidad, conﬁanza,
placer y comodidad.
Libertad de Riesgo (Freedom from Risk)
Grado en que el sistema mitiga riesgos eco-
nómicos, de salud, de seguridad o ambien-
tales potenciales.
Cobertura de Contexto (Context Coverage)
Grado en que el producto puede ser utili-
zado con efectividad, eﬁciencia, libertad de
riesgo y satisfacción tanto en los contextos
previstos como en otros no previstos ini-
cialmente.
2.1.3
Aplicación conceptual al caso MediSalud
‰ Ejemplo Empresarial
Un médico (usuario) intenta registrar una nota de evolución clínica (tarea) durante la
consulta externa de la mañana (contexto de uso). Si logra registrarla completa y sin
errores, hay efectividad; si lo hace en menos de 8 segundos, hay eciencia; si termina
la consulta sintiéndose cómodo con el sistema, hay satisfacción; si el sistema no expone
datos sensibles del paciente durante el proceso, hay libertad de riesgo; y si el mismo
ﬂujo funciona igual de bien en el hospital de Quito que en el centro ambulatorio de Manta,
hay cobertura de contexto.
2.1.4
Estructura general de una métrica en ISO/IEC 25022
Toda métrica de Calidad en Uso se expresa mediante la fórmula general:
X = A
B
donde A representa el resultado observado (tareas completadas, tiempo invertido, incidentes
detectados) y B representa la base de referencia (tareas intentadas, tiempo total disponible,
número de usuarios). El resultado X se interpreta siempre en función de un rango deseado,
deﬁnido previamente por la organización.
20
Taller ISO/IEC 25022 — Calidad en Uso
2.2
Parte 2 — Actividad Práctica
Ficha de Laboratorio
Objetivo:
Analizar la norma ISO/IEC 25022 y clasiﬁcar proble-
mas reales de MediSalud según sus cinco característi-
cas
Tiempo estimado:
±1 hora
Nivel de dicultad:
Básico – Intermedio
Herramientas requeridas:
Navegador web, editor de texto / Markdown, Miro o
similar (opcional)
Archivos / datos necesarios:
Lista
de
incidentes
de
MediSalud
HIS
(data/incidentes_2025.csv,
provisto
en
este
escenario)
Paso 1: Dataset de incidentes reportados
Crear el archivo data/incidentes_2025_iso_25022.csv con el siguiente contenido (frag-
mento representativo):
1
id,fecha,modulo,descripcion,rol_usuario,sede
2
1001,2025-11-03,HCE,Nota de evolucion tarda 22s en guardarse,Medico,Quito
3
1002,2025-11-03,Portal Citas,Usuario no logra agendar tras 3 intentos,Paciente,Guayaquil
4
1003,2025-11-04,Facturacion,Factura duplicada al reintentar pago,Admision,Cuenca
5
1004,2025-11-05,Telemedicina,Videollamada se corta a los 4 minutos,Paciente,Ambato
6
1005,2025-11-05,HCE,Datos de otro paciente visibles brevemente,Medico,Quito
7
1006,2025-11-06,Portal Citas,Formulario confuso, abandono de registro,Paciente,Manta
Listing 2.1: Fragmento de incidentes reportados en MediSalud HIS(ejemplo)
Paso 2: Clasiﬁcación según las cinco características
En equipos, clasiﬁcar cada incidente del dataset anterior en la característica de ISO/IEC
25022 que mejor lo representa, completando la tabla:
Tabla 2.2: Plantilla de clasiﬁcación de incidentes según ISO/IEC 25022
ID
Justicación
Característica
1001
1002
1003
1004
1005
1006
CAPÍTULO 2. COMPRENSIÓN DE ISO/IEC 25022
21
‰ Actividad para el Estudiante
Como grupo, discutan el incidente 1005. ¿Por qué corresponde principalmente a Libertad
de Riesgo y no a Efectividad, a pesar de tratarse también de un error del sistema?
3 Resultado Esperado
Cada equipo entrega una tabla de clasiﬁcación completa con justiﬁcación técnica, demos-
trando la capacidad de diferenciar las cinco características de la norma sobre casos reales,
no solo sobre deﬁniciones memorizadas.
Resolución de Problemas
Confusión frecuente: los estudiantes tienden a clasiﬁcar todo como «Efectividad». So-
lución docente: preguntar explícitamente «¿el usuario logró o no su objetivo?» (Efecti-
vidad) versus «¿a qué costo/riesgo lo logró?» (Eﬁciencia / Riesgo).
Preguntas de Discusión
1. ¿Puede un sistema ser efectivo pero no eﬁciente? Dé un ejemplo del caso MediSalud.
2. ¿Por qué la Cobertura de Contexto es especialmente relevante para una red hospitalaria
con sedes en cinco ciudades distintas?
Conclusiones Parciales
El estudiante ha comprendido que ISO/IEC 25022 provee un vocabulario común y estructu-
rado para describir problemas de calidad que, en la práctica diaria de MediSalud, se reportaban
de forma ambigua e inconsistente.
ESCENARIO 3
Comprensión del Modelo SQuaRE
‰ Objetivo del Escenario
Ubicar a ISO/IEC 25022 dentro de la familia completa ISO/IEC 25000 (SQuaRE), di-
ferenciando claramente entre modelo de calidad, medición de calidad, requerimientos y
evaluación, para que el estudiante comprenda el marco normativo completo en el que se
inserta el taller.
3.1
Parte 1 — Fundamento Teórico
3.1.1
¿Qué es SQuaRE?
SQuaRE es la familia de normas internacionales ISO/IEC 25000, que reemplazó y uniﬁcó
a las antiguas normas ISO/IEC 9126 e ISO/IEC 14598. SQuaRE organiza el ciclo completo de
gestión de la calidad del software en cinco divisiones:
Tabla 3.1: Divisiones de la familia ISO/IEC 25000 (SQuaRE)
División
Rango
Propósito
Gestión de calidad
2500n
Guía de uso de toda la familia SQuaRE.
Modelo de calidad
2501n
Deﬁne
qué
características
debe
tener
un
producto
(ISO/IEC 25010) y su calidad en uso.
Medición de calidad
2502n
Deﬁne cómo medir
cada característica: aquí reside
ISO/IEC 25022 (Calidad en Uso), junto con 25023 (ca-
lidad de producto) y 25024 (calidad de datos).
Requerimientos de calidad
2503n
Guía para especiﬁcar requerimientos de calidad.
Evaluación de calidad
2504n
Guía para el proceso de evaluación formal de calidad.
3.1.2
Relación entre ISO/IEC 25010 y 25022
ISO/IEC 25010 deﬁne el modelo de calidad en uso con sus cinco características (las
mismas vistas en el Escenario 2). ISO/IEC 25022 toma exactamente esas características y les
asocia métricas concretas, fórmulas y escalas de medición. Es decir: 25010 dice qué
medir; 25022 dice cómo medirlo.
22
CAPÍTULO 3. COMPRENSIÓN DEL MODELO SQUARE
23
ISO/IEC 25000
Guía general SQuaRE
ISO/IEC 25010
Modelo de Calidad (qué medir)
ISO/IEC 25022
Medición de Calidad en Uso (cómo medir)
ISO/IEC 25040
Proceso de Evaluación
Figura 3.1: Ubicación de ISO/IEC 25022 dentro de la familia SQuaRE
3.2
Parte 2 — Actividad Práctica
Ficha de Laboratorio
Objetivo:
Construir un mapa conceptual de la familia SQuaRE
aplicado a MediSalud y diferenciar los tres niveles de
calidad (interna, externa, en uso)
Tiempo estimado:
±1 hora
Nivel de dicultad:
Básico
Herramientas requeridas:
Draw.io / Miro
Archivos / datos necesarios:
Documento resumen de las normas (proporcionado por
el docente o buscado por los estudiantes en fuentes
oﬁciales de ISO)
Paso 1: Investigación dirigida
Cada grupo investiga y resume en minimo 2 páginas, en sus propias palabras, la diferencia
entre:
Calidad interna (código, arquitectura) — ISO/IEC 25010, vista estática.
Calidad externa (comportamiento observable en pruebas) — ISO/IEC 25010, vista diná-
mica en entorno controlado.
Calidad en uso (experiencia real del usuario) — ISO/IEC 25022, vista en producción.
24
Taller ISO/IEC 25022 — Calidad en Uso
Paso 2: Aplicación al caso MediSalud
Completar la tabla identiﬁcando, para cada nivel, un ejemplo concreto del sistema HIS:
Tabla 3.2: Los tres niveles de calidad aplicados a MediSalud HIS
Nivel
Ejemplo en MediSalud HIS
Calidad interna
Complejidad ciclomática del módulo de facturación medida con SonarQube.
Calidad externa
Pruebas de carga con JMeter simulando 500 usuarios concurrentes en el portal
de citas.
Calidad en uso
Tiempo real que tarda un médico en registrar una nota clínica durante con-
sulta externa (dato de producción).
3 Resultado Esperado
Cada grupo entrega un mapa conceptual (imagen o diagrama) que ubica correctamente
las normas ISO/IEC 25000, 25010, 25022 y 25040, y diferencia sin ambigüedad los tres
niveles de calidad usando ejemplos propios del caso MediSalud.
Preguntas de Discusión
1. ¿Puede un sistema tener excelente calidad interna (código limpio) y mala calidad en uso?
Explique con un ejemplo.
2. ¿Por qué SonarQube (calidad interna) no es suﬁciente para que MediSalud resuelva su
problemática de lentitud percibida por los médicos?
Conclusiones Parciales
El estudiante reconoce que la calidad en uso es el nivel más cercano al negocio y al paciente,
y que por ello será el foco exclusivo del resto del taller, sin descuidar que se apoya en buenas
prácticas de calidad interna y externa.
ESCENARIO 4
Identiﬁcación de Atributos de Cali-
dad en Uso
‰ Objetivo del Escenario
Identiﬁcar, a partir de las tareas reales de los usuarios de MediSalud HIS, los atributos
concretos de Calidad en Uso que deben medirse, estableciendo tareas, usuarios y contextos
de uso según la estructura exigida por ISO/IEC 25022.
4.1
Parte 1 — Fundamento Teórico
4.1.1
El modelo Usuario–Tarea–Contexto
ISO/IEC 25022 exige deﬁnir, antes de cualquier métrica, tres elementos:
1. Usuario primario: quién ejecuta la tarea (rol).
2. Tarea representativa: qué objetivo concreto persigue el usuario.
3. Contexto de uso: en qué condiciones (dispositivo, ubicación, carga del sistema, horario)
se ejecuta la tarea.
4.1.2
Atributos de calidad en uso
Un atributo es una propiedad medible derivada de una característica. Por ejemplo, de la
característica Efectividad se derivan atributos como «completitud de tarea» o «precisión de
tarea»; de Eﬁciencia, atributos como «tiempo de tarea» o «eﬁciencia de tarea humana».
4.2
Parte 2 — Actividad Práctica
25
26
Taller ISO/IEC 25022 — Calidad en Uso
Ficha de Laboratorio
Objetivo:
Deﬁnir tareas representativas de usuario y sus atribu-
tos de calidad en uso para tres procesos críticos de
MediSalud
Tiempo estimado:
3 horas
Nivel de dicultad:
Intermedio
Herramientas requeridas:
Editor de hojas de cálculo o Markdown
Archivos / datos necesarios:
Procesos críticos identiﬁcados en el capítulo de caso de
estudio
Paso 1: Selección de procesos
Cada grupo selecciona 3 de los 6 procesos críticos de MediSalud (Escenario introductorio) y
deﬁne, para cada uno, una tarea representativa siguiendo la plantilla:
Tabla 4.1: Plantilla Usuario–Tarea–Contexto
Campo
Ejemplo completado
Proceso
Atención médica y registro de HCE
Usuario primario
Médico tratante
Tarea representativa
Registrar una nota de evolución clínica completa de
un paciente
Contexto de uso
Consulta externa, horario 10:00–12:00, red interna del
hospital de Quito, carga alta de usuarios concurrentes
Atributos de Calidad en Uso relevantes
Tiempo de tarea (Eﬁciencia), completitud de la nota
(Efectividad), percepción de ﬂuidez (Satisfacción)
‰ Actividad para el Estudiante
Repitan la plantilla anterior para Agendamiento de citas por el paciente y para Factura-
ción de una consulta con seguro médico.
n Recomendaciones
Insista en que el contexto de uso no es un detalle decorativo: variables como «hora pico»
o «sede» explican después por qué la misma métrica puede arrojar valores muy distintos
entre Quito y Manta.
3 Resultado Esperado
Cada grupo entrega tres ﬁchas Usuario–Tarea–Contexto completas y coherentes con el
caso MediSalud, listas para ser convertidas en métricas concretas en el Escenario 6.
CAPÍTULO 4. IDENTIFICACIÓN DE ATRIBUTOS DE CALIDAD EN USO
27
Preguntas de Discusión
1. ¿Por qué es incorrecto deﬁnir una tarea como «usar el sistema HIS» en lugar de «registrar
una nota de evolución clínica»?
2. ¿Qué ocurre si se mide la eﬁciencia sin haber deﬁnido el contexto de uso (por ejemplo, sin
diferenciar hora pico de hora valle)?
Conclusiones Parciales
El estudiante ha aprendido a operacionalizar procesos de negocio abstractos en tareas medi-
bles, usuarios concretos y contextos de uso explícitos, requisito indispensable antes de diseñar
cualquier métrica ISO/IEC 25022.
ESCENARIO 5
Mapeo de Características de Calidad
‰ Objetivo del Escenario
Construir la matriz de mapeo que vincula cada tarea Usuario–Tarea–Contexto deﬁnida
en el Escenario 4 con las cinco características de ISO/IEC 25022, priorizando cuáles serán
medidas en el programa de MediSalud.
5.1
Parte 1 — Fundamento Teórico
5.1.1
¿Por qué priorizar?
Medir las cinco características para todas las tareas posibles no es viable ni deseable: consume
recursos y genera ruido. La práctica profesional recomienda priorizar según impacto en el
negocio y riesgo, criterios ya identiﬁcados en el caso de estudio.
5.1.2
Matriz de priorización
Se recomienda una matriz de doble entrada: Impacto en el negocio (alto/medio/bajo) frente
a Frecuencia de la tarea (alta/media/baja), seleccionando para medición prioritaria las combi-
naciones alto–alto y alto–medio.
5.2
Parte 2 — Actividad Práctica
Ficha de Laboratorio
Objetivo:
Elaborar la matriz de mapeo tarea–característica–
prioridad para el programa de medición de MediSalud
Tiempo estimado:
2 horas
Nivel de dicultad:
Intermedio
Herramientas requeridas:
Hoja de cálculo (Excel/Google Sheets)
Archivos / datos necesarios:
Fichas Usuario–Tarea–Contexto del Escenario 4
28
CAPÍTULO 5. MAPEO DE CARACTERÍSTICAS DE CALIDAD
29
Paso 1: Construcción de la matriz
Tabla 5.1: Matriz de mapeo tarea–característica–prioridad (fragmento)
Tarea
Impacto
Frecuencia
Característica(s)
ISO
25022
Prioridad
Registrar nota de evolución clínica
Alto
Alta
Eﬁciencia,
Efec-
tivi-
dad
1
Agendar cita en portal
Alto
Alta
Efectividad,
Sa-
tis-
fac-
ción
1
Facturar consulta con seguro
Alto
Media
Libertad
de
Ries-
go,
Efec-
tivi-
dad
2
Completar teleconsulta
Medio
Media
Efectividad,
Co-
ber-
tura
de
Con-
tex-
to
2
Consultar historial de resultados de laboratorio
Bajo
Alta
Satisfacción 3
3 Resultado Esperado
El equipo entrega una matriz priorizada con al menos 6 tareas, sirviendo como insumo
directo para el diseño de métricas del Escenario 6, donde solo se desarrollarán en profun-
didad las tareas de prioridad 1 y 2.
Preguntas de Discusión
1. ¿Qué riesgo corre una organización que intenta medir absolutamente todo desde el primer
día de un programa de calidad en uso?
2. ¿Por qué «Consultar historial de resultados» tiene menor prioridad pese a tener alta fre-
cuencia?
30
Taller ISO/IEC 25022 — Calidad en Uso
Conclusiones Parciales
El estudiante comprende que un programa de medición sostenible se construye de forma
incremental, comenzando por las tareas de mayor impacto y frecuencia, principio que también
rige la implementación de sistemas de monitoreo en la industria (por ejemplo, en observabilidad
de software).
ESCENARIO 6
Diseño de Métricas
‰ Objetivo del Escenario
Diseñar formalmente, siguiendo la estructura de ISO/IEC 25022, las métricas de Calidad
en Uso para las tareas priorizadas de MediSalud: fórmula, variables, unidad, rango deseado
e interpretación.
6.1
Parte 1 — Fundamento Teórico
6.1.1
Anatomía de una métrica ISO/IEC 25022
Toda métrica formal debe documentar:
Nombre de la métrica.
Característica asociada.
Propósito de la medición.
Fórmula (X = A/B u otra estructura).
Denición de variables.
Unidad de medida.
Rango deseado / umbral.
Fuente de datos.
Interpretación.
31
32
Taller ISO/IEC 25022 — Calidad en Uso
6.1.2
Catálogo de métricas ISO/IEC 25022 aplicadas a MediSalud
Tabla 6.1: Catálogo de métricas de Calidad en Uso — MediSalud HIS
Característica
Métrica
Fórmula
Efectividad
Completitud de tarea (registro de
HCE)
X
=
Notas completadas correctamente
Notas intentadas
Efectividad
Tasa de éxito de agendamiento
X = Citas agendadas con éxito
Intentos de agendamiento
Eﬁciencia
Tiempo de tarea (registro clínico)
X =
∑Tiempo por nota
Número de notas
Eﬁciencia
Eﬁciencia relativa del usuario
X =
Efectividad
Tiempo invertido
Satisfacción
Índice de satisfacción (encuesta)
X =
∑Puntajes de satisfacción
N. de encuestados
Libertad de Riesgo
Tasa de errores de facturación
X = Facturas erróneas
Facturas emitidas
Cobertura de Contexto
Consistencia entre sedes
X
=
1
−
|Métrica sede A −Métrica sede B|
Métrica sede A
‰ Ejemplo Empresarial
Métrica: Tiempo de tarea — registro de nota clínica.
Fórmula: X =
∑ti
n , donde ti es el tiempo (segundos) que tarda el registro i-ésimo y n
el número total de registros observados.
Rango deseado: X ≤8 segundos (según RNF-01 del caso de estudio).
Fuente de datos: logs de la aplicación web/HIS (marca de tiempo al abrir el formulario
y al conﬁrmar el guardado).
Interpretación: valores por encima de 8 segundos de forma sostenida indican fricción de
usabilidad o degradación de desempeño técnico, ambos con impacto directo en la atención
médica.
6.2
Parte 2 — Actividad Práctica
Ficha de Laboratorio
Objetivo:
Documentar formalmente 5 métricas ISO/IEC 25022
(una por característica) usando la ﬁcha estándar de
diseño de métrica
Tiempo estimado:
3 horas
Nivel de dicultad:
Intermedio – Avanzado
Herramientas requeridas:
Plantilla de ﬁcha de métrica (Markdown/Excel)
Archivos / datos necesarios:
Matriz priorizada del Escenario 5
CAPÍTULO 6. DISEÑO DE MÉTRICAS
33
Paso 1: Ficha estándar de métrica
Cada grupo documenta, para cada una de las 5 características, una métrica siguiendo esta
ﬁcha:
Plantilla: Ficha de Métrica ISO/IEC 25022
Nombre:
Característica:
Propósito:
Fórmula:
Variables:
Unidad:
Rango deseado:
Fuente de datos:
Frecuencia de medición:
Responsable:
8 Advertencia / Error Frecuente
Error frecuente: deﬁnir una fórmula sin especiﬁcar la unidad de las variables (por
ejemplo, no aclarar si el tiempo se mide en segundos o minutos). Esto genera indicadores
incomparables entre sedes o entre sprints de medición. Solución: exigir siempre la unidad
explícita en la ﬁcha.
3 Resultado Esperado
Cada equipo entrega un catálogo de al menos 5 métricas formalmente documentadas, listas
para ser calculadas automáticamente en los Escenarios 7 y 8 con datos reales (simulados)
de MediSalud.
Resolución de Problemas
Métrica ambigua: si dos estudiantes del mismo grupo calculan manualmente la mé-
trica y obtienen resultados distintos, la fórmula o las variables no están suﬁcientemente
especiﬁcadas; se debe revisar la ﬁcha.
Preguntas de Discusión
1. ¿Por qué es importante ﬁjar de antemano el rango deseado y no solo calcular el valor de
la métrica?
2. ¿Qué diferencia existe entre una métrica de Eﬁciencia y un simple cronómetro de tiempo
de respuesta del servidor?
34
Taller ISO/IEC 25022 — Calidad en Uso
Conclusiones Parciales
El estudiante ha traducido conceptos normativos abstractos en métricas formales, reprodu-
cibles y accionables, sentando las bases técnicas para la automatización que se abordará en los
siguientes escenarios.
ESCENARIO 7
Obtención de Datos
‰ Objetivo del Escenario
Identiﬁcar y generar las fuentes de datos necesarias (logs de aplicación, base de datos, en-
cuestas de satisfacción) para calcular las métricas diseñadas en el Escenario 6, preparando
los archivos que se automatizarán en el Escenario 8.
7.1
Parte 1 — Fundamento Teórico
7.1.1
Fuentes típicas de datos para Calidad en Uso
Tabla 7.1: Fuentes de datos según característica ISO/IEC 25022
Característica
Fuente típica de datos
Efectividad
Logs de aplicación (eventos de éxito/fracaso de tarea), base de datos
transaccional.
Eﬁciencia
Logs con marcas de tiempo (timestamps), trazas de Application Per-
formance Monitoring.
Satisfacción
Encuestas (SUS, CSAT, NPS), comentarios de soporte técnico.
Libertad de Riesgo
Registros de incidentes, logs de errores, auditorías de seguridad.
Cobertura de Contexto
Metadatos de sesión: sede, dispositivo, horario, tipo de red.
7.1.2
Calidad del dato antes que calidad del indicador
Un indicador construido sobre datos incompletos, duplicados o mal etiquetados produce
conclusiones erróneas, sin importar cuán correcta sea la fórmula ISO/IEC 25022 aplicada. Por
ello, este escenario dedica tiempo explícito a la limpieza y validación de datos antes de
automatizar nada.
7.2
Parte 2 — Actividad Práctica
35
36
Taller ISO/IEC 25022 — Calidad en Uso
Ficha de Laboratorio
Objetivo:
Generar y validar los conjuntos de datos base (logs
de HCE, encuestas de satisfacción, incidentes de fac-
turación) que alimentarán el cálculo automatizado de
métricas
Tiempo estimado:
3 horas
Nivel de dicultad:
Intermedio
Herramientas requeridas:
Python 3.11+, Jupyter Notebook, Pandas, DBeaver
(opcional), PostgreSQL o SQLite
Archivos / datos necesarios:
Scripts generadores provistos en este escenario
Paso 1: Generación del log simulado de registro de HCE
Crear el archivo scripts/generar_logs_hce.py:
1
"""
2
Genera un log sintetico de eventos de registro de notas de evolucion clinica
3
en el modulo HCE de MediSalud HIS, simulando 5 dias habiles y 5 sedes.
4
"""
5
import csv
6
import random
7
from datetime import datetime, timedelta
8
9
random.seed(42)
10
11
SEDES = ["Quito", "Guayaquil", "Cuenca", "Ambato", "Manta"]
12
MEDICOS_POR_SEDE = 12
13
FECHA_INICIO = datetime(2025, 11, 3, 7, 0, 0)
14
DIAS = 5
15
16
filas = []
17
evento_id = 1
18
19
for dia in range(DIAS):
20
fecha_dia = FECHA_INICIO + timedelta(days=dia)
21
for sede in SEDES:
22
# Mayor carga en Quito y Guayaquil (hospitales mas grandes)
23
n_eventos = 180 if sede in ("Quito", "Guayaquil") else 90
24
for _ in range(n_eventos):
25
hora = random.randint(7, 18)
26
minuto = random.randint(0, 59)
27
timestamp = fecha_dia.replace(hour=hora, minute=minuto)
28
29
# Simulamos que en horas pico (10-12h) el tiempo de registro sube
30
es_hora_pico = 10 <= hora <= 12
31
tiempo_base = random.gauss(6.5, 1.5)
32
if es_hora_pico:
33
tiempo_base += random.gauss(4.0, 2.0) # degradacion en pico
34
tiempo_segundos = max(1.5, round(tiempo_base, 2))
CAPÍTULO 7. OBTENCIÓN DE DATOS
37
35
36
# 96 % de las notas se completan correctamente
37
completada = random.random() < 0.96
38
39
medico_id = f"MED-{sede[:3].upper()}-{random.randint(1, MEDICOS_POR_SEDE):02d}"
40
41
filas.append({
42
"evento_id": evento_id,
43
"timestamp": timestamp.isoformat(),
44
"sede": sede,
45
"medico_id": medico_id,
46
"tiempo_segundos": tiempo_segundos,
47
"completada": int(completada),
48
})
49
evento_id += 1
50
51
with open("data/logs_hce.csv", "w", newline="", encoding="utf-8") as f:
52
writer = csv.DictWriter(f, fieldnames=filas[0].keys())
53
writer.writeheader()
54
writer.writerows(filas)
55
56
print(f"Se generaron {len(filas)} eventos en data/logs_hce.csv")
Listing 7.1: Generador de logs sintéticos de registro de HCE
Ejecutar:
1
python3 scripts/generar_logs_hce.py
2
head -5 data/logs_hce.csv
Listing 7.2: Ejecución del generador de logs
Paso 2: Generación de encuesta de satisfacción (CSAT)
Crear data/encuesta_satisfaccion.csv con columnas respuesta_id, sede, rol, puntaje_csat
(1-5), comentario. El docente puede proveer un dataset de 150 respuestas simuladas (dispo-
nible como material complementario del taller) o generarlo con un script análogo al anterior.
Paso 3: Validación de datos con Pandas
En Jupyter Notebook (scripts/01_validacion_datos.ipynb):
1
import pandas as pd
2
3
df = pd.read_csv("data/logs_hce.csv")
4
5
# 1. Verificar valores nulos
6
print("Valores nulos por columna:")
7
print(df.isnull().sum())
8
9
# 2. Verificar rangos logicos
10
print("\nTiempos fuera de rango (negativos o mayores a 120s):")
11
print(df[(df["tiempo_segundos"] < 0) | (df["tiempo_segundos"] > 120)])
38
Taller ISO/IEC 25022 — Calidad en Uso
12
13
# 3. Verificar duplicados
14
print("\nEventos duplicados:", df.duplicated(subset=["evento_id"]).sum())
15
16
# 4. Resumen descriptivo
17
print("\nResumen estadistico de tiempo_segundos:")
18
print(df["tiempo_segundos"].describe())
Listing 7.3: Validación básica de calidad del dato
8 Advertencia / Error Frecuente
Error frecuente: FileNotFoundError: data/logs_hce.csv.
Solución: veriﬁcar que el notebook o script se ejecuta desde la raíz del repositorio
(medisalud-calidad-uso/) y que la carpeta data/ existe (mkdir -p data).
3 Resultado Esperado
Al ﬁnalizar este escenario, el equipo dispone de al menos dos archivos CSV validados
(logs_hce.csv y encuesta_satisfaccion.csv), sin nulos, sin duplicados y con rangos
lógicos veriﬁcados, listos para ser procesados automáticamente.
Preguntas de Discusión
1. ¿Qué consecuencias tendría calcular la métrica de tiempo de tarea sin antes eliminar los
valores atípicos (outliers) causados por sesiones abandonadas?
2. ¿Por qué la fuente de datos de Satisfacción (encuestas) es cualitativamente distinta a la
de Eﬁciencia (logs)? ¿Qué implica esto para su frecuencia de recolección?
Conclusiones Parciales
El estudiante reconoce que la obtención de datos conﬁables es un prerrequisito técnico in-
eludible, y ha practicado técnicas básicas de validación de datos con Pandas, herramienta que
será la columna vertebral de la automatización en el Escenario 8.
ESCENARIO 8
Automatización de la Medición
‰ Objetivo del Escenario
Construir un pipeline en Python que calcule automáticamente las cinco métricas ISO/IEC
25022 del catálogo de MediSalud a partir de los datos validados en el Escenario 7, gene-
rando un archivo de indicadores reutilizable para los escenarios de visualización.
8.1
Parte 1 — Fundamento Teórico
8.1.1
¿Por qué automatizar?
Calcular métricas manualmente en una hoja de cálculo no escala: MediSalud requiere repor-
tes trimestrales y, eventualmente, continuos. La automatización garantiza reproducibilidad,
trazabilidad y la posibilidad de integrar la medición en un pipeline de Integración Continua /
Entrega Continua (CI/CD).
8.1.2
Arquitectura del pipeline de medición
Datos crudos
(CSV/logs)
Limpieza
Extract, Transform, Load (ETL) (Pandas)
Cálculo de
métricas ISO 25022
Indi
(JSO
Figura 8.1: Pipeline de automatización de la medición de Calidad en Uso
8.2
Parte 2 — Actividad Práctica
39
40
Taller ISO/IEC 25022 — Calidad en Uso
Ficha de Laboratorio
Objetivo:
Implementar en Python un módulo que calcule las mé-
tricas de Efectividad, Eﬁciencia, Satisfacción y Liber-
tad de Riesgo a partir de los datos generados en el
Escenario 7
Tiempo estimado:
4 horas
Nivel de dicultad:
Avanzado
Herramientas requeridas:
Python 3.11+, Pandas, NumPy, pytest (opcional para
pruebas unitarias)
Archivos / datos necesarios:
data/logs_hce.csv, data/encuesta_satisfaccion.csv,
data/incidentes_2025.csv
Paso 1: Módulo de cálculo de métricas
Crear scripts/metricas_iso25022.py:
1
"""
2
Modulo de calculo de metricas de Calidad en Uso (ISO/IEC 25022)
3
para el sistema MediSalud HIS.
4
5
Cada funcion retorna un diccionario con: valor, unidad, umbral y estado.
6
"""
7
import pandas as pd
8
9
10
UMBRAL_TIEMPO_TAREA = 8.0 # segundos, segun RNF-01
11
UMBRAL_TASA_ERROR_FACT = 0.01 # 1 %, segun RNF-03
12
UMBRAL_EFECTIVIDAD = 0.95 # 95 % de completitud esperada
13
14
15
def cargar_datos():
16
"""Carga los tres datasets base del programa de medicion."""
17
logs = pd.read_csv("data/logs_hce.csv")
18
encuesta = pd.read_csv("data/encuesta_satisfaccion.csv")
19
incidentes = pd.read_csv("data/incidentes_2025.csv")
20
return logs, encuesta, incidentes
21
22
23
def metrica_efectividad(logs: pd.DataFrame) -> dict:
24
"""
25
Efectividad = notas completadas correctamente / notas intentadas.
26
"""
27
total = len(logs)
28
completadas = logs["completada"].sum()
29
valor = round(completadas / total, 4) if total else 0.0
30
return {
31
"nombre": "Completitud de registro de HCE",
32
"caracteristica": "Efectividad",
33
"valor": valor,
CAPÍTULO 8. AUTOMATIZACIÓN DE LA MEDICIÓN
41
34
"unidad": "proporcion",
35
"umbral": UMBRAL_EFECTIVIDAD,
36
"cumple": valor >= UMBRAL_EFECTIVIDAD,
37
}
38
39
40
def metrica_eficiencia(logs: pd.DataFrame) -> dict:
41
"""
42
Eficiencia = tiempo promedio de registro de nota clinica (segundos).
43
"""
44
valor = round(logs["tiempo_segundos"].mean(), 2)
45
return {
46
"nombre": "Tiempo promedio de registro de HCE",
47
"caracteristica": "Eficiencia",
48
"valor": valor,
49
"unidad": "segundos",
50
"umbral": UMBRAL_TIEMPO_TAREA,
51
"cumple": valor <= UMBRAL_TIEMPO_TAREA,
52
}
53
54
55
def metrica_eficiencia_por_sede(logs: pd.DataFrame) -> pd.DataFrame:
56
"""Desagrega el tiempo promedio de tarea por sede (Cobertura de Contexto)."""
57
return (
58
logs.groupby("sede")["tiempo_segundos"]
59
.mean()
60
.round(2)
61
.reset_index()
62
.rename(columns={"tiempo_segundos": "tiempo_promedio_segundos"})
63
)
64
65
66
def metrica_satisfaccion(encuesta: pd.DataFrame) -> dict:
67
"""
68
Satisfaccion = promedio de puntaje CSAT (escala 1-5), normalizado a 0-1.
69
"""
70
promedio_csat = encuesta["puntaje_csat"].mean()
71
valor = round(promedio_csat / 5, 4)
72
return {
73
"nombre": "Indice de satisfaccion (CSAT normalizado)",
74
"caracteristica": "Satisfaccion",
75
"valor": valor,
76
"unidad": "proporcion (0-1)",
77
"umbral": 0.80,
78
"cumple": valor >= 0.80,
79
}
80
81
82
def metrica_libertad_riesgo(incidentes: pd.DataFrame, total_transacciones: int) -> dict:
83
"""
84
Libertad de Riesgo = tasa de incidentes de facturacion sobre el total
85
de transacciones de facturacion procesadas en el periodo.
42
Taller ISO/IEC 25022 — Calidad en Uso
86
"""
87
incidentes_facturacion = incidentes[incidentes["modulo"] == "Facturacion"]
88
valor = round(len(incidentes_facturacion) / total_transacciones, 4)
89
return {
90
"nombre": "Tasa de errores de facturacion",
91
"caracteristica": "Libertad de Riesgo",
92
"valor": valor,
93
"unidad": "proporcion",
94
"umbral": UMBRAL_TASA_ERROR_FACT,
95
"cumple": valor <= UMBRAL_TASA_ERROR_FACT,
96
}
97
98
99
def generar_reporte():
100
"""Orquesta el calculo de todas las metricas y consolida el resultado."""
101
logs, encuesta, incidentes = cargar_datos()
102
103
reporte = {
104
"efectividad": metrica_efectividad(logs),
105
"eficiencia": metrica_eficiencia(logs),
106
"satisfaccion": metrica_satisfaccion(encuesta),
107
# Se asume un total simulado de 8500 transacciones de facturacion
108
# en el periodo de medicion (dato provisto por el area financiera).
109
"libertad_riesgo": metrica_libertad_riesgo(incidentes, total_transacciones=8500),
110
}
111
112
eficiencia_sede = metrica_eficiencia_por_sede(logs)
113
114
return reporte, eficiencia_sede
115
116
117
if __name__ == "__main__":
118
reporte, eficiencia_sede = generar_reporte()
119
120
print("=== Reporte de Calidad en Uso - MediSalud HIS ===\n")
121
for clave, metrica in reporte.items():
122
estado = "CUMPLE" if metrica["cumple"] else "NO CUMPLE"
123
print(f"{metrica[’nombre’]}: {metrica[’valor’]} {metrica[’unidad’]} "
124
f"(umbral: {metrica[’umbral’]}) -> {estado}")
125
126
print("\n=== Eficiencia por sede (Cobertura de Contexto) ===")
127
print(eficiencia_sede.to_string(index=False))
Listing 8.1: Módulo de cálculo automatizado de métricas ISO/IEC 25022
Paso 2: Exportación de resultados a JSON
Añadir al ﬁnal del script anterior (o en un módulo separado scripts/exportar_reporte.py):
1
import json
2
from metricas_iso25022 import generar_reporte
3
4
reporte, eficiencia_sede = generar_reporte()
CAPÍTULO 8. AUTOMATIZACIÓN DE LA MEDICIÓN
43
5
6
salida = {
7
"metricas": reporte,
8
"eficiencia_por_sede": eficiencia_sede.to_dict(orient="records"),
9
}
10
11
with open("dashboards/indicadores.json", "w", encoding="utf-8") as f:
12
json.dump(salida, f, indent=2, ensure_ascii=False)
13
14
print("Reporte exportado a dashboards/indicadores.json")
Listing 8.2: Exportación de indicadores a JSON para consumo por dashboards
Paso 3: Automatización con GitHub Actions (integración continua de la me-
dición)
Crear .github/workflows/medicion_calidad.yml:
1
name: Medicion Calidad en Uso - MediSalud
2
3
on:
4
schedule:
5
- cron: "0 6 * * 1" # Cada lunes a las 06:00 UTC
6
workflow_dispatch: {}
7
8
jobs:
9
calcular-metricas:
10
runs-on: ubuntu-latest
11
steps:
12
- uses: actions/checkout@v4
13
- name: Configurar Python
14
uses: actions/setup-python@v5
15
with:
16
python-version: "3.11"
17
- name: Instalar dependencias
18
run: pip install pandas numpy
19
- name: Ejecutar calculo de metricas
20
run: python scripts/metricas_iso25022.py
21
- name: Exportar reporte JSON
22
run: python scripts/exportar_reporte.py
23
- name: Subir artefacto de indicadores
24
uses: actions/upload-artifact@v4
25
with:
26
name: indicadores-calidad-uso
27
path: dashboards/indicadores.json
Listing 8.3: Workﬂow de GitHub Actions para ejecutar la medición automáticamente
44
Taller ISO/IEC 25022 — Calidad en Uso
. Nota
Este ﬂujo convierte el programa de medición de Calidad en Uso en un proceso conti-
nuo y reproducible, ejecutado automáticamente cada semana sin intervención manual,
siguiendo el mismo principio que la integración continua aplica al código fuente.
Resolución de Problemas
Error ModuleNotFoundError: No module named ’pandas’ en GitHub Actions: veri-
ﬁcar que el paso Instalar dependencias se ejecuta antes del paso de cálculo, y que el nombre
del paquete coincide exactamente (pandas, no Pandas).
Error KeyError: ’modulo’ en metrica_libertad_riesgo: indica que el CSV de inci-
dentes no tiene la columna esperada; veriﬁcar el encabezado del archivo generado en el
Escenario 2.
El workow de GitHub Actions no se ejecuta con cron: GitHub puede retrasar
unos minutos la ejecución programada bajo carga alta; para pruebas, usar el disparador
manual workflow_dispatch.
n Recomendaciones
Es recomendable pedir a los estudiantes que además escriban una prueba unitaria simple
con pytest para metrica_eficiencia, veriﬁcando que el promedio se calcula correcta-
mente sobre un conjunto de datos controlado, reforzando así la relación entre pruebas de
software y conﬁabilidad de las métricas.
3 Resultado Esperado
Al ﬁnalizar este escenario, el equipo dispone de un pipeline Python ejecutable localmente
y en GitHub Actions, capaz de calcular las cuatro métricas principales y exportarlas en
formato JSON, listo para alimentar los dashboards del Escenario 9.
Preguntas de Discusión
1. ¿Qué ventajas ofrece programar la medición en GitHub Actions frente a ejecutarla ma-
nualmente cada trimestre?
2. ¿Qué riesgo existe si el umbral (UMBRAL_TIEMPO_TAREA) queda «hardcodeado» en el script
en lugar de estar en un archivo de conﬁguración externo?
Conclusiones Parciales
El estudiante ha automatizado por completo el cálculo de métricas de Calidad en Uso,
transformando fórmulas normativas en código ejecutable, reproducible e integrable en un ﬂujo
de integración continua, una competencia directamente transferible a un entorno profesional de
DevOps.
