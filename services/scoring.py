class PromptScoringEngine:
    """
    Hybrid prompt scoring engine.

    Combines:
    - Local Python analysis
    - Gemini semantic evaluation
    """

    def __init__(self, local_analysis, gemini_result):
        self.local_analysis = local_analysis
        self.gemini_result = gemini_result

    # --------------------------------------------------------
    # CLARITY
    # --------------------------------------------------------

    def clarity_score(self):
        """
        Clarity is primarily evaluated by Gemini.
        """

        return self.gemini_result.clarity

    # --------------------------------------------------------
    # CONTEXT
    # --------------------------------------------------------

    def context_score(self):
        """
        Context combines Gemini's evaluation
        with our local context detection.
        """

        gemini_score = self.gemini_result.context

        if self.local_analysis["has_context"]:
            local_score = 100
        else:
            local_score = 30

        return round(
            (gemini_score * 0.7)
            + (local_score * 0.3)
        )

    # --------------------------------------------------------
    # SPECIFICITY
    # --------------------------------------------------------

    def specificity_score(self):
        """
        Specificity combines Gemini's evaluation
        with local prompt signals.
        """

        gemini_score = self.gemini_result.specificity

        signals = 0

        if self.local_analysis["has_constraints"]:
            signals += 25

        if self.local_analysis["has_output_format"]:
            signals += 25

        if self.local_analysis["has_examples"]:
            signals += 25

        if self.local_analysis["word_count"] >= 20:
            signals += 25

        return round(
            (gemini_score * 0.7)
            + (signals * 0.3)
        )

    # --------------------------------------------------------
    # CONSTRAINT SCORE
    # --------------------------------------------------------

    def constraint_score(self):
        """
        Evaluate whether the prompt contains
        useful constraints.
        """

        if self.local_analysis["has_constraints"]:
            return 100

        return 30

    # --------------------------------------------------------
    # OUTPUT FORMAT SCORE
    # --------------------------------------------------------

    def output_format_score(self):
        """
        Evaluate whether the expected output
        format is defined.
        """

        if self.local_analysis["has_output_format"]:
            return 100

        return 30

    # --------------------------------------------------------
    # EXAMPLE SCORE
    # --------------------------------------------------------

    def example_score(self):
        """
        Evaluate whether examples are provided.
        """

        if self.local_analysis["has_examples"]:
            return 100

        return 20

    # --------------------------------------------------------
    # FINAL SCORE
    # --------------------------------------------------------

    def calculate_final_score(self):
        """
        Calculate weighted final prompt quality score.
        """

        clarity = self.clarity_score()

        context = self.context_score()

        specificity = self.specificity_score()

        constraints = self.constraint_score()

        output_format = self.output_format_score()

        examples = self.example_score()

        final_score = (
            clarity * 0.20
            + context * 0.20
            + specificity * 0.20
            + constraints * 0.15
            + output_format * 0.15
            + examples * 0.10
        )

        return round(final_score)

    # --------------------------------------------------------
    # COMPLETE SCORE BREAKDOWN
    # --------------------------------------------------------

    def get_breakdown(self):
        """
        Return the complete scoring breakdown.
        """

        return {
            "clarity": self.clarity_score(),
            "context": self.context_score(),
            "specificity": self.specificity_score(),
            "constraints": self.constraint_score(),
            "output_format": self.output_format_score(),
            "examples": self.example_score(),
            "final_score": self.calculate_final_score(),
        }


def calculate_local_score(local_analysis):
        """
        Calculate a deterministic score using only
        locally detected prompt characteristics.

        This is useful for comparing prompt versions.
        """

        score = 0

        # --------------------------------------------------------
        # WORD COUNT
        # --------------------------------------------------------

        word_count = local_analysis["word_count"]

        if word_count >= 50:
            score += 20

        elif word_count >= 30:
            score += 15

        elif word_count >= 15:
            score += 10

        else:
            score += 5


        # --------------------------------------------------------
        # ROLE
        # --------------------------------------------------------

        if local_analysis["has_role"]:
            score += 15


        # --------------------------------------------------------
        # CONTEXT
        # --------------------------------------------------------

        if local_analysis["has_context"]:
            score += 20


        # --------------------------------------------------------
        # CONSTRAINTS
        # --------------------------------------------------------

        if local_analysis["has_constraints"]:
            score += 15


        # --------------------------------------------------------
        # OUTPUT FORMAT
        # --------------------------------------------------------

        if local_analysis["has_output_format"]:
            score += 15


        # --------------------------------------------------------
        # EXAMPLES
        # --------------------------------------------------------

        if local_analysis["has_examples"]:
            score += 15


        return min(score, 100)