# Complete Pool Owner & Operator Manual

**Residential · Public · Commercial — Indoor & Outdoor Pools and Spas**

*Version 2.0 — July 2026. Expanded edition for AI-assistant knowledge bases (semantic database + vector store / RAG). Each section is self-contained, uses consistent terminology, and can be chunked at the `##` or `###` heading level without losing meaning.*

---

## 0. About This Manual

### 0.1 Purpose and Scope

This manual is the reference knowledge base for an AI assistant that helps end users with pool-related work. It covers residential backyard pools, public/municipal pools, commercial pools (hotels, gyms, HOAs, waterparks), spas/hot tubs, indoor and outdoor installations. Content spans onboarding, pool types, water chemistry, testing, chemical dosing, chemical safety, equipment, seasonal care, troubleshooting, and U.S. regulatory context (federal and state).

### 0.2 How an AI Agent Should Use This Document

- Every user interaction about dosing requires knowing the **pool profile** (Section 1.3): volume, surface material, sanitizer system, indoor/outdoor, and jurisdiction. If unknown, the agent should ask or help the user calculate volume (Section 1.4).
- All dosing figures in this manual are normalized to a **40,000 L (≈10,566 US gal) pool** unless stated otherwise. Scale linearly for other volumes.
- Regulatory content (Sections 12–13) applies to the **United States**. State requirements vary; the agent must always advise users to verify the current code with their state or local health department. Regulations cited were current as of mid-2026.
- Safety-critical rules (Section 6) override convenience. If a user describes mixing chemicals, chlorine gas exposure, or a fecal/vomit contamination event, the agent should prioritize the emergency procedures in Sections 6.6–6.8.
- Chemistry ranges differ by pool class: residential guidance follows CDC Healthy Swimming recommendations; public/commercial guidance follows the CDC Model Aquatic Health Code (MAHC) and state codes, which are stricter. When the user operates a public or commercial pool, use the MAHC/state values.

### 0.3 Units and Conventions

- ppm = parts per million = mg/L. 1 US gallon = 3.785 L. 1 lb = 453.6 g.
- FC = free chlorine, CC = combined chlorine (chloramines), TC = total chlorine (FC + CC), TA = total alkalinity, CH = calcium hardness, CYA = cyanuric acid (stabilizer), SWG = salt-water chlorine generator, LSI = Langelier Saturation Index.
- Temperature ranges are given in both °C and °F.
- "Shock" and "superchlorination" are used interchangeably for a deliberate large oxidizer dose.

---
## 1. Onboarding — What a New Pool Owner or Operator Needs First

*This section covers the documentation, information, and first actions every user needs before doing any pool work. An AI assistant should walk a new user through this section before giving chemistry advice.*

### 1.1 Documents to Locate and Keep (The Pool Binder)

Every pool owner/operator should assemble a "pool binder" (physical or digital) containing:

1. **Pool construction documents**: builder's contract, as-built drawings or site plan, dig sheet (dimensions and depths), surface/finish specification (plaster, pebble, vinyl, fiberglass gelcoat), and completion/inspection certificates.
2. **Building permit and final inspection sign-off** for the pool, barrier/fence, and any gas or electrical work. Most U.S. jurisdictions require permits for in-ground pools and many above-ground pools.
3. **Equipment manuals and warranty cards** for: pump(s), filter, heater/heat pump, salt-water chlorine generator (SWG), automatic chlorinator/feeder, automation/control system, pool cleaner, lights, and safety cover. Register warranties promptly — many manufacturers require registration within 30–90 days and may require professional installation for warranty validity.
4. **Pool volume record** (see 1.4) — the single most important number for all chemical dosing.
5. **Surface and finish records**: material, installation date, and manufacturer care requirements (new plaster has a special 28–30 day startup, see 1.6).
6. **Safety Data Sheets (SDS)** for every chemical stored on site. U.S. suppliers must provide these; they are also downloadable from manufacturer websites. Commercial facilities are required by OSHA's Hazard Communication Standard (29 CFR 1910.1200) to keep SDSs accessible to employees.
7. **Insurance documentation**: homeowners policy rider or liability coverage noting the pool; commercial facilities need liability insurance meeting state/local minimums.
8. **For public/commercial pools additionally**: operating permit/license from the health department, certified operator (CPO or equivalent) certificates, inspection reports, water test logs (many states mandate retention of 1–3 years), lifeguard certifications where applicable, VGB Act drain cover compliance documentation (model, install date, life expectancy), and the facility's emergency action plan.

### 1.2 First-Week Checklist for a New Pool Owner

1. Determine pool volume (1.4) and record it.
2. Identify surface material and sanitizer system (chlorine manual dosing, trichlor feeder, SWG, cartridge/mineral, bromine).
3. Locate main equipment: pump, filter (note type: sand, cartridge, DE), heater, valves, timers/automation, GFCI breakers, emergency shutoff.
4. Perform a full baseline water test (FC, CC, pH, TA, CH, CYA, salt if SWG, metals and phosphates ideally) — at home plus one professional/store lab test to cross-check.
5. Buy a quality test kit (Section 4) and basic chemicals; store them safely (Section 6).
6. Verify safety equipment: compliant barrier/fence and gates (Section 12.1), anti-entrapment drain covers, life ring or shepherd's crook, first-aid kit, and for public pools the required signage and rescue equipment.
7. Learn the emergency basics: how to shut off the pump, where the electrical disconnect is, Poison Control number in the U.S. (1-800-222-1222), and local emergency number (911).
8. Establish the testing/maintenance schedule appropriate to your pool class (Section 4.3).

### 1.3 The Pool Profile — Data an Assistant Needs Before Advising

| Field | Why It Matters | Example |
|---|---|---|
| Volume (L or gal) | All dosing scales with volume | 40,000 L / 10,566 gal |
| Surface material | Sets CH and TA targets; drain rules | Plaster, vinyl, fiberglass, pebble |
| Sanitizer system | Sets FC/CYA/salt targets | Liquid chlorine, trichlor feeder, SWG, bromine |
| Indoor or outdoor | CYA use, algae pressure, ventilation | Outdoor screened |
| Residential / public / commercial | Which code and ranges apply | Residential |
| Filter type | Cleaning procedure, pressure baseline | Sand, cartridge, DE |
| Heater type | pH/CH sensitivity | Gas, heat pump, solar, none |
| Climate & season | Freeze protection, algae pressure | Phoenix AZ, summer |
| Fill-water source | Baseline metals/CH/TA | Municipal, well |
| Jurisdiction (state/county) | Applicable code | Florida / Miami-Dade |

### 1.4 Calculating Pool Volume

Use average depth = (shallow depth + deep depth) ÷ 2.

- **Rectangular**: length × width × average depth. In meters → m³ → ×1,000 = liters. In feet → ft³ × 7.48 = gallons.
- **Circular**: 3.14 × radius² × average depth.
- **Oval**: length × width × average depth × 0.89.
- **Kidney/freeform**: (longest length × widest width × average depth) × 0.75, or sum of simpler shapes.

Example: 8 m × 4 m pool, 1.0 m shallow to 2.0 m deep → avg 1.5 m → 8 × 4 × 1.5 = 48 m³ = 48,000 L (≈12,680 gal).

Cross-check volume by the "measured dose response" method: add a known chlorine dose and compare the measured FC rise to the predicted rise; a consistent gap means the recorded volume is wrong.

### 1.5 Understanding Your Sanitizer System (Orientation)

- **Manual liquid chlorine / bleach**: cheapest, adds nothing but chlorine and a little salt; requires frequent dosing.
- **Trichlor tablet feeder or floater**: convenient and stabilized, but every tablet adds CYA (0.6 ppm CYA per 1 ppm FC) and acid — expect CYA creep and falling pH over a season.
- **Salt-water chlorine generator (SWG)**: converts dissolved salt (typically ~3,200 ppm) into chlorine in-line; pushes pH upward continuously; the cell needs inspection/cleaning and replacement every 3–7 years.
- **Cal-hypo feeder**: unstabilized chlorine that also adds calcium (~0.7 ppm CH per 1 ppm FC); common in commercial settings.
- **Bromine**: mainly spas/hot tubs and some indoor pools; not stabilized by CYA; regenerated with shock.
- **Supplemental systems (ozone, UV, AOP)**: reduce chlorine demand and kill chlorine-resistant pathogens (UV and ozone inactivate *Cryptosporidium*), but **never replace** the residual sanitizer in the water. The MAHC requires increased-risk venues (e.g., wading pools, splash pads) to add secondary UV/ozone disinfection.

### 1.6 Special Startup Situations

- **New plaster (first 28–30 days)**: plaster hydrates and releases calcium hydroxide; pH rises fast. Follow the builder's/NPC startup card: test and adjust pH and TA daily for the first 2 weeks, brush the entire pool 1–2× daily, do not add salt for ~28 days, delay heating, and do not use a wheeled cleaner. Water balance errors in the first month permanently affect finish quality.
- **New vinyl liner**: never drain; fill continuously to avoid liner wrinkles; sharp objects and low pH (<7.0) damage liners.
- **New fiberglass**: verify manufacturer's water chemistry requirements — many void warranties for CH above ~300 ppm or sustained LSI imbalance.
- **Newly filled pool of any type**: test fill water first (Section 9); balance TA → pH → CH → CYA → then chlorinate.

---
## 2. Pool Types and Classifications

*Pool class determines which rules, chemistry ranges, and maintenance rhythms apply. An assistant should classify the user's pool before answering compliance or chemistry questions.*

### 2.1 Regulatory Classes

**Residential (private) pool** — serves a single household and its guests. Regulated mainly through building codes at construction (barriers, electrical, plumbing — often via the International Swimming Pool and Spa Code, ISPSC, or state residential code) and the federal VGB Act for drain covers on new construction in some states. No health-department operating permit, no operator certification, no mandated water-testing log — but the same physical and chemical hazards exist, so residential owners should voluntarily follow CDC Healthy Swimming guidance.

**Public pool** — owned/operated by a government body or open to the general public (municipal pools, waterparks, community pools). Requires a health-department operating permit, routine inspections, mandated water chemistry ranges, record-keeping, certified operators in most states, lifeguards or warning signage per code, VGB-compliant drains, and ADA-accessible entry.

**Commercial / semi-public pool** — serves a defined clientele rather than the whole public: hotels/motels, apartment complexes, HOAs, gyms/health clubs, campgrounds, schools. Most states regulate these as a subclass of "public pools" with the same or slightly relaxed requirements. Hotel and HOA pools are the most commonly cited facilities in health inspections; ADA and VGB fully apply.

**Special-use venues** — spas/hot tubs, wading/kiddie pools, splash pads/interactive water features, therapy pools, swim-school pools, competition pools. These have their own rules: e.g., the MAHC prohibits cyanuric acid (stabilized chlorine) in spas and therapy pools, requires secondary disinfection (UV/ozone) for increased-risk venues like splash pads, and sets higher minimum FC for spas (3.0 ppm).

### 2.2 Indoor vs. Outdoor Pools

| Factor | Outdoor | Indoor |
|---|---|---|
| UV chlorine loss | High — sunlight destroys unstabilized FC (50%+ in 2 h) | None from sun |
| CYA (stabilizer) | Needed: 30–50 ppm residential; ≤100 ppm max (MAHC/WHO) | **Not recommended** (0–20 ppm max); CYA only slows chlorine with no UV benefit |
| Algae pressure | High (sun + pollen + debris) | Low |
| Chloramine buildup | Vented naturally | **Major issue** — trichloramine accumulates in air; causes "indoor pool smell," eye/respiratory irritation, corrodes structures |
| Ventilation | Not applicable | Critical: 4–6 air changes/hour typical; ASHRAE 62.1 outdoor-air rates; air temp kept ~1–2 °C (2–4 °F) above water temp; relative humidity 50–60% |
| Dehumidification | Not applicable | Required to protect building envelope from condensation/corrosion |
| Heating | Optional/seasonal | Nearly always; higher evaporation control matters |
| Winterizing | Often required | Not required |
| Shock practice | Sunlight assists oxidation | Prefer non-chlorine shock (MPS) or superchlorinate with strong ventilation while unoccupied; UV secondary systems reduce chloramines |

**Indoor-pool chloramine management**: keep CC ≤ 0.2 ppm (residential) / below state action level (often 0.4–0.5 ppm public); enforce swimmer showers before entry; run UV or ozone if available; increase outdoor-air ventilation during and after shocking; never shock an occupied indoor pool.

### 2.3 Construction Types and Their Chemistry Implications

**Concrete / gunite / shotcrete with plaster, quartz, or pebble finish**
- Most durable and customizable; alkaline surface interacts with water constantly.
- Needs CH 200–400 ppm and LSI near 0 or it etches (low LSI) or scales (high LSI).
- Can be drained by professionals (hydrostatic-valve precautions); acid-washed every 5–10 years; replastered every 10–25 years.

**Vinyl liner**
- Steel/polymer walls with a fitted liner; lower build cost; liner replaced every ~8–12 years.
- pH below 7.0 makes liners brittle and wrinkled; FC held above ~10 ppm for long periods bleaches print; CH 150–250 ppm still recommended to protect metal components.
- **Never fully drain** — liners shrink and float; water loss behind the liner causes floating liners after heavy rain.

**Fiberglass (one-piece shell)**
- Fast install, smooth gelcoat resists algae, lowest chemical demand.
- Keep CH moderate (most manufacturers ~150–300 ppm) and avoid persistent high pH which chalks the gelcoat; metal stains show readily.
- Never drain without professional bracing — shells can pop out of the ground from groundwater pressure.

**Above-ground**
- Steel/resin walls with vinyl liner; smaller volumes (10,000–60,000 L) so chemical doses are small and errors proportionally large — dose carefully.
- Same vinyl chemistry rules; winterizing is critical in freeze climates; most collapses come from ice or water-level mistakes.

**Specialty types**
- **Saltwater pools** (any shell + SWG): salt 2,700–4,500 ppm per manufacturer; not "chlorine-free" — the SWG makes chlorine on site. Salt splash can degrade soft natural stone coping and corrode nearby metal; bonding/grounding must be correct.
- **Infinity/vanishing edge**: catch basin adds volume; higher evaporation; balance both bodies of water.
- **Natural/biological pools**: plant-filtered, no chlorine; not recognized as sanitary "public pools" by most U.S. codes — residential/European niche.
- **Spas/hot tubs**: 32–40 °C; tiny volumes (1,000–2,000 L) mean chemistry swings fast; FC 3–10 ppm (CDC minimum 3 ppm), **no CYA**, bromine 4–8 ppm as alternative; drain and refill every 4–12 weeks (rule of thumb: liters ÷ 10 ÷ daily bathers = days between drains). Hot-tub temperature safety max: 40 °C (104 °F).
- **Splash pads / interactive features**: recirculating types are regulated like public pools plus MAHC-required secondary UV/ozone disinfection because of high fecal-contamination risk to toddlers.

### 2.4 Choosing Ranges by Pool Type — Quick Matrix

| Parameter | Residential outdoor | Residential indoor | Public/commercial pool (MAHC-aligned) | Spa/hot tub |
|---|---|---|---|---|
| FC | 2–4 ppm with CYA 30–50 (CDC min 1 ppm without CYA, 2 ppm with) | 1–3 ppm, CYA 0–20 | 1.0 ppm min without CYA; 2.0 ppm min with CYA; ≤10 ppm max open to bathers | 3–10 ppm (CDC/MAHC min 3) |
| pH | 7.2–7.8 (CDC allows 7.0–7.8) | 7.2–7.8 | 7.2–7.8 | 7.2–7.8 |
| CC | ≤0.2 ppm | ≤0.2 ppm | ≤0.4 ppm action level (many states) | ≤0.5 ppm |
| TA | 60–120 ppm by surface/SWG | Same | 60–180 ppm per state code | 60–120 ppm |
| CH | Surface-dependent 150–400 ppm | Same | 150–400 ppm typical code range | 150–250 ppm |
| CYA | 30–50 ppm (≤100 absolute max) | 0–20 ppm | ≤100 ppm max (MAHC/WHO); some states lower | **0 — prohibited by MAHC in spas** |
| Temp | Comfort 25–29 °C | 26–30 °C | Code max varies | ≤40 °C (104 °F) |

---
## 3. Core Water Chemistry Parameters and Ideal Ranges

*Each parameter includes its role, ranges (residential and public), and impact on swimmers, surfaces, and equipment. Public-pool figures follow the CDC Model Aquatic Health Code (MAHC); residential figures follow CDC Healthy Swimming guidance and industry standards (ANSI/APSP/ICC-11).*

### 3.1 Free Chlorine (FC) — Primary Sanitizer

- **Role**: kills bacteria (E. coli, Pseudomonas), viruses (norovirus), and algae; oxidizes swimmer waste. Effectiveness depends heavily on pH and CYA.
- **Ranges**:
  - Residential without CYA: 1–3 ppm (CDC minimum 1 ppm).
  - Residential with CYA 30–50 ppm: 3–5 ppm; keep FC ≥ 7.5% of CYA (industry/Trouble Free Pool ratio; e.g., CYA 40 → FC ≥ 3).
  - Public (MAHC): minimum 1.0 ppm unstabilized, minimum 2.0 ppm where CYA is used, maximum 10 ppm while open to bathers. Spas: minimum 3.0 ppm.
- **Swimmer impact**: low FC = infection risk (recreational water illnesses). Sustained FC >10 ppm with bathers = irritation risk; U.S. venues must close above 10 ppm under MAHC.
- **Surface impact**: prolonged shock-level FC fades vinyl and some paints; low FC lets algae stain surfaces.
- **Equipment impact**: adequate FC prevents biofilm and chloramine corrosion. High FC at normal pH is not by itself strongly corrosive.
- **Kinetics note**: hypochlorous acid (HOCl) is the killing form. At pH 7.5, ~50% of FC is HOCl; at pH 8.0, only ~24%. This is why pH control is inseparable from sanitation.

### 3.2 Combined Chlorine (CC) — Chloramines

- **Role indicator**: formed when FC reacts with nitrogen compounds (sweat, urine, cosmetics). CC = TC − FC. High CC signals unmet oxidation demand.
- **Range**: ideal 0; residential act at >0.2 ppm; many state codes require action or closure at 0.4–0.5 ppm for public pools.
- **Swimmer impact**: eye/skin irritation and the misleading "too much chlorine" smell; airborne trichloramine causes respiratory irritation in indoor facilities (documented lifeguard/swimmer asthma associations).
- **Equipment/structure impact**: chloramine-laden indoor air corrodes stainless steel (including structural elements), HVAC components, and electronics.
- **Action**: breakpoint chlorination (Section 5.2), improve ventilation (indoor), enforce pre-swim showers, consider UV/ozone.

### 3.3 pH — Acidity/Basicity

- **Role**: controls chlorine effectiveness, swimmer comfort, and water aggressiveness.
- **Range**: 7.2–7.8 for all pool classes (optimal 7.4–7.6, matching human tears; CDC home guidance allows 7.0–7.8; MAHC requires 7.2–7.8 for public venues). SWG pools often target 7.2–7.6 to offset upward drift.
- **Swimmer impact**: <7.0 stings eyes and dries skin; >8.0 halves chlorine effectiveness and promotes chloramine irritation.
- **Surface impact**: low pH etches plaster/grout and wrinkles vinyl; high pH scales tile, waterline, and finishes.
- **Equipment impact**: low pH corrodes copper heat exchangers, pump seals, and metal fixtures (gas heaters are the most vulnerable); high pH scales heater cores, salt cells, and plumbing.
- **Drift drivers**: aeration, waterfalls, SWGs, and fresh plaster push pH up; trichlor tablets, acid rain, and heavy bather load push it down.

### 3.4 Total Alkalinity (TA) — pH Buffer

- **Role**: bicarbonate buffering that resists pH swings.
- **Range**: plaster 80–120 ppm; vinyl/fiberglass 80–100 ppm; SWG pools 60–80 ppm to slow pH rise; public codes commonly accept 60–180 ppm.
- **Low TA** (<60): pH "bounce," etching, corrosion, swimmer discomfort.
- **High TA** (>120–180): pH locks high, chronic scaling, cloudy water, more acid demand.
- **Interaction**: lowering TA requires acid plus aeration cycles (Section 5.4); TA and pH always move together when dosing acid.

### 3.5 Calcium Hardness (CH)

- **Role**: keeps water saturated with calcium so it neither dissolves surfaces nor deposits scale (LSI component).
- **Range**: plaster/pebble 200–400 ppm; vinyl 150–250 ppm; fiberglass ~150–300 ppm (check manufacturer); spas 150–250 ppm.
- **Low CH**: water pulls calcium from plaster/grout (pitting, "plaster dust"), foams in spas, and corrodes heat exchangers.
- **High CH** (>400–500): waterline scale, cloudy water, scaled heaters and salt cells — manage by dilution with softer water plus LSI control and sequestrants.
- **Verified dosing note**: cal-hypo chlorine adds ~0.7 ppm CH per 1 ppm FC added (stoichiometric; see Section 5.9), so cal-hypo-fed pools see CH creep over a season.

### 3.6 Cyanuric Acid (CYA) — Chlorine Stabilizer

- **Role**: shields FC from UV destruction outdoors. Without CYA, sunlight destroys most FC within ~2 hours; with 30 ppm CYA, daily loss drops dramatically.
- **Range**: outdoor residential 30–50 ppm (SWG pools often 60–80 per manufacturer); indoor 0–20 ppm; absolute maximum 100 ppm (adopted by both MAHC and WHO). **Prohibited in spas and therapy pools under the MAHC**.
- **Trade-off**: CYA binds chlorine reversibly — it protects FC but slows its kill rate. High CYA with ordinary FC produces "chlorine lock": tests show chlorine present, but sanitizing power is inadequate (this matters for Crypto response — Section 6.8).
- **Sources of creep**: every trichlor tablet (+0.6 ppm CYA per 1 ppm FC) and dichlor granule (+0.9 ppm CYA per 1 ppm FC). A trichlor-fed pool can gain 50–100 ppm CYA in one season.
- **Reduction**: partial drain/refill only (bio/chemical CYA removers exist but are unreliable).

### 3.7 Salt (NaCl) — for SWG Pools

- **Range**: 2,700–4,500 ppm depending on cell manufacturer; common target 3,200 ppm. (Seawater ≈ 35,000 ppm — pool salt levels are ~1/10 of that, below taste threshold for most people.)
- **Low salt**: cell stops producing or damages its coating; **high salt**: cell overload errors, salty taste, possible corrosion of soft stone and fixtures.
- Salt does not evaporate — it leaves only via splash-out, backwash, leaks, or drainage. Test monthly and after heavy rain dilution.

### 3.8 Temperature

- Comfort: 25–29 °C (78–84 °F) general swimming; 26–28 °C competition; 30–34 °C learn-to-swim/therapy; spas ≤40 °C (104 °F) safety limit — CPSC-recognized maximum.
- Every +10 °C roughly doubles chemical reaction rates: warmer water eats FC faster, grows algae faster, and scales heaters faster (temperature is an LSI input).
- Cold water (<10–15 °C): most SWG cells shut down automatically; chlorine demand is minimal.

### 3.9 Secondary Parameters

| Parameter | Target | Notes |
|---|---|---|
| Phosphates | <100–125 ppb ideal | Algae nutrient; high levels raise chlorine demand; remove with lanthanum products |
| Nitrates | ~0 | Algae nutrient from fertilizer/runoff; only dilution removes |
| Iron | <0.2 ppm (ideally 0) | Brown/orange stains, green tint with clear water; common in well water |
| Copper | <0.2 ppm (ideally 0) | Blue-green stains, green hair; sources: corroding heat exchangers (low pH), copper algaecides, some well water |
| Manganese | <0.05 ppm | Purple/black staining |
| TDS | <1,500 ppm above startup (non-salt pools) | Very high TDS dulls water and slows chlorine; managed by dilution |
| Borates (optional additive) | 30–50 ppm | Secondary pH buffer and algae suppressant; keep out of reach of pets (toxic if drunk in quantity) |
| ORP (probe systems) | 650–750 mV | Automation setpoint used in commercial pools; MAHC references ORP controllers ≥650 mV |

### 3.10 Langelier Saturation Index (LSI) — Balance Master Metric

LSI = pH + TF + CF + AF − TDSF (temperature, calcium, alkalinity, TDS factors). Target **−0.3 to +0.3** (0 is perfectly balanced; industry plaster guidance often targets 0.0 ± 0.3).

- LSI < −0.3: aggressive water → etching, metal corrosion, plaster/grout damage.
- LSI > +0.3: scale-forming → cloudy water, scaled tile/heaters/cells.
- Winter note: cold water drops LSI — a pool balanced at 28 °C can turn corrosive at 5 °C, which is why closing chemistry targets slightly positive LSI.
- Assistants should compute LSI whenever a user reports etching, scale, or persistent cloudiness with "normal" individual readings.

---
## 4. Testing Methods, Supplies, and Schedules

### 4.1 Methods Compared

| Method | Pros | Cons | Accuracy | Typical Use |
|---|---|---|---|---|
| Test strips (AquaChek, Clorox) | Fast, cheap, multi-parameter | Subjective color match, humidity-sensitive, expire | Low–medium | Daily quick checks, residential |
| Liquid DPD/OTO kits (Taylor K-2005) | Good accuracy, widely available | Drop counting, reagent expiry ~1 yr; DPD bleaches out above ~10 ppm FC | Medium | Weekly residential testing |
| FAS-DPD titration (Taylor K-2006/K-2006C, TF-100/TF-Pro) | High accuracy (±0.2 ppm FC/CC), reads to 50 ppm FC, no color judgment | Slower, costlier reagents | High | Gold standard for owners and techs; required for SLAM/shock verification |
| Digital photometers (LaMotte ColorQ, Hanna Checker) | Numeric readout, removes color-blindness issues | Cost, vial cleanliness, still reagent-based | High | Service techs, commercial |
| Electronic probes (pH pens, TDS meters) | Instant, reusable | Need calibration (pH 7 and 10 buffers), probes drift/degrade | Medium–high | Supplementary |
| Automated controllers (ORP/pH, e.g., commercial chemistry controllers) | Continuous control, MAHC-recognized | Cost, sensor maintenance, still require manual verification | High (when calibrated) | Public/commercial pools — many state codes require or credit them |
| Smart monitors (WaterGuru Sense, Sutro, pHin) | Continuous data, app alerts | Subscription, sensor cassettes, limited parameters | Medium–high | Residential convenience |
| Lab / pool-store analysis | Full panel incl. metals, phosphates, CYA verification | Slow, per-test cost; store results vary with operator | Very high (lab) | Quarterly cross-check, problem diagnosis |

**Testing best practices**: sample elbow-deep (30–45 cm) away from returns; test promptly; keep reagents cool, dark, and replace annually; rinse cells with pool water before reading; for CYA turbidity tests, perform at room temperature in good light and repeat for confirmation; cross-check home kit vs. store lab when they disagree before making big chemical moves.

### 4.2 What to Test When Diagnosing

- Cloudy water → FC, CC, pH, TA, CH (compute LSI), filter pressure.
- Algae → FC, CYA (FC:CYA ratio), phosphates.
- Stains → metals (Fe, Cu, Mn) on pool water AND fill water; sequestrant history.
- Irritation complaints → pH first, then CC, then FC extremes.
- Scale/etching → full LSI panel including temperature.

### 4.3 Testing Schedules

**Residential**

- Every swim day / daily in season: FC and pH (strips or probe fine).
- Weekly: FC, CC, pH, TA (FAS-DPD kit).
- Monthly: CH, CYA, salt (SWG).
- Quarterly & at every fill: metals, phosphates, TDS (store/lab).

**Public/commercial (verify your state code — these are common MAHC-aligned minimums)**

- Before opening daily + every 2–4 hours while open: FC/CC and pH (many states; high-use venues hourly).
- Continuous: ORP/pH via automated controller where required.
- Daily: temperature, clarity check (main drain visible), flow rate/filter pressure, water level.
- Weekly: TA, CH, CYA (if used), TDS.
- Records: log every reading with time and initials; retain per state rule (commonly 1–3 years); logs are inspected.

---

## 5. Chemical Adjustment and Dosing (Verified)

*All doses are for a 40,000 L (≈10,566 US gal) pool and were verified stoichiometrically for this manual (calculation basis in Section 5.9). Scale linearly by volume. Always follow the product label — U.S. law (FIFRA) makes label directions legally binding for registered pool chemicals. Run the pump during and after additions; add chemicals one at a time, hours apart or as labels direct.*

### 5.1 Raising and Lowering Free Chlorine

**To raise FC by 1 ppm in 40,000 L:**

| Product | Amount for +1 ppm FC | Side effects |
|---|---|---|
| Liquid chlorine 12.5% (sodium hypochlorite) | ~320 mL | Slight pH rise (mostly temporary), adds a little salt |
| Liquid chlorine 10% | ~400 mL | Same |
| Household bleach 6% (plain, unscented only) | ~670 mL | Same |
| Cal-hypo 65% granular | ~62 g | Adds ~0.7 ppm CH per 1 ppm FC; pre-dissolve for vinyl |
| Dichlor 56% granular | ~72 g | Adds ~0.9 ppm CYA per 1 ppm FC |
| Trichlor 90% tablets | ~44 g equivalent | Adds ~0.6 ppm CYA per 1 ppm FC; strongly acidic; feeder/floater only |

- Pour liquid chlorine slowly in front of a return jet with pump running; pre-dissolve granulars in a bucket of pool water (add product to water, never water to product) for vinyl/fiberglass.
- **To lower FC**: stop dosing and let sunlight burn it down; for fast reduction use sodium thiosulfate per label or partial drain/refill. Keep bathers out above 10 ppm (MAHC closure threshold) — for residential, common practice is to re-enter at ≤5 ppm (with CYA 30–50, up to the FC/CYA-appropriate level) and CC ≤0.2.

### 5.2 Combined Chlorine — Breakpoint Shock

- Field rule: raise FC by **10× the CC reading** in one dose (breakpoint chlorination). Example: CC 0.5 ppm → raise FC by 5 ppm.
- Use unstabilized chlorine (liquid or cal-hypo). Non-chlorine shock (MPS/potassium monopersulfate, ~100 g per 10,000 L per label) oxidizes contaminants without raising FC — preferred for indoor pools and spas; note MPS reads as CC on DPD tests unless a deoxidizer reagent is used.
- Shock at dusk (outdoor) or when closed (indoor, with full ventilation). Re-open per Section 5.1 re-entry levels.

### 5.3 pH

**To lower pH ~0.2 (typical 40,000 L pool at TA ~100):**
- Muriatic acid 31.45%: ~400–500 mL, poured slowly into the deep end in front of a return. (Exact response depends on TA — verify with a follow-up test after 1–2 h of circulation; acid also lowers TA.)
- Dry acid (sodium bisulfate 93%): ~500–600 g pre-dissolved. Adds sulfates — avoid long-term in SWG/plaster pools.

**To raise pH ~0.2:**
- Soda ash (sodium carbonate): ~400–450 g pre-dissolved (also raises TA ~+4 ppm per dose).
- Aeration alone raises pH without chemicals (point returns up, run water features) — best when TA is already adequate.
- Borax (sodium tetraborate): ~700 g raises pH with less TA impact.

### 5.4 Total Alkalinity

- **Raise**: sodium bicarbonate (baking soda) — verified ~670 g per +10 ppm TA in 40,000 L. Broadcast over the deep end; limit to roughly 700 g per 10,000 L per day to avoid temporary clouding.
- **Lower**: dose muriatic acid in stages (each ~200–250 mL lowers TA ~5–10 ppm and drops pH), then aerate to bring pH back up without re-adding alkalinity. Repeat over days; test daily. There is no chemical that lowers TA without lowering pH.

### 5.5 Calcium Hardness

- **Raise**: calcium chloride. Verified doses per +10 ppm CH in 40,000 L: ~590 g of dihydrate flake (77% products, e.g., DowFlake) or ~445 g of anhydrous (94–97%). Pre-dissolve and add slowly to the deep end (solution gets hot — handle with care); wait 4–6 h after adding before other chemicals.
- **Lower**: dilution with lower-CH water is the only real fix; manage unavoidable high CH with LSI control (run pH/TA at lower ends) plus scale inhibitor/sequestrant. Reverse-osmosis trailer services exist in hard-water regions (AZ, TX, S. CA).

### 5.6 Cyanuric Acid

- **Raise**: granular CYA — ~400 g per +10 ppm in 40,000 L (verified: CYA doses at its own weight; 100% active). Add via a sock in front of a return or in the skimmer (label permitting); it dissolves over 2–5 days — don't retest sooner, and don't backwash the undissolved product away.
- Liquid stabilizer works in hours but costs more.
- **Lower**: partial drain and refill (percentage drained ≈ percentage CYA reduction).

### 5.7 Salt (SWG pools)

- **Raise**: pool-grade salt (NaCl ≥99%, no additives/YPS). Verified: **20 kg raises 40,000 L by +500 ppm**. Broadcast into the shallow end, brush until dissolved, run pump 24 h, keep SWG off until dissolved and verified.
- **Lower**: partial drain/refill only.

### 5.8 Metals and Phosphates

- **Metals**: keep out (fill-water pre-filter), keep pH in range, and hold in solution with sequestrants (HEDP/phosphonate-based, e.g., Jack's Magic, ProTeam Metal Magic) dosed weekly per label. Existing stains: ascorbic-acid treatment for iron, citric for copper — then immediately sequester and rebalance (stain treatments crash FC and pH).
- **Phosphates**: lanthanum-chloride removers (Orenda PR-10,000, SeaKlear) cloud the water and load the filter — clean the filter afterward. Target <100–125 ppb when fighting recurring algae.

### 5.9 Dosing Calculation Basis (for Assistant Math)

For any target change, grams of product = Volume(L) × Δppm ÷ 1,000 ÷ active fraction. Verified constants used above:
- Sodium hypochlorite "trade %" ≈ g available chlorine per 100 mL → mL = (L × ΔFC/1000)/(% ÷ 100).
- Cal-hypo CH side-effect: Ca fraction (40/143) ÷ available chlorine (0.99) × 2.5 (CaCO₃ conversion) ≈ **0.7 ppm CH per 1 ppm FC**.
- Dichlor CYA side-effect: 50.6% CYA content ÷ 55.5% avail. Cl ≈ **0.9 ppm CYA per 1 ppm FC**. Trichlor: 55.5% ÷ 91.5% ≈ **0.6**.
- Baking soda TA factor: NaHCO₃→CaCO₃ equivalence 50/84 → 672 g per 10 ppm per 40,000 L.
- CaCl₂·2H₂O→CaCO₃ factor 147/100 → 588 g per 10 ppm per 40,000 L.
- Cross-check any dose with a reputable calculator (PoolMath/TFP, Orenda app) before large additions.

---
## 6. Chemical Safety, Storage, and Emergency Response

*Pool chemicals cause an estimated 4,500 U.S. emergency-department visits per year, about one-third involving children — most from inhaling fumes when opening containers or mixing, and from handling without PPE (CDC MMWR 2019 analysis of 2015–2017 data). Every rule in this section traces to CDC, OSHA, NIOSH, or EPA guidance; sources are listed in Section 16.*

### 6.1 The Non-Negotiable Rules

1. **NEVER mix chlorine products with acid.** Chlorine + muriatic acid releases chlorine gas. Chlorine gas is immediately dangerous to life or health (IDLH) at just 10 ppm in air (NIOSH); OSHA's permissible exposure ceiling is 1 ppm. This includes residues: never put acid in a bucket, feeder, or measuring cup that held chlorine, or vice versa.
2. **NEVER mix different chlorine types** — trichlor + cal-hypo contact can ignite or explode spontaneously. Never add a new chlorine type to a feeder that held another.
3. **NEVER add water to chemicals — always add chemicals to water** when pre-dissolving. Water added to acid or dry chlorine can boil, spatter, and generate violent gas release.
4. **Never pre-mix chemicals together** to "save a trip." One product per bucket, per trip, per pour.
5. **Keep all chlorine products dry.** A splash of water into a cal-hypo drum starts a self-heating reaction that can produce fire and toxic gas (cal-hypo is a NFPA-classed oxidizer).
6. Add trichlor tablets only to feeders/floaters, never the skimmer of a pool with a heater (acidified water pools in the plumbing and corrodes the heat exchanger when the pump starts).

### 6.2 Personal Protective Equipment (PPE)

- Minimum for any chemical handling: chemical-splash goggles (not just glasses) and chemical-resistant gloves (nitrile or neoprene).
- For acids and dusty granulars: add an N95 (dust) or acid-gas respirator cartridge for large jobs, plus long sleeves and closed shoes.
- Handle chemicals outdoors or with strong ventilation; open containers at arm's length, pointed away from the face, downwind.
- Commercial facilities: OSHA Hazard Communication (29 CFR 1910.1200) requires SDSs on site, labeled containers, and documented employee training; eyewash access is required where corrosives are handled (29 CFR 1910.151).

### 6.3 Storage Rules (CDC / EPA / NFPA-aligned)

- Cool, dry, well-ventilated, **locked**, out of children's and pets' reach; below 35 °C (95 °F) per CDC guidance.
- Original containers only, labels intact, lids tight. Never transfer to food/drink containers.
- **Physical separation**: acids away from chlorine products; oxidizers away from fuels/solvents/fertilizer; liquids never stored above solids (drips = reactions). Separate by distance and secondary containment trays, not just shelf position.
- Off the floor (moisture) and out of direct sun. Do not store liquid chlorine >1 season — it loses ~50% strength in 6–12 months in heat.
- No smoking near storage; keep an ABC extinguisher nearby but understand oxidizer fires may require flooding water — follow the SDS.
- Buy only a season's supply; dispose of unknown/old chemicals through household-hazardous-waste programs, never in trash or drains.

### 6.4 Safe Addition Practice

- Test first; dose to numbers, not habit. One chemical at a time; wait per label (typically ≥1 h between compatible products, 4–6 h or a full turnover between chlorine and acid; never simultaneous).
- Pump running during addition and for 1–4 h after.
- Pour liquids slowly at knee height in front of a return to avoid splash; broadcast pre-dissolved solutions.
- Keep bathers out per label re-entry rules (acid/chlorine: usually until circulated and in-range; shock: until FC back to allowed range).
- Never leave chemicals unattended on the deck, even briefly — this is the classic child-injury scenario.

### 6.5 Exposure First Aid (general; follow the product SDS)

- **Eyes**: flush with clean water ≥15 minutes, lids open; remove contacts; seek medical care for acids/hypochlorite.
- **Skin**: remove contaminated clothing; wash with soap and copious water ≥15 min.
- **Inhalation** (chlorine/acid fumes): move to fresh air immediately; if breathing difficulty, call 911. Symptoms of chlorine gas exposure: coughing, chest tightness, burning eyes/nose/throat, shortness of breath — can be delayed.
- **Ingestion**: do NOT induce vomiting; rinse mouth; call Poison Control (US: **1-800-222-1222**) or emergency services with the product label in hand.

### 6.6 Chemical Incident in the Pump Room / Chlorine Gas Release

1. Evacuate everyone upwind immediately; do not attempt rescue without proper respiratory protection.
2. Call 911 for any significant gas release or symptomatic exposure.
3. Shut down chemical feeders and recirculation only if it is safe to reach the controls. (A classic public-pool incident: pump stops while the chlorinator and acid feeder keep injecting; on restart the accumulated slug of mixed chemicals gasses the pool — MAHC-based interlock rules now require feeders wired to shut off when flow stops. Verify your feeders are interlocked.)
4. Ventilate before re-entry; re-enter only when cleared (fire department has gas meters).

### 6.7 Fecal, Vomit, and Blood Contamination Response (CDC)

- **Formed stool**: close pool; remove material with a net/scoop (never vacuum into the filter); raise/confirm FC 2 ppm or higher (pH ≤7.5) and keep contaminated area circulating 25–30 minutes; disinfect the scoop; reopen when levels verified.
- **Diarrheal incident** (assume *Cryptosporidium*): close pool. Crypto is extremely chlorine-tolerant — standard FC does almost nothing. CDC hyperchlorination: raise FC to **20 ppm and hold 12.75 hours** (CT ≈ 15,300 mg·min/L) with pH ≤7.5 and CYA ≤15 ppm. **If CYA >15 ppm, partially drain and dilute to bring CYA ≤15 before hyperchlorinating (CDC precondition), because CYA drastically slows Crypto kill; consult the current CDC fecal-incident response guide for any extended-CT alternative.** Backwash filter to waste after treatment.
- **Vomit**: treat like formed stool unless swimmer likely has norovirus/was ill, then treat conservatively (norovirus needs elevated CT; follow CDC guidance).
- **Blood**: no documented transmission risk via properly chlorinated water; clean deck spills with 1:10 bleach solution; no closure required by CDC, though brief voluntary closure reassures patrons.
- Public pools: log every incident (time, type, response, readings) — inspectors ask.

### 6.8 Why CYA Changes Emergency Math

CYA binds chlorine and slows its kill rate. For everyday bacteria this is managed by the FC:CYA ratio; for Crypto it makes normal remediation impossible — hence the CDC's CYA ≤15 ppm precondition for the 20 ppm protocol above. Public venues that use stabilized chlorine should keep CYA at the low end deliberately. Spas and therapy pools must not use CYA at all (MAHC).

### 6.9 Handling Specific Chemicals — Hazard Notes

| Chemical | Main hazards | Key handling points |
|---|---|---|
| Liquid chlorine / bleach (NaOCl 6–12.5%) | Corrosive to eyes/skin; releases chlorine gas with acid | Goggles + gloves; pour low and slow; degrades in heat/sun |
| Cal-hypo (granular/tabs 65–73%) | Strong oxidizer; fire/explosion if contaminated (organics, trichlor, glycols); dust irritant | Keep bone-dry and isolated; dissolve product-into-water; never in trichlor feeders |
| Trichlor tabs (90%) | Strongly acidic; slow chlorine gas release in confined wet spaces; explosive with cal-hypo | Feeder/floater only; store away from cal-hypo and ammonia |
| Dichlor | Milder oxidizer; adds CYA | Same oxidizer rules |
| Muriatic acid (HCl 14.5–31.45%) | Corrosive; fumes (OSHA ceiling 5 ppm HCl) | Open outdoors; acid into water; acid-rated gloves/goggles; never near chlorine |
| Dry acid (sodium bisulfate) | Corrosive dust | Avoid inhalation; adds sulfate |
| Soda ash / baking soda / borax | Low hazard; dust/eye irritation | Basic dust care |
| Calcium chloride | Exothermic when dissolving (solution gets hot); irritant | Dissolve slowly in small batches; add product to water |
| MPS non-chlorine shock | Oxidizer, dust irritant | Standard oxidizer care |
| Algaecides (quats/polyquat/copper) | Eye irritants; copper stains | Dose precisely; avoid overdose foaming (quats) |
| CO₂ / acid-feed systems (commercial) | Asphyxiant in enclosed rooms | Ventilation + gas monitor in chemical rooms |

---
## 7. Circulation, Filtration, and Equipment

### 7.1 Circulation Fundamentals

- **Turnover** = time to filter one full pool volume. Residential practice: 1–2 turnovers/day (8–12 h pump runtime in season, less off-season; variable-speed pumps run longer at low speed for better filtration and lower cost). Public codes mandate maximums, commonly 6 h for pools, 2 h for wading pools, 30 min for spas (state-specific).
- Flow path: skimmer + main drain → pump strainer → filter → heater → sanitizer feeder/SWG (always LAST in line, protected by a check valve) → returns.
- Aim returns to create a circular flow; brush dead spots (steps, corners, behind ladders) weekly — algae starts where water doesn't move.
- Skimmer weirs, baskets, and pump strainers: check/empty weekly or after storms.

### 7.2 Filters

| Type | Filtration fineness | Maintenance | Notes |
|---|---|---|---|
| Sand | 20–40 µm | Backwash when pressure +8–10 psi over clean baseline; deep-clean or replace sand every 3–7 yrs | Tolerant workhorse; add clarifier or skip using DE powder trick for finer filtering |
| Cartridge | 10–20 µm | Hose off every 2–4 weeks in season; acid/degreaser soak 1–2×/yr; replace elements every 1–3 yrs | No backwash water waste; don't pressure-wash (embeds dirt) |
| DE (diatomaceous earth) | 2–5 µm (finest) | Backwash + recharge with DE slurry; full teardown 1–2×/yr; grids last 5–10 yrs | Best clarity; DE powder is a respirable hazard — wear a mask when handling; dispose per local rules |

Record the "clean filter pressure" after every cleaning; that baseline is the reference for the +8–10 psi rule.

### 7.3 Pumps

- Single-speed vs. variable-speed (VS): U.S. DOE efficiency rules effectively require VS motors for most new residential filter pumps ≥1 THP (10 CFR 431; in force since July 2021). VS pumps cut energy 50–80%.
- Never run dry; never run against closed valves. Prime loss → check strainer lid O-ring, water level, suction leaks.
- Freeze protection: run the pump continuously when air temp nears 0 °C if not winterized.

### 7.4 Heaters and Heat Pumps

- Gas heaters: fastest heat; copper/cupronickel exchangers are the pool's most chemistry-sensitive part — low pH dissolves them (copper stains follow), high LSI scales them. Bypass or check-valve any trichlor feeder downstream.
- Heat pumps: efficient in warm air; titanium exchangers resist corrosion but still scale; maintain CH/LSI.
- Solar: chemistry-neutral; panels add volume; run pump when sun is on panels.

### 7.5 Salt-Water Chlorine Generators (SWG)

- Inspect cell every 2–3 months; clean scale only when visible: 4:1 water:muriatic-acid soak, few minutes, rinse (over-acid-washing shortens cell life).
- Keep pH 7.2–7.6 and TA 60–80 to slow scale; cells self-report low-salt/low-temp cutoffs.
- Cell lifespan 3–7 yrs (≈10,000 h); "% output" and runtime set chlorine production — recalculate after season change.

### 7.6 Automation, Controllers, and Interlocks

- ORP/pH controllers dose to setpoints (ORP 650–750 mV) — standard in commercial pools, credited or required by many state codes; calibrate probes monthly.
- **Feeder interlock (safety-critical)**: chemical feeders must stop when circulation stops (flow switch/electrical interlock) to prevent the chlorine-gas restart incident described in 6.6. Verify on every commercial system and any residential system with both acid and chlorine feeds.
- GFCI protection is required for pool pumps, lights, and outlets (NEC Art. 680); bonding grid must connect all metal within 1.5 m of water.

### 7.7 Equipment–Chemistry Interlock Table

| Equipment | Sensitive to | Failure mode | Prevention |
|---|---|---|---|
| SWG cell | High pH/CH/TA (scale), low salt | Scaled plates, coating wear | TA 60–80, pH ≤7.6, clean sparingly, salt in range |
| Gas heater | Low pH, high LSI, trichlor feeders | Corroded or scaled exchanger, leaks, soot | pH 7.4–7.6, LSI ±0.3, check valve before feeder |
| Heat pump | High CH | Scaled titanium coil, efficiency loss | CH toward low end in hard-water areas |
| Cartridge filter | Scale, algae, oils | Blinded fabric, short cycles | Balanced LSI, degrease yearly, phosphate control |
| Sand filter | Oils, high CYA water chemistry neglect | Channeling, mudballing | Backwash discipline, periodic deep clean |
| DE filter | High CH, algae | Caked/scaled grids | Teardown cleans, correct DE charge |
| Pump seals/o-rings | Low pH, high FC over time | Leaks, motor bearing failure from drips | Balanced water, replace seals at signs of weeping |
| Vinyl liner | pH <7.0, FC >10 sustained, low water | Brittleness, fading, wrinkles, floating | Keep in range; never fully drain |
| Plaster | LSI extremes | Etching or scale/mottling | LSI −0.3…+0.3, correct startup |
| Auto-cover | Low pH condensate, chloramines under cover | Corroded mechanism | Vent after shocking; rinse tracks |

---

## 8. Seasonal Maintenance

### 8.1 Spring Opening (freeze climates)

1. Clean deck area first; remove, clean, dry, and store the winter cover.
2. Reinstall drain plugs, returns, skimmer baskets; reconnect pump/filter/heater; lubricate O-rings.
3. Raise water to mid-skimmer; prime pump; start circulation and check for leaks (equipment pad + visible plumbing).
4. Test fill/pool water fully (FC, CC, pH, TA, CH, CYA, metals, salt).
5. Balance in order: **TA → pH → CH → CYA → chlorine** (CYA can go in early since it dissolves slowly).
6. Shock to 10–12 ppm FC (or SLAM to your CYA-based shock level); run pump 24 h; brush entire pool.
7. Clean or backwash the filter; recheck chemistry daily until FC holds overnight and water is clear; then start SWG (if fitted) once salt verified and water ≥15 °C.

### 8.2 Peak Season

- FC + pH each swim day; weekly full test; monthly CYA/CH/salt.
- Shock after: heavy bather load, storms/heavy rain, CC >0.2, visible algae, water temp spikes.
- Brush + vacuum weekly; empty baskets; monitor filter pressure; maintain water level mid-skimmer.
- Watch CYA creep in trichlor pools — if CYA passes ~70–80 ppm, switch to liquid chlorine/cal-hypo for the rest of season.

### 8.3 Autumn Closing (freeze climates)

1. A week ahead: balance water (pH 7.4–7.6, TA per surface, CH in range; slightly positive LSI for cold water), brush and vacuum.
2. Shock to 10–12 ppm; add polyquat 60 algaecide and optional winter borate/enzyme; circulate 24 h.
3. Lower water level per cover type (mesh: 30–45 cm below skimmer or per manufacturer; solid: just below skimmer/return line unless using an Aquador/skimmer plug system).
4. Blow out plumbing lines with a compressor/shop vac and plug with expansion plugs; add pool antifreeze (propylene glycol pool-grade, NEVER automotive) to lines that can't be fully cleared.
5. Drain pump, filter, heater, SWG, chlorinator completely; store fragile parts indoors; leave valves open/mid-position.
6. Install and tension the cover; use air pillows under solid covers on above-ground pools.
7. Do NOT drain the pool itself — hydrostatic pressure destroys empty shells and liners.

### 8.4 Winter (closed or mild-climate running)

- Closed pools: monthly cover check, pump off cover water, top up pool if level drops below plumbing, peek at chemistry on thaws (a mid-winter FC/pH check prevents spring swamps).
- Mild climates (pool runs all year): keep FC in range (demand is low), run pump enough to filter and to protect from freezes (continuous when <0 °C), watch LSI — cold water is corrosive; SWGs stop below ~10–15 °C so supplement with liquid chlorine.

---

## 9. Water Source Considerations

*Always test fill water before first fill and at every major top-up; it sets your baseline and explains recurring problems.*

| Source | Typical issues | Pre-treatment |
|---|---|---|
| Municipal | High pH/TA; chlorine or chloramines present; occasionally phosphates added for pipe protection | Adjust TA/pH down after fill; phosphates may need removal |
| Well | Iron/manganese, high CH (or very soft), CO₂ (low pH), sulfur | Fill through a metal/sediment pre-filter; sequestrant immediately; aerate for CO₂ |
| Rain/cistern | Very soft, acidic, no CYA/CH | Raise TA, CH, pH substantially |
| Water delivery (truck) | Varies — ask for source analysis | Test on delivery |
| Softened household water | Near-zero CH | Blend with unsoftened or raise CH after fill |

Fill tips: inline hose pre-filters (carbon/RV type) remove sediment and some metals; run the hose through the skimmer only if lines are clean; log the fill date and starting chemistry in the pool binder.

---
## 10. Troubleshooting

### 10.1 Quick Troubleshooting Table

| Symptom | Most likely cause | Immediate action | See |
|---|---|---|---|
| Cloudy/dull water | High pH/LSI, low FC, or poor filtration | Test FC & pH; correct; run filter 24 h; clarifier if needed | 3.3, 3.10, 7.2 |
| Green water / algae on walls | Low FC for the CYA level ("chlorine lock") | Brush, SLAM/shock, run pump 24/7, verify CYA | 3.6, 10.2 |
| Mustard-yellow dust on shaded walls | Yellow/mustard algae | Brush + shock higher than normal; treat equipment & swimsuits too | 10.2 |
| Black spots on plaster | Black algae (rooted) | Aggressive brushing (stainless brush on plaster), spot-treat, extended high FC | 10.2 |
| Strong "chlorine" smell, red eyes | Chloramines (CC >0.2), often with pH off | Test pH & CC; breakpoint shock; ventilate if indoor | 3.2, 5.2 |
| Eye/skin irritation | pH out of range; high CC; very high FC | Test pH first, then CC/FC | 3.3 |
| White flakes/scale at waterline or in SWG stream | High LSI (pH/CH/TA/temp); SWG cell scale | Lower pH/TA; clean cell; LSI math | 3.10, 7.5 |
| Pitted/rough plaster, grout loss | Low LSI (low CH/pH/TA) | Raise CH, correct pH/TA | 3.5, 3.10 |
| Brown/green/black stains | Metals (Fe/Cu/Mn) | Sequestrant; ascorbic/citric test-spot; check fill water & heater | 5.8 |
| Green-tinted clear water; blond hair turning green | Copper in solution | Test Cu; sequester; find source (heater corrosion? algaecide?) | 5.8 |
| FC disappears daily, no algae | Low CYA (outdoor sun) or high organic load | Raise CYA to 30–50; overnight FC loss test | 3.6, 10.3 |
| FC won't register after big dose | Extreme demand (ammonia after winter) or reagent bleach-out at high FC | FAS-DPD test (not strips); dose in stages | 4.1 |
| pH keeps falling | Trichlor tabs, acid rain, low TA | Raise TA; consider switching sanitizer | 3.4 |
| pH keeps rising | New plaster, SWG, high TA, aeration | Lower TA toward 60–80; acid routine | 3.3, 3.4 |
| Salt cell shows low output | Scale on plates, cold water, low salt, aged cell | Inspect/clean; verify salt with independent test | 7.5 |
| High filter pressure | Dirty filter, scale in media | Backwash/clean; deep-clean per type | 7.2 |
| Low flow, air bubbles at returns | Suction-side leak, low water, clogged strainer/impeller | Check level, lids/O-rings, baskets | 7.3 |
| Foaming | Quat algaecide overdose, soft water (spas), soaps/lotions | Skim, dilute, use polyquat next time, raise CH (spa) | 5.8 |
| Sand in pool | Broken filter lateral | Open filter and replace | 7.2 |
| DE returning to pool | Torn grid/manifold crack | Teardown and replace | 7.2 |

### 10.2 Green Pool Recovery (SLAM Procedure)

1. Test CYA first — it sets your shock target. (SLAM = Shock Level And Maintain, the Trouble Free Pool method: shock FC ≈ 40% of CYA, e.g., CYA 40 → shock FC 16.)
2. Brush the whole pool; clean baskets; set filter to run 24/7.
3. Raise FC to shock level with liquid chlorine; retest every few hours at first, re-dosing back to shock level each time. Use FAS-DPD (strips and DPD can't read high FC).
4. Maintain shock level until ALL three pass: water clear, CC ≤0.5, and overnight FC loss ≤1.0 ppm (test at dusk and dawn with no sun).
5. Let FC drift down to normal range; clean the filter; verify pH last (pH readings are invalid while FC >10).
6. Yellow/mustard algae: same, but hold a higher "mustard shock" level ~24 h and chlorinate ladders, toys, swimwear, behind lights. Black algae: weeks of brushing + sustained high FC; on plaster use a stainless brush and trichlor-tab spot scrub with gloves.
7. Persistent re-blooms → test phosphates, check dead spots and filter condition, verify CYA hasn't crept up.

### 10.3 Diagnostic Tests Worth Knowing

- **Overnight FC Loss Test (OCLT)**: dose at dusk, test at dawn; loss >1 ppm with no sun = live organics/algae or ammonia — keep shocking.
- **Bucket test for leaks**: bucket of pool water on a step, water level marked inside and out; if pool drops faster than bucket over 24–48 h (pump on, then repeat pump off), you have a leak, and on/off difference localizes it to plumbing vs. shell.
- **Two-source test verification**: before any drastic action (drain, huge acid dose), confirm the reading with a second method/kit.

## 11. Common Myths and Mistakes

| Myth | Reality | Why it matters |
|---|---|---|
| "Strong chlorine smell = too much chlorine" | It's chloramines — the pool needs MORE oxidation (breakpoint shock), not less chlorine | Users cut chlorine and make it worse |
| "Clear water = safe water" | Crypto and other pathogens survive in sparkling water if FC/CYA is off | Test, don't eyeball |
| "My pH is always high; I'll just keep adding acid" | Chronic high pH usually means high TA or aeration; fix TA | Endless acid = sulfate/TDS creep and yo-yo pH |
| "Stabilizer is optional" / "more stabilizer is better" | CYA 30–50 outdoors is essential; >100 ppm locks chlorine | Both extremes cause algae/illness risk |
| "Any grocery bleach works" | Only plain, unscented, non-splashless sodium hypochlorite | Additives cause foam/film |
| "Shock and swim in an hour" | Re-enter only when FC is back in allowed range (often 8–24 h); MAHC closes venues >10 ppm | Chemical burns/irritation |
| "Tablets are maintenance-free" | Each tablet adds CYA and acid; season-long creep | Monitor CYA monthly |
| "Algaecide clears green pools" | Chlorine kills blooms; algaecide is prevention/insurance | Wasted money, delayed fix |
| "Vinyl/fiberglass pools don't need calcium" | Low CH still corrodes heaters, rails, and causes foam | Equipment protection |
| "Saltwater pools have no chlorine" | The SWG makes chlorine from salt | Same testing duties apply |
| "Rain fills = free water top-up, no action" | Rain is soft/acidic, dilutes CYA/salt/CH and adds runoff contaminants | Retest after storms |
| "Drain the pool to fix anything" | Empty shells heave/pop; liners shrink | Professional guidance for drains |
| "Peeing in the pool is harmless" | Urine + chlorine = chloramines and cyanogen chloride irritants | It literally creates the "chlorine smell" |
| "A pool cover means no chemistry" | Covered pools still consume sanitizer (slower) and pH drifts | Monthly checks minimum |
| "Pool store tests are always right" | Store results vary with operator/reagents; home FAS-DPD is often more consistent | Cross-check before big corrections |

---
## 12. U.S. Regulatory and Normative Framework

*Disclaimer: this section is informational, not legal advice. Pool regulation in the U.S. is primarily **state and local**; federal law covers specific hazards (entrapment, accessibility, chemical registration, worker safety). Codes change — always verify the current text with the authority having jurisdiction (AHJ): your state health department and local building department. Citations current as of mid-2026.*

### 12.1 Federal Requirements

**Virginia Graeme Baker Pool & Spa Safety Act (VGB Act, 15 U.S.C. §8001 et seq., effective Dec 19, 2008)**
- Applies to ALL public pools and spas (including hotels, HOAs, gyms, campgrounds).
- Every drain/suction outlet must have an anti-entrapment cover conforming to the successor standard ANSI/APSP/ICC-16 2017 (incorporated by CPSC rule, 16 CFR Part 1450).
- Single-main-drain pools need a secondary anti-entrapment system (SVRS, suction-limiting vent, gravity drainage, automatic pump shut-off) or drain disablement.
- Covers have a marked service life; replacement on schedule is a compliance item. Enforced by CPSC; states received incentive grants to adopt matching residential rules.

**Americans with Disabilities Act (ADA) — 2010 Standards for Accessible Design (28 CFR Parts 35/36)**
- Public-accommodation and government pools must provide accessible entry: pools with <300 linear ft of pool wall need at least one accessible means of entry (pool lift or sloped entry); ≥300 linear ft need two (primary must be lift or sloped entry). Wading pools: sloped entry; spas: lift, transfer wall, or transfer system.
- Applies to existing pools ("readily achievable" barrier removal for Title III businesses), not private residential pools.

**EPA — FIFRA (7 U.S.C. §136) and labeling**
- All sanitizers/algaecides sold as pesticides must be EPA-registered; **the label is law** — using a pool chemical inconsistently with its label is a federal violation. Check for the EPA Reg. No. on any sanitizer.
- Discharge of pool water (dechlorinated, pH-neutral) is regulated locally under Clean Water Act-derived municipal rules — never drain chlorinated water to storm drains without checking local requirements.

**OSHA (29 CFR 1910)** — applies to facilities with employees:
- Hazard Communication 1910.1200: SDS library, container labeling, employee training on pool chemicals.
- PPE (1910.132), eye/face protection (1910.133), eyewash where corrosives are used (1910.151).
- Exposure limits relevant to pump rooms: chlorine gas ceiling 1 ppm (PEL); hydrogen chloride ceiling 5 ppm; NIOSH IDLH for chlorine 10 ppm.
- Bloodborne Pathogens 1910.1030 for lifeguard/first-aid staff.

**CPSC guidance (non-mandatory but widely adopted)**
- Publication 362 "Safety Barrier Guidelines for Residential Pools": fence ≥48 in (1.22 m), self-closing self-latching gates opening outward from the pool, openings <4 in, and door alarms/power safety covers where the house is a barrier wall. Most state/local residential codes (and the ISPSC/IRC Appendix) mirror these numbers.
- Spa water max 104 °F (40 °C).

### 12.2 CDC Model Aquatic Health Code (MAHC)

- Voluntary model code (current: 4th edition, 2023) that states/localities adopt in whole or part; it is the de-facto national benchmark for public aquatic venues.
- Key MAHC water quality values: FC minimum 1.0 ppm (unstabilized) / 2.0 ppm (with CYA); spas minimum 3.0 ppm; FC maximum 10 ppm while open; pH 7.2–7.8; CYA ≤100 ppm (aligned with WHO); CYA prohibited in spas and therapy pools; secondary disinfection (UV/ozone) required for increased-risk venues (splash pads, wading pools).
- Also covers: certified operator training, lifeguard staffing, fecal-incident response, chemical-room design and feeder interlocks, turnover rates, signage, and record-keeping.
- The Council for the MAHC (CMAHC) manages the triennial revision cycle.

### 12.3 Industry Consensus Standards (ANSI)

- ANSI/APSP/ICC-16 2017 — suction outlet fittings (the VGB standard).
- ANSI/APSP/ICC-11 — water quality for public pools/spas (chemical operational ranges).
- ANSI/APSP/ICC-7 — entrapment avoidance in pool/spa suction systems.
- ANSI/PHTA/ICC-5 — residential in-ground pools (design/build); -4 above-ground; -3 permanently installed residential spas; -14 portable spas; -15 residential pool/spa energy efficiency.
- ICC **International Swimming Pool and Spa Code (ISPSC)** — model construction code (2024 current edition) adopted by many states/municipalities; covers barriers (48-in fences, gate hardware), suction entrapment, decks, diving envelopes, energy, and references the APSP standards.
- NSF/ANSI 50 — certification for pool equipment (filters, feeders, SWGs, drain covers testing).
- NFPA and IFC chapters govern bulk chemical storage in commercial plants.

### 12.4 State Regulation — How It Works and Key Examples

Public/commercial pools: every state has a health code chapter with an operating permit, water quality table, operator requirements, and inspection scheme. Residential pools: regulated at construction through the state building/residential code (many adopt the ISPSC or IRC Appendix G barriers).

| State | Public pool code | Notable points (verify current text) |
|---|---|---|
| Florida | FAC Chapter 64E-9 (Dept. of Health) | Permit + engineering review; FC range roughly 1–10 ppm pools / spas up to 10; pH 7.2–7.8; trained/certified operator required; strict signage; residential barriers under FL Building Code (Ch. 454) with the Residential Swimming Pool Safety Act (Ch. 515 F.S.) |
| California | 22 CCR §65503 et seq. + Health & Safety Code §§115920–115929 (SB 442) | Public FC minimum 1.0 ppm (spas 3.0), pH 7.2–7.8; **residential**: SB 442 requires TWO of seven drowning-protection features on new/remodeled home pools (enclosure, alarms, covers, etc.); Title 24 energy rules for pumps |
| Texas | 25 TAC Chapter 265, Subchapter L (2020 "TX pool code," MAHC-based) | FC min 1.0 ppm pools / 3.0 spas; CYA cap (≤100); certified operator for Class A/B; strong entrapment rules (post-VGB state) |
| New York | 10 NYCRR Subpart 6-1 (pools), 6-3 (aquatic spray grounds) | FC min commonly 0.6 ppm unstabilized pools (higher with CYA; spas 1.5); pH 7.2–7.8; supervision Level rules for lifeguards; NYC has additional Health Code Art. 165 |
| Arizona | AAC R18-5-2 Article 2 + county codes (e.g., Maricopa Ch. VI) | County health departments run programs; ARS §36-1681 residential barrier statute (48-in fence etc.); high evaporation/CH management is a regional practice issue |

**Operator certification**: most states require a certified operator for public pools — accepted credentials commonly include PHTA **Certified Pool Operator (CPO)**, NRPA **Aquatic Facility Operator (AFO)**, or state-specific courses. Even where optional (some residential-only contexts), certification is industry best practice for anyone maintaining commercial water.

**Contractor licensing**: pool construction/repair generally requires a state contractor license (e.g., FL CPC license, CA C-53); electrical work must meet NEC Article 680 and be permitted.

### 12.5 Compliance Checklist by Pool Class

**Residential owner**
- Barrier/fence per local code (typically ≥48 in, self-closing/latching gate) + door alarms where required (check state, e.g., CA SB 442 two-feature rule).
- VGB-style dual drains/compliant covers on new construction (state building code).
- GFCI + bonding per NEC 680 (any electrical work permitted/inspected).
- Drain/discharge rules before emptying pool water.
- Insurance disclosure; "attractive nuisance" liability awareness — barriers matter legally, not just morally.

**Public/commercial operator**
- Health-department operating permit displayed; annual renewals; plan review before modifications.
- Certified operator (CPO/AFO or state equivalent) named and current.
- Daily water-chemistry logs retained (state-specified, often 1–3 yrs).
- VGB drain-cover documentation with service-life dates.
- ADA-accessible entry maintained and usable (lift battery charged, not stored away).
- Lifeguards or approved warning signage per bather load/venue class.
- SDS library, chemical-room ventilation, feeder interlocks, staff HazCom training (OSHA).
- Fecal/vomit/blood incident SOP posted (per CDC/MAHC); emergency action plan; rescue equipment inspected.
- Bather-load limits posted; MAHC-based turnover and clarity (main drain visible) standards met.

---

## 13. Public and Commercial Pool Operations Primer

*For users operating hotel, HOA, gym, campground, or municipal pools — beyond residential practice.*

- **Bather load**: codes cap occupancy by surface area (common legacy formula ~1 bather per 2–2.5 m² of water; state-specific). Post the limit.
- **Turnover compliance**: verify flow meter readings against the permit (pools commonly ≤6 h; spas ≤30 min; wading ≤1–2 h).
- **Chemical controllers**: ORP ≥650 mV setpoint typical; manual verification tests still required by code even with automation.
- **Daily opening routine**: test & log chemistry, check main-drain visibility (clarity closure standard), drain covers intact, safety equipment in place, gates/latches working, first-aid stocked, phone works.
- **Shock/superchlorination**: schedule while closed; post signage; verify FC ≤10 ppm (or state re-entry level) before reopening.
- **Staff**: certified operator on record; lifeguard certifications current; documented chemical-safety training for anyone touching chemicals (this is the single biggest injury-prevention lever per CDC).
- **Records that inspectors request**: chemistry logs, incident log (fecal/injury), maintenance log (cell cleaning, filter service, cover replacements), operator certificates, permits.

---
## 14. Glossary

- **AFO** — Aquatic Facility Operator; NRPA operator certification accepted by many states.
- **AHJ** — Authority Having Jurisdiction; the agency whose code applies to your pool.
- **Bather load** — Maximum simultaneous swimmers allowed by code for a venue.
- **Breakpoint chlorination** — Chlorine dose (~10× CC) that fully oxidizes chloramines instead of creating more.
- **Bonding** — Electrically connecting all metal near the pool to eliminate voltage gradients (NEC 680).
- **Cal-hypo** — Calcium hypochlorite; unstabilized granular/tablet chlorine, adds ~0.7 ppm CH per 1 ppm FC.
- **CC (Combined Chlorine)** — Chloramines; FC bound to nitrogen compounds; irritant, smelly, weak sanitizer.
- **CH (Calcium Hardness)** — Dissolved calcium measured as CaCO₃.
- **Chlorine lock** — Sluggish, ineffective chlorine caused by excessive CYA relative to FC.
- **CPO** — Certified Pool Operator (PHTA); the most widely recognized U.S. operator credential.
- **Crypto (Cryptosporidium)** — Chlorine-tolerant parasite; leading cause of pool diarrhea outbreaks; requires hyperchlorination (Section 6.7).
- **CT value** — Concentration × time; disinfection dose metric (mg·min/L) used in CDC remediation protocols.
- **CYA (Cyanuric Acid)** — Stabilizer/conditioner protecting FC from UV; max 100 ppm; banned in spas (MAHC).
- **Dichlor** — Stabilized granular chlorine; adds ~0.9 ppm CYA per 1 ppm FC.
- **DPD / FAS-DPD** — Colorimetric and titration chlorine test chemistries; FAS-DPD is the precision method.
- **Free Chlorine (FC)** — Active sanitizing chlorine (HOCl + OCl⁻).
- **GFCI** — Ground-fault circuit interrupter; required on pool electrical circuits.
- **Hydrostatic relief valve** — One-way valve in the pool floor that lets groundwater in to stop an empty shell from floating.
- **IDLH** — Immediately Dangerous to Life or Health concentration (NIOSH); chlorine gas = 10 ppm.
- **ISPSC** — International Swimming Pool and Spa Code (ICC model construction code).
- **LSI (Langelier Saturation Index)** — Scale/corrosion balance index from pH, TA, CH, temperature, TDS; target ±0.3.
- **MAHC** — CDC Model Aquatic Health Code; national model health code for public aquatic venues.
- **MPS** — Potassium peroxymonosulfate; non-chlorine oxidizer shock.
- **Muriatic acid** — ~31.45% hydrochloric acid; lowers pH/TA.
- **NSF/ANSI 50** — Equipment certification standard for pool products.
- **OCLT** — Overnight Chlorine Loss Test; ≤1 ppm loss overnight indicates organics are defeated.
- **ORP** — Oxidation-Reduction Potential (mV); automation proxy for sanitizer activity; ≥650 mV typical setpoint.
- **PHTA** — Pool & Hot Tub Alliance (formerly APSP/NSPF); standards body and CPO issuer.
- **Polyquat 60** — Non-foaming, copper-free polymer algaecide.
- **ppm** — Parts per million (= mg/L).
- **RWI** — Recreational Water Illness (e.g., crypto, giardia, legionella, pseudomonas rash).
- **Sequestrant / chelator** — Chemical that binds dissolved metals to prevent staining.
- **SLAM** — Shock Level And Maintain; CYA-indexed algae elimination method.
- **SDS** — Safety Data Sheet; hazard document required for every chemical on site.
- **SVRS** — Safety Vacuum Release System; anti-entrapment device for single-drain pools.
- **SWG** — Salt-Water chlorine Generator (electrolytic cell).
- **TA (Total Alkalinity)** — Bicarbonate buffer capacity.
- **TDS** — Total Dissolved Solids.
- **Trichlor** — Stabilized slow-dissolve chlorine tablets; acidic; adds ~0.6 ppm CYA per 1 ppm FC.
- **Turnover** — Time to circulate one pool volume through the filter.
- **VGB Act** — Federal anti-entrapment law for public pools/spas.
- **Weir** — The flapper door on a skimmer that traps debris.

---

## 15. Appendices

### 15.1 Ideal Ranges Card (print/laminate)

| Parameter | Residential target | Public (MAHC-aligned) | Notes |
|---|---|---|---|
| FC (no CYA) | 1–3 ppm | 1.0 min – 10 max | CDC home min 1 |
| FC (with CYA 30–50) | 3–5 ppm (≥7.5% of CYA) | 2.0 min – 10 max | Higher CYA → higher FC |
| FC spa | 3–10 ppm | 3.0 min | No CYA in spas |
| CC | ≤0.2 ppm | ≤0.4 (act) | Shock at breach |
| pH | 7.2–7.8 (opt. 7.4–7.6) | 7.2–7.8 | SWG: aim 7.2–7.6 |
| TA | 80–120 plaster / 80–100 vinyl-FG / 60–80 SWG | 60–180 per code | |
| CH | 200–400 plaster / 150–250 vinyl / 150–300 FG | 150–400 typical | Spas 150–250 |
| CYA | 30–50 outdoor / 0–20 indoor | ≤100 max; 0 in spas | SWG often 60–80 |
| Salt (SWG) | 2,700–4,500 ppm (mfr) | — | Target ~3,200 |
| Phosphates | <100–125 ppb | Same | |
| Metals Fe/Cu | <0.2 / <0.2 ppm (ideally 0) | Same | |
| Temp | 25–29 °C pools; ≤40 °C spas | Code max | |
| LSI | −0.3 to +0.3 | Same | |

### 15.2 Dosing Quick Table (per 40,000 L / 10,566 gal — scale linearly)

| Goal | Product | Dose |
|---|---|---|
| +1 ppm FC | Liquid chlorine 12.5% / 10% / bleach 6% | 320 / 400 / 670 mL |
| +1 ppm FC | Cal-hypo 65% | 62 g (adds 0.7 ppm CH) |
| +1 ppm FC | Dichlor 56% | 72 g (adds 0.9 ppm CYA) |
| −0.2 pH | Muriatic acid 31.45% | 400–500 mL (TA-dependent) |
| +0.2 pH | Soda ash | 400–450 g |
| +10 ppm TA | Baking soda | ~670 g |
| +10 ppm CH | Calcium chloride dihydrate 77% | ~590 g |
| +10 ppm CYA | Stabilizer granules | ~400 g |
| +500 ppm salt | Pool salt | 20 kg |
| Breakpoint shock | Liquid chlorine | dose to raise FC 10× CC |

### 15.3 Weekly Log Sheet Template

| Date | Time | FC | CC | pH | TA | CH | CYA | Salt | Temp | Filter psi | Chemicals added (product, amount) | Initials | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |

### 15.4 Metric ↔ US Conversions

- 1 US gal = 3.785 L · 1,000 gal = 3,785 L · 10,000 gal = 37,854 L
- 1 lb = 453.6 g · 1 oz = 28.35 g · 1 fl oz = 29.57 mL · 1 cup ≈ 237 mL · 1 qt ≈ 946 mL
- °F = °C × 1.8 + 32 · ppm = mg/L
- Dose scaling: dose₂ = dose₁ × (volume₂ ÷ volume₁)

### 15.5 Onboarding Quick-Start (one page)

1. Record pool volume, surface, sanitizer type, indoor/outdoor, jurisdiction (Section 1.3–1.4).
2. Assemble the pool binder: permits, manuals, warranties, SDSs (1.1).
3. Buy a FAS-DPD test kit; run a full baseline test + one store/lab cross-check (4.1).
4. Verify safety: barrier & gates, drain covers, GFCI, no chemicals within kids' reach (12.5).
5. Balance in order TA → pH → CH → CYA → FC (8.1).
6. Set the schedule: FC/pH each swim day; weekly full test; monthly CYA/CH/salt (4.3).
7. Learn the three never-rules: never mix chlorine+acid, never mix chlorine types, never add water to chemicals (6.1).
8. Public/commercial: confirm permit, certified operator, logs, VGB docs, ADA entry (12.5).

---

## 16. Sources and Verification Notes

*Chemical safety and regulatory content in this manual was checked against the following primary sources (accessed July 2026). Dosing arithmetic was verified stoichiometrically (Section 5.9). An assistant citing this manual can point users to these originals.*

**Water treatment & testing (residential)**
- CDC Healthy Swimming — Home Pool and Hot Tub Water Treatment and Testing: FC ≥1 ppm pools (≥2 ppm with CYA), ≥3 ppm hot tubs, pH 7.0–7.8, no CYA in hot tubs, test ≥2×/day. https://www.cdc.gov/healthy-swimming/about/home-pool-and-hot-tub-water-treatment-and-testing.html
- CDC Healthy Swimming — Pool Safety Guidelines. https://www.cdc.gov/healthy-swimming/safety/what-you-can-do-to-stay-healthy-in-swimming-pools.html

**Public pool operations**
- CDC Model Aquatic Health Code, 4th ed. (2023): FC 1.0/2.0 ppm minimums, 10 ppm max, spa 3.0 ppm, pH 7.2–7.8, CYA ≤100 & spa prohibition (§5.7.3). Code: https://www.cdc.gov/model-aquatic-health-code/media/pdfs/2023-MAHC-508.pdf · Annex: https://cmahc.org/2023-MAHC-Annex-4th-Edition.pdf · CYA section rationale: https://cmahc.org/mahc_sections/1733
- CDC — Operating Public Pools toolkit. https://www.cdc.gov/healthy-swimming/toolkit/operating-public-pools-hot-tubs-and-splash-pads.html

**Chemical safety**
- CDC — Pool Chemical Safety toolkit (storage <35 °C/95 °F, training, SDS access, feeder interlock guidance). https://www.cdc.gov/healthy-swimming/toolkit/pool-chemical-safety.html
- CDC MMWR 68(19), 2019 — Pool Chemical Injuries in Public and Residential Settings, US 2008–2017 (~4,500 ED visits/yr; ⅓ children). https://www.cdc.gov/mmwr/volumes/68/wr/pdfs/mm6819a2-h.pdf
- NIOSH Pocket Guide — Chlorine (IDLH 10 ppm; OSHA PEL C 1 ppm). https://www.cdc.gov/niosh/npg/npgd0115.html and https://www.cdc.gov/niosh/idlh/7782505.html
- NIOSH Pocket Guide — Hydrogen chloride (OSHA PEL C 5 ppm). https://www.cdc.gov/niosh/npg/npgd0332.html
- OSHA chemical data — Chlorine: https://www.osha.gov/chemicaldata/650 · Hydrogen chloride: https://www.osha.gov/chemicaldata/620
- CDC fecal incident response recommendations (formed stool 2 ppm/25–30 min; diarrheal 20 ppm/12.75 h, CYA ≤15). Reference PDF: https://eiph.id.gov/wp-content/uploads/EH/Pools/Preventswimmingpoolchemicalinjuries.pdf and CDC Healthy Swimming toolkit pages.

**Federal law & standards**
- CPSC — VGB Act overview and drain-cover standard (ANSI/APSP/ICC-16 2017 incorporation): https://www.cpsc.gov/Business--Manufacturing/Business-Education/Business-Guidance/Pool-and-Spa-Drain-Covers · Federal Register 2019 rule: https://www.federalregister.gov/documents/2019/05/24/2019-10845/virginia-graeme-baker-pool-and-spa-safety-act-incorporation-by-reference-of-successor-standard · Act text: https://www.poolsafely.gov/wp-content/uploads/2016/04/vgba.pdf
- ADA.gov — Accessible Pools: Means of Entry and Exit: https://www.ada.gov/resources/accessible-pools-requirements/ · Existing-pool Q&A: https://www.ada.gov/resources/q&a-accessibility-requirements-pools-public/
- CPSC Pub. 362 — Safety Barrier Guidelines for Residential Pools: https://www.cpsc.gov/s3fs-public/362%20Safety%20Barrier%20Guidelines%20for%20Pools.pdf
- ICC — International Swimming Pool and Spa Code (ISPSC) & referenced APSP/PHTA standards: https://codes.iccsafe.org/codes/standards/apsp-standards · PHTA standards catalog: https://www.phta.org/standards-codes/phta-standards/find-a-standard/

**State code examples**
- Florida FAC 64E-9 (Public Swimming Pools and Bathing Places): https://flrules.org/gateway/ChapterHome.asp?Chapter=64E-9
- State-by-state pool code directory: https://cpoclass.com/pool-code/
- Texas 25 TAC Ch. 265; California 22 CCR & HSC §§115920–115929; New York 10 NYCRR Subpart 6-1; Arizona AAC R18-5 Art. 2 — via each state's administrative code portal (see directory above).

**Dosing effects (industry-verified references)**
- Trouble Free Pool Wiki — chemical effects (dichlor/trichlor CYA contribution, cal-hypo CH contribution, FC/CYA relationship): https://www.troublefreepool.com/wiki/index.php?title=CYA_Chlorine_Relationship and https://www.troublefreepool.com/wiki/index.php?title=Chemical_Storage_and_Safety
- Orenda Technologies — chlorine/pH/CYA chemistry explainers: https://blog.orendatech.com/chlorine-ph-and-cya-relationships

**Corrections made vs. common published figures** (found during verification of the base document):
1. Cal-hypo calcium contribution is **~0.7 ppm CH per 1 ppm FC**, not 7 ppm (stoichiometric: Ca fraction 40/143 ÷ available Cl ~0.99 × 2.5 CaCO₃ factor).
2. Calcium chloride dihydrate dose is **~590 g per +10 ppm CH per 40,000 L**, not 1.25 kg (factor 147/100 vs. CaCO₃).
3. Liquid chlorine 12.5% dose is **~320 mL per +1 ppm FC per 40,000 L** (~400 mL for 10%); "500 mL" is only correct for ~8% product.
4. Salt dose corrected to **20 kg per +500 ppm per 40,000 L** (exact mass balance).

**End of Manual** — structured for chunked embedding: split at `##` (major topics) or `###` (subtopics); each chunk is self-contained with parameter names spelled out at first use.
