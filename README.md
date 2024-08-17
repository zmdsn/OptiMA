# OptiMA: Optimization Modeling and what-if Analysis via LLM-based Multi-Agent Framework

## Abstract
In recent years, large language models (LLMs) have shown great potential in mathematical optimization modeling. Existing research has primarily focused on employing LLMs for either modeling or what-if analysis, without integrating the two, therefore, this paper presents OptiMA. OptiMA is a multi-agent framework that leverages LLMs with the objective of seamlessly amalgamating both modeling and what-if analysis within one framework. Firstly, OptiMA is structured around two primary workflows: building and repairing. The building workflow is designed to construct an optimization model, utilizing a static order of agents to enhance the framework's robustness. The repairing workflow, activated in the event of modeling or coding errors, uses a dynamic order of agents to maximize the self-organizing capabilities of the agents. Secondly, retrieval-augmented generation (RAG) is used to improve the accuracy and the efficiency of code repair by introducing additional information. Lastly, a more general optimized modeling data structure was defined to adapt to diverse scenarios. Experiments have shown that among various LLMs that OptiMA can use, GPT4 is the best. And OptiMA outperforms the existing state-of-the-art prompt-based methods in accuracy. Moreover, it also outperforms existing methods in what-if analysis scenarios.



## Instances

Please view the raw data:

[IndustryOR and MAMO](https://github.com/Cardinal-Operations/ORLM)

[nl4opt](https://github.com/nl4opt)

[nlp4lp](https://github.com/teshnizi/OptiMUS)

[OptiGuide](https://github.com/microsoft/OptiGuide)


> Only test instances we  open source here. We are going through the company's open source review process and will open source all content at a later date.