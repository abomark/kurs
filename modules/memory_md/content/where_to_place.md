Mappen ligger i **hjemmekatalogen din** - ikke i prosjektet.

```
~/.snowflake/cortex/
├── agents/      # custom agent-konfigurasjoner
├── memory/      # ← persistent memory (denne)
└── ...
```

**Konsekvens:** Memory følger _deg_, ikke prosjektet. Bytter du arbeidsmappe
fra `riskmodell-2026/` til `compliance-pipeline/`, har Cortex Code fortsatt
tilgang til alt du har lagret.

I praksis betyr det at memory er ditt **personlige verktøyskrin** - ikke
en delt ressurs med teamet.
