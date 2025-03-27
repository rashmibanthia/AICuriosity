### https://storage.googleapis.com/deepmind-media/gemma/Gemma3Report.pdf

- Key architectural modifications in Gemma 3 that enable a longer context length and reduce the KV-cache memory issues compared to Gemma 2 

The second main architectural improvement is an increase in context size to 128K tokens, without reducing performance. A challenge with long
context is the memory explosion of the KV cache during inference. To reduce this issue, we interleave multiple local layers between each global layer, and assign a smaller span of only 1024 tokens to the local layers. Therefore, only the global layers attend to long context, and we have 1 global for every 5 local layers.

- SigLIP vision encoder enhance Gemma 3’s multimodal capabilities, handles images with different resolutions and aspect ratios

In terms of multimodality, most Gemma 3 models are compatible with a tailored version of the SigLIP vision encoder (Zhai et al., 2023). The
language models treat images as a sequence of soft tokens encoded by SigLIP. We reduce the inference cost of image processing by condensing
the vision embeddings into a fixed size of 256 vectors. The encoder works at a fixed resolution and we take inspiration from LLaVA (Liu et al., 2024) to enable flexible resolutions with a Pan and Scan (P&S) method.

-  Pre-training and post-training processes improve multilingual performance, mathematical reasoning, and instruction following

Post Training - Techniques. Our post-training approach relies on an improved version of knowledge distillation (Agarwal et al., 2024; Anil et al., 2018; Hinton et al., 2015) from a large IT teacher, along with a RL finetuning phase based on improved versions of BOND (Sessa et al., 2024), WARM (Ramé
et al., 2024b), and WARP (Ramé et al., 2024a). 🤔 🤷‍♀️

- Knowledge distillation

Gemma 3 uses two teacher models—a large teacher and a small teacher—for knowledge distillation.