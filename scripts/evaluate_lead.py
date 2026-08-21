#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Arqueólogo Creativo V3.0 - Motor Guardián (evaluate_lead.py)
Evaluador automatizado de proyectos, cálculo de presupuesto con fricción y generador de propuestas blindadas.
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
        "core_specialty": "Desarrollo y Diseño Creativo",
        "monthly_target_revenue_eur": 5000,
        "max_concurrent_projects": 3
    },
    "financial_floors": {
        "baseline_hourly_rate_eur": 75,
        "minimum_project_ticket_eur": 1500,
        "upfront_retainer_percentage": 50,
        "out_of_scope_hourly_rate_eur": 85
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
        "urgencia_extrema_sin_recargo",
        "multiples_decisores_sin_consenso",
        "rechazo_al_anticipo"
    ],
    "standard_clauses": {
        "max_review_rounds": 2,
        "client_feedback_sla_days": 7,
        "ip_transfer_condition": "100% pago recibido",
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
    
    # Try default template location
    template_path = os.path.join(os.path.dirname(__file__), "..", "templates", "creator_constitution_template.json")
    if os.path.exists(template_path):
        try:
            with open(template_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            pass
            
    return DEFAULT_CONSTITUTION

def calculate_verdict(raw_hours, friction_factor, hourly_rate, min_ticket, flags_count, client_budget=None):
    base_hours_adjusted = raw_hours * friction_factor
    base_cost = max(base_hours_adjusted * hourly_rate, min_ticket)
    
    # Pricing Tiers
    tier_1_essential = round(base_cost * 0.75, -1)
    tier_2_recommended = round(base_cost, -1)
    tier_3_vip = round(base_cost * 1.6, -1)
    
    # Risk & Quality Score (0 to 100)
    score = 100
    score -= (flags_count * 20)
    if friction_factor >= 2.0:
        score -= 15
    if client_budget and client_budget < tier_1_essential:
        score -= 30
        
    score = max(0, min(100, score))
    
    if score >= 75 and flags_count == 0:
        verdict = "GO (Aprobado)"
        verdict_code = "GO"
    elif score >= 45 and flags_count <= 2:
        verdict = "GO CONDICIONADO (Aprobado con Blindaje Estricto)"
        verdict_code = "CONDITIONAL_GO"
    else:
        verdict = "NO-GO (Rechazo Tajante)"
        verdict_code = "NO_GO"
        
    return {
        "verdict": verdict,
        "verdict_code": verdict_code,
        "score": score,
        "raw_hours": raw_hours,
        "friction_factor": friction_factor,
        "adjusted_hours": base_hours_adjusted,
        "hourly_rate": hourly_rate,
        "tier_1_essential": tier_1_essential,
        "tier_2_recommended": tier_2_recommended,
        "tier_3_vip": tier_3_vip
    }

def generate_evaluation_markdown(client_name, project_title, evaluation, constitution, detected_flags, notes=""):
    floors = constitution.get("financial_floors", {})
    clauses = constitution.get("standard_clauses", {})
    
    emoji = "🟢" if evaluation["verdict_code"] == "GO" else ("🟡" if evaluation["verdict_code"] == "CONDITIONAL_GO" else "🔴")
    
    md = f"""# {emoji} DICTAMEN DE EVALUACIÓN & PROPUESTA BLINDADA: {project_title.upper()}
### *Motor Guardián V3.0 — Arqueólogo Creativo*
**Fecha de Evaluación:** {datetime.now().strftime('%Y-%m-%d %H:%M')}  
**Cliente / Prospecto:** {client_name}  

---

## 📊 1. FICHA TÉCNICA DEL DICTAMEN

| Parámetro | Valor Evaluado | Referencia Constitución |
|---|---|---|
| **Veredicto Final** | **{emoji} {evaluation['verdict']}** | Criterio de Viabilidad |
| **Puntuación de Seguridad** | **{evaluation['score']} / 100** | Umbral Mínimo: 45/100 |
| **Horas Base Estimadas** | {evaluation['raw_hours']} horas | Estimación en bruto |
| **Multiplicador de Fricción** | **{evaluation['friction_factor']}x** | Compensación Falacia Planificación |
| **Horas Ajustadas Reales** | **{evaluation['adjusted_hours']:.1f} horas** | Carga operativa real |
| **Tarifa Suelo Aplicada** | {evaluation['hourly_rate']} €/h | Suelo no negociable |
| **Red Flags Detectadas** | {len(detected_flags)} señales | Límite crítico: $\\ge 3$ |

"""
    if detected_flags:
        md += "### 🚩 Señales de Alerta Detectadas:\n"
        for flag in detected_flags:
            md += f"* ⚠️ **{flag}**\n"
        md += "\n"

    if notes:
        md += f"### 📝 Notas de Contexto:\n{notes}\n\n"

    md += f"""---

## 🏷️ 2. ESTRUCTURA DE PRESUPUESTO EN 3 NIVELES (ANCHOR PRICING)

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ 💰 OPCIONES DE PROPUESTA COMERCIAL BLINDADA                                            │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 1. OPCIÓN A (ESENCIAL / CORE):         {evaluation['tier_1_essential']:,.0f} € + IVA                             │
│    • Alcance núcleo estricto, sin extras ni reuniones extendidas.                      │
│    • 1 ronda de revisión incluida.                                                     │
│                                                                                        │
│ 2. OPCIÓN B (RECOMENDADA / ESTÁNDAR):  {evaluation['tier_2_recommended']:,.0f} € + IVA  ⭐️ OBJETIVO               │
│    • Solución integral completa con entregables atómicos garantizados.                 │
│    • 2 rondas de feedback estructuradas. Soporte estándar durante el hito.             │
│                                                                                        │
│ 3. OPCIÓN C (VIP / LLAVE EN MANO):     {evaluation['tier_3_vip']:,.0f} € + IVA                             │
│    • Prioridad máxima en calendario y entrega rápida (Fast-Track).                     │
│    • Asesoría directa 1 a 1, cesión comercial ampliada y soporte post-entrega.         │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 🛡️ 3. TÉRMINOS Y CLÁUSULAS ANTI-ABUSO OBLIGATORIAS

1. **Anticipo de Reserva:** **{floors.get('upfront_retainer_percentage', 50)}% por adelantado** para reservar fechas en agenda e iniciar producción.
2. **Límite de Revisiones:** Máximo **{clauses.get('max_review_rounds', 2)} rondas de correcciones** dentro del alcance acordado. Cualquier cambio estructural o adicional se facturará a **{floors.get('out_of_scope_hourly_rate_eur', 85)} €/h**.
3. **SLA de Feedback del Cliente:** Máximo **{clauses.get('client_feedback_sla_days', 7)} días hábiles** para enviar correcciones. Transcurrido ese plazo, las fechas de entrega se reprogramarán según disponibilidad de agenda.
4. **Propiedad Intelectual:** La entrega de archivos finales, derechos o accesos definitivos se efectuará **únicamente tras el pago del 100%** de la factura.

---

## ✉️ 4. PLANTILLA DE EMAIL / RESPUESTA AL CLIENTE

> **Asunto:** Propuesta de trabajo y opciones de colaboración — {project_title}  
>
> Hola {client_name},
>
> Gracias por ponerte en contacto y por compartir los detalles de **{project_title}**. He analizado los requisitos y objetivos para asegurar que el proyecto se ejecute con el máximo nivel de oficio y calidad técnica.
>
> Para adaptarnos al alcance que mejor encaje con vuestras prioridades y plazos, he preparado **3 opciones de colaboración cerradas**:
>
> * **Opción A (Esencial - {evaluation['tier_1_essential']:,.0f}€ + IVA):** Enfoque directo en la solución base indispensable del proyecto.
> * **Opción B (Recomendada / Completa - {evaluation['tier_2_recommended']:,.0f}€ + IVA):** El desarrollo integral estándar de inicio a fin con 2 rondas de feedback incluidas.
> * **Opción C (VIP / Entrega Prioritaria - {evaluation['tier_3_vip']:,.0f}€ + IVA):** Modalidad llave en mano con calendario acelerado y soporte prioritario.
>
> En todas las opciones trabajamos con un anticipo del 50% para fijar las fechas en calendario y garantizar la entrega en plazo.
>
> ¿Qué opción encaja mejor con lo que tenéis en mente para cerrar el calendario y arrancar?
>
> Un cordial saludo,  
> **{constitution.get('profile', {}).get('name', 'Tu Nombre')}**
"""
    return md

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
    parser = argparse.ArgumentParser(description="Arqueólogo Creativo V3.0 - Motor Guardián / Evaluador de Proyectos")
    parser.add_argument("--client", default="Cliente Prospecto", help="Nombre del cliente")
    parser.add_argument("--project", default="Nuevo Encargo", help="Título o descripción del proyecto")
    parser.add_argument("--hours", type=float, default=20.0, help="Horas estimadas en bruto")
    parser.add_argument("--friction", type=float, default=1.5, help="Multiplicador de fricción (1.0, 1.5, 2.0, 2.5)")
    parser.add_argument("--budget", type=float, default=None, help="Presupuesto sugerido por el cliente (opcional)")
    parser.add_argument("--flags", nargs="*", default=[], help="Lista de red flags detectadas")
    parser.add_argument("--notes", default="", help="Notas adicionales de contexto")
    parser.add_argument("--constitution", default=None, help="Ruta al archivo creator_constitution.json")
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
        client_budget=args.budget
    )
    
    md_content = generate_evaluation_markdown(
        client_name=args.client,
        project_title=args.project,
        evaluation=evaluation,
        constitution=constitution,
        detected_flags=args.flags,
        notes=args.notes
    )
    
    output_path = args.output
    if not output_path:
        sanitized_title = "".join(c for c in args.project if c.isalnum() or c in (' ', '_', '-')).rstrip().replace(" ", "_")
        output_path = f"EVALUACION_{sanitized_title}.md"
        
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(md_content)
        
    # Save to history log
    history_file = os.path.join(os.path.dirname(__file__), "..", "DOCS", "leads_history.json")
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "client": args.client,
        "project": args.project,
        "verdict": evaluation["verdict_code"],
        "score": evaluation["score"],
        "tier_2_eur": evaluation["tier_2_recommended"],
        "flags": args.flags
    }
    save_to_history(log_entry, history_file)
    
    print(f"[✓] Evaluación completada con éxito.")
    print(f"    • Veredicto: {evaluation['verdict']}")
    print(f"    • Puntuación: {evaluation['score']}/100")
    print(f"    • Presupuesto Recomendado: {evaluation['tier_2_recommended']:,.0f} € + IVA")
    print(f"    • Documento generado: {output_path}")

if __name__ == "__main__":
    main()
