import re


class PromptAnalyzer:
    """
    Analyze a prompt using local Python logic.
    No API call is required.
    """

    def __init__(self, prompt: str):
        self.prompt = prompt.strip()
        self.text = self.prompt.lower()

    # --------------------------------------------------------
    # BASIC STATISTICS
    # --------------------------------------------------------

    def word_count(self) -> int:
        """
        Count words in the prompt.
        """

        if not self.prompt:
            return 0

        return len(self.prompt.split())

    def sentence_count(self) -> int:
        """
        Estimate the number of sentences.
        """

        if not self.prompt:
            return 0

        sentences = re.split(
            r"[.!?]+",
            self.prompt
        )

        return len(
            [
                sentence
                for sentence in sentences
                if sentence.strip()
            ]
        )

    # --------------------------------------------------------
    # ROLE DETECTION
    # --------------------------------------------------------

    def has_role(self) -> bool:
        """
        Check whether the prompt gives the AI a role.
        """

        role_patterns = [
            "act as",
            "you are",
            "assume you are",
            "role:",
            "expert",
            "senior",
            "professional",
        ]

        return any(
            pattern in self.text
            for pattern in role_patterns
        )

    # --------------------------------------------------------
    # CONTEXT DETECTION
    # --------------------------------------------------------

    def has_context(self) -> bool:
        """
        Check whether the prompt provides contextual information.
        """

        context_keywords = [
            "context",
            "background",
            "project",
            "application",
            "company",
            "business",
            "for my",
            "for a",
            "for an",
        ]

        return any(
            keyword in self.text
            for keyword in context_keywords
        )

    # --------------------------------------------------------
    # CONSTRAINT DETECTION
    # --------------------------------------------------------

    def has_constraints(self) -> bool:
        """
        Check whether the prompt contains constraints.
        """

        constraint_keywords = [
            "must",
            "only",
            "exactly",
            "maximum",
            "minimum",
            "limit",
            "do not",
            "don't",
            "avoid",
            "without",
            "should",
        ]

        return any(
            keyword in self.text
            for keyword in constraint_keywords
        )

    # --------------------------------------------------------
    # OUTPUT FORMAT DETECTION
    # --------------------------------------------------------

    def has_output_format(self) -> bool:
        """
        Check whether the user specifies an output format.
        """

        format_keywords = [
            "json",
            "markdown",
            "table",
            "list",
            "csv",
            "xml",
            "bullet points",
            "steps",
            "format",
        ]

        return any(
            keyword in self.text
            for keyword in format_keywords
        )

    # --------------------------------------------------------
    # EXAMPLE DETECTION
    # --------------------------------------------------------

    def has_examples(self) -> bool:
        """
        Check whether the prompt provides examples.
        """

        example_keywords = [
            "example",
            "for instance",
            "sample",
            "input:",
            "output:",
        ]

        return any(
            keyword in self.text
            for keyword in example_keywords
        )

    # --------------------------------------------------------
    # LOCAL SCORE
    # --------------------------------------------------------

    def calculate_score(self) -> int:
        """
        Calculate a simple prompt quality score.

        This is our own application logic,
        not an LLM-generated score.
        """

        if not self.prompt:
            return 0

        score = 40

        if self.word_count() >= 10:
            score += 10

        if self.word_count() >= 30:
            score += 5

        if self.has_role():
            score += 10

        if self.has_context():
            score += 10

        if self.has_constraints():
            score += 10

        if self.has_output_format():
            score += 10

        if self.has_examples():
            score += 5

        return min(score, 100)

    # --------------------------------------------------------
    # COMPLETE ANALYSIS
    # --------------------------------------------------------

    def analyze(self) -> dict:
        """
        Return all local analysis results.
        """

        return {
            "word_count": self.word_count(),
            "sentence_count": self.sentence_count(),
            "has_role": self.has_role(),
            "has_context": self.has_context(),
            "has_constraints": self.has_constraints(),
            "has_output_format": self.has_output_format(),
            "has_examples": self.has_examples(),
            "score": self.calculate_score(),
        }