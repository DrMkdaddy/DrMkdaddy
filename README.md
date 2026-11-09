# Noor Mkdad

Platform and systems engineer. I build Linux infrastructure and LLM serving systems.

[Email](mailto:noorhayatywadam@gmail.com) · [Resume](https://drmkdaddy.github.io/DrMkdaddy/resume.pdf) · [stanzaapi.com](https://stanzaapi.com) · [Engineering notes](https://github.com/StanzaAPI/engineering-notes)

I'm looking for a full-time platform, backend, or systems role. I'm also interested in AI infrastructure work.

## Selected work

| Project | What it is | Result |
| :-- | :-- | :-- |
| [Local inference stack](https://github.com/DrMkdaddy/local-inference-stack) | OpenAI-compatible gateway for one RX 9070 XT, with cost-aware routing, MCP, Prometheus, and a Nix deploy. | $0.19–0.41 per million tokens; 424 tok/s at 8 slots. |
| [KV-serving scheduler](https://github.com/DrMkdaddy/kv-serving-scheduler) | Go scheduler for llama.cpp with a hard KV budget: block allocation, admission control, and preemption. | 120% of capacity; high-priority TTFT p99 74 ms under mixed load. |
| [Tiered KV cache](https://github.com/DrMkdaddy/valkey-kv-l2) | Valkey L2 for an LLM KV cache, with content-addressed blocks and LRU spill. | Fixed pool served 4/200 sequences; tiered served 200/200. Restore beats prefill above ~4k tokens. |
| [llama.cpp Vulkan kernel](https://github.com/DrMkdaddy/llama-vulkan-matvec-rdna4) | K-quant dequantization hoisting and 8-row blocking in `mul_mat_vecq` for RDNA4. | +13.4% aggregate at 8 slots; eight concurrent greedy outputs bit-identical. [PR #31022](https://github.com/ggml-org/llama.cpp/pull/31022). |
| [X12 parser benchmark](https://github.com/StanzaAPI/benchmark-harness) | Public benchmark for the zero-regex X12 streaming parser behind Stanza API, compared against node-x12 and x12-parser. | 255,000 records in 14.2 s inside a 25 MB V8 old-space cap. |
| [Platform infra](https://github.com/DrMkdaddy/platform-infra) | OpenTofu and NixOS configuration for a Proxmox lab, with recovery runbooks. | Provisioning and host configuration are committed; recovery is documented per failure mode. |

## Stanza API

I built and operate [Stanza API](https://stanzaapi.com): 12 production APIs for healthcare claims, payments, and supply-chain data. It has SDKs in four languages and an MCP server.

## Tools

Go, TypeScript, Python. NixOS, OpenTofu, Proxmox, Cloudflare Workers. llama.cpp, Vulkan, AMD RDNA4.

## Other repositories

[Qwen MoE streaming](https://github.com/DrMkdaddy/qwen-moe-stream) · [Speculative decoding](https://github.com/DrMkdaddy/speculative-decoding-lab) · [Quantization quality](https://github.com/DrMkdaddy/quant-quality-harness) · [Paged attention](https://github.com/DrMkdaddy/paged-attention-lab)

## Upstream

Merged: [stable-diffusion.cpp #2293](https://github.com/leejet/stable-diffusion.cpp/pull/2293), [rerun #12943](https://github.com/rerun-io/rerun/pull/12943). Open: [llama.cpp #31022](https://github.com/ggml-org/llama.cpp/pull/31022).
