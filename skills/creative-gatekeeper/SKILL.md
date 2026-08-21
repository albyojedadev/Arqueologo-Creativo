---
name: creative-gatekeeper
description: "Motor Guardián y Evaluador de Proyectos V3.0: Sistema de deliberación en tiempo real para evaluar nuevos clientes y propuestas. Aplica suelos de tarifas, multiplicadores de fricción, detector de red flags, propuesta comercial en 3 niveles y email de respuesta blindado."
author: "Alby Ojeda & Antigravity"
version: "3.0.0"
language: "es / en"
---

# 🛡️ SKILL: MOTOR GUARDIÁN Y EVALUADOR DE PROYECTOS (CREATIVE GATEKEEPER V3.0)
### *Filtro de Clientes, Blindaje de Tarifas y Generación de Presupuestos*

Este procedimiento define el flujo de trabajo interactivo para evaluar cualquier oportunidad comercial, solicitud de presupuesto o lead de cliente, aplicando la **Constitución del Creador** generada en la auditoría del Arqueólogo Creativo.

---

## 🎯 OBJETIVO Y CUÁNDO INVOCAR ESTA SKILL
Invoca esta skill cuando el usuario reciba:
* Un email, mensaje directo o llamada solicitando presupuesto o colaboración.
* Una propuesta de un cliente existente o nuevo.
* Una idea de nuevo servicio o encargo y dude si aceptarlo o cuánto cobrar.

---

## 🧭 FLUJO DE TRABAJO EN 4 FASES

### 📥 FASE 1: INGESTA DEL LEAD & CARGA DE CONSTITUCIÓN
1. **Cargar Límites del Usuario:** Verificar si existe `templates/creator_constitution_template.json` o un archivo de constitución personalizado en el proyecto. Si no existe, aplicar los valores por defecto (suelo 75€/h, ticket mínimo 1.500€, anticipo 50%, fricción 1.5x).
2. **Recepción del Lead:** Solicitar al usuario que pegue el texto del mensaje del cliente, el briefing o las notas de la reunión.

---

### 🎙️ FASE 2: INTERROGATORIO DE CLARIFICACIÓN (3-4 PREGUNTAS CLAVE)
El asistente formula de 3 a 4 preguntas rápidas y directas al usuario para diagnosticar el contexto:
1. *«¿Qué plazos o fecha de entrega solicita el cliente?»*
2. *«¿Quién aporta los materiales base (textos, referencias, accesos) o hay que crearlos desde cero?»*
3. *«¿Qué nivel de solvencia, urgencia o autoridad te ha transmitido en la comunicación inicial?»*
4. *«¿Cuántas horas estimas que te llevaría si todo saliera perfecto?»*

---

### ⚖️ FASE 3: DELIBERACIÓN DEL TRIBUNAL GUARDIÁN (6 AGENTES)

El tribunal analiza la propuesta bajo sus directrices operativas:

1. 🧭 **IP & Career Scout (`agents/gatekeeper/01_career_alignment_scout.md`):** Evalúa el valor de portfolio, retención de crédito o derechos y coste de oportunidad sobre proyectos propios.
2. 📐 **Craft & Scope Architect (`agents/gatekeeper/02_craft_scope_architect.md`):** Traduce el encargo en entregables atómicos y detecta bloqueadores técnicos.
3. 🔍 **Client Red Flag Profiler (`agents/gatekeeper/03_client_redflag_profiler.md`):** Escanea frases trampa (*"es rápido", "dará visibilidad"*) y perfil de riesgo.
4. 👹 **Scope Creep Red Team (`agents/gatekeeper/04_scope_creep_red_team.md`):** Identifica riesgos de horas no pagadas e impone el límite de 2 revisiones y penalizaciones por demora.
5. 💰 **Financial CFO (`agents/gatekeeper/05_cfo_pricing_guardian.md`):** Aplica la fórmula de precio con factor de fricción:
   $$\text{Precio Base} = (\text{Horas Estimadas} \times \text{Factor de Fricción [1.5x - 2.5x]}) \times \text{Tarifa Suelo/h}$$
   Y estructura la propuesta en **3 Niveles Psicológicos (Tier 1 Esencial, Tier 2 Recomendado, Tier 3 VIP)**.
6. 🧠 **Operational Psychologist (`agents/gatekeeper/06_operational_psychologist_gatekeeper.md`):** Emite el **Veredicto Final Vinculante (GO / GO CONDICIONADO / NO-GO)** y redacta la respuesta formal.

---

### 📦 FASE 4: ENTREGA DEL DICTAMEN Y PROPUESTA COMERCIAL

El asistente entrega al usuario un documento estructurado con:

1. **📊 Ficha de Decisión & Scoring (0 a 100):**
   * Semáforo y Veredicto (`GO` / `GO CONDICIONADO` / `NO-GO`).
   * Desglose de Red Flags y Green Flags detectadas.
2. **🏷️ Propuesta de Presupuesto Blindado en 3 Niveles:**
   * **Opción A (Esencial):** Alcance reducido, sin extras ni revisiones extendidas.
   * **Opción B (Recomendada / Estándar de Oro):** Solución integral, precio justo con factor de fricción y 2 rondas de feedback.
   * **Opción C (VIP / Llave en Mano):** Entrega urgente, consultoría directa y soporte prioritario.
3. **🛡️ Cláusulas Anti-Fricción Incluidas:**
   * 50% de anticipo para iniciar.
   * Máximo 2 rondas de revisión (extras a tarifa de exceso de alcance).
   * SLA de 7 días de feedback del cliente o reprogramación de fechas.
   * Cesión de derechos sujeta al pago del 100%.
4. **✉️ Email de Respuesta para el Cliente:**
   * Redactado en tono profesional, asertivo y de alta autoridad, listo para copiar y enviar.
5. **🗂️ Registro Opcional:**
   * Guardar la decisión en `DOCS/leads_history.json` para análisis retrospectivo en la próxima auditoría anual.
