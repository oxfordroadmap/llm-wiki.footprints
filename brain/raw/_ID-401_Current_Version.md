---
id: ID-401
title: "From Stacks to Circuits: A Regenerative Socio-Technical Roadmap for AI Infrastructure within Planetary Boundaries"
summary: This study introduces a Regenerative Socio-Technical roadmap that reframes AI infrastructure as a system-of-systems governed by planetary limits and integrated sustainability considerations.
date: 1 June, 2026
keywords:
  - Carbon emissions
  - Environmental management
  - Green manufacturing
  - Circular Economy
  - Roadmapping
  - Socio-Technical Systems
  - Scalability
  - Twin Transition
version: "48"
tags:
  - SS08
  - Digital_Circular_Economy
---
# From Stacks to Circuits: A Regenerative Socio-Technical Roadmap for AI Infrastructure within Planetary Boundaries

  > version: 48

Han-Teng Liao*  
_Independent Researcher_

Penang, Malaysia  
h.liao@ieee.org  
0000-0003-1081-5599  
  
Karen Ang  
_Independent Researcher_  
  
Kulim, Malaysia  
karenang118@gmail.com  
0009-0008-5923-0106  
  

  

_Abstract_— Current scaling trajectories for Generative AI, typified by linear supply-side "stacks," prioritize performance density while externalizing significant thermodynamic and material costs. As the "Twin Transition" of green and digital transformation accelerates, the industry faces technology gaps—including Scope 3 emissions and e-waste recycling—that impede sustainable scaling and lead to social tensions. This study proposes a Regenerative Socio-Technical roadmap that repurposes the Sustainable Production and Consumption system map to reframe artificial intelligence infrastructure as a system-of-systems governed ultimately by planetary limits. By integrating the Institute of Electrical and Electronics Engineers International Roadmap for Devices and Systems (IEEE IRDS) sustainability considerations for semiconductor facilities, the study proposes a metabolic circuit framework that centers "Values and Needs" within production and consumption relationship loops. This study identifies critical gaps in current Nvidia-centric roadmaps and proposes a competing reference architecture. It demonstrates how a spontaneous order of resource parsimony and planetary accountability can provide an actionable pathway for regulatory compliance and industrial resilience in the digital circular economy.

Keywords— Carbon emissions; Environmental management; Green manufacturing; Circular Economy; Roadmapping; Socio-Technical Systems; Scalability; Twin Transition

#            I.         INTRODUCTION: FROM STACKS TO CIRCUITS

## A.    Context: Rapid and Intensive Scaling of Generative AI

The rapid scaling of Generative Artificial Intelligence (AI) infrastructure, typified by linear "stack" models such as the Nvidia "five-layer cake" architecture [1], [2], [3], has outpaced the development of governance frameworks capable of managing its systemic environmental footprint. This intensive scaling, which treats the AI stack as an optimized pipeline from "Electrons to Tokens", is driven by a performance-at-all-costs paradigm that prioritizes responsive fluency over thermodynamic efficiency and environmental sustainability.

This scaling trajectory imposes significant stress on the existing technology gaps identified in the 2024 Institute of Electrical and Electronics Engineers (IEEE) International Roadmap for Devices and Systems (IRDS™) regarding the Environment, safety, health & sustainability (ESHS) of the Environmental Sustainability of the Semiconductor Facilities (ESSF) [4]. Specifically, the roadmap emphasizes that facility-level resource consumption must consider the interconnectivity of water and energy, and the roadmap itself represents the collaborative outcomes by expert representatives of leading semiconductor manufacturers, original equipment manufacturers (OEMs), materials suppliers, analytical labs, and consultants. The roadmap also specifies quantitative targets in order to support "building climate-resilient facilities, meeting stringent emission limits, and managing large and growing footprints are all critical objectives the industry faces" (p.4)

Empirical data, particularly manufacturing and environmental impact metrics, provide science-based evidence for systemic evaluation. For example, the development of Digital Product Passports (DPPs) aims to assist industrial managers in accounting for operational decision-making within reverse supply chains [5]. DPPs are widely expected to serve as core enablers of the circular economy [6], demonstrated by recent regulatory models in the EU Battery Regulation [7] and the textile industry [8]. Consequently, the European Commission regards the DPP as a fundamental mechanism for driving this transition towards a product level circular economy [9], [10], [6], [11].

As Europe actively pursues the "Twin Transition" of green and digital transformation, the digital circular economy (DCE) has emerged as a critical nexus [6], [7] for ensuring that technological growth remains within planetary boundaries [12]. Thus, the integrated demands of ESHS issues require rigorous alignment between digital innovation and material circularity. Without this synchronization, any Twin Transition initiative will risk becoming a ecological liability where efficiency gains accelerate resource depletion. This alignment is especially critical at a time when the global economy is driven by capital expenditure (CapEx) on generative AI infrastructure that is inherently energy- and resource-intensive.

## B.    Motivation: What if Generative AI is Not Regenerative?

A fundamental misalignment persists between the financial valuation of AI as an infinite digital asset and the physical reality of its resource-bound production and consumption patterns. This study argues that the current human-machine metabolism prioritizes computational throughput at the expense of planetary stability and cohesive social relations. While the prevailing industry narrative, championed by figures such as Nvidia CEO Jensen Huang, frames the AI stack as an optimized journey from "electrons to tokens" [1], [2], [3], this paper interrogates the long-term viability of high-throughput tokenomics through the lens of an "atoms-to-values" framework grounded in material circular circularity. Tokenomics needs such physical ground truths to remain sustainable.

A primary driver of this misalignment is the Jevons Paradox: as energy and hardware efficiency gains reduce the unit cost of tokens and compute, aggregate demand expands at a velocity that outpaces those efficiency gains, resulting in a net increase in total energy and material consumption. This rebound dynamic is clearly observable at the regional infrastructure level. In Taiwan, Jensen Huang asserted that "human labor needs rice, but AI labor needs electricity" [13] , calling for expanded energy capacity in Taiwan in May 2026. It is coincided with state utility Taipower enforcing strict regulatory ceilings on new data center grid applications north of Taoyuan, due to acute supply-demand imbalances between southern generation capacity and northern demand [14]. This Grid Paradox illustrates how linear scaling assumptions collide with physical and regulatory constraints. It underscores the urgency of moving beyond static corporate social responsibility (CSR) reporting toward dynamic system models that treat waste heat, water, and embodied carbon as recoverable liabilities rather than sunk costs.

The social dimensions of these socio-economic tensions have attracted equally high-level institutional scrutiny. Pope Leo XIV's 2026 Encyclical, _Magnifica Humanitas_ [15], explicitly identifies underpaid data labelling, content moderation, and rare-earth and critical mineral extraction as "new forms of slavery," highlighting the human and environmental cost underpinning AI scaling. These structural issues force a critical question: What if generative AI is not regenerative?

Addressing both the thermodynamic and socio-economic dimensions requires embedding reflective governance and regulatory technology (RegTech, the use of technology to automate and deliver regulatory compliance) directly within the AI stack. Challenging "efficiency as ultimate value" paradigm, this architecture must align with the EU Corporate Sustainability Due Diligence Directive (CSDDD) and the Safe and Sustainable by Design (SSbD) guidelines [16]. EU CSDDD requires companies to conduct human rights and environmental due diligence across value chains, whereas SSbD advances frameworks for eliminating hazardous substances and processes.

This alignment ensures that both the "AI _of_ the environment" (its physical and environmental footprints) and "AI _for_ the environment" (its application toward environment and sustainability objectives) [17] are rigorously designed, monitored and audited. Ultimately, tokenomics must be re-engineered to support Industry 5.0 practices that balance the Triple Bottom Line (TBL) of profit, people and the planet.

## C.    Objectives: Sensible, Technical, yet Holistic Roadmap

This study synthesizes regenerative accounting and socio-technical systems (STS) theory into a unified framework for computing economics and infrastructure governance.

The central research question is formulated as follows: _How can an integrated Regenerative Socio-Technical (RST) framework enable AI infrastructure governance to remain within planetary and regional resource boundaries while meeting regulatory mandates__, such as CBAM and SSbD?_

By formalizing ecological debt as an observable balance-sheet liability and systemic resilience as a trackable engineering parameter, this roadmap introduces a definitive reference architecture for transitioning toward a sustainable, regenerative digital circular economy.

#             II.        EXISTING THEORIES & PREVIOUS WORK

This section bridges the gap between industry execution —represented by the five-layer stack— and strategic roadmapping, addressing the necessity of a rigorous sustainability audit. This includes using integrating IRDS parameters and, feedbacks and value-alignment within Sustainable Production and Consumption (SPaC) loops [18].

## A.    Electrons to Tokens: Scaling Through Orchestration

Any new conceptualization of a DCE must contend with Nvidia's scaling-centric strategy, given its primary role of the AI value chain in 2025-2026. Nvidia's five-layer cake (Energy, Chips, Infrastructure, Models, and Applications) is a high-throughput pipeline designed to commoditize energy and maximize the value of a token [1], [2], [3]**.** This mental model treats the data center as a factory where electricity is the raw material and the final product is the token —the fundamental unit of AI intelligence. The industry thus shifts from traditional "atoms to values" manufacturing toward a high-throughput "electrons to tokens" tokenomics model. Nvidia's five-layer cake functions as a linear scaling framework that treats computing as an extractive process, assuming that efficiency gains justify increased total throughput.

## B.    Critique: Sustainability and the Planetary Limits
atom-to-values "electrons-to-tokens"
Spurred by AI workloads, data center electricity consumption is projected to double by 2026, reaching total energy demand level of Germany [19]. This trajectory contributes to the global e-waste stream [20], [21], [22], even as AI is proposed as a tool to manage that waste [23], [24]. The "electrons-to-tokens" paradigm remains socio-technically blind, as shown in TABLE I. By treating energy as a static utility and lacking circularity, it ignores the regenerative relations needed to sustain the human and material base.

TABLE I. THE 5-LAYER AI PRODUCTION STACK (ADAPTED FROM [1])

|   |   |   |
|---|---|---|
|Layer|Functional Domain|Industrial Role|
|L5|Applications|End-user services (e.g., Enterprise Agents, Robotics, and Smart Apps)|
|L4|Models|Cognitive engines (e.g., LLM)|
|L3|Infrastructure|AI and Data Centers (e.g. compute)|
|L2|Chips|Semiconductor hardware (GPU/TPU/NPU acceleration)|
|L1|Energy|Power generation and cooling: often thermodynamic and resource input|

Consequently, this electrons-to-tokens linear view rests on resource assumptions that face structural friction at the Energy, Chips, and Infrastructure layers. These standards and critiques preceded Large Language Models (LLMs). Under Recommendation ITU-T L.1480 ("Enabling the net zero transition: Assessing how the use of ICT solutions impacts greenhouse gas emissions of other sectors") [25]. this narrow scaling view fails systemic auditing, especially regarding higher-order impacts such as rebound effects, via the Jevons Paradox. Viewed through a System-of-Systems (SoS) lens [26], as token unit economics decline, an AI Agent boom can trigger non-linear shifts in aggregate demand. This rebound effect expands macro-energy consumption beyond the structural adaptation velocity of local power networks, posing severe risks to socio-environmental sustainability.

## C.    Baselines, Grid Volatility, and Energy Communities

 AI demand escalation challenges utility supplies. Rapid AI and data center investments reshape global load profiles, forcing energy security, affordability, and sustainability boundaries to shift rapidly [27]. Modern hyperscale data centers exhibit highly volatile electricity and water use, intensifying frictions between digital growth and sustainable development  [28]. Aggressive procurement of clean energy to claim operational carbon neutrality on paper pushes energy policies toward "all-of-the-above" options, including nuclear power, while externalizing risks and costs onto local grids [29].

To mitigate these disruptions, power systems research highlights Energy Communities as vital for local grid resilience and decarbonization [30], [31], [32].  Transitioning from passive consumers to proactive prosumers with localized generation and storage, these communities allow active end-users to share energy virtually within a defined geographic perimeter. Their viability depends on enabling policy schemes, practitioner support frameworks, and coordinated aggregator business models.

## D.   Regenerative Accounting: Managing Ecological Debt for Systemic Reliability within Sustainability Limits

The current state of AI adoption is characterized by upstream and downstream ecological debt [33], accelerating across supply chains through acute grid stress, rapid e-waste accumulation, and mounting thermal entropy [34], [35]. Green AI narratives focused on algorithmic optimization and offsets can obscure the material reality: hyperscale data centers treat biophysical systems as extractive pools, drawing massive water volumes for cooling and accelerating the obsolescence of advanced hardware. The linear "electrons-to-tokens" model operates detached from the finite carrying capacities of ecological systems, creating metabolic friction that undermines long-term resilience. The UNU Global E-waste Monitor highlights that e-waste is the fastest-growing waste stream globally [20], a trend exacerbated by the short replacement cycles of GPUs and components for AI centers.

This study builds on Regenerative Accounting, adapted here into a closed-loop biophysical optimization framework for digital infrastructure [36]. Rather than retroactively logging resource depletion as a business cost, a regenerative model embeds ecological restoration obligations and feedback loops as active functions in system accounting [37]. Nature is treated as an institutional actor whose regenerative capacity must govern operations. Just as generative models are deployed to assess risks in debt-for-nature swaps [38], a reciprocal computational logic is applied inward to the computing stack to audit token production against regional infrastructure limits.

By synthesizing these accounting pillars with the material turn in ecological macroeconomics, this study proposes an enforceable eco-debt ceiling. This construct codifies lifecycle ecological liabilities—such as mineral extraction, water depletion, and digital waste—into system-level constraints [35], [37]. Enforcing a ceiling on compute throughput based on real-time environmental baselines injects sufficiency, accountability, and reparative redistribution into the orchestration layer. The architectural layers are thus compelled to operate within localized constraints that protect civil resource sovereignty, respect planetary limitations and implement circular economy policies.

Furthermore, the manufacturing phase of advanced semiconductors consumes large volumes of water and generates persistent chemical waste, creating a metabolic lock-in that layered linear stacks cannot address [39].

## E.    The IEEE IRDS™ lens: Sustainability Technology Gaps

Sustainability-oriented semiconductor manufacturing requires benchmarking against planetary limits [40]. As the successor to the International Technology Roadmap for Semiconductors (ITRS), the IEEE International Roadmap for Devices and Systems (IRDS™) aggregates expert predictions for the next fifteen years of electronics development. The 2024 IRDS edition includes an updated Environment, safety, health & sustainability (ESH/S): Environmental sustainability of semiconductor facilities (ESSF) roadmap chapter [4].

Foundational work like this shifts industry from reactive compliance toward proactive, design-centric principles consistent with SSbD. Three key pillars are relevant to this study:

·        IRDS ESH/S ESSF Roadmap [4]: Specifies Key Performance Indicators (KPIs) for water and energy efficiency and promotes the minimization of hazardous chemistries at the process design phase, including Green Tool Characteristics.

·        Framework for Critical Semiconductor Materials [41]**:** Develops requirements to assess critical materials (e.g., advanced lithography) based on toxicity, circularity, and eco-impact before high-volume deployment.

·        Novel Sensing for Environmental Solutions [42]: Extends SSbD to applications by designing devices with high selectivity and low power for real-time resource monitoring.

For engineering managers and technology strategists, the 2024 IRDS ESSF signals that sustainability is now a mission-critical enabler for growth. AI-driven demand for larger, more complex facilities intersects with resource scarcity (water and energy), tightening regulations (e.g., per- and polyfluoroalkyl substances [PFAS], greenhouse gas [GHG] limits), and physical climate risks [43], [44]. The widening technology gaps identified in the roadmaps will be stressed by surging global demand in AI, electric vehicles (EVs), and high-performance computing, forcing managers to balance economic scalability, supply chain resilience, and environmental sustainability [45].

## F.    The Sustainability-Scaling Gap

While Nvidia's five-layer cake remains a dominant blueprint, it operates as a linear, extractive model decoupled from the physical and regulatory boundaries. A critical gap persists: the industry lacks a unified "Sustainability Audit" to reconcile the resource intensity of tokenomics with constraints such as the Carbon Border Adjustment Mechanism (CBAM) and SSbD regulations. CBAM prices the carbon content of imported goods to prevent carbon leakage [46]. Without a framework linking downstream demand to upstream resource limits, the industry risks hitting a hard ceiling that halts industrial growth due to environmental non-compliance or resource exhaustion.

This study addresses this gap by introducing an integrated Regenerative Socio-Technical (RST) framework. This architecture functions as a bidirectional metabolic loop, translating static IRDS environmental parameters into live operational telemetry within SPaC relationship loops. By grounding computational demands in regional grid limits and regulatory thresholds, the RST framework shifts governance away from unconstrained scaling toward verifiable, bounded utility management, directly answering the socio-technical and regulatory objectives of this study's roadmap.

#                                   III.       METHODOLOGY

## A.    Presented Study, Research Question(s), and Hypothesis

This study investigates the systemic tension between the critical planetary boundaries and resource-intensive, extractive nature of generative AI infrastructure. It addresses the core inquiries formulated at the end of Section II, seeking to establish an integrated auditing framework that reconciles linear "tokenomics" with environmental constraints.

The research is guided by the hypothesis that a Regenerative Socio-Technical (RST) framework—which integrates environmental factors (e.g., IRDS parameters) into the core of Sustainable Production and Consumption (SPaC) relationship loops [18]—can effectively mitigate Scope 3 emissions and fulfill SSbD mandates while sustaining digital infrastructure growth for human development.

## B.    Repurposing SPaC loops as RST framework

|   |
|---|
|Fig. 1. The "Atom-to-Values" System of Systems (SoS) loops for AI compute (adapted and expanded from the Sustainable Production and Consumption (SPaC) framework by J. Barber in [18].|

To address the systemic tensions between generative AI infrastructure and planetary boundaries, this study repurposes the traditional SPaC framework into an RST system dynamics model. To better conceptualize modern digital infrastructure driven by AI compute, the proposed model introduces sector-specific node definitions tailored to deep-tech hardware, establishes a clear specification of environmental mandates, and embeds explicit system dynamics feedback structures.

Fig. 1, the proposed "Atom-to-Values" SoS model maps the system dynamics of compute a TBL taxonomy. It aims to balance profit, people and the planet for sustainable growth, thereby providing a circular reference:

**Profit (The Core Capital Loop):** The inner cycle tracks the economic engine of AI hardware.

·        _Extraction_ represents the input of critical minerals, water, and energy;

·        _Production_ corresponds to semiconductor fabrication and AI generation;

·        _Distribution_ covers hardware logistics, digital networks, and software platforms;

·        _Consumption_ encompasses smart apps and consumer agents; and

·        _Investment_ reflects massive capital expenditure (CapEx) reinjected into compute capacity building.

 At the epicenter, the Values/Needs (Demand) of chips, compute, and hyperscale systems act as a socio-technical governance anchor where value-based requirements—such as KPIs and SSbD criteria—shape demand and funding priorities.

**Planet (The Ecological Ceiling and Recovery):** Centered on the _Extraction_ and _Waste (impacts)_ nodes, this dimension enforces two distinct environmental system dynamics that enforce physical boundaries: _(a) Oscillating Dynamics:_ A critical feedback loop characterized by material and information delays, capturing the systemic risks of ecological disruption. _(b) Recycling Dynamics:_ A closed-loop material recovery pathway engineered to mitigate ecological strain and risks.

**People** (**The Socio-Technical Transitions**): Intersecting the nodes of _Social Relations_, _Consumption_, and _Investment_, this dimension captures societal governance through the last of the three system dynamics: (c) _Balancing Dynamics_. By aligning profit with socio-economic and inter-generational public procurement justice, it actively shapes lifestyle, saving, and investment behaviors to sustain healthy social and economic relationships.

## C.    Applied Research Methods

By applying design science research principles—a methodology widely established in information systems research [47], [48], [49], this article generates a conceptual DCE framework. This framework details how the semiconductor and AI sectors produce digital deep-tech solutions for sustainable supply chains, where "digital deep tech" denotes advanced technical applications integrated with significant scientific or engineering innovations. This study views that, in high-tech manufacturing, green digital deep tech serves as the nerves of information, communication, and control, incorporating sustainable production, resource efficiency, and circular business models.

## D.   Data Collection

The data collection protocol relies on secondary document analysis, ecosystem modeling, and industry standard mapping. The collected objects and artifacts consist of:

·        **Industry** **Roadmap** **Data:** Technical specifications and energy consumption guidelines derived from the IRDS ESH/S ESSF roadmaps [4], which are expected to be shaped by CBAM and SSbD regulatory demands.

·        **Tokenomics and Infrastructure Scaling Data:** Architecture requirements, performance metrics, and production layers surrounding the linear model.

·        **Analytical Formulas:** Mathematical equations, performance curves, and operational scaling models for compute inference efficiency compiled from baseline literature [50], [51], [52], establishing quantified expressions of systemic impacts.

## E.    Analysis Method

A theory-generating case study approach [53], [54] is applied by categorizing and resensitizing the linear structures of the semiconductor and AI sectors into accessible, circular system dynamics design reference architecture. Quantitative formulas of compute inference costs are strategically integrated to enrich the "Atom-to-Values" SoS loops, enabling a balanced qualitative and quantitative description of sustainable compute capacity.

This perspective integrates system dynamic insights from the architectural Roofline Model of compute throughput as a baseline variable for measuring thermodynamic efficiency and broader environmental impacts. By exploring how these analytical formulas can be integrated with Regenerative Accounting, this paper transforms sustainability requirements into drivers of generative innovation rather than mere compliance burdens. Shifting the design focus from raw compute density to "values-to-atoms" circular sensitivities formalizes ecological debt as an observable balance-sheet item and resilience as a trackable technical parameter, offering a definitive reference architecture for the transition toward a regenerative digital circular economy.

#     IV.       Results: Regenerative Socio-Technical Reference Architecture

By redefining the generative AI infrastructure stack as a metabolic loop, this study proposes an integrated an integrated Regenerative Socio-Technical (RST) framework.

## A.    Boundary Inputs for Metabolic Governance

The first primary result of this study is the formal translation of multi-scalar telemetry data into an integrated baseline for automated system regulation. Rather than treating physical infrastructure limits, micro-architectural telemetry, and international policy mandates as disjointed operational layers, the RST architecture synthesizes them into a unified, real-time boundary matrix. This matrix establishes the foundational parameters for metabolic governance, defining the biophysical constraints under which the computing fabric must achieve operational closure. Table II illustrates these structural frictions as they exist within the 2026 infrastructure ecosystem.

Table II. Three-Tiered System Constraints (Baseline for Metabolic Governance)

|   |   |   |   |
|---|---|---|---|
|Layer|Primary Data Source|Operational Core Parameters|Homeostatic Threshold Examples|
|Physical Infra-structure|IEEE IRDS ESSF Roadmaps [4]|Water intensity, chemical toxicity, facility energy density, etc.|<0.5 liters per kWh  compute; PFAS  and emission controls [4]|
|Operational Compute|Inference Efficiency [50], [51], [52]|Model FLOP Utilization (MFU), memory wall bounds, High-Bandwidth Memory (HBM) capacity|Exponential thermodynamic efficiency drops at low concurrency regimes ( );   memory sprawl|
|Policy & Governance|EU SSbD / CBAM [16], [46]; Papal Encyclical [15]|Border carbon adjustments, regional grid caps, labor exploitation audits.|Strict 5 MW grid allocation ceiling north of Taoyuan [14]; zero-exploitation supply chains [15].|

To demonstrate the structural utility of these parameters, the RST reference architecture is explicitly contrasted against the prevailing linear "stack" model, which focuses narrowly on unidirectional electrons-to-tokens conversion [1], [2], [3]**.** Table III summarizes how such model overlooks critical externalized liabilities, which the RST architecture is engineered to internalize and regulate.

Table III. The 5-Layer AI Production Stack Liabilities

|   |   |   |
|---|---|---|
|Layer|Functional Domain|Key Externalized Liability  <br>(Systemic Metabolic Friction)|
|L5|Applications|Uncapped token demand generation driving the Jevons Paradox rebound effect [25]|
|L4|Models|Extreme density causing unmitigated HBM capacity sprawl [50], [51], [52]|
|L3|Infrastructure|Cooling water depletion and unbuffered regional grid volatility [28],[29]|
|L2|Chips|Embodied carbon of advanced lithography and e-waste lifecycles [20], [21], [22]|
|L1|Energy|Extractive reliance on municipal grids, delaying green digital transitions [14], [29]|

Instead of treating energy and natural resources as infinite, exogenous supply inputs, the RST framework accounts for localized socio-technical and thermodynamic boundaries.

## B.    Compute Baselines and Thermodynamics

The RST reference architecture recognizes that token generation within frontier AI accelerators is bottlenecked by a memory-to-compute imbalance (the “memory wall”). Shuttling model weights from HBM into local registers during sequential autoregressive inference creates a state of thermodynamic structural coupling, where physical silicon layouts dictate an application’s metabolic energy profile. To amortize the thermodynamic cost of data transit, the system must maintain a minimum operational batch threshold ( ):

where   is a dimensionless hardware constant expressing the ratio of peak performance ( ) to memory bandwidth ( )—empirically   across 2026 accelerators—  represents active layer parameters, and   tracks the total parameter footprint. Falling below this threshold ( ) drops the architecture into a low-concurrency regime that draws high static baseline power while idling on memory-bus transfers, generating high metabolic entropy per token.

This bandwidth bottleneck is compounded by Key-Value (KV) cache memory consumption ( ), which scales linearly with context length ( ) as a biophysical liability:

where   is batch size,   is the hidden dimension,   is network layer depth, and   is precision byte density. At extreme frontiers,   surpasses the model weight footprint, forcing the orchestration layer to shard workloads across multi-GPU clusters to aggregate high-speed HBM capacity.

## C.    Systemic Volatility Indicator (SVI) Framework

Unregulated, these two hardware constraints (  and ) create a profound structural contradiction. Maximizing computational efficiency via optimal batch sizes ( ) causes the concurrent processing of extended context windows ( ) to expand   linearly, triggering hardware out-of-memory faults. Conversely, down-batching ( ) to preserve memory footprint traps the hardware in a memory-bound idling state, expending massive baseline power for sub-optimal throughput.

To resolve this tension and connect intra-chip constraints with regional energy networks, the architecture implements an automated metabolic governor mediated by a dimensionless Systemic Volatility Indicator **(** **)**, bounded at zero to prevent negative indexing:

where  is the instantaneous operating batch size,  is the hardware roofline threshold, and  represents the localized power grid utilization ratio relative to institutional ceilings (such as Taipower’s 5 MW regional allocation caps [14]). This indicator mathematically formalizes two primary operational states:

·   **State A (Maximum Volatility):** When under-batched workloads ( ) run during peak regional grid stress ( ), the metric approaches unity ( ), signaling high eco-debt accumulation where grid stability is sacrificed for sub-optimal computational throughput.

·   **State B (Architectural Homeostasis):** When the system achieves full batch saturation ( ) or executes non-latent workloads during off-peak windows ( ), the metric resolves to zero ( ), indicating the computation is safely buffered by the biophysical capacity of the ecosystem.

## D.   Socio-Technical Regenerative Steering Loops: Metabolic Governance and Architectural Homeostasis

Replacing linear models with circular systems thinking, the RST reference architecture introduces socio-technical regenerative steering loops governed by the . This governor acts as a cybernetic steering engine, dynamically balancing real-time orchestration (e.g., KV cache allocation and Roofline thresholds) with the macro-level environmental boundaries (PUE/WUE tolerances and CBAM/CSDDD compliance pathways) shown in the outer area of Fig. 1. This homeostatic orchestrator alters execution profiles to minimize thermodynamic entropy when the  exceeds its regulatory ceiling. It either bundles fragmented requests into efficient workloads ( ) or automatically shifts non-latent processing tasks to decentralized regional energy micro-grids.

Over medium-to-long horizons, this governor mitigates the feedback loops and cascading SoS failures. At the core execution layer, scaling context horizons ( ) causes linear Key-Value cache memory sprawl ( ). Left unregulated, this fragmentation forces orchestration layers to shard workloads across multi-GPU clusters purely to pool HBM capacity rather than harvest raw compute engines. This fragmentation traps the hardware in a high-entropy, low-concurrency regime ( ) that draws near-maximum static baseline power while idling on memory-bus transfers. To sustain latency under these conditions, operators are trapped in a cycle of exponential capital expenditure, constructing additional hyperscale facilities that compound regional grid stress ( ). By embedding these feedback circuits directly into the compute scheduler, the RST reference architecture establishes an operational structural coupling where regulatory mandates and planetary boundaries act as the definitive homeostatic regulators of the system.

## E.    Regenerative Accounting of Environmental and Social Externalities: Achieving Operational Closure

By mapping hardware execution through closed metabolic circuits, the RST reference architecture translates abstract sustainability concepts into quantifiable engineering vectors, with non-exhaustive examples below:

·        **Memory Wall Carbon (** **):** Minimizing data transport directly minimizes localized thermal dissipation, fulfilling SSbD principles at the silicon layer.

·        **Batch Size Economics:** Operating in low-batch regimes ( ) divides the baseline energy cost across tokens, rendering inference carbon-intensive.

·        **Lifecycle Amortization:** The volume of inference tokens generated over a hardware lifespan must offset embodied carbon liabilities; rapid model deprecation turns this cycle into an ecological liability.

·        **Thermal Constraints (** **):** Extreme bandwidth penalties force ultra-dense multi-GPU packing, penalizing Water Usage Effectiveness (WUE) and generating municipal resource depletion.

By mapping relevant parameters as above, the RST reference architecture translates abstract sustainability concepts into four quantifiable engineering and metrology vectors to support DPPs [5], [6], [7] and automated industrial engineering and auditing.

To sum up, the RST reference architecture offers a more scalable and controllable model to manage physical limits of thermodynamics and material scarcity.

#                                             V.        Discussion

## A.    Answering the Research Questions

The integrated Regenerative Socio-Technical (RST) framework bridges the gap between micro-level hardware telemetry and macro-systemic environmental governance by accounting for compute costs within SPaC loops. The results reveal that local optimization for client latency enforces an aggregate energy penalty across the macro-grid. When workloads operate beneath the roofline balance point, the system experiences severe arithmetic underutilization, drawing near-peak baseline thermal power to sustain continuous HBM weight fetches across memory buses. This operational reality exposes the extractive political economy of Nvidia's linear five-layer cake model, which organizes the computing stack as a unidirectional hierarchy that externalizes massive power and infrastructure burdens onto regional public utilities and volatile energy geographies.

Furthermore, multi-dimensional scaling of context windows forces infrastructure layers into memory-driven hardware fragmentation. Workloads are sharded across multi-GPU clusters purely to pool physical memory capacity, trapping the hardware in a low-concurrency regime that continuously expends near-peak baseline power while idling. To maintain throughput under these constraints, hyperscale data centers invest massive CapEx to build redundant facilities. Because each new facility inherits identical idling penalties, material waste, GHG footprints, and localized grid stress compound exponentially.

To break this cycle, the proposed reference architecture shifts the paradigm from an extractive "electrons-to-tokens" model toward an "atoms-to-values" closed loop. Rather than treating waste and thermal entropy as ignored externalities, they are internalized as institutional metabolic liabilities. Parameterizing waste at the SoS level transitions industrial practice from qualitative CSR reporting toward quantitative, real-time auditing. Utilizing DPPs and RegTech to track the GPU lifecycle and capture cooling telemetry allows operators to route water and heat waste directly back into the circularity of local ecosystems.

## B.    Match and Contribution

This study contributes to the DCE literature by providing the first SoS Regenerative Reference Architecture within SPaC relationship loops, governed by quantified boundary conditions. This contribution matches three objectives:

1. **Emerging Technology Management:** Traditional frameworks evaluate Generative AI infrastructure as a weightless asset, masking its biophysical footprint. This work reframes accelerator arrays as an interconnected SoS with thermodynamic liabilities. This "system-to-planet" vantage point equips technology managers with architectural tools to navigate macro-grid volatility induced by frontier LLMs.

2. **Practical Frameworks:** To bridge abstract sustainability goals and ground-truth engineering, this study introduces an actionable framework rooted in Regenerative Accounting, SPaC, and STS theory. Controlled by the SVI, it operationalizes DPPs and RegTech to automate real-time resource routing, shifting industrial practice toward quantitative, enforceable auditing.

3. **Value Creation and Alignment:** The RST model redefines industrial value creation away from brute-force scaling toward circular efficiency, collective social learning, and regional resilience. Centered on a "Values/Needs" core, it permits socio-ethical specifications—such as the _Magnifica Humanitas_ encyclical [15]_—_to protect human dignity. Boundary conditions can then involve rare-earth extraction networks and data annotation supply chains based on community consensus.

To transition these insights to institutional adoption, engineering managers can utilize the actionable compliance checklist below:

·   **Grid and Energy Community:** Respect regional grid capacity and local energy community needs.

·   **Thermodynamic Loop:** Structurally explore waste-to-value loops, using IRDS heat recovery KPIs.

·   **Lifecycle** **Circularity:** Use DPPs to track GPU lifecycles, component refurbishment, and e-waste processing against SSbD and CSDDD guidelines.

·   **Asset Amortization:** Amortize hardware pre-training and operational footprints over realistic, extended lifecycles.

·   **Supply Chain Ethics:** Actively audit labor conditions, including the rare-earth extraction and data annotation.

#    VI.       Conclusion: Roadmap for Regenerative AI

This section concludes with a technical roadmap establishing a DCE that is powered by Regenerative AI that remains tethered to planetary realities.

## A.    Limitations

While this study introduces a holistic RST reference architecture for token-driven AI, it faces three limitations mapped at different Technology Readiness Levels (TRLs):

·   **Conceptual Stage (TRL 1–2):** The framework has yet to be adopted **by** official IEEE IRDS International Focus Teams (IFTs) for formal industry roadmapping.

·   **Lack of Micro-Telemetry:** While macroscopically mapping material and thermodynamic flows (TRL 9 hardware constraints) onto SPaC loops, the study lacks component-level requirement guidelines or physical hardware telemetry specifications.

·   **Validation Needs (TRL 2–3)**: The proposed RA protocols and SVI require extensive peer review and large-scale pilot implementations of DPPs across diversified global supply chains (GVC) to verify distributed data integrity for real-time auditing.

## B.    Concluding Remarks: Computes within Boundaries

This study contributes a multi-disciplinary critique of the energy-intensive trajectories of the 2025–2026 token-based economy, shifting from linear "Device-to-System" scaling to a circular "System-to-Planet" relationship. Our main finding shows that without a "Circular Governor" enabled by RA and DPPs, the AI industry faces an imminent "Hard Landing" against planetary limits. Isolating engineering efficiency from metabolic consumption accelerates resource depletion, validating Jevons' Paradox.

This misalignment is currently visible in Taiwan: Taipower has suspended new power applications for data centers exceeding 5 MW north of Taoyuan to prevent localized grid failure [14], This occurs at the exact juncture where Nvidia has established its "Constellation" regional headquarters in the Beitou-Shilin Technology Park, triggering explicit leadership warnings regarding the island's binding energy limits [13].

The proposed RST reference architecture provides the IEEE community with an initial blueprint needed to internalize ecological debt as a core technical requirement.

## C.    Future Work/Perspectives

Based on our vision for the Safe-and-Sustainable-by-Design (SSbD) Chips Value Chain Services (SCVCS) Research Initiative [55], future research will investigate how to transform chips and AI supply chains into environmentally accountable, circular networks by using AI orchestrators, trustworthy autonomous agents, and digital product passports to balance high manufacturing yields with strict sustainability and regulatory compliance. To achieve this, future work must bridge the gap between reference models and technical objectives across the IEEE roadmap ecosystem:

·        **Power and Energy Socio-Technical Alignment**: The 2024 _IEEE Power and Energy Technology Assessment_ and _the 2023 Control for Societal-scale Challenges_ should set strategic directions on energy communities and hyperscale facilities, interacting with the IEEE Heterogeneous Integration Roadmap (HIR), specifically Chapters 2 (High-Performance Computing), 8 (Advanced Manufacturing), and 10 (Integrated Power Electronics).

·        **Materials and Chip Supply Chain Alignment:** Annual IEEE IRDS activities should apply an SoS approach to monitor material-chips-hyperscale value chains, deploying DPPs to track material and chip lifecycles, and considering the Regenerative Accounting framework.

·        **Energy Community Expansion and Inter-Agency Action:** The IEEE International Roadmap Committee (IRC) should charter a "Socio-Technical Governance" domain to analyze infrastructure through the Planetary Boundary Resilience lens. This system thinking should shape agendas like the United for Smart Sustainable Cities (U4SSC) into a new coalition: United for Smart Sustainable Intelligence (U4SSI) to help leaders and investors align value propositions that foster resilient, circular systems.

Ultimately, deep technologies demand deep systems thinking anchored in reality. Transforming generative AI into a truly regenerative asset requires standardizing actionable technical frameworks for real-time, enforceable regenerative accountability of both energy and compute resources.

##### Acknowledgment

The authors gratefully acknowledge the constructive feedback of the double-blind peer reviewers whose scrutiny strengthened this work; all remaining errors and interpretations are solely the authors' own responsibility.

##### References

[1]    J. Huang, “AI is a 5-layer cake,” _NVIDIA Blog_, Mar. 10, 2026. Accessed: Apr. 18, 2026. [Online]. Available: https://blogs.nvidia.com/blog/ai-5-layer-cake/

[2]    NVIDIA, “Keynote at NVIDIA GTC San Jose 2026,” _NVIDIA_, 2026. Accessed: Apr. 20, 2026. [Online]. Available: https://www.nvidia.com/gtc/keynote/

[3]    NVIDIA, _Tokens, the building blocks of ai_, 2026. Available: https://www.youtube.com/watch?v=O-_-CEeFHCM

[4]    IEEE, “2024 IRDS Edition: Environmental Sustainability, Health, and Safety (ESHS) and Environmental Sustainability for Semiconductor Facilities (ESSF),” IEEE International Roadmap for Devices and Systems (IRDS), Technical Report, 2024. Available: https://irds.ieee.org/images/files/pdf/2024/2024IRDS_ESHS-ESSF.pdf

[5]    S. F. Jensen, J. H. Kristensen, S. Adamsen, A. Christensen, and B. V. Waehrens, “Digital product passports for a circular economy: Data needs for product life cycle decision-making,” _Sustainable Production and Consumption_, vol. 37, pp. 242–255, 2023.

[6]    K. Voulgaridis, T. Lagkas, C. M. Angelopoulos, A.-A. A. Boulogeorgos, V. Argyriou, and P. Sarigiannidis, “Digital product passports as enablers of digital circular economy: a framework based on technological perspective,” _Telecommun Syst_, vol. 85, no. 4, pp. 699–715, Apr. 2024, doi: 10.1007/s11235-024-01104-x.

[7]    J. Walden, A. Steinbrecher, and M. Marinkovic, “Digital product passports as enabler of the circular economy,” _Chemie Ingenieur Technik_, vol. 93, no. 11, pp. 1717–1727, Nov. 2021, doi: 10.1002/cite.202100121.

[8]    C. Carvalho, M. J. A. M. Abreu, and C. J. Silva, “The integration of the Digital Product Passport (DPP) in the textile industry: a systematic literature review,” in _Advances in Fashion and Design Research III_, J. Cunha, A. C. Broega, H. Carvalho, and B. Providência, Eds., Cham: Springer Nature Switzerland, 2025, pp. 480–489. doi: 10.1007/978-3-031-83185-0_44.

[9]    European Commission, “EU countries commit to leading the green digital transformation,” Directorate-General for Communications Networks, Content and Technology, European Commission, Mar. 2021. Accessed: May 17, 2022. [Online]. Available: https://digital-strategy.ec.europa.eu/en/news/eu-countries-commit-leading-green-digital-transformation

[10]  P. Migliorini, “Circular economy, sustainable production and consumption,” Nov. 2023. Available: https://unece.org/sites/default/files/2023-12/09Nov_APIWorkshop_am_item%20II_No.1_EU_P.Migliorini.pdf

[11]  T. Ebert, “Ecodesign for Sustainable Products Regulation (ESPR) and Digital Product Passport (DPP),” Apr. 2025. Available: https://www.berec.europa.eu/system/files/2025-05/EC,%20DG%20CNECT.pdf

[12]  Z. Xu, Z. Wang, and H.-T. Liao, “People-centered Computing Within Limits: System Thinking on Interventions of Internet Platforms,” in _Proceedings of the 2019 3rd International Conference on Cloud and Big Data Computing_, Oxford, United Kingdom: ACM, Aug. 2019, pp. 16–20. doi: 10.1145/3358505.3358523.

[13]  L. Wang, “Nvidia CEO touts surge in spending in Taiwan,” _The Taipei Times_, p. 1, May 28, 2026.

[14]  S. Huang, “The energy paradox of taiwan’s sovereign AI ambition,” _Center for Asia-Pacific Resilience and Innovation (CAPRI) Analysis_, Mar. 2026. Available: https://caprifoundation.org/the-energy-paradox-of-taiwans-sovereign-ai-ambition/

[15]  Pope Leo XIV, “Encyclical letter _magnifica humanitas_: on safeguarding the human person in the time of artificial intelligence,” Vatican City: The Holy See, May 2026. Available: https://www.vatican.va/content/leo-xiv/en/encyclicals/documents/20260515-magnifica-humanitas.html

[16]  European Commission, “Safe and sustainable by design: Accelerating the industrial transition,” Mar. 2026.

[17]  H.-T. Liao, C.-L. Pan, and Y. Zhang, “Smart digital platforms for carbon neutral management and services: Business models based on ITU standards for green digital transformation,” _Front. Ecol. Evol._, vol. 11, p. 1134381, Mar. 2023, doi: 10.3389/fevo.2023.1134381.

[18]  P. Vergragt, L. Akenji, and P. Dewick, “Sustainable production, consumption, and livelihoods: global and regional research perspectives,” _Journal of Cleaner Production_, vol. 63, pp. 1–12, Jan. 2014, doi: 10.1016/j.jclepro.2013.09.028.

[19]  International Energy Agency, “Electricity 2024: analysis and forecast to 2026,” Paris: IEA, Technical Report, 2024. Available: https://www.iea.org/reports/electricity-2024

[20]  V. Forti, C. P. Baldé, R. Kuehr, and G. Bel, _The global e-waste monitor 2020: quantities, flows and the circular economy guide_. Bonn/Geneva/Rotterdam: United Nations University (UNU)/UNITAR, 2020. Available: https://ewastemonitor.info/gem-2020/

[21]  P. Wang, L.-Y. Zhang, A. Tzachor, and W.-Q. Chen, “E-waste challenges of generative artificial intelligence,” _Nat Comput Sci_, vol. 4, no. 11, pp. 818–823, Nov. 2024, doi: 10.1038/s43588-024-00712-6.

[22]  A. de Vries-Gao, “Recalibrating global artificial intelligence e-waste estimates,” _Resources, Conservation and Recycling_, vol. 229, p. 108872, Apr. 2026, doi: 10.1016/j.resconrec.2026.108872.

[23]  J. Chen, S. Huang, S. BalaMurugan, and G. S. Tamizharasi, “Artificial intelligence based e-waste management for environmental planning,” _Environmental Impact Assessment Review_, vol. 87, p. 106498, Mar. 2021, doi: 10.1016/j.eiar.2020.106498.

[24]  T. Rahman, Md. A. Moktadir, S. Kumar Paul, and S. M. Ali, “Challenges to GenAI adoption in e-waste management,” in _2025 IEEE International Conference on Industrial Engineering and Engineering Management (IEEM)_, Dec. 2025, pp. 0258–0262. doi: 10.1109/IEEM63636.2025.11357757.

[25]  ITU, “Recommendation ITU-T L.1480: Enabling the net zero transition: Assessing how the use of information and communication technology solutions impact greenhouse gas emissions of other sectors,” Geneva, Switzerland: ITU-T Study Group 5, Recommendation L.1480, Dec. 2022. Available: https://www.itu.int/rec/T-REC-L.1480

[26]  J. Boardman and B. Sauser, “System of Systems - the meaning of of,” in _2006 IEEE/SMC International Conference on System of Systems Engineering_, Apr. 2006, p. 6 pp.-. doi: 10.1109/SYSOSE.2006.1652284.

[27]  International Energy Agency, “Key questions on energy and AI,” Paris, France: IEA, Analysis Report, 2026. Available: https://www.iea.org/reports/key-questions-on-energy-and-ai

[28]  F. Abdi, “Hyperscale data centers in Europe : infrastructure, sustainability, and strategic importance.” 2025. Accessed: May 28, 2026. [Online]. Available: https://lutpub.lut.fi/handle/10024/170753

[29]  J. O’Brien, “AI’s energy appetite: lessons from leading hyperscalers on sustainable procurement.” Johns Hopkins University, 2025. Accessed: May 28, 2026. [Online]. Available: https://jscholarship.library.jhu.edu/handle/1774.2/70484

[30]  T. Sousa, T. Soares, P. Pinson, F. Moret, T. Baroche, and E. Sorin, “Peer-to-peer and community-based markets: A comprehensive review,” _Renewable and Sustainable Energy Reviews_, vol. 104, pp. 367–378, Apr. 2019, doi: 10.1016/j.rser.2019.01.036.

[31]  G. Iazzolino, N. Sorrentino, D. Menniti, A. Pinnarelli, M. De Carolis, and L. Mendicino, “Energy communities and key features emerged from business models review,” _Energy Policy_, vol. 165, p. 112929, Jun. 2022, doi: 10.1016/j.enpol.2022.112929.

[32]  M. L. Lode, G. te Boveldt, T. Coosemans, and L. Ramirez Camargo, “A transition perspective on Energy Communities: A systematic literature review and research agenda,” _Renewable and Sustainable Energy Reviews_, vol. 163, p. 112479, Jul. 2022, doi: 10.1016/j.rser.2022.112479.

[33]  I. Collinson, “‘Limitless computation on a finite planet?’ the actually existing ecology of generative AI.” Cham: Springer Nature Switzerland, 2026, pp. 407–419. doi: 10.1007/978-3-032-07605-2_19.

[34]  S. Naznin, S. A. Y. Khan, and K. Nisar, “Governing the environmental footprint of generative AI: from green efficiency to climate justice,” _Journal of Management & Social Science_, vol. 2, no. 3, pp. 963–969, Dec. 2025.

[35]  B. Brevini, “Between power and nature: an eco-political economy of AI,” _The Political Economy of Communication_, vol. 12, no. 1, 2026, Accessed: Apr. 28, 2026. [Online]. Available: http://polecom.org/index.php/polecom/article/download/197/432

[36]  I. Edstrom, “Regenerative accounting: the pillars & vision,” _Accounting Alchemy Network_, Apr. 18, 2024. Accessed: May 05, 2026. [Online]. Available: https://cpatrendlines.com/2024/07/17/accounting-arc-with-donny-shimamoto-center-for-accounting-transformation-regenerative-accounting-ingrid-edstrom-pioneers-a-holistic-approach-to-financial-practicesrc-9-regenerative-accounting-pi/

[37]  M. A. Wibowo, N. A. Achsani, J. Winoto, and A. Justianto, “Ecological GDP reform through regenerative macroeconomics: a systematic review of theoretical paradigms,” _J. Environ. Account. Manag._, vol. 14, no. 3, pp. 371–389, Sep. 2026, doi: 10.5890/JEAM.2026.09.001.

[38]  N. Tkachenko, S. Frieder, R.-R. Griffiths, and C. Nedopil, “Analyzing global utilization and missed opportunities in debt-for-nature swaps with generative AI,” _Front. Artif. Intell._, vol. 7, p. 1167137, Feb. 2024, doi: 10.3389/frai.2024.1167137.

[39]  K. Wang, _Green etching techniques for mems applications: sustainable, fluorine-free etching methods for micro-electro-mechanical systems_. Boca Raton: CRC Press, 2025. doi: 10.1201/9781003674795.

[40]  L. T. Kenny, “IRDS environmental, safety, health and sustainability (ESH/S) roadmap: initiative update,” in _ICOS Semiconductors Workshop_, Apr. 2023. Available: https://icos-semiconductors.eu/wp-content/uploads/2023/04/Leo-Kenny-The-IRDS-Environmental-Safety-Health-and-Sustainability-ESHS-Roadmap-initiative-update.pdf

[41]  A. Ueda _et al._, “Green materials in semiconductors: perspective from the IRDS beyond-CMOS roadmap,” _Nanotechnology_, vol. 36, no. 14, p. 142001, Feb. 2025, doi: 10.1088/1361-6528/adb041.

[42]  T. Nishida, R. A. Potyrailo, and L. T. Kenny, “Enabling sustainable solutions for the global environment through novel sensing,” in _American Physical Society (APS) IoT Program_, Apr. 2017. Available: https://higherlogicdownload.s3.amazonaws.com/APS/65bbda9a-3271-43aa-a2e2-83224f62ae31/UploadedImages/Documents/2-3-Kenny-Environmental-Sensing.pdf

[43]  L. S. Beu and M. A. Gresham, “An overview of semiconductor industry efforts to reduce PFAS use and emissions in plasma processes,” in _Advanced Etch Technology and Process Integration for Nanopatterning XIII_, SPIE, Apr. 2024, pp. 162–166. doi: 10.1117/12.3013226.

[44]  E. A. Joseph, N. Marchack, R. Bruce, J. Pitera, T. Todorov, and D. Sanders, “The semiconductor supply chain in an era of low GWP and/or PFAS-free gas chemistries,” in _Advanced Etch Technology and Process Integration for Nanopatterning XIV_, SPIE, Apr. 2025, p. 1342902. doi: 10.1117/12.3058167.

[45]  C. Wyon and M. V. de Voorde, “New challenges for the semiconductor ecosystem,” _IEEE Electron Devices Reviews_, vol. 2, pp. 330–360, 2025, doi: 10.1109/EDR.2025.3638339.

[46]  G. Magacho, E. Espagne, and A. Godin, “Impacts of the CBAM on EU trade partners: consequences for developing countries,” _Climate Policy_, vol. 24, no. 2, pp. 243–259, Feb. 2024, doi: 10.1080/14693062.2023.2200758.

[47]  S. T. March and G. F. Smith, “Design and natural science research on information technology,” _Decision Support Systems_, vol. 15, no. 4, pp. 251–266, Dec. 1995, doi: 10.1016/0167-9236(94)00041-2.

[48]  S. Fatima, K. C. Desouza, C. Buck, and E. Fielt, “Public AI canvas for AI-enabled public value: A design science approach,” _Government Information Quarterly_, vol. 39, no. 4, p. 101722, Oct. 2022, doi: 10.1016/j.giq.2022.101722.

[49]  H.-T. Liao, C.-L. Pan, and Y. Zhang, “Collaborating on ESG consulting, reporting, and engaging education: Using partner maps for capability building design,” _Front. Environ. Sci._, vol. 11, p. 1119011, Mar. 2023, doi: 10.3389/fenvs.2023.1119011.

[50]  R. Pope _et al._, “Efficiently scaling transformer inference,” _Proceedings of the 6th Meeting on Systems and Machine Learning (SysML)_, vol. 5, pp. 606–624, Mar. 2023.

[51]  Y. Chen _et al._, “Towards coarse-to-fine evaluation of inference efficiency for large language models,” _arXiv_, 2024, doi: 10.48550/arxiv.2404.11502.

[52]  R. Pope, “How GPT, Claude, and Gemini are actually trained and served,” Apr. 2026. Available: https://youtu.be/xmkSf5IS-zw

[53]  K. M. Eisenhardt, “Building theories from case study research,” _The Academy of Management Review_, vol. 14, no. 4, p. 532, Oct. 1989, doi: 10.2307/258557.

[54]  W. H. Dutton, O. Goroshko, S. Dembitskyi, E. Chernenko, G. Blank, and N. Boiko, “Trust in media, information, and the government in Ukraine: a virtuous circle of challenges,” Jun. 19, 2025. doi: 10.2139/ssrn.5311707.

[55]  H.-T. Liao and K. Ang, “Orchestrating sustainable AI and semiconductor ecosystems: RegTech and FinTech frameworks,” 2026, doi: 10.17605/OSF.IO/DPJYN.


---

# SS08 - Digital_Circular_Economy
## Special Session 08 - Digital Circular Economy: Digital Deep tech Driven Circular Economy

[Call for Contributions - ICE 2026](https://ice-conference.org/call-for-contributions/)

##### Chairs

Chair: 

Prof. Christos Kalloniatis, University of the Aegean

Co-Chair: 

Prof. Ricardo Jardim Goncalves, New University of Lisbon | José Ferreira, UNINOVA

##### Important Dates

30 April 2026: Full Paper Submission  
20 May 2026: Notification of acceptance  
29 May 2026: Camera ready

##### Description

The Digital Circular Economy workshop explores how advanced digital technologies can accelerate the transition from linear to circular systems across industry, cities, and society. Positioned at the intersection of sustainability, circular economy, and deep tech, the workshop invites researchers, practitioners, innovators, and policymakers to share original contributions on the design, implementation, and impact of digitally enabled circular solutions. The workshop welcomes work addressing how technologies such as artificial intelligence, IoT, blockchain, robotics, data-driven platforms, and Digital Product Passports can support resource efficiency, product lifecycle transparency, waste reduction, sustainable production, circular business models, and regulatory compliance. Particular emphasis is placed on interdisciplinary approaches that connect technological innovation with education, skills development, governance, and real-world industrial adoption. Inspired by the vision of Europe’s twin green and digital transition, this workshop aims to create a vibrant forum for exchanging ideas, presenting emerging research, discussing practical applications, and building collaborations across academia, industry, SMEs, and the public sector. We encourage submissions of research papers, case studies, pilot implementations, methodological contributions, and experience reports that demonstrate novel pathways toward a more sustainable, resilient, and digitally driven circular economy.

##### Review Committee  

- Panagiotis Psomos, University of the Aegean
- Amir Taherkordi, University of Oslo
- George Demetriou, Ecode de Ponts Bussiness School
- Federica Acerbi, Politecnico di Milano
- Thomas Schröder, Technical University Dortmund
- Dev Ramanujan, Technical University of Denmark
- Rebeka Kovačič Lukman, University of Maribor
- Ioannis Athanasiadis, Wageningen University
- Christina Alcaraz, University of Malaga
- Vasco Delgado-Gomes, New University of Lisbon