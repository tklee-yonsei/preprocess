from .interfaces import PreprocessorInterface

class PreprocessorService(PreprocessorInterface):
    def normalize(self, signal):
        # 실제 신호 정규화 로직
        if not signal:
            return []
        max_val = max(signal)
        normalized_signal = [x / max_val for x in signal]
        return normalized_signal

    def filter(self, signal, filter_type, cutoff_frequency):
        # 실제 필터링 로직 구현
        if not signal:
            return []

        if filter_type == "lowpass":
            filtered_signal = [x for x in signal if x <= cutoff_frequency]
        elif filter_type == "highpass":
            filtered_signal = [x for x in signal if x >= cutoff_frequency]
        else:
            # 지원하지 않는 필터 유형에 대한 기본 동작
            filtered_signal = signal

        return filtered_signal