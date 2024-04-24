# Spoken Language Understanding (SLU) System - Slot Filling Project
This repository contains the project work on enhancing slot filling in spoken language understanding (SLU) systems. The project focuses on improving the accuracy of semantic information extraction from sentences using sequence labeling techniques.
To know more details, please check our PDF.
## Abstract
The rapid progress in spoken language understanding (SLU) systems has led to significant advancements in intent detection (ID) and slot filling (SF) tasks. This paper primarily focuses on slot filling, driven by the characteristics of the dataset used.

## Introduction
- **Intent Detection (ID)**: Understands the user's intended meaning.
- **Slot Filling (SF)**: Extracts semantic information from sentences.

## Related Work
1. **Baseline Model**: Utilizes BiLSTM for sequence annotation, suitable for short texts with local context dependencies.
2. **Traditional Models**: Employ pre-trained fixed vector embeddings like Word2Vec and single RNN models.
3. **CTRAN**: An encoder-decoder architecture with a shared encoder for SF and ID tasks.

## Improvements Based on the Baseline
1. **Dataset Analysis**: Addressed data uneven distribution and speech recognition content issues.
2. **Noise Reduction**: Implemented the Levenshtein distance algorithm to correct misidentifications in speech-to-text conversion.
3. **Using Historical Dialogues**: Incorporated previous user inputs to provide context for better understanding.
4. **Incorporating Pre-trained Models**: Replaced Word2Vec with pre-trained models like Bert-base-Chinese (BBC) for improved word embeddings.

## CTRAN Adaptation on SLU
Adapted the CTRAN model for our specific task and dataset, achieving significant performance improvement over the baseline.

## Optimal Solution
- **Dataset**: Manual transcript
- **Algorithm**: Lev Noise Reduction Algorithm
- **Pre-trained Model**: Bert-base-Chinese (BBC)
- **Model**: CTRAN adaptation

## Conclusion
The project demonstrates the effectiveness of adapting existing approaches to improve slot filling in SLU systems, highlighting the significance of selecting suitable techniques based on dataset characteristics.

## Assignment of Responsibilities
- **BolunZhang**: Pre-training model addition and experimentation, Levenshtein denoising algorithm implementation and experimentation.
- **Chaofeng**: Literature research, Ctran adaption and evaluation, problem definition and related works search.
- **MingboDai**: Dataset analysis, baseline model problem exploration, historical model implementation and experimentation.


## License
This project is licensed under the [MIT License](LICENSE).
