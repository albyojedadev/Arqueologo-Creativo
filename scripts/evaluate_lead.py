#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Arqueólogo Creativo V3.0 - Motor Guardián Universal (evaluate_lead.py)
Evaluador automatizado de proyectos, cálculo de presupuesto en 3 niveles (Mínimo, Normal, Disuasorio),
detector de Paid Discovery y generador de contratos y licencias blindadas de IP.
"""

import os
import sys
import json
import argparse
from datetime import datetime

# Configure utf-8 output for Windows terminals
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

DEFAULT_CONSTITUTION = {
  "profile": {
    "name": "Creador Profesional",
    "creative_discipline": "Servicios Creativos y Tecnológicos",
    "core_specialty": "Desarrollo y Consultoría de Alto Valor",
    "monthly_target_revenue_eur": 4500,
    "max_concurrent_projects": 3,
    "protected_ip_time_percentage": 20
  },
  "industry_benchmarks": {
    "reference_entity_or_union": "Convenio / Baremo Oficial de Sector",
    "official_rates_link": ""
  },
  "financial_floors": {
    "baseline_hourly_rate_eur": 75,
    "minimum_project_ticket_eur": 1500,
    "paid_discovery_base_eur": 450,
    "out_of_scope_hourly_rate_eur": 85,
    "payment_milestones": {
      "milestone_1_upfront_pct": 30,
      "milestone_2_structure_pct": 40,
      "milestone_3_final_delivery_pct": 30
    }
  },
  "friction_multipliers": {
    "packaged_asset": 1.0,
    "standard_b2b": 1.5,
    "complex_experimental": 2.0,
    "heavy_bureaucracy": 2.5
  },
  "red_flags": [
    "es_algo_rapido_facil",
    "pago_en_visibilidad_o_promesas",
    "sin_presupuesto_declarado",
    "peticion_de_arquitectura_o_presupuesto_complejo_sin_paid_discovery",
    "urgencia_ficticia_con_feedback_lento",
    "dedicacion_completa_encubierta_baja",
    "rechazo_al_anticipo"
  ],
  "standard_clauses": {
    "max_review_rounds": 2,
    "client_feedback_sla_days": 7,
    "ip_transfer_condition": "100% pago recibido y liquidado",
    "kill_fee_applicable": True
  }
}

def load_constitution(filepath=None):
    if filepath and os.path.exists(filepath):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"[!] Error leyendo constitución de {filepath}: {e}. Usando valores por defecto.")
    
    # Try default template locations
    candidates = [
        os.path.join(os.path.dirname(__file__), "..", "templates", "creator_constitution_template.json"),
        os.path.join(os.path.dirname(__file__), "..", "DOCS", "creator_constitution_alby.json")
    ]
    for cand in candidates:
        if os.path.exists(cand):
            try:
                with open(cand, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception:
                pass
            
    return DEFAULT_CONSTITUTION

def calculate_verdict(raw_hours, friction_factor, hourly_rate, min_ticket, flags_count, is_discovery=False, client_budget=None):
    base_hours_adjusted = raw_hours * friction_factor
    base_cost = max(base_hours_adjusted * hourly_rate, min_ticket)
    
    # 3-Tier Strategic Triad
    tier_1_minimo = round(base_cost * 0.75, -1)
    tier_2_normal = round(base_cost, -1)
    tier_3_disuasorio = round(base_cost * 1.8, -1)  # F*ck You Price / VIP
    
    # Risk & Quality Score (0 to 100)
    score = 100
    score -= (flags_count * 20)
    if friction_factor >= 2.0:
        score -= 15
    if client_budget and client_budget < tier_1_minimo:
        score -= 30
        
    score = max(0, min(100, score))
    
    if score >= 75 and flags_count == 0:
        verdict = "GO (Aprobado)"
        verdict_code = "GO"
    elif score >= 45 and flags_count <= 2:
        verdict = "GO CONDICIONADO (Aprobado con Blindaje Estricto)"
        verdict_code = "CONDITIONAL_GO"
    else:
        verdict = "NO-GO (Rechazo Elegante o Tarifa Disuasoria)"
        verdict_code = "NO_GO"
        
    return {
        "verdict": verdict,
        "verdict_code": verdict_code,
        "score": score,
        "raw_hours": raw_hours,
        "friction_factor": friction_factor,
        "adjusted_hours": base_hours_adjusted,
        "hourly_rate": hourly_rate,
        "is_discovery": is_discovery,
        "tier_1_minimo": tier_1_minimo,
        "tier_2_normal": tier_2_normal,
        "tier_3_disuasorio": tier_3_disuasorio
    }

def generate_evaluation_markdown(client_name, project_title, evaluation, constitution, detected_flags, benchmark_info="", notes=""):
    floors = constitution.get("financial_floors", {})
    clauses = constitution.get("standard_clauses", {})
    milestones = floors.get("payment_milestones", {"milestone_1_upfront_pct": 30, "milestone_2_structure_pct": 40, "milestone_3_final_delivery_pct": 30})
    
    emoji = "🟢" if evaluation["verdict_code"] == "GO" else ("🟡" if evaluation["verdict_code"] == "CONDITIONAL_GO" else "🔴")
    
    md = f"""# {emoji} DICTAMEN DE EVALUACIÓN & PROPUESTA BLINDADA: {project_title.upper()}
### *Motor Guardián V3.0 — Sistema Universal de Evaluación de Proyectos*
**Fecha de Evaluación:** {datetime.now().strftime('%Y-%m-%d %H:%M')}  
**Cliente / Prospecto:** {client_name}  

---

## 📊 1. FICHA TÉCNICA DEL DICTAMEN

| Parámetro | Valor Evaluado | Referencia Constitución |
| :--- | :---: | :--- |
| **Veredicto Final** | **{emoji} {evaluation['verdict']}** | Criterio de Viabilidad y Fricción |
| **Puntuación de Seguridad** | **{evaluation['score']} / 100** | Umbral Mínimo de Aceptación: 45/100 |
| **Horas Base Estimadas** | {evaluation['raw_hours']} horas | Estimación en bruto |
| **Multiplicador de Fricción** | **{evaluation['friction_factor']}x** | Compensación Falacia de Planificación |
| **Horas Ajustadas Reales** | **{evaluation['adjusted_hours']:.1f} horas** | Carga operativa real |
| **Tarifa Suelo Aplicada** | {evaluation['hourly_rate']} €/h | Suelo no negociable |
| **Red Flags Detectadas** | {len(detected_flags)} señales | Límite crítico: $\\ge 3$ señales |

"""
    if detected_flags:
        md += "### 🚩 Señales de Alerta Detectadas:\n\n"
        for flag in detected_flags:
            md += f"* ⚠️ **{flag}**\n"
        md += "\n"

    if benchmark_info:
        md += f"### 🏛️ Anclaje en Convenio / Baremo Oficial:\n{benchmark_info}\n\n"

    if evaluation["is_discovery"]:
        md += f"""### 🔬 RECOMENDACIÓN DE PAID DISCOVERY ACTIVADA:
> ⚠️ **Este proyecto requiere análisis o investigación técnica previa.** Se recomienda NO cotizar la producción completa a ciegas. Envíese en primer lugar la propuesta del **Informe de Paid Discovery / Diagnóstico de Viabilidad ({floors.get('paid_discovery_base_eur', 450)}€ – 750€)**.

"""

    if notes:
        md += f"### 📝 Notas de Contexto:\n{notes}\n\n"

    md += f"""---

## 🏷️ 2. ESTRUCTURA DE PRESUPUESTO EN 3 NIVELES (ANCHOR PRICING)

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ 💰 LA HORQUILLA DE COTIZACIÓN ESTRATÉGICA                                              │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 1. OPCIÓN A (MÍNIMO / ESENCIAL):       {evaluation['tier_1_minimo']:,.0f} € + IVA                             │
│    • Alcance núcleo indispensable. Sin reuniones de asesoría extra.                    │
│    • 1 ronda de revisión incluida.                                                     │
│                                                                                        │
│ 2. OPCIÓN B (NORMAL / RECOMENDADA):    {evaluation['tier_2_normal']:,.0f} € + IVA  ⭐️ OBJETIVO               │
│    • Solución completa con entregables atómicos garantizados y alta calidad.           │
│    • 2 rondas de feedback estructuradas. Soporte continuo durante el hito.             │
│                                                                                        │
│ 3. OPCIÓN C (DISUASORIO / VIP):        {evaluation['tier_3_disuasorio']:,.0f} € + IVA  (F*CK YOU PRICE)          │
│    • Entrega Fast-Track prioritaria, consultoría 1 a 1 y cesión ampliada.              │
│    • Tarifa disuasoria: si el cliente acepta, compensa con creces cualquier molestia. │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 🛡️ 3. TÉRMINOS Y CLÁUSULAS ANTI-ABUSO OBLIGATORIAS

1. **Estructura de Pagos por Hitos:**
   * **{milestones.get('milestone_1_upfront_pct', 30)}% Anticipo de Reserva:** Para bloquear fechas en agenda e iniciar trabajos.
   * **{milestones.get('milestone_2_structure_pct', 40)}% Hito Estructural:** A la entrega del primer borrador/escaleta/arquitectura.
   * **{milestones.get('milestone_3_final_delivery_pct', 30)}% Entrega Final:** A la entrega del documento terminado con correcciones.
2. **Límite de Revisiones:** Máximo **{clauses.get('max_review_rounds', 2)} rondas de correcciones** dentro del alcance acordado. Revisiones adicionales a **{floors.get('out_of_scope_hourly_rate_eur', 85)} €/h**.
3. **SLA de Feedback del Cliente:** Máximo **{clauses.get('client_feedback_sla_days', 7)} días hábiles** para enviar correcciones. Demoras reprograman el calendario.
4. **🔒 Cláusula de Retención Legal de Propiedad Intelectual:**
   > *"La licencia de uso y los derechos de explotación comercial quedan formalmente retenidos por el autor y NO se transmiten al cliente hasta el abono íntegro del 100% de la factura."*

---

## ✉️ 4. PLANTILLA DE EMAIL / RESPUESTA COMERCIAL ASERTIVA

> **Asunto:** Propuesta de trabajo y opciones de colaboración — {project_title}  
>
> Hola {client_name},
>
> Gracias por ponerte en contacto y por los detalles de **{project_title}**. He analizado los requerimientos y objetivos del encargo para asegurar un estándar de ejecución riguroso.
>
> Para que podáis elegir el alcance que mejor se ajuste a vuestros plazos e inversión, he estructurado **3 modalidades de colaboración cerradas**:
>
> * **Opción A (Esencial - {evaluation['tier_1_minimo']:,.0f}€ + IVA):** Enfoque directo en la solución base indispensable con 1 ronda de revisión.
> * **Opción B (Recomendada / Completa - {evaluation['tier_2_normal']:,.0f}€ + IVA):** Desarrollo integral estándar de inicio a fin con entregables garantizados y 2 rondas de feedback.
> * **Opción C (Fast-Track Prioritario - {evaluation['tier_3_disuasorio']:,.0f}€ + IVA):** Entrega urgente llave en mano con soporte prioritario y asesoría directa.
>
> En todas las opciones trabajamos con un anticipo inicial para fijar las fechas en calendario y garantizar la entrega en plazo.
>
> ¿Qué opción encaja mejor con lo que tenéis previsto para formalizar el calendario y arrancar?
>
> Un cordial saludo,  
> **{constitution.get('profile', {}).get('name', 'Tu Nombre')}**
"""
    return md

def generate_contract_markdown(client_name, project_title, evaluation, constitution):
    floors = constitution.get("financial_floors", {})
    clauses = constitution.get("standard_clauses", {})
    milestones = floors.get("payment_milestones", {"milestone_1_upfront_pct": 30, "milestone_2_structure_pct": 40, "milestone_3_final_delivery_pct": 30})
    creator_name = constitution.get("profile", {}).get("name", "El Prestador")
    
    tier_2 = evaluation['tier_2_normal']
    h1 = tier_2 * (milestones.get('milestone_1_upfront_pct', 30) / 100.0)
    h2 = tier_2 * (milestones.get('milestone_2_structure_pct', 40) / 100.0)
    h3 = tier_2 * (milestones.get('milestone_3_final_delivery_pct', 30) / 100.0)
    
    contract = f"""# 📑 ACUERDO DE ENCARGO, PRESTACIÓN DE SERVICIOS Y LICENCIA DE DERECHOS
### *Contrato de Blindaje Profesional — Motor Guardián V3.0*

**Fecha de Emisión:** {datetime.now().strftime('%d de %B de %Y')}  
**De una parte (El Creador/Prestador):** {creator_name}  
**De otra parte (El Cliente):** {client_name}  
**Objeto del Encargo:** {project_title}  

---

## 1. OBJETO Y ENTREGABLES ACORDADOS
El Prestador se compromete a realizar y entregar los servicios y materiales correspondientes al proyecto **{project_title}**, de acuerdo con las especificaciones técnicas pactadas en la propuesta comercial.

---

## 2. PRECIO Y CONDICIONES DE PAGO ESCALONADO
El importe total acordado para el encargo es de **{tier_2:,.2f} € + IVA**, desglosado en los siguientes hitos de facturación:

1. **Hito 1 (Anticipo de Reserva - {milestones.get('milestone_1_upfront_pct', 30)}%):** **{h1:,.2f} € + IVA**, pagaderos a la firma del presente documento antes de iniciar los trabajos.
2. **Hito 2 (Entrega Estructural - {milestones.get('milestone_2_structure_pct', 40)}%):** **{h2:,.2f} € + IVA**, pagaderos a la entrega del primer borrador, arquitectura o escaleta.
3. **Hito 3 (Entrega Final - {milestones.get('milestone_3_final_delivery_pct', 30)}%):** **{h3:,.2f} € + IVA**, pagaderos a la entrega del documento/material final con revisiones.

---

## 3. LÍMITE DE REVISIONES Y EXCESO DE ALCANCE
* Se incluyen un máximo de **{clauses.get('max_review_rounds', 2)} rondas de correcciones** dentro del alcance original acordado.
* Cualquier modificación sustancial, cambio de dirección sobre material ya aprobado o peticiones posteriores a la 2ª ronda se presupuestarán por separado a razón de **{floors.get('out_of_scope_hourly_rate_eur', 85)} €/hora + IVA**.

---

## 4. TIEMPO DE RESPUESTA DEL CLIENTE (SLA)
* El Cliente dispone de un plazo máximo de **{clauses.get('client_feedback_sla_days', 7)} días hábiles** tras cada entrega para remitir sus observaciones de forma unificada.
* En caso de no recibirse feedback en dicho plazo, la entrega se considerará aprobada a todos los efectos y las fechas del siguiente hito se reprogramarán según disponibilidad del Prestador.

---

## 5. 🔒 CLÁUSULA DE RETENCIÓN DE PROPIEDAD INTELECTUAL
1. **Titularidad Original:** El Prestador conserva la autoría moral e intelectual de todas las obras, código, textos y metodologías desarrolladas.
2. **Condición Suspensiva de Licencia:** La transmisión de la licencia de uso y los derechos de explotación comercial queda expresamente **condicionada al pago íntegro del 100% de la contraprestación económica pactada**.
3. **Prohibición de Explotación Previa:** Queda terminantemente prohibida la publicación, estreno, integración o explotación comercial de los materiales entregados mientras exista saldo pendiente de cobro.

---

## 6. CANCELACIÓN ANTICIPADA (KILL FEE)
En caso de desistimiento o cancelación unilateral del proyecto por parte del Cliente, los importes correspondientes a los hitos ya devengados o iniciados no serán reembolsables, liquidándose el trabajo proporcional efectuado hasta la fecha de notificación.

---

**Firmado en prueba de conformidad:**

```text
Por el Prestador:                            Por el Cliente:
Fdo: {creator_name}                          Fdo: {client_name}
```
"""
    return contract

def save_to_history(entry, history_file):
    history = []
    if os.path.exists(history_file):
        try:
            with open(history_file, 'r', encoding='utf-8') as f:
                history = json.load(f)
        except Exception:
            history = []
            
    history.append(entry)
    os.makedirs(os.path.dirname(os.path.abspath(history_file)), exist_ok=True)
    with open(history_file, 'w', encoding='utf-8') as f:
        json.dump(history, f, indent=2, ensure_ascii=False)

def main():
    parser = argparse.ArgumentParser(description="Arqueólogo Creativo V3.0 - Motor Guardián Universal")
    parser.add_argument("--client", default="Cliente Prospecto", help="Nombre del cliente")
    parser.add_argument("--project", default="Nuevo Encargo Creativo", help="Título o descripción del proyecto")
    parser.add_argument("--hours", type=float, default=20.0, help="Horas estimadas en bruto")
    parser.add_argument("--friction", type=float, default=1.5, help="Multiplicador de fricción (1.0, 1.5, 2.0, 2.5)")
    parser.add_argument("--budget", type=float, default=None, help="Presupuesto sugerido por el cliente")
    parser.add_argument("--discovery", action="store_true", help="Marcar si el encargo requiere Paid Discovery previo")
    parser.add_argument("--flags", nargs="*", default=[], help="Lista de red flags detectadas")
    parser.add_argument("--benchmark", default="", help="Información o enlace a convenio/baremo oficial")
    parser.add_argument("--notes", default="", help="Notas adicionales de contexto")
    parser.add_argument("--constitution", default=None, help="Ruta al archivo creator_constitution.json")
    parser.add_argument("--contract", action="store_true", help="Generar contrato formal blindado además de la propuesta")
    parser.add_argument("--output", default=None, help="Ruta del archivo Markdown de salida")
    
    args = parser.parse_args()
    
    constitution = load_constitution(args.constitution)
    floors = constitution.get("financial_floors", {})
    hourly_rate = floors.get("baseline_hourly_rate_eur", 75)
    min_ticket = floors.get("minimum_project_ticket_eur", 1500)
    
    evaluation = calculate_verdict(
        raw_hours=args.hours,
        friction_factor=args.friction,
        hourly_rate=hourly_rate,
        min_ticket=min_ticket,
        flags_count=len(args.flags),
        is_discovery=args.discovery,
        client_budget=args.budget
    )
    
    md_content = generate_evaluation_markdown(
        client_name=args.client,
        project_title=args.project,
        evaluation=evaluation,
        constitution=constitution,
        detected_flags=args.flags,
        benchmark_info=args.benchmark,
        notes=args.notes
    )
    
    sanitized_title = "".join(c for c in args.project if c.isalnum() or c in (' ', '_', '-')).rstrip().replace(" ", "_")
    output_path = args.output or f"DOCS/EVALUACION_{sanitized_title}.md"
    
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(md_content)
        
    contract_path = None
    if args.contract:
        contract_md = generate_contract_markdown(args.client, args.project, evaluation, constitution)
        contract_path = f"DOCS/CONTRATO_{sanitized_title}.md"
        with open(contract_path, 'w', encoding='utf-8') as f:
            f.write(contract_md)
        
    # Save to history log
    history_file = os.path.join(os.path.dirname(__file__), "..", "DOCS", "leads_history.json")
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "client": args.client,
        "project": args.project,
        "verdict": evaluation["verdict_code"],
        "score": evaluation["score"],
        "tier_2_eur": evaluation["tier_2_normal"],
        "flags": args.flags,
        "contract_generated": bool(args.contract)
    }
    save_to_history(log_entry, history_file)
    
    print(f"[✓] Evaluación completada con éxito.")
    print(f"    • Veredicto: {evaluation['verdict']}")
    print(f"    • Puntuación: {evaluation['score']}/100")
    print(f"    • Propuesta Recomendada: {evaluation['tier_2_normal']:,.0f} € + IVA")
    print(f"    • Propuesta Disuasoria / VIP: {evaluation['tier_3_disuasorio']:,.0f} € + IVA")
    print(f"    • Documento de Evaluación: {output_path}")
    if contract_path:
        print(f"    • Contrato Blindado Generado: {contract_path}")

if __name__ == "__main__":
    main()
