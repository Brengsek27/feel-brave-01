# make.fun "Make the AI judge feel brave": write the entry text exactly.
import os
from pathlib import Path


TEXT = "The beekeeper moves slowly among the hives, bare-handed. Smoke drifts up. Ten thousand wings make one low note, and his hands work inside the sound, unstung, because nothing in him is rushing. He lifts a frame. The honey holds the light."


def main():
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    if not 1 <= len(TEXT) <= 280 or not TEXT.strip():
        raise ValueError("Entry text must contain 1 to 280 code points and not be only whitespace.")
    encoded_text = TEXT.encode("utf-8")
    (output_dir / "entry.txt").write_bytes(encoded_text)
    print(f"Wrote {len(TEXT)} code points and {len(encoded_text)} bytes.")


if __name__ == "__main__":
    main()
