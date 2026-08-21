# 💎 Arqueólogo Creativo & Motor Guardián (V3.0)
## *Creative Archaeologist & Gatekeeper: Forensic Audit & Project Evaluation System*

![License](https://img.shields.io/badge/License-MIT-blue.svg)
![Version](https://img.shields.io/badge/Version-3.0.0-gold.svg)
![Security](https://img.shields.io/badge/Security-Read--Only-green.svg)
![Privacy](https://img.shields.io/badge/Privacy-PrivaDoc%20Integrated-success.svg)

---

### 🇪🇸 ESPAÑOL: DESCRIPCIÓN DEL ECOSISTEMA DUAL

**Arqueólogo Creativo V3.0** es un sistema operativo integral de estrategia, asignación de recursos y blindaje profesional para creadores (guionistas, diseñadores narrativos, desarrolladores de software/videojuegos, ilustradores y consultores).

El framework opera mediante **2 motores complementarios**:

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                     💎 ECOSISTEMA ARQUEÓLOGO CREATIVO V3.0                            │
├────────────────────────────────────────┬───────────────────────────────────────────────┤
│ 🔍 MOTOR 1: AUDIT ENGINE (Periódico)   │ 🛡️ MOTOR 2: GATEKEEPER ENGINE (Diario/Semanal)│
├────────────────────────────────────────┼───────────────────────────────────────────────┤
│ • Escaneo forense de disco y metadatos.│ • Ingesta y análisis de nuevos leads/briefs.  │
│ • Diagnóstico DAFO y embudo de activos.│ • Tribunal Guardián de 6 agentes en directo.  │
│ • Rescate de diamantes inconclusos.    │ • Detección de Red Flags y Scope Creep.       │
│ • Índice IE con Factor de Fricción.    │ • Presupuestos 3-Tier (Anchor Pricing).       │
│ ────────────────────────────────────── │ ───────────────────────────────────────────── │
│ 📄 OUTPUT: Constitución del Creador    │ 📄 OUTPUT: Dictamen GO/NO-GO + Propuesta      │
│   (`CREATOR_CONSTITUTION.md / .json`)  │   blindada en Word (.docx) e email asertivo.  │
└────────────────────────────────────────┴───────────────────────────────────────────────┘
```

---

### 🏛️ 1. LOS TRIBUNALES AUDITORES (6 AGENTES EN CADA MOTOR)

| Rol del Agente | 🔍 Motor 1: Arqueólogo (Auditoría Forense) | 🛡️ Motor 2: Guardián (Evaluador de Leads) |
|---|---|---|
| **01. Scout** | Oportunidad de mercado, adaptabilidad e IP. | Alineación de carrera, valor de portfolio y coste de oportunidad. |
| **02. Architect** | Calidad de oficio, voz autoral y originalidad. | Viabilidad técnica, entregables atómicos y claridad del brief. |
| **03. Profiler** | Disposición de pago real (B2C vs B2B). | Detección de Red Flags lingüísticas y solvencia del cliente. |
| **04. Red Team** | Antítesis crítica, costes ocultos y saturación. | Cazador de Scope Creep, cláusula de 2 revisiones y SLAs. |
| **05. CFO** | Facturación histórica y ratio de eficiencia (IE). | Pricing con factor de fricción y propuesta 3-Tier (Esencial, Recomendada, VIP). |
| **06. Psychologist** | Síntesis operativa y roadmap atómico de 90 días. | Veredicto vinculante (GO / CONDITIONAL / NO-GO) y email asertivo. |

---

### 📐 2. FÓRMULA DE PRICING CON FACTOR DE FRICCIÓN

$$\text{Presupuesto Base} = (\text{Horas Estimadas} \times \text{Factor de Fricción}) \times \text{Tarifa Suelo/h}$$

* **$1.0\times$ (Cero Fricción):** Activos terminados o servicios estandarizados.
* **$1.5\times$ (Fricción Media):** Servicios B2B con interlocutor único y requisitos claros.
* **$2.0\times$ (Fricción Alta):** Software, videojuegos o proyectos con integraciones complejas.
* **$2.5\times$ (Riesgo Crítico):** Clientes con burocracia pesada o dinámicas de microgestión.

---

### 🚀 3. INSTALACIÓN Y USO RÁPIDO

```bash
# 1. Clonar el repositorio
git clone https://github.com/albyojedadev/Arqueologo-Creativo.git
cd Arqueologo-Creativo

# 2. Instalar dependencias
pip install python-docx

# ----------------------------------------------------
# 🔍 MOTOR 1: AUDITORÍA FORENSE (Modo Arqueólogo)
# ----------------------------------------------------
# Escaneo de metadatos ligero
python scripts/safe_scanner.py --path "C:/Ruta/A/Tu/Copia_Auditoria" --output "inventario.json"

# Compilar informe maestro en Word
py scripts/generate_docx_report.py --input "DOCS/00_INFORME_MAESTRO_ARQUEOLOGO_V2_5.md" --output "INFORME_MAESTRO.docx" --author "Tu Nombre"

# ----------------------------------------------------
# 🛡️ MOTOR 2: EVALUACIÓN DE PROYECTO (Modo Guardián)
# ----------------------------------------------------
# Evaluar un nuevo encargo y generar dictamen + propuesta
python scripts/evaluate_lead.py \
  --client "Estudio Nexus" \
  --project "Guion Cortometraje Animacion" \
  --hours 25 \
  --friction 1.5 \
  --flags "urgencia_extrema" "sin_presupuesto_declarado" \
  --output "DOCS/EVALUACION_NEXUS.md"

# Compilar propuesta comercial maquetada en Word
py scripts/generate_docx_report.py --input "DOCS/EVALUACION_NEXUS.md" --output "DOCS/PROPUESTA_NEXUS.docx" --author "Tu Nombre"
```

---

### 🛡️ 4. PROTOCOLO DE SEGURIDAD Y PRIVACIDAD

1. **🔒 MODO SOLO LECTURA:** Los scripts jamás modifican ni eliminan archivos de tu disco.
2. **📁 REGLA DE COPIA SEGURA:** Trabaja siempre sobre una carpeta de copia (ej. `Mi_Copia_Auditoria`).
3. **🔐 ANONIMIZACIÓN CON PRIVADOC:** Para procesar contratos o facturas sensibles de forma 100% local en tu navegador antes de la auditoría:
   👉 **[PrivaDoc (Prueba Gratis)](https://privadoc-lovat.vercel.app/)**

---

### 🇬🇧 ENGLISH SUMMARY (V3.0)

**Creative Archaeologist & Gatekeeper V3.0** is a dual-engine operating system for creative professionals. 
* **Engine 1 (Audit Mode):** Runs read-only forensic disk scans, calculates Friction-Adjusted Economic Efficiency (IE), generates asset funnels and 48-hour binary experiments.
* **Engine 2 (Gatekeeper Mode):** Evaluates real-time incoming leads, detects client red flags, enforces financial floors, calculates friction-adjusted quotes, and generates 3-tier proposals and ready-to-send assertive emails.

---

### 📜 LICENCIA / LICENSE
Distribuido bajo Licencia MIT. Creado por **Alby Ojeda** & **Antigravity**.
