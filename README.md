<div align="center">
# 🎬 AI-Powered Business Intelligence Dashboard

### Amazon Prime Video Catalogue Analytics · Interactive BI · AI-Assisted Exploration

[![GitHub](https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github)](https://github.com/sakshibhardwaj27/AI-Powered-Business-Intelligence-Dashboard)
[![Live
Demo](https://img.shields.io/badge/Live%20Demo-Open%20App-FF4B4B?style=for-the-badge&logo=streamlit)](https://sakshibhardwaj27-ai-powered-business-intelligence-da-app-eddlvb.streamlit.app/)
![Python](https://img.shields.io/badge/Python-Data%20Analysis-3776AB?style=for-the-badge&logo=python)
![Power
BI](https://img.shields.io/badge/Power%20BI-Business%20Reporting-F2C811?style=for-the-badge&logo=powerbi)

**Explore a streaming catalogue through interactive visualisations,
business-focused summaries, and a natural-language AI Analyst.**

[Overview](#-project-overview) · [Features](#-key-features) ·
[Architecture](#-solution-architecture) ·
[Data](#-dataset--data-understanding) · [Run
Locally](#-run-the-project-locally) · [AI
Analyst](#-how-the-ai-analyst-works) ·
[Limitations](#-limitations-and-responsible-interpretation) · [Interview
Guide](#-project-defence-interview-guide)
</div>

------------------------------------------------------------------------

## 📌 Project overview

The **AI-Powered Business Intelligence Dashboard for Amazon Prime
Video** is an end-to-end analytics project combining data preparation,
exploratory data analysis (EDA), business reporting, interactive
visualisation, database modelling, and an LLM-powered question-answering
interface.

It uses catalogue metadata---such as title type, release year, genres,
country information, runtime, and available ratings---to help users
explore questions like:

-   How is the catalogue distributed between movies and TV shows?
-   Which genres or countries appear most frequently in the available
    data?
-   How does the catalogue vary by release year?
-   How are available ratings and runtime values distributed?
-   Can a user ask a question in plain English instead of starting with
    a chart?

The solution offers two complementary experiences:

1.  **Structured BI:** visual summaries, filters, KPI-style indicators,
    and charts for repeatable exploration.
2.  **AI-assisted exploration:** a natural-language interface that uses
    a Groq-accessed large language model (LLM) to generate responses
    from the context supplied by the application.

> **Scope note:** This dataset describes titles and their metadata. It
> does not, by itself, contain individual viewing histories, watch time,
> subscriber churn, customer retention, revenue, or licensing costs. The
> project therefore supports **catalogue analysis**, not direct
> measurement of audience engagement or commercial performance.

## 🎯 Project objectives

-   Turn raw catalogue data into a more accessible analytical
    experience.
-   Practise a complete workflow: data inspection → cleaning → analysis
    → modelling → visualisation → application → deployment.
-   Present information through interactive charts and filters rather
    than raw tables alone.
-   Explore how a natural-language LLM interface can complement
    traditional BI.
-   Demonstrate data storytelling, SQL schema design, and deployment
    skills in one portfolio project.

## ✨ Key features

```{=html}
<details open>
```
```{=html}
<summary>
```
`<strong>`{=html}📊 Interactive dashboard and
visualisations`</strong>`{=html}
```{=html}
</summary>
```
-   Explore catalogue attributes through interactive charts.
-   Filter the data where supported by the application.
-   Inspect distributions and comparisons across fields such as content
    type, release year, genre, ratings, runtime, and country.
-   Use hover interactions and chart controls provided by Plotly.
-   Review high-level summaries/KPI-style values before exploring
    details.

```{=html}
</details>
```
```{=html}
<details>
```
```{=html}
<summary>
```
`<strong>`{=html}🤖 AI Analyst`</strong>`{=html}
```{=html}
</summary>
```
-   Enter a question in natural language.
-   Send the question and relevant data context to an LLM accessed
    through the Groq API.
-   Display a generated response inside the Streamlit application.
-   Use suggested questions to help users get started.
-   Maintain chat messages during the Streamlit session and provide a
    way to clear the conversation.

**Important:** LLM responses are generated text, not guaranteed facts.
Numerical answers should be checked against the dataset and calculated
summaries.

```{=html}
</details>
```
```{=html}
<details>
```
```{=html}
<summary>
```
`<strong>`{=html}🧹 Data preparation and EDA`</strong>`{=html}
```{=html}
</summary>
```
-   Inspect columns, types, missing values, and repeated records.
-   Prepare fields for analysis and visualisation.
-   Handle list-like metadata fields, such as genres or countries,
    carefully when category-level analysis requires it.
-   Explore the data before deciding which metrics and charts are
    useful.

```{=html}
</details>
```
```{=html}
<details>
```
```{=html}
<summary>
```
`<strong>`{=html}🗄️ SQL schema and ER modelling`</strong>`{=html}
```{=html}
</summary>
```
-   Design a relational representation of the catalogue data.
-   Document entities and relationships with a schema and
    entity-relationship (ER) diagram.
-   Use the modelling artefacts to communicate how the data could be
    organised in a database.

The schema/ER diagram documents the modelling design; it should not be
interpreted as proof that the deployed Streamlit app queries a live
production database unless that integration is implemented.

```{=html}
</details>
```
```{=html}
<details>
```
```{=html}
<summary>
```
`<strong>`{=html}📈 Power BI reporting`</strong>`{=html}
```{=html}
</summary>
```
-   Build a business-reporting view for exploring catalogue patterns.
-   Use a BI tool for structured visual reporting alongside the custom
    Streamlit application.
-   Keep the purpose of each tool distinct: Power BI supports reporting,
    while Streamlit supports a custom Python application and AI
    interaction.

```{=html}
</details>
```
```{=html}
<details>
```
```{=html}
<summary>
```
`<strong>`{=html}☁️ Deployment`</strong>`{=html}
```{=html}
</summary>
```
-   Publish the Streamlit app through Streamlit Community Cloud.
-   Keep dependencies in `requirements.txt`.
-   Configure API credentials through Streamlit secrets rather than
    hardcoding them in source code.

```{=html}
</details>
```
## 🧰 Technology stack

  -----------------------------------------------------------------------
  Technology                          Role in the project
  ----------------------------------- -----------------------------------
  **Python**                          Main language for data preparation
                                      and application logic

  **Pandas**                          Loading, inspecting, cleaning,
                                      filtering, transforming, and
                                      summarising tabular data

  **Plotly**                          Interactive charts

  **Streamlit**                       Web application, controls,
                                      dashboard layout, and AI Analyst
                                      interface

  **Groq API + LLM**                  Natural-language response
                                      generation from supplied prompt
                                      context

  **Power BI**                        Business reporting and dashboard
                                      visualisation

  **SQL**                             Relational schema design and
                                      database concepts

  **Git & GitHub**                    Version control and project
                                      repository

  **Streamlit Community Cloud**       Hosting the Streamlit application
  -----------------------------------------------------------------------

> The table describes tools used across the project. It does not imply
> that every tool is called by every part of the deployed application.

## 🧭 Solution architecture

``` mermaid
flowchart TD
    A[Amazon Prime Video catalogue dataset] --> B[Python + Pandas]
    B --> C[Data inspection and cleaning]
    C --> D[Exploratory data analysis]
    C --> E[Prepared data for the app]
    D --> F[Analysis findings and chart planning]
    F --> G[Power BI reporting]
    E --> H[Streamlit application]
    H --> I[Filters and KPI-style summaries]
    H --> J[Plotly visualisations]
    H --> K[AI Analyst interface]
    K --> L[Prompt + relevant data context]
    L --> M[Groq API / language model]
    M --> N[Generated natural-language response]
    N --> H
    O[SQL schema + ER diagram] -. documents a relational design .-> P[Database modelling artefacts]
```

### Workflow explained

1.  **Understand the data:** inspect the fields and determine which
    questions the dataset can answer.
2.  **Prepare the data:** address data-quality issues and make fields
    suitable for analysis.
3.  **Explore patterns:** use descriptive summaries and EDA to
    understand distributions and relationships.
4.  **Design the reporting experience:** choose charts and summary
    metrics that match the analytical questions.
5.  **Build the dashboard:** provide interactive visualisations and
    filters in Streamlit, alongside the Power BI report.
6.  **Add natural-language interaction:** pass a user's question and
    relevant context to the LLM through Groq.
7.  **Deploy and maintain:** configure dependencies and secrets, then
    publish the Streamlit app.

## 🗂️ Dataset & data understanding

The project uses a dataset of **Amazon Prime Video title metadata**.
Common fields in this type of catalogue dataset include:

  ------------------------------------------------------------------------
  Field                    What it describes       Example analysis
  ------------------------ ----------------------- -----------------------
  `title`                  Title or catalogue      Search and
                           entry name              identification

  `type`                   Content type, such as   Catalogue split
                           movie or TV show        

  `release_year`           Release year            Year-wise distribution

  `age_certification`      Available age           Certification
                           certification           distribution

  `genres`                 Genre labels associated Genre frequency
                           with a title            

  `production_countries` / Country metadata,       Country-level
  country field            depending on the source distribution
                           schema                  

  `runtime`                Runtime value, where    Runtime distribution
                           available               

  `imdb_score`             IMDb rating, where      Rating distribution or
                           available               comparison

  `tmdb_score`             TMDb rating, where      Rating distribution or
                           available               comparison

  `tmdb_popularity`        TMDb popularity field,  Explore
                           where available         popularity-score
                                                   distribution
  ------------------------------------------------------------------------

**Column names and availability can differ between dataset versions.**
Use the actual column names in the repository's data file or notebook
when reproducing the analysis.

### Data-quality considerations

-   **Missing values:** inspect missingness and decide on a
    column-specific treatment. Do not replace missing ratings with
    arbitrary scores.
-   **Duplicate rows:** check for repeated records and determine whether
    they are true duplicates before removing them.
-   **List-like columns:** genres and countries may be stored as lists
    or list-like strings. Parse and transform them carefully before
    category-level analysis.
-   **Data types:** ensure numeric measures are numeric and years are
    represented consistently.
-   **Interpretation:** a missing score does not mean a title has a
    score of zero; missing metadata should not be treated as a real
    measurement.

### What the dataset can and cannot tell us

  -----------------------------------------------------------------------
  The data can support                The data alone cannot establish
  ----------------------------------- -----------------------------------
  Catalogue composition               Number of people who watched a
                                      title

  Genre and country distribution      Total watch time or completion rate

  Release-year patterns               Subscriber churn or retention

  Distribution of available ratings   Revenue, profit, or licensing
                                      return

  Comparisons using available         Causal impact of a content decision
  metadata                            
  -----------------------------------------------------------------------

**A catalogue pattern is a useful observation, but it is not
automatically a business outcome.**

## 📊 Analytical questions the dashboard is designed to explore

1.  What proportion of catalogue entries are movies versus TV shows?
2.  How does the number of titles vary by release year?
3.  Which genres are most frequently represented?
4.  How are available ratings distributed?
5.  How does runtime vary across content categories?
6.  Which countries appear most often in the production metadata?
7.  How do rating distributions differ between categories, where enough
    valid data is available?
8.  Are there missing-data patterns that could affect comparisons?

These are **analysis questions**, not pre-declared findings. State a
specific numerical result in an interview only after checking it in your
notebook or dashboard.

## 🧠 How the AI Analyst works

The AI Analyst gives users a conversational way to explore the data.

``` mermaid
sequenceDiagram
    actor User
    participant App as Streamlit application
    participant Prompt as Prompt/context preparation
    participant API as Groq API / LLM

    User->>App: Ask a question
    App->>Prompt: Combine question with relevant data context
    Prompt->>API: Send prompt through API
    API-->>Prompt: Return generated response
    Prompt-->>App: Provide response text
    App-->>User: Display answer in the chat
```

### Typical interaction

A user might ask:

-   "How is the catalogue split between movies and TV shows?"
-   "What patterns can I explore by release year?"
-   "Explain what the ratings chart shows."
-   "Which fields would help compare genres?"

The actual answer depends on the supplied data context and the model
response. These examples illustrate the intended interaction; they are
not evidence that the model has access to every row or can answer every
calculation accurately.

### Why use an LLM?

Traditional dashboards are excellent for predefined metrics and
repeatable visualisations. An LLM adds a conversational layer so users
can ask questions in everyday language. In this project, the LLM
complements the visual dashboard rather than replacing the underlying
data-processing logic.

### Why Groq?

Groq provides an API through which an application can access supported
language models. It was used to connect the AI Analyst to a language
model. Model availability, names, rate limits, and pricing can change,
so the configured model should be checked against current Groq
documentation.

### AI reliability and boundaries

-   The model may misunderstand a question or produce a plausible but
    incorrect answer.
-   A response is only as well-grounded as the context supplied to the
    model.
-   If only a subset or summary of the data is supplied, the model
    cannot reliably infer exact results for the entire dataset.
-   API availability, rate limits, and model configuration can affect
    the feature.
-   Important numeric claims should be calculated with Python/SQL and
    checked against the source data.
-   Do not upload confidential or personal information to an external
    model API.

## 🗄️ SQL schema and ER diagram

The project includes SQL schema design and an ER diagram to explain a
possible relational structure for the catalogue.

### Why model the data relationally?

-   **Clarity:** separate entities and their attributes are easier to
    understand.
-   **Consistency:** keys and relationships help maintain valid
    references.
-   **Flexibility:** a title can be associated with multiple genres or
    countries without forcing every relationship into one field.
-   **Querying:** relational structures can support aggregations, joins,
    and category-level analysis.

### Primary key vs foreign key

-   A **primary key** uniquely identifies a row in its own table.
-   A **foreign key** references a key in another table and establishes
    a relationship.

For example, a title entity could use a unique title identifier, while a
title-to-genre mapping table could reference that identifier and a genre
identifier. This is an illustrative relational design; use the exact
entities and relationships in the project's own SQL and ER diagram when
explaining the implementation.

### Why include an ER diagram?

An ER diagram lets a reviewer understand the proposed data model before
reading SQL. It documents entities, keys, and relationships visually and
helps communicate how the catalogue could be organised for querying.

## 📈 Power BI and Streamlit: why both?

  -----------------------------------------------------------------------
  Aspect                  Power BI                Streamlit
  ----------------------- ----------------------- -----------------------
  Main purpose in this    BI reporting            Custom interactive
  project                                         analytics application

  Strength                Report and dashboard    Python-driven custom
                          authoring               interface

  User interaction        Report filters and      App controls, custom
                          visual interactions     logic, and AI chat

  AI integration          Depends on available    Can call Python
                          configuration and       functions and external
                          services                APIs

  Best fit here           Structured visual       Custom app experience
                          reporting               and natural-language
                                                  interaction
  -----------------------------------------------------------------------

The two tools are complementary in this portfolio project. A separate
Power BI report is not the same thing as a Streamlit page, and exact
refresh or data-connection behaviour depends on how each artefact is
configured.

## 🚀 Run the project locally

### Prerequisites

-   Python installed
-   Git
-   A Groq API key if you want to use the AI Analyst
-   The repository's required dataset and project files

### 1. Clone the repository

``` bash
git clone https://github.com/sakshibhardwaj27/AI-Powered-Business-Intelligence-Dashboard.git
cd AI-Powered-Business-Intelligence-Dashboard
```

### 2. Create and activate a virtual environment

**Windows (PowerShell):**

``` powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux:**

``` bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

``` bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configure the API secret

Create `.streamlit/secrets.toml` locally, if the application expects the
key under this name:

``` toml
GROQ_API_KEY = "your_groq_api_key_here"
```

Replace the placeholder with your own key. **Never commit this file or
publish your API key.** Ensure `.streamlit/secrets.toml` is excluded by
`.gitignore`. On Streamlit Community Cloud, configure the same secret in
the app's Secrets settings.

If your current `llm.py` uses a different secret name, use the exact
name expected by that file.

### 5. Start the app

If the entry point is `app.py`:

``` bash
streamlit run app.py
```

If the repository uses a different entry file, use that file instead.

### 6. Open the app

Streamlit normally prints a local URL in the terminal, often
`http://localhost:8501`. Open the URL shown in the terminal.

> **Troubleshooting:** Check that the uploaded or selected CSV is not
> empty, required columns exist, dependencies are installed, and secrets
> use the expected names. If a Plotly chart reports a duplicate element
> ID, give each chart a unique Streamlit key. If the AI feature fails,
> check the API key, model availability, network access, and API quota.

## ☁️ Deployment

**[Open the live
application](https://sakshibhardwaj27-ai-powered-business-intelligence-da-app-eddlvb.streamlit.app/)**

**[View source code on
GitHub](https://github.com/sakshibhardwaj27/AI-Powered-Business-Intelligence-Dashboard)**

Deployment checklist:

-   [ ] Dependencies are listed in `requirements.txt`.
-   [ ] Secrets are configured in Streamlit's secret manager.
-   [ ] API keys are not committed to GitHub.
-   [ ] The deployed app can read the expected input data.
-   [ ] The app handles empty or invalid uploads gracefully.
-   [ ] Charts update correctly when filters change.
-   [ ] AI failures display understandable feedback.
-   [ ] The live link works from a fresh browser session.

## 📁 Project artefacts

The project work includes these artefact types:

-   Python-based data cleaning and EDA
-   Interactive Streamlit dashboard and AI Analyst
-   Plotly visualisations
-   Power BI report/dashboard
-   SQL schema design
-   Entity-relationship (ER) diagram
-   Project report and presentation
-   GitHub repository and deployed web application

Use the repository's actual file and folder names when navigating these
artefacts. This README intentionally avoids guessing exact paths for
files that may have been renamed during development.

## 🧪 Validation and quality checks

-   [ ] Row count and column names match the dataset being used.
-   [ ] Missing values and duplicate handling are documented accurately.
-   [ ] KPI totals reconcile with the cleaned data.
-   [ ] Filters affect all intended charts consistently.
-   [ ] Charts have clear labels, units, and titles.
-   [ ] AI responses do not claim access to fields or records that were
    not supplied.
-   [ ] Important numerical answers can be reproduced with Python or
    SQL.
-   [ ] The deployed app works with current dependencies and secrets.
-   [ ] README feature descriptions match the actual implementation.
-   [ ] Any impact percentages in the resume are supported by a
    documented measurement.

## 📏 Impact metrics: report only what you can verify

A portfolio project should distinguish measured results from expected
benefits.

The resume may mention improvements in manual reporting time or
insight-generation time. Those percentages should be presented as
measured outcomes only if there is evidence for the baseline, the
post-implementation result, and the calculation method.

For a time-based metric:

\[ `\text{Time reduction (\%)}`{=tex} =
`\frac{\text{Baseline time} - \text{New time}}{\text{Baseline time}}`{=tex}
`\times 100`{=tex} \]

If no timed comparison was performed, describe the benefit
qualitatively---for example, "centralised catalogue exploration and
added natural-language access"---instead of presenting an estimate as a
measured result. Similarly, verify the actual number of records before
stating "10K+".

## ⚖️ Limitations and responsible interpretation

1.  **Metadata, not viewing telemetry:** the dataset does not establish
    who watched a title, how long they watched, or whether they
    subscribed or returned.
2.  **No causal claims:** catalogue patterns do not prove that a
    particular genre caused higher engagement or business performance.
3.  **LLM uncertainty:** generated explanations may be incomplete or
    incorrect and should be verified for important decisions.
4.  **Input quality:** inconsistent formats, missing columns, empty
    files, or malformed list-like values can affect the analysis.
5.  **API dependency:** the AI feature relies on external API access,
    supported model availability, and service limits.
6.  **Scale:** larger datasets may require database-backed aggregation,
    caching, and performance testing.
7.  **No production claim:** this is a portfolio demonstration, not
    evidence of a production deployment at Amazon or an official Amazon
    Prime Video system.

## 🔮 Future improvements

-   Add automated validation for uploaded datasets and clearer error
    messages.
-   Separate exact numerical calculations from LLM-generated
    explanations.
-   Provide traceable supporting rows or aggregates for AI answers.
-   Add tests for data transformations, filters, and KPI calculations.
-   Improve accessibility, chart labelling, and mobile layout.
-   Add a database-backed analytical layer for larger datasets.
-   Integrate legitimate viewing, completion, or subscription data---if
    available and appropriately governed---to support engagement or
    retention analysis.
-   Document repeatable evaluation of response quality and application
    usability.

## 💬 Project defence: interview guide

```{=html}
<details>
```
```{=html}
<summary>
```
`<strong>`{=html}1. Explain the project in 60--90
seconds.`</strong>`{=html}
```{=html}
</summary>
```
"I built an AI-powered BI dashboard to explore Amazon Prime Video
catalogue metadata. I used Python and Pandas for data preparation and
analysis, designed a SQL schema and ER diagram, created a Power BI
report, and developed a Streamlit application with Plotly visualisations
and filters. I also integrated an AI Analyst using an LLM accessed
through Groq, allowing users to ask natural-language questions about the
supplied data context. The goal was to make catalogue exploration more
accessible. One important limitation is that the dataset contains title
metadata rather than actual viewing or subscription activity, so I do
not claim to measure retention or watch time."

```{=html}
</details>
```
```{=html}
<details>
```
```{=html}
<summary>
```
`<strong>`{=html}2. Why use both Power BI and
Streamlit?`</strong>`{=html}
```{=html}
</summary>
```
"Power BI supports structured BI reporting and interactive report
exploration. Streamlit gives me more flexibility to build a Python-based
application and connect custom functionality, including the AI Analyst.
They serve complementary purposes in the project."

```{=html}
</details>
```
```{=html}
<details>
```
```{=html}
<summary>
```
`<strong>`{=html}3. Does the AI calculate every metric directly from the
entire dataset?`</strong>`{=html}
```{=html}
</summary>
```
"Not necessarily. The LLM responds based on the question and the context
supplied by the application. If the context contains only a subset or
summary, the model cannot be assumed to know the exact answer for every
record. For critical metrics, I would calculate the result
deterministically using Python or SQL and then use the LLM to explain
it."

```{=html}
</details>
```
```{=html}
<details>
```
```{=html}
<summary>
```
`<strong>`{=html}4. Can this project measure customer
retention?`</strong>`{=html}
```{=html}
</summary>
```
"No, not with the catalogue metadata alone. Retention requires
information such as subscription status over time or repeat activity. My
project analyses catalogue characteristics and available metadata. I
would need additional data to calculate retention accurately."

```{=html}
</details>
```
```{=html}
<details>
```
```{=html}
<summary>
```
`<strong>`{=html}5. How do you know the AI's answer is
correct?`</strong>`{=html}
```{=html}
</summary>
```
"I do not assume every generated answer is correct. I validate numerical
results against the source data and would use deterministic calculations
for important metrics. Prompting with relevant context can help, but it
does not eliminate hallucinations."

```{=html}
</details>
```
```{=html}
<details>
```
```{=html}
<summary>
```
`<strong>`{=html}6. What did SQL contribute if the app uses a
CSV?`</strong>`{=html}
```{=html}
</summary>
```
"The SQL schema and ER diagram document how the data could be organised
relationally and demonstrate my database-modelling work. I would
distinguish that design artefact from a live database connection: I
would claim that the app queries SQL only if that integration is
actually implemented."

```{=html}
</details>
```
```{=html}
<details>
```
```{=html}
<summary>
```
`<strong>`{=html}7. How would you prove the claimed time
savings?`</strong>`{=html}
```{=html}
</summary>
```
"I would define a baseline task, measure how long it takes to complete
manually, repeat the same task using the dashboard, and calculate the
percentage difference. Without that comparison, I would describe the
expected workflow benefit rather than presenting the percentage as a
measured outcome."

```{=html}
</details>
```
```{=html}
<details>
```
```{=html}
<summary>
```
`<strong>`{=html}8. What would you improve first?`</strong>`{=html}
```{=html}
</summary>
```
"I would strengthen input validation, make AI answers more traceable to
reproducible calculations, and add tests for KPI accuracy and filter
behaviour. Those improvements would increase reliability before adding
more features."

```{=html}
</details>
```
## 🧾 Glossary

  -----------------------------------------------------------------------
  Term                                Simple explanation
  ----------------------------------- -----------------------------------
  **BI (Business Intelligence)**      Turning data into reports and
                                      insights that support decisions

  **EDA**                             Exploring data to understand its
                                      structure, quality, and patterns

  **KPI**                             A key measure used to track a
                                      defined objective or activity

  **Schema**                          The structure of a database,
                                      including tables and columns

  **ER diagram**                      A visual map of entities and their
                                      relationships

  **LLM**                             A language model that generates
                                      text from input context

  **Prompt**                          Instructions and context provided
                                      to a model

  **Hallucination**                   A plausible-sounding but
                                      unsupported or incorrect model
                                      response

  **API**                             A defined interface through which
                                      software systems communicate

  **Deployment**                      Making an application available in
                                      an environment where users can
                                      access it
  -----------------------------------------------------------------------

## 👩‍💻 Author

**Sakshi Bhardwaj** · Data Science / Analytics Portfolio Project

-   **GitHub:** [sakshibhardwaj27](https://github.com/sakshibhardwaj27)
-   **Project repository:** [AI-Powered Business Intelligence
    Dashboard](https://github.com/sakshibhardwaj27/AI-Powered-Business-Intelligence-Dashboard)
-   **Live demo:** [Open Streamlit
    app](https://sakshibhardwaj27-ai-powered-business-intelligence-da-app-eddlvb.streamlit.app/)

------------------------------------------------------------------------

::: {align="center"}
**Built to make catalogue data easier to explore---with interactive BI
and AI-assisted analysis.**
:::
