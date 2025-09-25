# Gradient BFCL Fork

Currently has support for the models:
- `meta-llama/Llama-3.3-70B-Instruct`
- `openai/gpt-oss-120b:cerebras`
Accessed through Hugging Face: `BASE_URL=https://router.huggingface.co/v1`

And models through UbiOps:
- `ubiops-deployment/llama-3-3//llama-3-3`, `BASE_URL=https://api.intermax.ubiops.com/v2.1/projects/gradient-ds-proxy/openai-compatible/v1`.
- `ubiops-deployment/gpt-oss//openai/gpt-oss-120b`, `BASE_URL=https://api.ubiops.com/v2.1/projects/gen-ai/openai-compatible/v1`.

To benchmark models, follow the steps below:

1. Go into berkeley-function-call-leaderboard directory:
`$ cd berkeley-function-call-leaderboard`

2. Install dependencies
`$ pip install -e .`

3. Go into bfcl_eval directory:
`$ cd bfcl_eval`

4. Export path to current working directory (example), or specify desired directory (results will be stored in specified dir.):\
`$ export BFCL_PROJECT_ROOT=$(pwd)`

5. Copy .env.example into .env file, and fill out the API key and endpoint.

6. Generate results for specific model in specific test category (API endpoint and key must match specified model):\
`$ bfcl generate --model meta-llama/Llama-3.3-70B-Instruct --test-category simple_python`

7. Evaluate results for specific model in specific test category:\
`$ bfcl evaluate --model meta-llama/Llama-3.3-70B-Instruct --test-category simple_python`

8. Plot score using `plot_score.py`