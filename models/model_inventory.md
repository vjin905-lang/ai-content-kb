# Model Inventory — ComfyUI SD1.5 Anime Portrait Pipeline

## Checkpoints (models/checkpoints/)
| File | Size | Source | Purpose |
|------|------|--------|---------|
| Counterfeit-V2.5.safetensors | 4.0 GB | hf-mirror: gsdf/Counterfeit-V2.5 | Anime style checkpoint, SD1.5-based |
| v1-5-pruned-emaonly.safetensors | 4.0 GB | hf-mirror: stable-diffusion-v1-5 | SD1.5 base (fallback) |

## LoRA (models/loras/)
| File | Size | Source | Strength | Purpose |
|------|------|--------|----------|---------|
| anime_screencap_style.safetensors | 144 MB | CivitAI #4982 | 0.6 | Anime screencap style consistency |
| fix_hand.safetensors | 225 KB | CivitAI #111363 | 1.0 | Hand structure fix (SD1.5 mitigation) |

## ControlNet (models/controlnet/)
| File | Size | Source | Purpose |
|------|------|--------|---------|
| control_v11p_sd15_openpose.pth | 1.34 GB | hf-mirror: lllyasviel/ControlNet-v1-1 | Pose/skeleton control |
| control_v11p_sd15_lineart.pth | 1.34 GB | hf-mirror: lllyasviel/ControlNet-v1-1 | Outlines/contour control |

## IP-Adapter (models/ipadapter/)
| File | Size | Source | Purpose |
|------|------|--------|---------|
| ip-adapter_sd15.safetensors | 43 MB | hf-mirror: h94/IP-Adapter | Base IP-Adapter |
| ip-adapter-plus_sd15.safetensors | 94 MB | hf-mirror: h94/IP-Adapter | Plus version |
| ip-adapter-plus-face_sd15.safetensors | 94 MB | hf-mirror: h94/IP-Adapter | Face-specific version |

## CLIP Vision (models/clip_vision/)
| File | Size | Source | Purpose |
|------|------|--------|---------|
| CLIP-ViT-H-14-laion2B-s32B-b79K.safetensors | 2.4 GB | hf-mirror: h94/IP-Adapter | CLIP image encoder |

## Embeddings (models/embeddings/)
| File | Size | Source | Purpose |
|------|------|--------|---------|
| bad-hands-5.pt | 7 KB | hf-mirror: yesyeahvh/bad-hands-5 | Negative embedding for hands |

## Custom Nodes
| Plugin | Source | Purpose |
|--------|--------|---------|
| ComfyUI_IPAdapter_plus | GitHub: cubiq/ComfyUI_IPAdapter_plus | IP-Adapter workflow nodes |
| comfyui_controlnet_aux | GitHub: Fannovel16/comfyui_controlnet_aux | OpenPose/Lineart preprocessors |
| comfyui-manager 4.2.2 | pip | Plugin manager |

## ComfyUI Patches (Windows compatibility)
- `app/logger.py`: OSError protection in LogInterceptor.flush()
- `comfy/utils.py`: tqdm disable in model_trange()

## Current Optimal Recipe (2026-06-27)
```
Checkpoint: Counterfeit-V2.5
  → LoRA: anime_screencap_style (0.6)
  → LoRA: fix_hand (1.0)
  → Resolution: 640×896
  → Steps: 28, CFG: 6.0
  → Sampler: dpmpp_2m + karras
  → Prompt: see configs/render_profiles/anime_portrait_v2.json
```
