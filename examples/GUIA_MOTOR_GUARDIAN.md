# 🛡️ GUÍA PRÁCTICA DEL MOTOR GUARDIÁN (CREATIVE GATEKEEPER V3.0)
### *De la Auditoría Anual a la Toma de Decisiones y Presupuestación Diaria*

---

## 🌟 ¿Qué es el Motor Guardián?

El **Arqueólogo Creativo (Motor 1)** se utiliza de forma periódica o anual para excavar en tu disco duro, diagnosticar cuellos de botella y rescatar activos abandonados.

El **Motor Guardián (Motor 2)** es el compañero operativo diario que nace de esa auditoría: un **comité deliberador en tiempo real** que evalúa cualquier propuesta, encargo o cliente potencial antes de que aceptes o fijes un precio, protegiendo tus tarifas mínimas, tu tiempo de proyectos propios y tu salud mental.

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        💎 FLUJO INTEGRADO DEL ECOSISTEMA                              │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 1. 🔍 AUDITORÍA FORENSE ➔ Extrae la "Constitución del Creador" (Límites & Tarifas)    │
│ 2. 📥 ENTRA UN LEAD     ➔ Pides al asistente IA / ejecutas `evaluate_lead.py`          │
│ 3. 🎙️ INTERROGATORIO   ➔ 3-4 preguntas rápidas de clarificación                        │
│ 4. ⚖️ TRIBUNAL GUARDIÁN ➔ 6 agentes deliberan (Carrera, Alcance, Red Flags, CFO, etc.)│
│ 5. 📦 ENTREGABLES       ➔ Dictamen GO/NO-GO + Presupuesto 3-Tier + Email al Cliente    │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 🛠️ Cómo Utilizar el Motor Guardián

### Opción A: Modo Asistente Interactivo con IA (Skill `/creative-gatekeeper`)
Cuando un cliente te escriba por email o WhatsApp, simplemente inicia una conversación con el asistente y di:
> *"Me acaba de llegar esta propuesta de [Nombre del Cliente]. Evalúala con el Motor Guardián."*

El asistente ejecutará el protocolo de 4 fases:
1. Lee tu `creator_constitution_template.json` o te pregunta tus tarifas base.
2. Te formulará de 3 a 4 preguntas incisivas sobre plazos, materiales y sensación de solvencia.
3. El tribunal de 6 agentes deliberará en directo.
4. Te devolverá el semáforo (**GO / GO CONDICIONADO / NO-GO**), la propuesta en 3 opciones de precio con el factor de fricción aplicado, las cláusulas anti-abuso y el email listo para copiar y enviar.

---

### Opción B: Modo CLI / Terminal Rápido (`evaluate_lead.py`)
Si quieres un cálculo inmediato y generar un informe y propuesta formal:

```bash
# Ejemplo: Evaluar un encargo de 25 horas estimadas con fricción estándar B2B (1.5x)
python scripts/evaluate_lead.py \
  --client "Productora Acme" \
  --project "Biblia de Animacion Serie TV" \
  --hours 30 \
  --friction 1.5 \
  --flags "urgencia_extrema" "sin_presupuesto_declarado" \
  --output "examples/EVALUACION_ACME.md"

# Compilar la propuesta a Word (.docx) maquetado
py scripts/generate_docx_report.py \
  --input "examples/EVALUACION_ACME.md" \
  --output "examples/PROPUESTA_ACME.docx" \
  --author "Tu Nombre"
```

---

## 📐 La Ecuación del Presupuesto Justo

$$\text{Presupuesto Base} = (\text{Horas Estimadas} \times \text{Factor de Fricción}) \times \text{Tarifa Suelo/h}$$

* **Fricción 1.0x (Cero Fricción):** Activos terminados o servicios muy estandarizados.
* **Fricción 1.5x (Fricción Media):** Servicios B2B con interlocutor profesional y briefing claro.
* **Fricción 2.0x (Fricción Alta):** Proyectos con dependencias externas, software experimental o comités múltiples.
* **Fricción 2.5x (Riesgo Crítico):** Clientes con burocracia pesada o dinámicas de microgestión.

---

## 🏷️ Estructura en 3 Opciones de Cotización (Anchor Pricing)

Nunca envíes un único precio cerrado que invite a regatear. El Motor Guardián estructura siempre 3 opciones psicológicas:

1. **Opción A (Esencial / Core - 75% del valor base):** Resuelve el problema básico sin extras, reuniones adicionales ni soporte extendido. (1 ronda de revisión).
2. **Opción B (Recomendada / Estándar - 100% del valor justo):** La solución completa con entregables garantizados y 2 rondas de corrección. *(Es la opción objetivo).*
3. **Opción C (VIP / Llave en Mano - 160% del valor base):** Entrega acelerada (Fast-Track), consultoría directa 1 a 1, cesión de derechos ampliada y soporte prioritario.

---

## 🛡️ Las 4 Cláusulas Anti-Abuso Obligatorias

1. **50% de Anticipo Previo:** No se inicia ningún trabajo ni se bloquea calendario sin confirmación bancaria.
2. **Máximo 2 Rondas de Revisión:** Todo cambio adicional se presupuesta a la tarifa de exceso de alcance (ej. 85€/h).
3. **SLA de Feedback (7 días):** Si el cliente tarda más de 7 días hábiles en responder, las fechas se reprograman según disponibilidad.
4. **Propiedad Intelectual:** La entrega de archivos finales o derechos se efectúa exclusivamente tras el pago del 100%.
