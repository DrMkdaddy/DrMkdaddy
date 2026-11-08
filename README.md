# Noor Mkdad

Platform and systems engineer. I build the parts you cannot afford to get
wrong: ledgers, parsers, KV caches, and the measurements that say whether any
of it worked.

[noorhayatywadam@gmail.com](mailto:noorhayatywadam@gmail.com) ·
[stanzaapi.com](https://stanzaapi.com) ·
[engineering notes](https://github.com/StanzaAPI/engineering-notes)

## Selected work

**[Stanza API](https://stanzaapi.com)**: 12 production APIs on Cloudflare
Workers for healthcare claims, payments, supply chain and regulatory data. 44
typed clients published to npm, PyPI, NuGet and crates.io from one OpenAPI spec
per API, plus an MCP server for agent callers.

**[X12 parser](https://github.com/StanzaAPI/benchmark-harness)**: 255,000 claim
transactions in 14.2 s inside a hard 25 MB V8 heap cap. Under the same cap
node-x12 takes 49% longer and x12-parser 2.7x; uncapped, node-x12 ties. The
harness is public, including the cases where this parser loses.

**[KV tier](https://github.com/DrMkdaddy/valkey-kv-l2)**: a fixed KV pool served
4 of 200 sequences; spilling to Valkey served 200 of 200. Restore beats
recomputing the prefix only above roughly 4k tokens, measured against prefill
on the same card.

**[Serving scheduler](https://github.com/DrMkdaddy/kv-serving-scheduler)**:
admission control and preemption for llama.cpp, measured at 120% of capacity.
Every policy reports p99 TTFT and goodput, including the policies that shed
load.

**[Inference stack](https://github.com/DrMkdaddy/local-inference-stack)**:
OpenAI-compatible gateway on one RX 9070 XT at $0.19–0.41 per million tokens,
with a per-request cost ceiling that refuses rather than overspends.

**[llama.cpp Vulkan patch](https://github.com/DrMkdaddy/llama-vulkan-matvec-rdna4)**:
hoisted K-quant dequantization in `mul_mat_vecq`, +13.4% aggregate at 8 slots
with bit-identical output and single-stream speed unchanged. Upstream PR
[#31022](https://github.com/ggml-org/llama.cpp/pull/31022).

## Background

Linux, Proxmox, NixOS, OpenTofu, Go, TypeScript, Python. Recent work runs from
a declarative Proxmox lab with a runbook per failure mode to inference kernels
on one consumer GPU.

Open to full-time platform, backend and systems roles. Email is the fastest way
to reach me.
