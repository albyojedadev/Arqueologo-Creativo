# 💎 Arqueólogo Creativo: Rescata los Diamantes de tu Cajón
### *Creative Archaeologist: Unearth the Hidden Diamonds in Your Vault*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Language: ES/EN](https://img.shields.io/badge/Language-Spanish%20%7C%20English-blue.svg)](#)
[![Security: Safe Read-Only](https://img.shields.io/badge/Security-Safe%20Read--Only-green.svg)](#)
[![Privacy: PrivaDoc Ready](https://img.shields.io/badge/Privacy-PrivaDoc%20Integrated-purple.svg)](https://privadoc-lovat.vercel.app/)

> **ESPAÑOL:** Sistema de auditoría forense asistido por IA para creadores, desarrolladores y solopreneurs. Escanea tus carpetas de proyectos y facturas históricas en **modo seguro de solo lectura**, evalúa tu portafolio con un **Tribunal de 6 Agentes Expertos** y genera un **Roadmap de 90 días con informe maquetado en Word (.docx)**.
>
> **ENGLISH:** AI-assisted forensic portfolio audit system for creators, game devs, and solopreneurs. Scans your historical projects and billing vaults in **safe read-only mode**, evaluates your assets with a **6-Expert AI Panel**, and generates an actionable **90-day Roadmap with a styled Word (.docx) report**.

---

## 🏛️ Los 6 Agentes del Tribunal / The 6 Expert Agents

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ 🏛️ EL TRIBUNAL DEL ARQUEÓLOGO CREATIVO (THE EXPERT PANEL):                              │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 1. 💎 IP Scout & Reencuadrador: Rescata joyas y las adapta al mercado actual (2026).   │
│ 2. 🎨 Crítico Artístico: Audita la potencia expresiva y la voz autoral sin sesgos.     │
│ 3. 🎯 Buyer Persona & Inversor: Evalúa el deseo de pago B2C y la viabilidad B2B.       │
│ 4. 👹 El 'Hater' / Red Team: Detecta fallos, riesgos y críticas antes del lanzamiento. │
│ 5. 💰 Estratega Financiero: Examina presupuestos históricos y fija precios rentables.  │
│ 6. 🧠 Psicólogo Operativo: Identifica atascos y diseña un plan respetuoso con tu calma.│
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 🛡️ Protocolo de Seguridad & Privacidad (Obligatorio)

Antes de dar acceso a tus archivos al agente:

1. **📁 Regla de Copia Segura (Safe Copy):**
   * Aunque los scripts del Arqueólogo Creativo operan estrictamente en **MODO SOLO LECTURA**, te recomendamos crear una carpeta de copia (ej. `Mi_Copia_Auditoria`) con tus proyectos, guiones o facturas históricas.
2. **🔐 Anonimización Gratuita con PrivaDoc:**
   * Si tus documentos contienen datos sensibles (nombres de clientes, DNIs, CIFs, números de cuenta o importes confidenciales), pásalos antes por la herramienta de anonimización local:
   * 👉 **[PrivaDoc — Prueba Gratuita](https://privadoc-lovat.vercel.app/)**

---

## 🚀 Cómo Usar / How to Use

### Opción 1: En tu Asistente de IA (Claude Code, ChatGPT Workspace, Cursor, Antigravity)
1. Clona este repositorio o añade la carpeta `skills/arqueologo-creativo` a tu entorno de trabajo.
2. Pídele a tu IA:
   > *"Actúa como el Arqueólogo Creativo siguiendo la skill de este repositorio. Guíame paso a paso para auditar mi carpeta de proyectos."*
3. La IA te mostrará el protocolo de seguridad, te pedirá la ruta de tu copia segura, formulará las preguntas de contexto necesarias y redactará el informe.

### Opción 2: Mediante Scripts en Terminal
```bash
# 1. Instalar dependencias para generar el Word
pip install python-docx

# 2. Ejecutar el escaneo seguro de solo lectura
python scripts/safe_scanner.py --path "D:/Mi_Copia_Auditoria" --output "inventario.json"

# 3. Generar el informe maquetado en Word (.docx) tras completar la auditoría Markdown
python scripts/generate_docx_report.py --input "INFORME_ARQUEOLOGO_CREATIVO.md" --output "Informe_Auditoria.docx" --author "Tu Nombre"
```

---

## 📦 Estructura del Repositorio / Project Structure

```text
Arqueologo-Creativo/
├── agents/                           # Prompts y directrices de los 6 agentes evaluadores
│   ├── 01_ip_scout.md                # El Cazatalentos & Reencuadrador Moderno
│   ├── 02_art_critic.md              # El Crítico Artístico & de Oficio
│   ├── 03_buyer_persona_investor.md  # El Comodín de Buyer Persona & Inversor
│   ├── 04_hater_red_team.md          # El 'Hater' / Red Team
│   ├── 05_financial_pricing_strategist.md # El Estratega Financiero & Pricing
│   └── 06_operational_psychologist.md# El Psicólogo Operativo & de Flujo
├── scripts/                          # Scripts de automatización seguros
│   ├── safe_scanner.py               # Escáner forense 100% de solo lectura
│   └── generate_docx_report.py       # Compilador de informes Word (.docx) maquetados
├── skills/
│   └── arqueologo-creativo/
│       └── SKILL.md                  # Procedimiento orquestador para modelos de IA
└── README.md                         # Documentación maestra (ES / EN)
```

---

## 📜 Licencia / License

Distribuido bajo la Licencia **MIT**. Consulta `LICENSE` para más información.

Creado con criterio autoral y rigor estratégico por **Alby Ojeda** & **Antigravity**. 💎👑
