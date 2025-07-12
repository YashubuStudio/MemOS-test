"""Minimal transformers stub for test environment."""

class DynamicCache:
    pass

class AutoModelForCausalLM:
    @classmethod
    def from_pretrained(cls, *args, **kwargs):
        return cls()

class AutoTokenizer:
    @classmethod
    def from_pretrained(cls, *args, **kwargs):
        return cls()

    def apply_chat_template(self, messages, tokenize=False, add_generation_prompt=False):
        return "".join(m.get("content", "") for m in messages)

    def __call__(self, inputs, return_tensors=None):
        class Dummy:
            def to(self, device):
                return self
        return Dummy()

    def batch_decode(self, ids, skip_special_tokens=True):
        return [""]

class LogitsProcessorList(list):
    pass

class TemperatureLogitsWarper:
    def __init__(self, *args, **kwargs):
        pass

class TopKLogitsWarper:
    def __init__(self, *args, **kwargs):
        pass

class TopPLogitsWarper:
    def __init__(self, *args, **kwargs):
        pass
