**Hva er Tool Interface?**

Tool Interface er mekanismen som lar språkmodellen utføre **handlinger i den
virkelige verden** - i stedet for bare å generere tekst.

Konkret:

1. Modellen velger et verktøy basert på brukerens forespørsel
   (f.eks. "kjør denne SQL-en")
2. Sender strukturerte parametere til verktøyet (f.eks. `{"sql": "SELECT 1"}`)
3. Mottar resultatet tilbake og bruker det i svaret

Uten verktøy kan en LLM bare _snakke om_ ting. Med Tool Interface kan den
faktisk kjøre SQL, lese/skrive filer, søke i dokumentasjon, navigere i
brukergrensesnittet, og lage diagrammer. **Det er broen mellom modellens
"tenkning" og faktiske handlinger i Snowflake-miljøet.**

**Verktøyene i Cortex Code:**

| Kategori | Verktøy |
|---|---|
| **Søk** | `snowflake_object_search`, `snowflake_product_docs`, `snowflake_semantic_view_search`, `snowflake_marketplace_search` |
| **Utførelse** | `snowflake_sql_execute`, `system_execute_sql`, `bash` |
| **Filoperasjoner** | `read`, `write`, `edit`, `multi_edit` |
| **Spesialiserte** | `snowflake_multi_cortex_analyst`, `pivot_table`, `notebook_action`, `data_to_chart` |
| **Navigasjon** | `snowsight_navigate`, `get_page_context`, `read_active_pane` |
