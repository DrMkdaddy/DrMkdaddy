<div align="center">

# Noor Mkdad

**Platform & systems engineer · Linux infrastructure · LLM serving**

[Email](mailto:noorhayatywadam@gmail.com) · [Resume](https://drmkdaddy.github.io/DrMkdaddy/resume.pdf) · [stanzaapi.com](https://stanzaapi.com) · [Engineering notes](https://github.com/StanzaAPI/engineering-notes)

</div>

---

I build Linux infrastructure and LLM serving systems, and I publish the benchmarks behind them. I care about systems that can explain their own numbers: bounded memory, measured latency, and the failure cases left in the write-up.

**Open to full-time platform, backend, and systems roles.** AI infrastructure is the through-line.

## Selected work

| Project | What it is | Measured result | Focus |
| :-- | :-- | :-- | :-- |
| **[Local inference stack](https://github.com/DrMkdaddy/local-inference-stack)** | OpenAI-compatible gateway for one RX 9070 XT: cost-aware routing, MCP, Prometheus, Nix deploy. | $0.19–0.41 per million tokens; 424 tok/s at 8 slots. | `AI Infra` `Backend` |
| **[KV-serving scheduler](https://github.com/DrMkdaddy/kv-serving-scheduler)** | Go scheduler for llama.cpp with a hard KV budget: block allocation, admission control, preemption. | 120% of capacity; high-priority TTFT p99 74 ms under mixed load. | `Systems` `AI Infra` |
| **[Tiered KV cache](https://github.com/DrMkdaddy/valkey-kv-l2)** | Valkey L2 for an LLM KV cache, with content-addressed blocks and LRU spill. | Fixed pool served 4/200 sequences; tiered served 200/200. Restore beats prefill only above ~4k tokens. | `AI Infra` `Storage` |
| **[llama.cpp Vulkan kernel](https://github.com/DrMkdaddy/llama-vulkan-matvec-rdna4)** | K-quant dequantization hoisting and 8-row blocking in `mul_mat_vecq` for RDNA4. | +13.4% aggregate at 8 slots; eight concurrent greedy outputs bit-identical. [PR #31022](https://github.com/ggml-org/llama.cpp/pull/31022). | `Systems` `GPU` |
| **[X12 parser benchmark](https://github.com/StanzaAPI/benchmark-harness)** | Public harness for the zero-regex streaming parser behind Stanza API, benchmarked against node-x12 and x12-parser. | 255,000 records in 14.2 s inside a 25 MB V8 old-space cap. | `Backend` `Performance` |
| **[Platform infra](https://github.com/DrMkdaddy/platform-infra)** | Declarative Proxmox lab: OpenTofu provisioning, NixOS host configuration, recovery runbooks. | The lab is rebuildable from source, not from memory. | `Platform` `IaC` |

## Production platform

I built and operate **[Stanza API](https://stanzaapi.com)**: 12 production APIs for healthcare claims, payments, and supply-chain data. Typed SDKs in four languages, and an MCP server so agents can call every API as a tool.

## Stack

**Day to day:** Go, TypeScript, Python. **Infrastructure:** NixOS, OpenTofu, Proxmox, Cloudflare Workers. **Inference:** llama.cpp, Vulkan, AMD RDNA4.

## More work

[Qwen MoE streaming](https://github.com/DrMkdaddy/qwen-moe-stream) · [Speculative decoding](https://github.com/DrMkdaddy/speculative-decoding-lab) · [Quantization quality](https://github.com/DrMkdaddy/quant-quality-harness) · [Paged attention](https://github.com/DrMkdaddy/paged-attention-lab)

## Open source

Merged fixes in [stable-diffusion.cpp #2293](https://github.com/leejet/stable-diffusion.cpp/pull/2293) and [rerun #12943](https://github.com/rerun-io/rerun/pull/12943); open Vulkan kernel PR in [llama.cpp #31022](https://github.com/ggml-org/llama.cpp/pull/31022).

---

<sub>Benchmarks are public and re-runnable. The negative results stay in the write-up.</sub>
