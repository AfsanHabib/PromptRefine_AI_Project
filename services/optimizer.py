import json

from pydantic import BaseModel

from services.gemini import generate_response


# ============================================================
# GEMINI RESPONSE MODEL
# ============================================================

class PromptResult(BaseModel):
    """
    Structured response returned by Gemini.

    Gemini is responsible for semantic analysis
    and prompt optimization.

    Gemini does NOT calculate the final overall score.
    """

    clarity: int
    context: int
    specificity: int

    missing_items: list[str]

    optimized_prompt: str

    standard: str
    zero_shot: str
    few_shot: str
    developer: str
    system: str
    json_mode: str


# ============================================================
# OPTIMIZE PROMPT
# ============================================================

def optimize_prompt(user_prompt: str) -> PromptResult:
    """
    Send the user's prompt to Gemini and receive
    structured semantic analysis and optimized prompts.
    """

    # ========================================================
    # BUILD GEMINI INSTRUCTION
    # ========================================================

    instruction = f"""
You are an expert Prompt Engineer.

Your job is to analyze and improve the user's prompt.

IMPORTANT:

You are NOT responsible for calculating the final
overall prompt quality score.

The application will calculate the final score separately
using its own scoring engine.

You only need to evaluate:

1. Clarity
2. Context
3. Specificity

You must also:

4. Identify missing information.
5. Create an optimized version of the prompt.
6. Create different prompt variations.

Return ONLY valid JSON.

Do NOT use Markdown code fences.

Do NOT add explanations outside the JSON.

Use exactly this JSON structure:

{{
    "clarity": 0,
    "context": 0,
    "specificity": 0,

    "missing_items": [],

    "optimized_prompt": "",

    "standard": "",
    "zero_shot": "",
    "few_shot": "",
    "developer": "",
    "system": "",
    "json_mode": ""
}}

clarity:
Evaluate how clearly the user communicates the task.

context:
Evaluate whether enough background information is provided.

specificity:
Evaluate how specific the requested task and expected result are.

Each score must be an integer from 0 to 100.

IMPORTANT:

Do not calculate or return an overall score.

missing_items should contain the important information
that would improve the original prompt.

Examples:

- Target audience
- Expected output format
- Technical constraints
- Programming language
- Framework
- Input data
- Desired level of detail
- Examples
- Performance requirements

Only include genuinely useful missing information.

optimized_prompt should be a substantially improved version
of the original prompt.

It should preserve the user's original intention.

Do not invent unnecessary requirements.

standard:
Create a clean general-purpose version of the prompt.

zero_shot:
Create a version that does not rely on examples.

few_shot:
Create a version that includes a useful example.

developer:
Create a version suitable for a developer-oriented AI
assistant or coding workflow.

system:
Create a system-level instruction version.

json_mode:
Create a version that explicitly instructs the AI to
return structured JSON.

USER PROMPT:

{user_prompt}
"""

    # ========================================================
    # GEMINI REQUEST
    # ========================================================

    try:

        response_text = generate_response(
            instruction
        )

    except Exception as error:

        raise RuntimeError(
            "Failed to communicate with Gemini API."
        ) from error


    # ========================================================
    # EXTRACT RESPONSE
    # ========================================================

    response_text = response_text.strip()


    # ========================================================
    # REMOVE MARKDOWN CODE FENCES
    # ========================================================

    if response_text.startswith("```json"):

        response_text = response_text[
            len("```json"):
        ]


    if response_text.startswith("```"):

        response_text = response_text[
            len("```"):
        ]


    if response_text.endswith("```"):

        response_text = response_text[
            :-len("```")
        ]


    response_text = response_text.strip()


    # ========================================================
    # PARSE JSON
    # ========================================================

    try:

        data = json.loads(
            response_text
        )

    except json.JSONDecodeError as error:

        raise ValueError(
            "Gemini returned invalid JSON.\n\n"
            f"Gemini response:\n{response_text}"
        ) from error


    # ========================================================
    # VALIDATE RESPONSE
    # ========================================================

    try:

        result = PromptResult(
            **data
        )

    except Exception as error:

        raise ValueError(
            "Gemini returned JSON with an unexpected structure."
        ) from error


    # ========================================================
    # VALIDATE SCORE RANGES
    # ========================================================

    if not 0 <= result.clarity <= 100:

        raise ValueError(
            "Gemini returned an invalid clarity score."
        )


    if not 0 <= result.context <= 100:

        raise ValueError(
            "Gemini returned an invalid context score."
        )


    if not 0 <= result.specificity <= 100:

        raise ValueError(
            "Gemini returned an invalid specificity score."
        )


    # ========================================================
    # RETURN RESULT
    # ========================================================

    return result