// Innholdsevaluerings-workflow for content-review-skillen.
// Kjør via Workflow({scriptPath: ".claude/skills/content-review/eval_workflow.js"}).
// VIKTIG: oppdater MODULES under til dagens modul-liste (se SKILL.md steg 1)
// før kjøring - ikke bruk `args` (har vært ustabil).

export const meta = {
  name: 'content-quality-eval',
  description: 'Scorer alt kursinnhold (6 metrikker) + web-verifiserer høyrisiko produktpåstander',
  phases: [
    { title: 'Score', detail: '1 agent per modul scorer innhold + ekstraherer produktpåstander' },
    { title: 'Verify', detail: 'web-verifiser høyrisiko-påstander' },
  ],
}

// <<< ERSTATT med dagens modul-liste (SKILL.md steg 1) >>>
const MODULES = [
  'agents_md', 'arkitektur', 'at_mentions', 'autonomous_loop', 'avslutning',
  'context_engineering', 'cortex_code', 'cortex_in_snowsight', 'cortex_interaction',
  'demo_1', 'demo_2', 'demo_bundled_skill', 'evolusjon', 'gruppeoppgave_1',
  'gruppeoppgave_2', 'gruppeoppgave_3', 'individuell_oppgave_1', 'individuell_oppgave_2',
  'individuell_oppgave_3', 'individuell_oppgave_4', 'individuell_oppgave_5',
  'individuell_oppgave_at_mentions', 'individuell_oppgave_bundled_skill',
  'individuell_oppgave_kohort', 'individuell_oppgave_konkurrent', 'individuell_oppgave_kurs_kunde',
  'individuell_oppgave_modellvalg', 'individuell_oppgave_plan_mode', 'kostnader',
  'memory_md', 'oppvarming', 'plan_mode', 'skills_md', 'tilgjengelige_modeller',
]

const SCORE_SCHEMA = {
  type: 'object', additionalProperties: false,
  properties: {
    module: { type: 'string' },
    files: {
      type: 'array',
      items: {
        type: 'object', additionalProperties: false,
        properties: {
          file: { type: 'string' },
          F: { type: ['integer', 'null'] },
          F_unverified: { type: 'boolean' },
          R: { type: 'integer' },
          Rel: { type: ['integer', 'null'] },
          P: { type: ['integer', 'null'] },
          Full: { type: 'string', enum: ['ferdig', 'UTKAST', 'placeholder', 'tom'] },
          T: { type: 'string' },
          note: { type: 'string' },
        },
        required: ['file', 'F', 'F_unverified', 'R', 'Rel', 'P', 'Full', 'T', 'note'],
      },
    },
    module_scores: {
      type: 'object', additionalProperties: false,
      properties: {
        F: { type: 'number' }, R: { type: 'number' }, Rel: { type: 'number' },
        P: { type: 'number' }, Full: { type: 'string' }, T: { type: 'string' },
      },
      required: ['F', 'R', 'Rel', 'P', 'Full', 'T'],
    },
    product_claims: {
      type: 'array',
      items: {
        type: 'object', additionalProperties: false,
        properties: {
          claim: { type: 'string' }, file: { type: 'string' },
          risk: { type: 'integer' }, web_verifiable: { type: 'boolean' },
        },
        required: ['claim', 'file', 'risk', 'web_verifiable'],
      },
    },
    summary: { type: 'string' },
  },
  required: ['module', 'files', 'module_scores', 'product_claims', 'summary'],
}

const VERIFY_SCHEMA = {
  type: 'object', additionalProperties: false,
  properties: {
    claim: { type: 'string' },
    verdict: { type: 'string', enum: ['støttet', 'delvis støttet', 'motsagt', 'ingen kilde funnet'] },
    source: { type: 'string' },
    note: { type: 'string' },
  },
  required: ['claim', 'verdict', 'source', 'note'],
}

const scorePrompt = (slug) => `Du evaluerer ÉN modul i et NORSK kurs om Snowflake Cortex Code (agentisk kode-assistent i Snowflake) for ANALYTIKERE/DATA SCIENTISTS I NORSKE BANKER.

Modulmappe: modules/${slug}/

Les ALT av (bruk Read/Bash/Grep): content/*.md; config.py HVIS QUESTIONS/STATEMENTS; claude_answers.py HVIS finnes; og KUN prosaen i app_logic.py (module_header subtitle, crumb, st.subheader - ikke kode).

Score HVER content-enhet (én rad per .md; for config: én rad "config: spørsmål") på:
- F (1-5): faktuell. F_unverified=true HVIS Cortex Code/Snowflake-PRODUKTSPESIFIKK påstand du ikke kan verifisere fra generell kunnskap (hurtigtaster, verktøynavn som @(serverSkill:lineage), filstier, modeller i Cortex, Horizon Catalog). Generelle korrekte AI/LLM-konsepter: F=5. Tom/placeholder: F=null.
- R (1-5, HØY=DÅRLIG): kilde-/fabrikasjonsrisiko. 5 = spesifikk, AI-draftet, uverifisert produktpåstand som MÅ sjekkes. 1 = generelt/trivielt.
- Rel (1-5): relevans for bank-analytikere. null for tom.
- P (1-5): pedagogisk verdi. null for tom.
- Full: "ferdig" | "UTKAST" | "placeholder" | "tom".
- T ("1".."5" | "n/a"): nøktern bank-tone.
- note: kort (norsk).

module_scores = representativt snitt (F/R/Rel/P tall, Full "ferdig"/"blandet"/"UTKAST"/"placeholder", T tall-streng/"n/a").
product_claims = HVER konkrete Cortex Code/Snowflake-produktpåstand VERBATIM + risk(1-5) + web_verifiable. Ikke generiske/banale.
summary = 1-2 setninger. Returner KUN strukturert output. Vurdering, ikke omskriving.`

phase('Score')
const results = (await parallel(
  MODULES.map((slug) => () => agent(scorePrompt(slug), { label: `score:${slug}`, phase: 'Score', schema: SCORE_SCHEMA }))
)).filter(Boolean)

const seen = new Set(), highRisk = []
for (const r of results) {
  for (const c of (r.product_claims || [])) {
    if (c.risk >= 4 && c.web_verifiable) {
      const key = c.claim.toLowerCase().replace(/\s+/g, ' ').trim().slice(0, 80)
      if (!seen.has(key)) { seen.add(key); highRisk.push({ ...c, module: r.module }) }
    }
  }
}
highRisk.sort((a, b) => b.risk - a.risk)
const toVerify = highRisk.slice(0, 18)
log(`${results.length} moduler scoret. ${highRisk.length} unike høyrisiko-påstander, verifiserer ${toVerify.length}.`)

phase('Verify')
const verifyPrompt = (c) => `Web-verifiser denne påstanden om Snowflake Cortex Code mot OFFENTLIG dokumentasjon (foretrekk docs.snowflake.com/en/user-guide/cortex-code/). Bruk WebSearch/WebFetch (via ToolSearch).

Påstand (modul "${c.module}", fil ${c.file}): "${c.claim}"

verdict: "støttet" / "delvis støttet" / "motsagt" / "ingen kilde funnet". source: URL eller "". note: kort (norsk). Hvis ingen autoritativ kilde: si "ingen kilde funnet" - IKKE gjett.`

const verifications = toVerify.length
  ? (await parallel(toVerify.map((c) => () => agent(verifyPrompt(c), { label: `verify:${c.module}`, phase: 'Verify', schema: VERIFY_SCHEMA })))).filter(Boolean)
  : []

return { results, verifications, highRiskCount: highRisk.length }
