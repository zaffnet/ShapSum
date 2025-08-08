## ShapSum: Shapley value based Multi-Document Summarization System


ShapSum is a multi-document summarizer. Given a document, it constructs a sentence similarity graph using lexical and semantic cues (WordNet, POS). Then it ranks sentences based on Shapley values from cooperative game theory to capture influence/coverage. The top-k nodes act as summary sentences for the document. We devised a novel approach of treating the problem of text summarization as a case of information diffusion and used Shapley Value, a solution concept from co-cooperative game theory for summary extraction. Our model outperformed the state-of -the-art results on DUC dataset.
