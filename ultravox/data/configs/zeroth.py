from ultravox.data import types

ZT_KO_CONFIG = types.DatasetConfig(
    name="zeroth-korean",
    path="Bingsu/zeroth-korean",
    subset="data",
    splits=[
        types.DatasetSplitConfig(name="train", num_samples=22_263),
        types.DatasetSplitConfig(name="test", num_samples=457),
    ],
    transcript_template="{{text_proc.format_asr_text(text)}}",
    assistant_template="{{text_proc.format_asr_text(text)}}",
)

ZT_KO_TRANS_CONFIG = types.DatasetConfig(
    name="zeroth-korean-transcription",
    base="zeroth-korean",
    user_template=types.TRANSCRIPTION_USER_TEMPLATE,
    # FIXME: cer?
    eval_config=types.EvalConfig(metric="wer", args={"lang_id": "en"}),
)

# ZT_KO_CONT_CONFIG = types.DatasetConfig(
#     name="gigaspeech-xl-continuation",
#     base="gigaspeech-xl",
#     user_template=types.CONTINUATION_USER_TEMPLATE,
#     assistant_template=types.CONTINUATION_ASSISTANT_TEMPLATE,
# )

configs = [ZT_KO_CONFIG, ZT_KO_TRANS_CONFIG]
