def generate_prompt(style, subject, mood, camera_info):
    prompt = f"""
Highly detailed prompt for AI image generation:

- Subject: {subject}
- Style: {style}
- Mood & Atmosphere: {mood}
- Camera Details: {camera_info if camera_info else "default settings"}
- Image Quality: Ultra high resolution, cinematic composition
- Lighting: soft, natural, or dramatic based on mood
- Lens: 35mm, f/1.8 (unless otherwise specified)
"""
    return prompt.strip()
